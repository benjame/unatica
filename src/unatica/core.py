"""Core functionality for macOS App Uninstaller.

This module contains the core functionality for uninstalling macOS applications
and cleaning up their associated files.

Functions:
    get_bundle_identifier: Get the bundle identifier of an application
    get_additional_paths: Get list of paths that may contain app residual files
    check_permissions: Check if we have sufficient permissions
    is_root: Check if running as root
    is_app_running: Check if an application is currently running
    backup_app: Create a backup of the application
    remove_file_or_dir: Safely remove a file or directory
    uninstall_app: Main function to uninstall an application
"""

# 导入标准库
import os
import shutil
import subprocess
import tempfile
import logging
from datetime import datetime
from typing import List, Optional, Tuple

# 导入 Rich 库
from rich.console import Console
from rich.theme import Theme
from rich.prompt import Confirm

# 创建自定义主题
custom_theme = Theme(
    {
        "info": "cyan",  # 信息类消息使用青色
        "warning": "yellow",  # 警告类消息使用黄色
        "error": "bold red",  # 错误类消息使用粗体红色
        "success": "bold green",  # 成功类消息使用粗体绿色
    }
)

# 创建控制台对象
console = Console(theme=custom_theme)


def get_bundle_identifier(app_path: str) -> str:
    """获取应用的 Bundle Identifier。

    Args:
        app_path: 应用程序的完整路径

    Returns:
        str: 应用的 Bundle Identifier，如果获取失败则返回空字符串
    """
    try:
        result = subprocess.run(
            ["mdls", "-name", "kMDItemCFBundleIdentifier", app_path],
            capture_output=True,
            text=True,
            check=True,
        )
        if result.stdout:
            return result.stdout.split("=")[-1].strip(' "\n')
    except subprocess.SubprocessError as e:
        logging.warning(f"Failed to get Bundle Identifier: {e}")
    return ""


def get_additional_paths(app_name: str) -> List[str]:
    """获取应用程序可能存在的残留文件路径列表。

    Args:
        app_name: 应用程序名称

    Returns:
        List[str]: 可能包含应用程序残留文件的路径列表
    """
    home = os.path.expanduser("~")
    app_path = f"/Applications/{app_name}.app"

    # 获取 Bundle Identifier 用于查找更多相关文件
    bundle_id = get_bundle_identifier(app_path)

    # 基本路径列表
    paths = [
        f"{home}/Library/Application Support/{app_name}",
        f"{home}/Library/Caches/{app_name}",
        f"{home}/Library/Logs/{app_name}",
        f"{home}/Library/Saved Application State/{app_name}.savedState",
        f"{home}/Library/WebKit/{app_name}",
        f"{home}/Library/Containers/{app_name}",
    ]

    # 如果有 Bundle Identifier，添加相关路径
    if bundle_id:
        paths.extend(
            [
                f"{home}/Library/Preferences/{bundle_id}.plist",
                f"{home}/Library/Containers/{bundle_id}",
                f"{home}/Library/Application Scripts/{bundle_id}",
                f"{home}/Library/Group Containers/{bundle_id}",
            ]
        )

    return paths


def check_permissions(path: str) -> bool:
    """检查是否有足够的权限操作指定路径。

    Args:
        path: 要检查的路径

    Returns:
        bool: 如果有足够权限返回 True，否则返回 False
    """
    try:
        # 检查读权限
        if not os.access(path, os.R_OK):
            return False
        # 检查写权限
        if not os.access(path, os.W_OK):
            return False
        # 如果是目录，检查执行权限
        if os.path.isdir(path) and not os.access(path, os.X_OK):
            return False
        return True
    except Exception as e:
        logging.error(f"Failed to check permissions: {e}")
        return False


def is_root() -> bool:
    """检查是否以 root 权限运行。

    Returns:
        bool: 如果是 root 用户返回 True，否则返回 False
    """
    return os.geteuid() == 0


def is_app_running(app_name: str) -> bool:
    """检查应用是否正在运行。

    Args:
        app_name: 应用程序名称

    Returns:
        bool: 如果应用正在运行返回 True，否则返回 False
    """
    try:
        result = subprocess.run(
            ["pgrep", "-if", app_name], capture_output=True, text=True
        )
        return bool(result.stdout.strip())
    except subprocess.SubprocessError as e:
        logging.error(f"Failed to check application running status: {e}")
        return False


def backup_app(app_path: str) -> str:
    """创建应用程序的备份。

    Args:
        app_path: 应用程序的完整路径

    Returns:
        str: 备份文件的路径，如果备份失败返回空字符串
    """
    backup_dir = tempfile.mkdtemp(prefix="app_backup_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}")

    try:
        shutil.copytree(app_path, backup_path)
        logging.info(f"Backup created: {backup_path}")
        return backup_path
    except Exception as e:
        logging.error(f"Failed to create backup: {e}")
        console.print(f"[warning]Warning: Failed to create backup: {str(e)}[/warning]")
        return ""


def remove_file_or_dir(path: str) -> Tuple[bool, Optional[str]]:
    """安全地删除文件或目录。

    Args:
        path: 要删除的文件或目录的路径

    Returns:
        Tuple[bool, Optional[str]]: (是否成功, 错误信息)
    """
    try:
        if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
            logging.info(f"Deleted: {path}")
            return True, None
    except Exception as e:
        error_msg = str(e)
        logging.error(f"Failed to delete {path}: {error_msg}")
        return False, error_msg
    return False, "Path does not exist"


def uninstall_app(app_name: str, force: bool = False, verbose: bool = False) -> None:
    """卸载 macOS 应用程序并清理残留文件。

    Args:
        app_name: 要卸载的应用程序名称
        force: 是否强制卸载（跳过确认）
        verbose: 是否显示详细信息

    Raises:
        FileNotFoundError: 当应用程序不存在时
        RuntimeError: 当应用程序正在运行时
        PermissionError: 当没有足够权限时
    """

    # 构建应用程序路径
    app_path = f"/Applications/{app_name}.app"

    # 验证应用名称是否合法(不包含非法字符)
    if not app_name or any(c in app_name for c in ["/", "\0", ".."]):
        raise ValueError("Application name contains illegal characters")

    # 检查应用是否存在
    if not os.path.exists(app_path):
        raise FileNotFoundError(f"Application does not exist: {app_path}")

    # 检查应用是否在运行
    if is_app_running(app_name):
        raise RuntimeError(f"{app_name} is running, please close the application first")

    # 检查权限
    if not check_permissions(app_path) and not is_root():
        raise PermissionError(
            "Administrator privileges are required to delete this application"
        )

    # 如果不是强制模式，请求确认
    if not force:
        if not Confirm.ask(
            f"Are you sure you want to uninstall {app_name}? This action is irreversible."
        ):
            console.print("[warning]Operation cancelled[/warning]")
            return

        # 创建备份
        if backup_path := backup_app(app_path):
            console.print(f"[info]Backup created: {backup_path}[/info]")

    # 删除主程序
    console.print(f"\n[info]Uninstalling {app_name}...[/info]")
    success, error = remove_file_or_dir(app_path)
    if not success:
        raise RuntimeError(f"Failed to delete application: {error}")

    # 清理残留文件
    for path in get_additional_paths(app_name):
        if os.path.exists(path):
            success, error = remove_file_or_dir(path)
            if verbose:
                if success:
                    console.print(f"[success]Deleted: {path}[/success]")
                else:
                    console.print(
                        f"[warning]Failed to delete: {path} ({error})[/warning]"
                    )

    # 显示卸载成功信息
    console.print(
        f"\n[success]✨ {app_name} has been successfully uninstalled[/success]"
    )
