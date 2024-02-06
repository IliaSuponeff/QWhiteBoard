# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shelf_info_page.ui'
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
	QHBoxLayout, QLabel, QPushButton, QSizePolicy,
	QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_ShelfInfoPage(object):
	def setupUi(self, ShelfInfoPage):
		if not ShelfInfoPage.objectName():
			ShelfInfoPage.setObjectName(u"ShelfInfoPage")
		ShelfInfoPage.resize(682, 583)
		self.verticalLayout = QVBoxLayout(ShelfInfoPage)
		self.verticalLayout.setObjectName(u"verticalLayout")
		self.shelf_name_lbl = QLabel(ShelfInfoPage)
		self.shelf_name_lbl.setObjectName(u"shelf_name_lbl")
		self.shelf_name_lbl.setTextFormat(Qt.MarkdownText)
		self.shelf_name_lbl.setAlignment(Qt.AlignCenter)

		self.verticalLayout.addWidget(self.shelf_name_lbl)

		self.gLayout_1 = QGridLayout()
		self.gLayout_1.setObjectName(u"gLayout_1")
		self.info_lbl_1 = QLabel(ShelfInfoPage)
		self.info_lbl_1.setObjectName(u"info_lbl_1")
		self.info_lbl_1.setTextFormat(Qt.MarkdownText)
		self.info_lbl_1.setAlignment(Qt.AlignCenter)

		self.gLayout_1.addWidget(self.info_lbl_1, 0, 0, 1, 1)

		self.info_lbl_2 = QLabel(ShelfInfoPage)
		self.info_lbl_2.setObjectName(u"info_lbl_2")
		self.info_lbl_2.setTextFormat(Qt.MarkdownText)
		self.info_lbl_2.setAlignment(Qt.AlignCenter)

		self.gLayout_1.addWidget(self.info_lbl_2, 1, 0, 1, 1)

		self.chage_datetime_edit = QDateTimeEdit(ShelfInfoPage)
		self.chage_datetime_edit.setObjectName(u"chage_datetime_edit")
		self.chage_datetime_edit.setFocusPolicy(Qt.NoFocus)
		self.chage_datetime_edit.setWrapping(True)
		self.chage_datetime_edit.setAlignment(Qt.AlignCenter)
		self.chage_datetime_edit.setReadOnly(True)
		self.chage_datetime_edit.setButtonSymbols(QAbstractSpinBox.NoButtons)
		self.chage_datetime_edit.setCalendarPopup(False)

		self.gLayout_1.addWidget(self.chage_datetime_edit, 1, 1, 1, 1)

		self.create_datetime_edit = QDateTimeEdit(ShelfInfoPage)
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


		self.verticalLayout.addLayout(self.gLayout_1)

		self.info_lbl_5 = QLabel(ShelfInfoPage)
		self.info_lbl_5.setObjectName(u"info_lbl_5")
		self.info_lbl_5.setTextFormat(Qt.MarkdownText)
		self.info_lbl_5.setAlignment(Qt.AlignCenter)

		self.verticalLayout.addWidget(self.info_lbl_5)

		self.description_te = QTextEdit(ShelfInfoPage)
		self.description_te.setObjectName(u"description_te")
		self.description_te.setReadOnly(True)

		self.verticalLayout.addWidget(self.description_te)

		self.hLayout_2 = QHBoxLayout()
		self.hLayout_2.setObjectName(u"hLayout_2")
		self.hSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.hLayout_2.addItem(self.hSpacer_1)

		self.open_shelf_btn = QPushButton(ShelfInfoPage)
		self.open_shelf_btn.setObjectName(u"open_shelf_btn")

		self.hLayout_2.addWidget(self.open_shelf_btn)

		self.edit_shelf_btn = QPushButton(ShelfInfoPage)
		self.edit_shelf_btn.setObjectName(u"edit_shelf_btn")

		self.hLayout_2.addWidget(self.edit_shelf_btn)

		self.archive_swap_btn = QPushButton(ShelfInfoPage)
		self.archive_swap_btn.setObjectName(u"archive_swap_btn")

		self.hLayout_2.addWidget(self.archive_swap_btn)

		self.delete_shelf_btn = QPushButton(ShelfInfoPage)
		self.delete_shelf_btn.setObjectName(u"delete_shelf_btn")

		self.hLayout_2.addWidget(self.delete_shelf_btn)


		self.verticalLayout.addLayout(self.hLayout_2)

		self.vSpacer_1 = QSpacerItem(20, 192, QSizePolicy.Minimum, QSizePolicy.Expanding)

		self.verticalLayout.addItem(self.vSpacer_1)


		self.retranslateUi(ShelfInfoPage)

		QMetaObject.connectSlotsByName(ShelfInfoPage)
	# setupUi

	def retranslateUi(self, ShelfInfoPage):
		ShelfInfoPage.setWindowTitle(QCoreApplication.translate("ShelfInfoPage", u"Form", None))
		self.shelf_name_lbl.setText(QCoreApplication.translate("ShelfInfoPage", u"## ShelfName", None))
		self.info_lbl_1.setText(QCoreApplication.translate("ShelfInfoPage", u"### Create on", None))
		self.info_lbl_2.setText(QCoreApplication.translate("ShelfInfoPage", u"### Change on", None))
		self.info_lbl_5.setText(QCoreApplication.translate("ShelfInfoPage", u"### Description", None))
		self.description_te.setDocumentTitle("")
		self.open_shelf_btn.setText(QCoreApplication.translate("ShelfInfoPage", u"Open", None))
		self.edit_shelf_btn.setText(QCoreApplication.translate("ShelfInfoPage", u"Edit", None))
		self.archive_swap_btn.setText(QCoreApplication.translate("ShelfInfoPage", u"Archivate", None))
		self.delete_shelf_btn.setText(QCoreApplication.translate("ShelfInfoPage", u"Delete", None))
	# retranslateUi

