import argparse
import os.path
import sys
from PySide6.QtGui import QIcon, QPixmap, Qt
from PySide6.QtWidgets import QApplication, QMessageBox


class LogLevel:
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"
    DEBUG = "DEBUG"


class ApplicationContext:

    def __init__(self, application: QApplication):
        assert application is not None

        # Application properties
        self._application = application
        self._debug_mode = False
        self._version = "1.0"
        self._application_name = "WhiteBoard"
        self._organization_name = "git.IliaSuponeff"
        self._organization_domain = "https://github.com/IliaSuponeff"

        # Application resources directories
        root = os.path.abspath(os.path.dirname(sys.argv[0]))
        self._resources_dir = os.path.join(root, "resources")
        self._icons_dir = os.path.join(self._resources_dir, "icons")
        self._database_file = os.path.join(root, "database.sqlite")

        # Loading application settings
        self._analyze_cmd_args()
        self._set_application_settings()

    @property
    def application(self) -> QApplication:
        return self._application

    @property
    def debug_mode(self) -> bool:
        return self._debug_mode

    @property
    def version(self) -> str:
        return self._version

    @property
    def application_name(self) -> str:
        return self._application_name

    @property
    def organization_name(self) -> str:
        return self._organization_name

    @property
    def organization_domain(self) -> str:
        return self._organization_domain

    def load_icon(self, icon_name: str) -> QIcon:
        return QIcon(self.load_pixmap(icon_name))

    def load_pixmap(self, pixmap_name: str) -> QPixmap:
        path = os.path.join(self._icons_dir, pixmap_name)
        if os.path.exists(path):
            return QPixmap(path)

        return self._default_pixmap()

    def log(self, log_type: LogLevel, title: str, *messages, is_window_log: bool = False) -> None:
        if not self.debug_mode and log_type == LogLevel.DEBUG:
            return

        self._stdlog(log_type, title, *messages)
        if is_window_log:
            message_box = QMessageBox(
                QMessageBox.Icon.Information if LogLevel.INFO == log_type or log_type == LogLevel.DEBUG else
                QMessageBox.Icon.Warning if LogLevel.WARNING == log_type else
                QMessageBox.Icon.Critical if LogLevel.ERROR == log_type else
                QMessageBox.Icon.NoIcon,
                title,
                "\n".join(messages),
                QMessageBox.StandardButton.Ok
            )
            # message_box.setFixedSize(320, 240)
            message_box.show()
            message_box.exec()

    def _set_application_settings(self) -> None:
        self.application.setApplicationName(self.application_name)
        self.application.setApplicationVersion(self.version)
        display_name = f"{self.application_name} v{self.version}{' [DEBUG]' if self.debug_mode else ''}"
        self.application.setApplicationDisplayName(display_name)
        self.application.setOrganizationName(self.organization_name)
        self.application.setOrganizationDomain(self.organization_domain)
        self.application.setWindowIcon(self.load_icon("icon.png"))

    def _analyze_cmd_args(self) -> None:
        parser = argparse.ArgumentParser(
            prog=self.application_name,
            description="Program to use it as Paint"
        )
        parser.add_argument(
            "-d", "--debug",
            action="store_true", default=False,
            help="set flag of debug mode as true"
        )
        ns = parser.parse_args(sys.argv[1:])

        self._debug_mode = ns.debug

    @staticmethod
    def _default_pixmap() -> QPixmap:
        pixmap = QPixmap(64, 64)
        pixmap.fill(Qt.GlobalColor.lightGray)
        return pixmap

    @staticmethod
    def _stdlog(log_type: LogLevel, title: str, *messages) -> None:
        print(f"[LOG-{log_type}][{title}]", "{")
        print(*[f"\t{message}" for message in messages], sep=os.linesep)
        print("}")
