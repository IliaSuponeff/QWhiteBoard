from controllers.abc_controller import AbstractPageController
from controllers.application_context import ApplicationContext
from views.ui_main_page import Ui_MainPage

class MainPage(AbstractPageController):

    def __init__(self, context: ApplicationContext, bindings: dict[str, list[str]] = {}) -> None:
        super().__init__(context, Ui_MainPage(), bindings)
