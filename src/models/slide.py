from PySide6.QtGui import QPixmap


class SlideModel:

    def __init__(self, _id, album_name: str, position: int, filepath: str) -> None:
        self._id = _id
        self._album_name = album_name
        self._position = position
        self._pixmap = QPixmap(filepath)

        assert not self._pixmap.isNull()

    @property
    def id(self) -> int:
        return self._id

    @property
    def album_name(self) -> str:
        return self._album_name

    @property
    def position(self) -> int:
        return self._position

    @position.setter
    def position(self, value: int) -> None:
        if value < 0:
            return

        self._position = value

    @property
    def pixmap(self) -> QPixmap:
        return self._pixmap

    def __str__(self) -> str:
        return f"SlideModel(id={self._id}, album_name={self._album_name}, position={self._position})"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, __value: object) -> bool:
        if __value is None:
            return False

        if not isinstance(__value, SlideModel):
            return False

        return self._id == __value._id or (
            self._album_name == __value._album_name and
            self._position == __value._position
        )
