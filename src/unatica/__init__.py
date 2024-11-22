"""
Unatica.app
~~~~~~~~~~

A Safe and Simple macOS App Uninstaller.
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__license__ = "MIT"

from .core import (
    uninstall_app,
    get_bundle_identifier,
    get_additional_paths,
    check_permissions,
    is_root,
    is_app_running,
    backup_app,
)

__all__ = [
    "uninstall_app",
    "get_bundle_identifier",
    "get_additional_paths",
    "check_permissions",
    "is_root",
    "is_app_running",
    "backup_app",
]
