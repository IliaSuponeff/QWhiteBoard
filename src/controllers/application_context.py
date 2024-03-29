import argparse
import os.path
import sys, io, typing
from datetime import datetime
from pprint import pprint
from PySide6.QtSql import QSqlDatabase
from PySide6.QtGui import QIcon, QPixmap, Qt
from PySide6.QtWidgets import QApplication, QMessageBox, QDialog


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
        self._is_archive_mode = False

        # Application resources directories
        root = os.path.abspath(os.path.dirname(sys.argv[0]))
        self._resources_dir = os.path.join(root, "resources")
        self._logs_dir = os.path.join(self._resources_dir, "logs")
        self._icons_dir = os.path.join(self._resources_dir, "icons")
        self._albums_dir = os.path.join(self._resources_dir, "albums")
        self._sql_scripts_dir = os.path.join(self._resources_dir, "sql_scripts")
        self._validate_dirs()

        self._database_filename = os.path.join(self._resources_dir, "database.sqlite")
        self._database = None

        self._clearing_logs()
        self._logs_wrappers = {
            "closings": [
                open(
                    os.path.join(self._logs_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log"),
                    "a",
                    encoding="UTF-8"
                ),
            ],
            "unclosings": [sys.stderr]
        }

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

    @property
    def resources_dir(self) -> str:
        return self._resources_dir

    @property
    def albums_dir(self) -> str:
        return self._albums_dir

    @property
    def database_filename(self) -> str:
        return self._database_filename

    @property
    def database(self) -> typing.Optional[QSqlDatabase]:
        return self._database

    @property
    def is_archive_mode(self) -> bool:
        return self._is_archive_mode

    @is_archive_mode.setter
    def is_archive_mode(self, value: bool):
        self._is_archive_mode = value

    @database.setter
    def database(self, value: QSqlDatabase):
        self._database = value

    def call_dialog(self, dialog: QDialog) -> tuple[QDialog, int]:
        dialog.show()
        exec_code = dialog.exec()
        self.log(
            LogLevel.DEBUG,
            "Call dialog",
            f"Dialog: {dialog}",
            f"Execution message: '{dialog.execution_message}'",
            f"Execution code: {exec_code}"
        )
        return dialog, exec_code

    def load_sql_script(self, script_name: str, default_script: str = "") -> str:
        path = os.path.join(self._sql_scripts_dir, f"{script_name}.sql")
        if not os.path.exists(path):
            self.log(
                LogLevel.ERROR,
                "SQL script not found",
                f"Script name: {script_name}",
                f"Path: {path}",
                f"Default script: '{default_script}'"
            )
            return default_script

        script_data = default_script
        with open(path, "r", encoding="UTF-8") as sql_script:
                script_data = sql_script.read()

        if not script_data:
            self.log(
                LogLevel.ERROR,
                "SQL script is empty",
                f"Script name: {script_name}",
                f"Path: {path}",
                f"Default script: '{default_script}'"
            )
            return default_script

        return script_data

    def load_icon(self, icon_name: str) -> QIcon:
        return QIcon(self.load_pixmap(icon_name))

    def load_pixmap(self, pixmap_name: str) -> QPixmap:
        path = os.path.join(self._icons_dir, pixmap_name)
        if os.path.exists(path):
            return QPixmap(path)

        self.log(
            LogLevel.DEBUG,
            "Not found image",
            f"Try load image from: {self._icons_dir}",
            f"Image name: {pixmap_name}"
        )

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

    def _clearing_logs(self) -> None:
        if not os.path.exists(self._logs_dir):
            return
        
        files = list(sorted(os.listdir(self._logs_dir)))
        if len(files) >= 5:
            for file in files[:-5]:
                os.remove(os.path.join(self._logs_dir, file))

    def _validate_dirs(self) -> None:
        dirs = list(filter(lambda x: x.endswith("_dir") and x.startswith("_"), dir(self)))
        for _dir in dirs:
            if not hasattr(self, _dir):
                continue

            path = getattr(self, _dir)
            if not os.path.exists(path):
                os.makedirs(path)

    def _stdlog(self, log_type: LogLevel, title: str, *messages) -> None:
        for log_wrapper_type in self._logs_wrappers:
            for log_wrapper in self._logs_wrappers[log_wrapper_type]:
                if log_wrapper is None or not isinstance(log_wrapper, io.TextIOWrapper):
                    continue

                print(f"[LOG-{log_type}][{title}]", "{", file=log_wrapper)
                print(*[f"\t{message}" for message in messages], sep=os.linesep, file=log_wrapper)
                print("}", file=log_wrapper)

    @staticmethod
    def _default_pixmap() -> QPixmap:
        pixmap = QPixmap(64, 64)
        pixmap.fill(Qt.GlobalColor.lightGray)
        return pixmap

    def __del__(self) -> None:
        for log_wrapper_type in self._logs_wrappers:
            if log_wrapper_type != "closings":
                continue

            for log_wrapper in self._logs_wrappers[log_wrapper_type]:
                if log_wrapper is None or not isinstance(log_wrapper, io.TextIOWrapper):
                    continue

                log_wrapper.close()

        if self.database is not None and self.database.isOpen():
            self.database.close()
