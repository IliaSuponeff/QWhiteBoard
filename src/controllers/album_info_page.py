from controllers.abc_controller import AbstractPageController
from controllers.application_context import ApplicationContext
from controllers.database import DatabaseController
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
    
    @property
    def album(self) -> AlbumModel:
        return self._album

    def updateData(self, album: AlbumModel) -> None:
        self._album = album
        self.ui.album_name_lbl.setText(f"## {album.name}")
        self.ui.create_datetime_edit.setDateTime(album.create_on)
        self.ui.chage_datetime_edit.setDateTime(album.change_on)
        self.ui.slide_type_le.setText(str(album.slide_type.name))
        self.ui.slide_size_le.setText(f"{album.slide_size.width()}x{album.slide_size.height()}")
        self.ui.description_te.setPlainText(album.description.replace('\\n', '\n').replace('\\r', '\r').replace('\\t', '\t'))
        self.ui.archive_swap_btn.setText('Unarchivate' if album.is_archived else 'Archivate')
        self.ui.open_album_btn.setDisabled(self.context.is_archive_mode)
        self.ui.edit_album_btn.setDisabled(self.context.is_archive_mode)

    def controller_bindings(self) -> dict[str, tuple[str, object]]:
        return {}

    def controller_images(self) -> dict[str, str]:
        return {}

