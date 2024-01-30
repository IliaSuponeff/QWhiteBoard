from controllers.abc_controller import AbstractPageController
from controllers.application_context import ApplicationContext
from views.ui_album_info_page import Ui_AlbumInfoPage
from models.album import AlbumModel, SlideType


class AlbumInfoPage(AbstractPageController):

    def __init__(self, context: ApplicationContext, bindings: dict[str, list[str]] = {}) -> None:
        super().__init__(context, Ui_AlbumInfoPage(), bindings)

    @property
    def ui(self) -> Ui_AlbumInfoPage:
        return self._ui
