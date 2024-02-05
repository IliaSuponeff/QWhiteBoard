# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shelf_construct_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
	QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
	QTextEdit, QVBoxLayout, QWidget)

class Ui_ShelfConstructDialog(object):
	def setupUi(self, ShelfConstructDialog):
		if not ShelfConstructDialog.objectName():
			ShelfConstructDialog.setObjectName(u"ShelfConstructDialog")
		ShelfConstructDialog.setWindowModality(Qt.ApplicationModal)
		ShelfConstructDialog.resize(600, 600)
		ShelfConstructDialog.setMinimumSize(QSize(600, 400))
		ShelfConstructDialog.setModal(True)
		self.vLayout_1 = QVBoxLayout(ShelfConstructDialog)
		self.vLayout_1.setObjectName(u"vLayout_1")
		self.hLayout_1 = QHBoxLayout()
		self.hLayout_1.setObjectName(u"hLayout_1")
		self.info_lbl_1 = QLabel(ShelfConstructDialog)
		self.info_lbl_1.setObjectName(u"info_lbl_1")
		self.info_lbl_1.setTextFormat(Qt.MarkdownText)
		self.info_lbl_1.setAlignment(Qt.AlignCenter)

		self.hLayout_1.addWidget(self.info_lbl_1)

		self.name_le = QLineEdit(ShelfConstructDialog)
		self.name_le.setObjectName(u"name_le")
		self.name_le.setAlignment(Qt.AlignCenter)

		self.hLayout_1.addWidget(self.name_le)

		self.shelf_img_lbl = QLabel(ShelfConstructDialog)
		self.shelf_img_lbl.setObjectName(u"shelf_img_lbl")
		self.shelf_img_lbl.setAlignment(Qt.AlignCenter)

		self.hLayout_1.addWidget(self.shelf_img_lbl)


		self.vLayout_1.addLayout(self.hLayout_1)

		self.info_lbl_3 = QLabel(ShelfConstructDialog)
		self.info_lbl_3.setObjectName(u"info_lbl_3")
		self.info_lbl_3.setTextFormat(Qt.MarkdownText)
		self.info_lbl_3.setAlignment(Qt.AlignCenter)

		self.vLayout_1.addWidget(self.info_lbl_3)

		self.description_text_edit = QTextEdit(ShelfConstructDialog)
		self.description_text_edit.setObjectName(u"description_text_edit")

		self.vLayout_1.addWidget(self.description_text_edit)

		self.hLayout_3 = QHBoxLayout()
		self.hLayout_3.setObjectName(u"hLayout_3")
		self.hSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.hLayout_3.addItem(self.hSpacer_1)

		self.construct_btn = QPushButton(ShelfConstructDialog)
		self.construct_btn.setObjectName(u"construct_btn")

		self.hLayout_3.addWidget(self.construct_btn)


		self.vLayout_1.addLayout(self.hLayout_3)


		self.retranslateUi(ShelfConstructDialog)

		QMetaObject.connectSlotsByName(ShelfConstructDialog)
	# setupUi

	def retranslateUi(self, ShelfConstructDialog):
		ShelfConstructDialog.setWindowTitle(QCoreApplication.translate("ShelfConstructDialog", u"Dialog", None))
		self.info_lbl_1.setText(QCoreApplication.translate("ShelfConstructDialog", u"## Shelf name", None))
		self.name_le.setInputMask("")
		self.shelf_img_lbl.setText("")
		self.info_lbl_3.setText(QCoreApplication.translate("ShelfConstructDialog", u"## Description", None))
		self.construct_btn.setText(QCoreApplication.translate("ShelfConstructDialog", u"Construct", None))
	# retranslateUi

