# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'album_construct_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDialog,
	QFrame, QHBoxLayout, QLabel, QLineEdit,
	QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
	QTextEdit, QVBoxLayout, QWidget)

class Ui_AlbumConstructDialog(object):
	def setupUi(self, AlbumConstructDialog):
		if not AlbumConstructDialog.objectName():
			AlbumConstructDialog.setObjectName(u"AlbumConstructDialog")
		AlbumConstructDialog.setWindowModality(Qt.ApplicationModal)
		AlbumConstructDialog.resize(600, 600)
		AlbumConstructDialog.setMinimumSize(QSize(600, 400))
		AlbumConstructDialog.setModal(True)
		self.vLayout_1 = QVBoxLayout(AlbumConstructDialog)
		self.vLayout_1.setObjectName(u"vLayout_1")
		self.hLayout_1 = QHBoxLayout()
		self.hLayout_1.setObjectName(u"hLayout_1")
		self.info_lbl_1 = QLabel(AlbumConstructDialog)
		self.info_lbl_1.setObjectName(u"info_lbl_1")
		self.info_lbl_1.setTextFormat(Qt.MarkdownText)
		self.info_lbl_1.setAlignment(Qt.AlignCenter)

		self.hLayout_1.addWidget(self.info_lbl_1)

		self.name_le = QLineEdit(AlbumConstructDialog)
		self.name_le.setObjectName(u"name_le")
		self.name_le.setAlignment(Qt.AlignCenter)

		self.hLayout_1.addWidget(self.name_le)

		self.album_img_lbl = QLabel(AlbumConstructDialog)
		self.album_img_lbl.setObjectName(u"album_img_lbl")
		self.album_img_lbl.setAlignment(Qt.AlignCenter)

		self.hLayout_1.addWidget(self.album_img_lbl)


		self.vLayout_1.addLayout(self.hLayout_1)

		self.hLayout_2 = QHBoxLayout()
		self.hLayout_2.setObjectName(u"hLayout_2")
		self.slide_img_lbl = QLabel(AlbumConstructDialog)
		self.slide_img_lbl.setObjectName(u"slide_img_lbl")
		self.slide_img_lbl.setAlignment(Qt.AlignCenter)

		self.hLayout_2.addWidget(self.slide_img_lbl)

		self.info_lbl_2 = QLabel(AlbumConstructDialog)
		self.info_lbl_2.setObjectName(u"info_lbl_2")
		self.info_lbl_2.setTextFormat(Qt.MarkdownText)
		self.info_lbl_2.setAlignment(Qt.AlignCenter)

		self.hLayout_2.addWidget(self.info_lbl_2)

		self.slide_type_box = QComboBox(AlbumConstructDialog)
		self.slide_type_box.setObjectName(u"slide_type_box")
		self.slide_type_box.setSizeAdjustPolicy(QComboBox.AdjustToContents)
		self.slide_type_box.setModelColumn(0)

		self.hLayout_2.addWidget(self.slide_type_box)


		self.vLayout_1.addLayout(self.hLayout_2)

		self.size_edit_frame = QFrame(AlbumConstructDialog)
		self.size_edit_frame.setObjectName(u"size_edit_frame")
		self.horizontalLayout_3 = QHBoxLayout(self.size_edit_frame)
		self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
		self.info_lbl_4 = QLabel(self.size_edit_frame)
		self.info_lbl_4.setObjectName(u"info_lbl_4")
		self.info_lbl_4.setTextFormat(Qt.MarkdownText)
		self.info_lbl_4.setAlignment(Qt.AlignCenter)

		self.horizontalLayout_3.addWidget(self.info_lbl_4)

		self.width_edit = QSpinBox(self.size_edit_frame)
		self.width_edit.setObjectName(u"width_edit")
		sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.width_edit.sizePolicy().hasHeightForWidth())
		self.width_edit.setSizePolicy(sizePolicy)
		self.width_edit.setAlignment(Qt.AlignCenter)
		self.width_edit.setButtonSymbols(QAbstractSpinBox.NoButtons)

		self.horizontalLayout_3.addWidget(self.width_edit)

		self.size_img_lbl = QLabel(self.size_edit_frame)
		self.size_img_lbl.setObjectName(u"size_img_lbl")
		self.size_img_lbl.setAlignment(Qt.AlignCenter)

		self.horizontalLayout_3.addWidget(self.size_img_lbl)

		self.info_lbl_5 = QLabel(self.size_edit_frame)
		self.info_lbl_5.setObjectName(u"info_lbl_5")
		self.info_lbl_5.setTextFormat(Qt.MarkdownText)
		self.info_lbl_5.setAlignment(Qt.AlignCenter)

		self.horizontalLayout_3.addWidget(self.info_lbl_5)

		self.heigth_edit = QSpinBox(self.size_edit_frame)
		self.heigth_edit.setObjectName(u"heigth_edit")
		sizePolicy.setHeightForWidth(self.heigth_edit.sizePolicy().hasHeightForWidth())
		self.heigth_edit.setSizePolicy(sizePolicy)
		self.heigth_edit.setAlignment(Qt.AlignCenter)
		self.heigth_edit.setButtonSymbols(QAbstractSpinBox.NoButtons)

		self.horizontalLayout_3.addWidget(self.heigth_edit)


		self.vLayout_1.addWidget(self.size_edit_frame)

		self.info_lbl_3 = QLabel(AlbumConstructDialog)
		self.info_lbl_3.setObjectName(u"info_lbl_3")
		self.info_lbl_3.setTextFormat(Qt.MarkdownText)
		self.info_lbl_3.setAlignment(Qt.AlignCenter)

		self.vLayout_1.addWidget(self.info_lbl_3)

		self.description_text_edit = QTextEdit(AlbumConstructDialog)
		self.description_text_edit.setObjectName(u"description_text_edit")

		self.vLayout_1.addWidget(self.description_text_edit)

		self.hLayout_3 = QHBoxLayout()
		self.hLayout_3.setObjectName(u"hLayout_3")
		self.hSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.hLayout_3.addItem(self.hSpacer_1)

		self.construct_btn = QPushButton(AlbumConstructDialog)
		self.construct_btn.setObjectName(u"construct_btn")

		self.hLayout_3.addWidget(self.construct_btn)


		self.vLayout_1.addLayout(self.hLayout_3)


		self.retranslateUi(AlbumConstructDialog)

		self.slide_type_box.setCurrentIndex(-1)


		QMetaObject.connectSlotsByName(AlbumConstructDialog)
	# setupUi

	def retranslateUi(self, AlbumConstructDialog):
		AlbumConstructDialog.setWindowTitle(QCoreApplication.translate("AlbumConstructDialog", u"Dialog", None))
		self.info_lbl_1.setText(QCoreApplication.translate("AlbumConstructDialog", u"## Album name", None))
		self.name_le.setInputMask("")
		self.album_img_lbl.setText("")
		self.slide_img_lbl.setText("")
		self.info_lbl_2.setText(QCoreApplication.translate("AlbumConstructDialog", u"## Slide Type", None))
		self.info_lbl_4.setText(QCoreApplication.translate("AlbumConstructDialog", u"### Width", None))
		self.size_img_lbl.setText("")
		self.info_lbl_5.setText(QCoreApplication.translate("AlbumConstructDialog", u"### Height", None))
		self.info_lbl_3.setText(QCoreApplication.translate("AlbumConstructDialog", u"## Description", None))
		self.construct_btn.setText(QCoreApplication.translate("AlbumConstructDialog", u"Construct", None))
	# retranslateUi

