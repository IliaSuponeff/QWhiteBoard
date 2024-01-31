from controllers.abc_controller import AbstractPageController
from controllers.application_context import ApplicationContext
from views.ui_album_info_page import Ui_AlbumInfoPage
from models.album import AlbumModel, SlideType, EMPTY_ALBUM


class AlbumInfoPage(AbstractPageController):

    def __init__(self, context: ApplicationContext, bindings: dict[str, list[str]] = {}) -> None:
        super().__init__(context, Ui_AlbumInfoPage(), bindings)
        self._album: AlbumModel = EMPTY_ALBUM
        self.updateData(EMPTY_ALBUM)

    @property
    def ui(self) -> Ui_AlbumInfoPage:
        return self._ui

    def updateData(self, album: AlbumModel) -> None:
        self._album = album
        self.ui.album_name_lbl.setText(f"## {album.name}")
        # self.ui.
        