# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'album_info_page.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
	QMetaObject, QObject, QPoint, QRect,
	QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
	QFont, QFontDatabase, QGradient, QIcon,
	QImage, QKeySequence, QLinearGradient, QPainter,
	QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDateTimeEdit, QGridLayout,
	QHBoxLayout, QLabel, QLineEdit, QPushButton,
	QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
	QWidget)

class Ui_AlbumInfoPage(object):
	def setupUi(self, AlbumInfoPage):
		if not AlbumInfoPage.objectName():
			AlbumInfoPage.setObjectName(u"AlbumInfoPage")
		AlbumInfoPage.resize(691, 583)
		AlbumInfoPage.setMaximumSize(QSize(16777215, 16777215))
		self.verticalLayout = QVBoxLayout(AlbumInfoPage)
		self.verticalLayout.setObjectName(u"verticalLayout")
		self.album_name_lbl = QLabel(AlbumInfoPage)
		self.album_name_lbl.setObjectName(u"album_name_lbl")
		self.album_name_lbl.setTextFormat(Qt.MarkdownText)
		self.album_name_lbl.setAlignment(Qt.AlignCenter)

		self.verticalLayout.addWidget(self.album_name_lbl)

		self.gLayout_1 = QGridLayout()
		self.gLayout_1.setObjectName(u"gLayout_1")
		self.info_lbl_1 = QLabel(AlbumInfoPage)
		self.info_lbl_1.setObjectName(u"info_lbl_1")
		self.info_lbl_1.setTextFormat(Qt.MarkdownText)
		self.info_lbl_1.setAlignment(Qt.AlignCenter)

		self.gLayout_1.addWidget(self.info_lbl_1, 0, 0, 1, 1)

		self.create_datetime_edit = QDateTimeEdit(AlbumInfoPage)
		self.create_datetime_edit.setObjectName(u"create_datetime_edit")
		sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.create_datetime_edit.sizePolicy().hasHeightForWidth())
		self.create_datetime_edit.setSizePolicy(sizePolicy)
		self.create_datetime_edit.setFocusPolicy(Qt.NoFocus)
		self.create_datetime_edit.setWrapping(True)
		self.create_datetime_edit.setAlignment(Qt.AlignCenter)
		self.create_datetime_edit.setReadOnly(True)
		self.create_datetime_edit.setButtonSymbols(QAbstractSpinBox.NoButtons)
		self.create_datetime_edit.setCalendarPopup(False)

		self.gLayout_1.addWidget(self.create_datetime_edit, 0, 1, 1, 1)

		self.info_lbl_2 = QLabel(AlbumInfoPage)
		self.info_lbl_2.setObjectName(u"info_lbl_2")
		self.info_lbl_2.setTextFormat(Qt.MarkdownText)
		self.info_lbl_2.setAlignment(Qt.AlignCenter)

		self.gLayout_1.addWidget(self.info_lbl_2, 1, 0, 1, 1)

		self.chage_datetime_edit = QDateTimeEdit(AlbumInfoPage)
		self.chage_datetime_edit.setObjectName(u"chage_datetime_edit")
		self.chage_datetime_edit.setFocusPolicy(Qt.NoFocus)
		self.chage_datetime_edit.setWrapping(True)
		self.chage_datetime_edit.setAlignment(Qt.AlignCenter)
		self.chage_datetime_edit.setReadOnly(True)
		self.chage_datetime_edit.setButtonSymbols(QAbstractSpinBox.NoButtons)
		self.chage_datetime_edit.setCalendarPopup(False)

		self.gLayout_1.addWidget(self.chage_datetime_edit, 1, 1, 1, 1)

		self.hLayout_1 = QHBoxLayout()
		self.hLayout_1.setObjectName(u"hLayout_1")
		self.slide_type_le = QLineEdit(AlbumInfoPage)
		self.slide_type_le.setObjectName(u"slide_type_le")
		self.slide_type_le.setAlignment(Qt.AlignCenter)
		self.slide_type_le.setReadOnly(True)

		self.hLayout_1.addWidget(self.slide_type_le)

		self.info_lbl_4 = QLabel(AlbumInfoPage)
		self.info_lbl_4.setObjectName(u"info_lbl_4")
		self.info_lbl_4.setTextFormat(Qt.MarkdownText)
		self.info_lbl_4.setAlignment(Qt.AlignCenter)

		self.hLayout_1.addWidget(self.info_lbl_4)

		self.slide_size_le = QLineEdit(AlbumInfoPage)
		self.slide_size_le.setObjectName(u"slide_size_le")
		self.slide_size_le.setAlignment(Qt.AlignCenter)
		self.slide_size_le.setReadOnly(True)

		self.hLayout_1.addWidget(self.slide_size_le)


		self.gLayout_1.addLayout(self.hLayout_1, 2, 1, 1, 1)

		self.info_lbl_3 = QLabel(AlbumInfoPage)
		self.info_lbl_3.setObjectName(u"info_lbl_3")
		self.info_lbl_3.setTextFormat(Qt.MarkdownText)
		self.info_lbl_3.setAlignment(Qt.AlignCenter)

		self.gLayout_1.addWidget(self.info_lbl_3, 2, 0, 1, 1)


		self.verticalLayout.addLayout(self.gLayout_1)

		self.info_lbl_5 = QLabel(AlbumInfoPage)
		self.info_lbl_5.setObjectName(u"info_lbl_5")
		self.info_lbl_5.setTextFormat(Qt.MarkdownText)
		self.info_lbl_5.setAlignment(Qt.AlignCenter)

		self.verticalLayout.addWidget(self.info_lbl_5)

		self.description_te = QTextEdit(AlbumInfoPage)
		self.description_te.setObjectName(u"description_te")
		self.description_te.setReadOnly(True)

		self.verticalLayout.addWidget(self.description_te)

		self.hLayout_2 = QHBoxLayout()
		self.hLayout_2.setObjectName(u"hLayout_2")
		self.hSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.hLayout_2.addItem(self.hSpacer_1)

		self.open_album_btn = QPushButton(AlbumInfoPage)
		self.open_album_btn.setObjectName(u"open_album_btn")

		self.hLayout_2.addWidget(self.open_album_btn)

		self.edit_album_btn = QPushButton(AlbumInfoPage)
		self.edit_album_btn.setObjectName(u"edit_album_btn")

		self.hLayout_2.addWidget(self.edit_album_btn)

		self.archive_swap_btn = QPushButton(AlbumInfoPage)
		self.archive_swap_btn.setObjectName(u"archive_swap_btn")

		self.hLayout_2.addWidget(self.archive_swap_btn)

		self.delete_album_btn = QPushButton(AlbumInfoPage)
		self.delete_album_btn.setObjectName(u"delete_album_btn")

		self.hLayout_2.addWidget(self.delete_album_btn)


		self.verticalLayout.addLayout(self.hLayout_2)

		self.vSpacer_1 = QSpacerItem(20, 192, QSizePolicy.Minimum, QSizePolicy.Expanding)

		self.verticalLayout.addItem(self.vSpacer_1)


		self.retranslateUi(AlbumInfoPage)

		QMetaObject.connectSlotsByName(AlbumInfoPage)
	# setupUi

	def retranslateUi(self, AlbumInfoPage):
		AlbumInfoPage.setWindowTitle(QCoreApplication.translate("AlbumInfoPage", u"Form", None))
		self.album_name_lbl.setText(QCoreApplication.translate("AlbumInfoPage", u"## AlbumName", None))
		self.info_lbl_1.setText(QCoreApplication.translate("AlbumInfoPage", u"### Create on", None))
		self.info_lbl_2.setText(QCoreApplication.translate("AlbumInfoPage", u"### Change on", None))
		self.slide_type_le.setText(QCoreApplication.translate("AlbumInfoPage", u"A4", None))
		self.info_lbl_4.setText(QCoreApplication.translate("AlbumInfoPage", u"### Slide Size", None))
		self.slide_size_le.setText(QCoreApplication.translate("AlbumInfoPage", u"2100x2970", None))
		self.info_lbl_3.setText(QCoreApplication.translate("AlbumInfoPage", u"### SlideType", None))
		self.info_lbl_5.setText(QCoreApplication.translate("AlbumInfoPage", u"### Description", None))
		self.description_te.setDocumentTitle("")
		self.open_album_btn.setText(QCoreApplication.translate("AlbumInfoPage", u"Open", None))
		self.edit_album_btn.setText(QCoreApplication.translate("AlbumInfoPage", u"Edit", None))
		self.archive_swap_btn.setText(QCoreApplication.translate("AlbumInfoPage", u"Archivate", None))
		self.delete_album_btn.setText(QCoreApplication.translate("AlbumInfoPage", u"Delete", None))
	# retranslateUi

