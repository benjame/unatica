#!/usr/bin/env python3
"""
Copyright 2024 Jensen Yu

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

import sys
import argparse
import logging
from pathlib import Path
from typing import Optional

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from unatica.core import uninstall_app

# 创建控制台对象
console = Console()

# 定义版本号
__version__ = "0.0.1"


def setup_logging() -> None:
    """配置日志系统。"""
    log_dir = Path.home() / "Library" / "Logs" / "AppUninstaller"
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file = log_dir / "uninstall.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
    )


def show_welcome() -> None:
    """显示欢迎信息。"""
    welcome_text = f"""
    macOS Application Uninstaller v{__version__}

    This tool helps you completely uninstall macOS applications, including related
    configuration files and caches.
    Use -h or --help to view help information.
    """
    console.print(Panel(welcome_text, title="Welcome", border_style="cyan"))


def show_help() -> None:
    """显示帮助信息。"""
    table = Table(title="Command Usage", border_style="cyan")
    table.add_column("Command", style="cyan")
    table.add_column("Description", style="white")

    table.add_row("uninstall-app", "Interactive mode")
    table.add_row(
        'uninstall-app -n "Application Name"', "Uninstall specified application"
    )
    table.add_row(
        'uninstall-app -n "Application Name" -f', "Force uninstall (skip confirmation)"
    )
    table.add_row(
        'uninstall-app -n "Application Name" -v', "Display detailed information"
    )

    console.print(table)


def create_parser() -> argparse.ArgumentParser:
    """创建命令行参数解析器。

    Returns:
        argparse.ArgumentParser: 配置好的参数解析器
    """
    parser = argparse.ArgumentParser(
        description="macOS Application Uninstaller - Uninstall application and clean up residual files"
    )

    parser.add_argument("-n", "--name", help="Application name to uninstall", type=str)

    parser.add_argument(
        "-f",
        "--force",
        help="Force uninstall, skip confirmation prompt",
        action="store_true",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        help="Display detailed operation information",
        action="store_true",
    )

    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )

    return parser


def main() -> None:
    """程序主入口函数。"""
    try:
        # 设置日志
        setup_logging()
        logging.info("Starting uninstallation program")

        # 解析命令行参数
        parser = create_parser()
        args = parser.parse_args()

        # 显示欢迎信息
        show_welcome()

        # 从命令行参数中获取应用名称
        app_name: Optional[str] = None
        # 如果未指定应用名称，则显示帮助信息并提示输入应用名称
        if not args.name:
            show_help()
            console.print(
                "\n[info]Please enter the name of the application to uninstall:[/info]"
            )
            # 获取用户输入的应用名称
            app_name = console.input(">>> ").strip()
            if not app_name:
                console.print("[error]Error: Application name cannot be empty[/error]")
                sys.exit(1)
        else:
            # 如果指定了应用名称，则使用命令行参数中的应用名称
            app_name = args.name.strip()

        # 如果应用名称不为空，则执行卸载操作
        if app_name:
            uninstall_app(app_name, force=args.force, verbose=args.verbose)

    except KeyboardInterrupt:
        console.print("\n[warning]Operation cancelled[/warning]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[error]Error: {str(e)}[/error]")
        logging.exception("Program execution error")
        sys.exit(1)
    finally:
        logging.info("Program execution ended")


if __name__ == "__main__":
    main()
