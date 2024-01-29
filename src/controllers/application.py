from PySide6.QtWidgets import QApplication
from controllers.application_context import ApplicationContext, LogLevel, datetime
from controllers.main_window import WhiteBoardWindow
from controllers.database import DatabaseController


class QWhiteBoardApplication(QApplication):

    def __init__(self) -> None:
        super().__init__()
        self._context = ApplicationContext(self)
        self._main_window = WhiteBoardWindow(self.context)
        self._database = DatabaseController(self.context)

        self.context.log(
            LogLevel.INFO,
            "Application started",
            f"DateTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Database connetion: is-valid={self.database.isValid()} is-open={self.database.isOpen()}",
            f"Debug mode: {self.context.debug_mode}"
        )

    @property
    def context(self) -> ApplicationContext:
        return self._context

    @property
    def main_window(self):
        return self._main_window

    @property
    def database(self) -> DatabaseController:
        return self._database

    def execute(self) -> int:
        if not self.database.isValid() or not self.database.isOpen():
            self.context.log(
                LogLevel.ERROR,
                "Database is not valid",
                f"Can't open database: {self.database.lastError().text()}",
                is_window_log=True
            )
            return -1
        
        self._main_window.show()
        exec_code = self.exec()
        self.context.log(
            LogLevel.INFO,
            "Application finished",
            f"DateTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Return code: {exec_code}"
        )
        return exec_code
