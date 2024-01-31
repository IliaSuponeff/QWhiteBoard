from enum import Enum
from PySide6.QtCore import QSize, QDateTime


class SlideType(Enum):
    A0 = QSize(8410, 11890)
    A1 = QSize(5940, 8410)
    A2 = QSize(4200, 5940)
    A3 = QSize(2970, 4200)
    A4_VERTICAL = QSize(2100, 2970)
    A4_HORIZONTAL = QSize(2970, 2100)
    A5 = QSize(1480, 2100)
    A6 = QSize(1050, 1480)
    CUSTOM = QSize(4000, 4000)

    @classmethod
    def minimum_width(cls) -> int:
        return min(
            [_type.value.width() for _type in cls]
        )

    @classmethod
    def minimum_height(cls) -> int:
        return min(
            [_type.value.height() for _type in cls]
        )

    @classmethod
    def maximum_width(cls) -> int:
        return max(
            [_type.value.width() for _type in cls]
        )

    @classmethod
    def maximum_height(cls) -> int:
        return max(
            [_type.value.height() for _type in cls]
        )


class AlbumModel:

    def __init__(
            self, _id: int, shelf_name: str, name: str,
            create_on: QDateTime, change_on: QDateTime,
            slide_type: SlideType, slide_size: QSize,
            description: str, is_archived: bool
        ) -> None:
        self._id = _id
        self._shelf_name = shelf_name
        self._name = name
        self._create_on = create_on
        self._change_on = change_on
        self._slide_type = slide_type
        self._slide_size = slide_size
        self._description = description
        self._is_archived = bool(is_archived)

    @property
    def id(self) -> int:
        return self._id

    @property
    def shelf_name(self) -> str:
        return self._shelf_name

    @shelf_name.setter
    def shelf_name(self, value: str) -> None:
        self._shelf_name = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def create_on(self) -> QDateTime:
        return self._create_on

    @property
    def change_on(self) -> QDateTime:
        return self._change_on

    @change_on.setter
    def change_on(self, value: QDateTime) -> None:
        self._change_on = value

    @property
    def slide_type(self) -> SlideType:
        return self._slide_type

    @property
    def slide_size(self) -> QSize:
        if self._slide_type == SlideType.CUSTOM:
            return self._slide_size

        return self.slide_type.value

    @slide_size.setter
    def slide_size(self, value: QSize) -> None:
        if self.slide_type != SlideType.CUSTOM:
            return

        self._slide_size = value


    @slide_type.setter
    def slide_type(self, value: SlideType) -> None:
        self._slide_type = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        self._description = value

    @property
    def is_archived(self) -> bool:
        return self._is_archived

    @is_archived.setter
    def is_archived(self, value: bool) -> None:
        self._is_archived = bool(value)

    def __str__(self) -> str:
        return f"AlbumModel(id={self._id}, shelf_id={self._shelf_name}, name={self._name}, slide_type={self.slide_type}, slide_size={self.slide_size}, is_archived={self._is_archived})"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, __value: object) -> bool:
        if __value is None:
            return False

        if not isinstance(__value, AlbumModel):
            return False

        return self._id == __value._id or self._name == __value._name


EMPTY_ALBUM = AlbumModel(
    -1, "", "", QDateTime.currentDateTime(), QDateTime.currentDateTime(),
    SlideType.A4_VERTICAL, SlideType.A4_VERTICAL.value, "", False
)
