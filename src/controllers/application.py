from PySide6.QtWidgets import QApplication
from controllers.application_context import ApplicationContext, LogLevel, datetime
from controllers.main_window import WhiteBoardWindow


class QWhiteBoardApplication(QApplication):

    def __init__(self) -> None:
        super().__init__()
        self._context = ApplicationContext(self)
        self._main_window = WhiteBoardWindow(self.context)

        self.context.log(
            LogLevel.INFO,
            "Application started",
            f"DateTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Debug mode: {self.context.debug_mode}"
        )

    @property
    def context(self) -> ApplicationContext:
        return self._context

    @property
    def main_window(self):
        return self._main_window

    def execute(self) -> int:
        self._main_window.show()
        exec_code = self.exec()
        self.context.log(
            LogLevel.INFO,
            "Application finished",
            f"DateTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Return code: {exec_code}"
        )
        return exec_code
