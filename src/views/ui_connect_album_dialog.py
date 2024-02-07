# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connect_album_dialog.ui'
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
	QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
	QSpacerItem, QVBoxLayout, QWidget)

class Ui_ConnectAlbumDialog(object):
	def setupUi(self, ConnectAlbumDialog):
		if not ConnectAlbumDialog.objectName():
			ConnectAlbumDialog.setObjectName(u"ConnectAlbumDialog")
		ConnectAlbumDialog.resize(775, 600)
		ConnectAlbumDialog.setMinimumSize(QSize(600, 450))
		ConnectAlbumDialog.setMaximumSize(QSize(900, 600))
		ConnectAlbumDialog.setModal(True)
		self.vLayout_3 = QVBoxLayout(ConnectAlbumDialog)
		self.vLayout_3.setObjectName(u"vLayout_3")
		self.hLayout_2 = QHBoxLayout()
		self.hLayout_2.setObjectName(u"hLayout_2")
		self.img_lbl_1 = QLabel(ConnectAlbumDialog)
		self.img_lbl_1.setObjectName(u"img_lbl_1")
		self.img_lbl_1.setAlignment(Qt.AlignCenter)

		self.hLayout_2.addWidget(self.img_lbl_1)

		self.title_lbl = QLabel(ConnectAlbumDialog)
		self.title_lbl.setObjectName(u"title_lbl")
		self.title_lbl.setTextFormat(Qt.MarkdownText)
		self.title_lbl.setAlignment(Qt.AlignCenter)

		self.hLayout_2.addWidget(self.title_lbl)

		self.hSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.hLayout_2.addItem(self.hSpacer_2)


		self.vLayout_3.addLayout(self.hLayout_2)

		self.hLayout_3 = QHBoxLayout()
		self.hLayout_3.setObjectName(u"hLayout_3")
		self.vLayout_4 = QVBoxLayout()
		self.vLayout_4.setObjectName(u"vLayout_4")
		self.info_lbl_1 = QLabel(ConnectAlbumDialog)
		self.info_lbl_1.setObjectName(u"info_lbl_1")
		self.info_lbl_1.setTextFormat(Qt.MarkdownText)
		self.info_lbl_1.setAlignment(Qt.AlignCenter)

		self.vLayout_4.addWidget(self.info_lbl_1)

		self.global_albums_list = QListWidget(ConnectAlbumDialog)
		self.global_albums_list.setObjectName(u"global_albums_list")

		self.vLayout_4.addWidget(self.global_albums_list)


		self.hLayout_3.addLayout(self.vLayout_4)

		self.vLayout_2 = QVBoxLayout()
		self.vLayout_2.setObjectName(u"vLayout_2")
		self.add_album_to_shelf_btn = QPushButton(ConnectAlbumDialog)
		self.add_album_to_shelf_btn.setObjectName(u"add_album_to_shelf_btn")

		self.vLayout_2.addWidget(self.add_album_to_shelf_btn)

		self.remove_album_from_shelf_btn = QPushButton(ConnectAlbumDialog)
		self.remove_album_from_shelf_btn.setObjectName(u"remove_album_from_shelf_btn")

		self.vLayout_2.addWidget(self.remove_album_from_shelf_btn)

		self.vSpacer_1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

		self.vLayout_2.addItem(self.vSpacer_1)


		self.hLayout_3.addLayout(self.vLayout_2)

		self.vLayout_1 = QVBoxLayout()
		self.vLayout_1.setObjectName(u"vLayout_1")
		self.info_lbl_2 = QLabel(ConnectAlbumDialog)
		self.info_lbl_2.setObjectName(u"info_lbl_2")
		self.info_lbl_2.setTextFormat(Qt.MarkdownText)
		self.info_lbl_2.setAlignment(Qt.AlignCenter)

		self.vLayout_1.addWidget(self.info_lbl_2)

		self.shelf_albums_list = QListWidget(ConnectAlbumDialog)
		self.shelf_albums_list.setObjectName(u"shelf_albums_list")

		self.vLayout_1.addWidget(self.shelf_albums_list)


		self.hLayout_3.addLayout(self.vLayout_1)


		self.vLayout_3.addLayout(self.hLayout_3)

		self.hLayout_1 = QHBoxLayout()
		self.hLayout_1.setObjectName(u"hLayout_1")
		self.hSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.hLayout_1.addItem(self.hSpacer_1)

		self.save_btn = QPushButton(ConnectAlbumDialog)
		self.save_btn.setObjectName(u"save_btn")

		self.hLayout_1.addWidget(self.save_btn)


		self.vLayout_3.addLayout(self.hLayout_1)


		self.retranslateUi(ConnectAlbumDialog)

		QMetaObject.connectSlotsByName(ConnectAlbumDialog)
	# setupUi

	def retranslateUi(self, ConnectAlbumDialog):
		ConnectAlbumDialog.setWindowTitle(QCoreApplication.translate("ConnectAlbumDialog", u"Dialog", None))
		self.img_lbl_1.setText("")
		self.title_lbl.setText(QCoreApplication.translate("ConnectAlbumDialog", u"## Shelf Edit Title", None))
		self.info_lbl_1.setText(QCoreApplication.translate("ConnectAlbumDialog", u"### Global albums", None))
		self.add_album_to_shelf_btn.setText(QCoreApplication.translate("ConnectAlbumDialog", u"Add to shelf", None))
		self.remove_album_from_shelf_btn.setText(QCoreApplication.translate("ConnectAlbumDialog", u"Remove from shelf", None))
		self.info_lbl_2.setText(QCoreApplication.translate("ConnectAlbumDialog", u"### Shelfs albums", None))
		self.save_btn.setText(QCoreApplication.translate("ConnectAlbumDialog", u"Save", None))
#if QT_CONFIG(shortcut)
		self.save_btn.setShortcut(QCoreApplication.translate("ConnectAlbumDialog", u"Return", None))
#endif // QT_CONFIG(shortcut)
	# retranslateUi

