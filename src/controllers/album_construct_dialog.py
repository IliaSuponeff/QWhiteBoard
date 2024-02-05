import abc
from controllers.abc_controller import AbstractDialogController
from controllers.application_context import ApplicationContext, LogLevel
from controllers.database import DatabaseController
from views.ui_album_construct_dialog import Ui_AlbumConstructDialog
from models.album import AlbumModel, EMPTY_ALBUM, SlideType
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QSize


class AlbumConstructDialog(AbstractDialogController):

    def __init__(self,album: AlbumModel , context: ApplicationContext, bindings: dict[str, list[str]] = {}) -> None:
        super().__init__(context, Ui_AlbumConstructDialog(), bindings)
        self._album = album
        self._initUI()

    def _initUI(self) -> None:
        input_validator = QRegularExpressionValidator()
        input_validator.setRegularExpression(r"^[a-zA-Zа-яА-Я0-9 ]*$")

        self.ui.width_edit.setMinimum(SlideType.minimum_width())
        self.ui.heigth_edit.setMinimum(SlideType.minimum_height())
        self.ui.width_edit.setMaximum(SlideType.maximum_width())
        self.ui.heigth_edit.setMaximum(SlideType.maximum_height())

        self.ui.name_le.setValidator(input_validator)
        self.ui.name_le.setText(self.album.name)
        self.ui.slide_type_box.addItems(list(SlideType.__members__))
        self.ui.slide_type_box.setCurrentText(str(self.album.slide_type.name))
        self.ui.width_edit.setValue(self.album.slide_size.width())
        self.ui.heigth_edit.setValue(self.album.slide_size.height())
        self.ui.description_text_edit.setText(self.album.description)

    @property
    def album(self) -> AlbumModel:
        return self._album

    @property
    def ui(self) -> Ui_AlbumConstructDialog:
        return self._ui

    def controller_bindings(self) -> dict[str, tuple[str, object]]:
        return {
            "construct_btn": ("clicked", self._on_clicked_construct_btn),
            "slide_type_box": ("currentTextChanged", self._on_change_slide_type)
        }

    def controller_images(self) -> dict[str, str]:
        return {
            "size_img_lbl": "size.png",
            "album_img_lbl": "album.png",
            "slide_img_lbl": "slide.png"
        }

    def _on_clicked_construct_btn(self) -> None:
        if not self._is_valide_album_data():
            self.context.log(
                LogLevel.ERROR,
                "Album exsists",
                f"Album with name: '{self.ui.name_le.text().strip()}'",
                "Already exsist in appliccation",
                f"Change it, and try againg",
                is_window_log=True
            )
            return

        self._album = self._compile_album()
        self.close()

    @abc.abstractmethod
    def _is_valide_album_data(self) -> bool:
        return True

    def _on_change_slide_type(self, value: str) -> None:
        is_custom = value == SlideType.CUSTOM.name
        self.ui.heigth_edit.setDisabled(not is_custom)
        self.ui.width_edit.setDisabled(not is_custom)
        if not is_custom:
            slide_type = SlideType[self.ui.slide_type_box.currentText()]
            self.ui.heigth_edit.setValue(slide_type.value.height())
            self.ui.width_edit.setValue(slide_type.value.width())

    @abc.abstractmethod
    def _compile_album(self) -> AlbumModel:
        pass


class CreationAlbumDialog(AlbumConstructDialog):

    def __init__(self, context: ApplicationContext) -> None:
        super().__init__(EMPTY_ALBUM, context)

    def _compile_album(self) -> AlbumModel:
        # New album data
        name: str = self.ui.name_le.text().strip()
        slide_type: SlideType = SlideType[self.ui.slide_type_box.currentText()]
        width: int = self.ui.width_edit.value()
        height: int = self.ui.heigth_edit.value()
        description: str = self.ui.description_text_edit.toPlainText().strip()

        db: DatabaseController = self.context.database
        return db.create_new_album(name, slide_type, QSize(width, height), description)

    def _is_valide_album_data(self) -> bool:
        name: str = self.ui.name_le.text().strip()
        return len(name) > 0 and not self.context.database.is_contain_album(album_name=name)


class EditAlbumDialog(AlbumConstructDialog):

    def __init__(self, album: AlbumModel, context: ApplicationContext) -> None:
        super().__init__(album, context)

    def _compile_album(self) -> AlbumModel:
        # New album data
        name: str = self.ui.name_le.text().strip()
        slide_type: SlideType = SlideType[self.ui.slide_type_box.currentText()]
        width: int = self.ui.width_edit.value()
        height: int = self.ui.heigth_edit.value()
        description: str = self.ui.description_text_edit.toPlainText().strip()

        db: DatabaseController = self.context.database
        return db.create_new_album(name, slide_type, QSize(width, height), description)

    def _is_valide_album_data(self) -> bool:
        name: str = self.ui.name_le.text().strip()
        return len(name) > 0 and not self.context.database.is_contain_album(album_name=name)