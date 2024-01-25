from PySide6.QtWidgets import QApplication
from controllers.application_context import ApplicationContext, LogLevel
from controllers.main_window import WhiteBoardWindow


class QWhiteBoardApplication(QApplication):

    def __init__(self) -> None:
        super().__init__()
        self._context = ApplicationContext(self)
        self._main_window = WhiteBoardWindow(self.context)

    @property
    def context(self) -> ApplicationContext:
        return self._context

    @property
    def main_window(self):
        return self._main_window

    def execute(self) -> int:
        self._main_window.show()
        return self.exec()
