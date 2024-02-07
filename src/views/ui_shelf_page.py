# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shelf_page.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
	QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
	QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_ShelfPage(object):
	def setupUi(self, ShelfPage):
		if not ShelfPage.objectName():
			ShelfPage.setObjectName(u"ShelfPage")
		ShelfPage.resize(717, 637)
		self.vLayout_2 = QVBoxLayout(ShelfPage)
		self.vLayout_2.setObjectName(u"vLayout_2")
		self.hLayout_3 = QHBoxLayout()
		self.hLayout_3.setObjectName(u"hLayout_3")
		self.back_btn = QPushButton(ShelfPage)
		self.back_btn.setObjectName(u"back_btn")

		self.hLayout_3.addWidget(self.back_btn)

		self.img_lbl_1 = QLabel(ShelfPage)
		self.img_lbl_1.setObjectName(u"img_lbl_1")
		self.img_lbl_1.setAlignment(Qt.AlignCenter)

		self.hLayout_3.addWidget(self.img_lbl_1)

		self.shelf_name_lbl = QLabel(ShelfPage)
		self.shelf_name_lbl.setObjectName(u"shelf_name_lbl")
		self.shelf_name_lbl.setTextFormat(Qt.MarkdownText)
		self.shelf_name_lbl.setAlignment(Qt.AlignCenter)

		self.hLayout_3.addWidget(self.shelf_name_lbl)

		self.hSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.hLayout_3.addItem(self.hSpacer_1)


		self.vLayout_2.addLayout(self.hLayout_3)

		self.hLayout_2 = QHBoxLayout()
		self.hLayout_2.setObjectName(u"hLayout_2")
		self.albums_tools_frame = QFrame(ShelfPage)
		self.albums_tools_frame.setObjectName(u"albums_tools_frame")
		sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(2)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.albums_tools_frame.sizePolicy().hasHeightForWidth())
		self.albums_tools_frame.setSizePolicy(sizePolicy)
		self.vLayout_1 = QVBoxLayout(self.albums_tools_frame)
		self.vLayout_1.setObjectName(u"vLayout_1")
		self.hLayout_1 = QHBoxLayout()
		self.hLayout_1.setObjectName(u"hLayout_1")
		self.add_new_album_btn = QPushButton(self.albums_tools_frame)
		self.add_new_album_btn.setObjectName(u"add_new_album_btn")

		self.hLayout_1.addWidget(self.add_new_album_btn)

		self.connect_album_btn = QPushButton(self.albums_tools_frame)
		self.connect_album_btn.setObjectName(u"connect_album_btn")

		self.hLayout_1.addWidget(self.connect_album_btn)

		self.disconnect_album_btn = QPushButton(self.albums_tools_frame)
		self.disconnect_album_btn.setObjectName(u"disconnect_album_btn")

		self.hLayout_1.addWidget(self.disconnect_album_btn)


		self.vLayout_1.addLayout(self.hLayout_1)

		self.albums_list = QListWidget(self.albums_tools_frame)
		self.albums_list.setObjectName(u"albums_list")

		self.vLayout_1.addWidget(self.albums_list)


		self.hLayout_2.addWidget(self.albums_tools_frame)

		self.albums_info_stack = QStackedWidget(ShelfPage)
		self.albums_info_stack.setObjectName(u"albums_info_stack")
		sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		sizePolicy1.setHorizontalStretch(3)
		sizePolicy1.setVerticalStretch(0)
		sizePolicy1.setHeightForWidth(self.albums_info_stack.sizePolicy().hasHeightForWidth())
		self.albums_info_stack.setSizePolicy(sizePolicy1)
		self.albums_info_stack.setFrameShape(QFrame.StyledPanel)
		self.albums_info_stack.setFrameShadow(QFrame.Raised)
		self.empty_page = QWidget()
		self.empty_page.setObjectName(u"empty_page")
		self.albums_info_stack.addWidget(self.empty_page)

		self.hLayout_2.addWidget(self.albums_info_stack)


		self.vLayout_2.addLayout(self.hLayout_2)


		self.retranslateUi(ShelfPage)

		QMetaObject.connectSlotsByName(ShelfPage)
	# setupUi

	def retranslateUi(self, ShelfPage):
		ShelfPage.setWindowTitle(QCoreApplication.translate("ShelfPage", u"Form", None))
		self.back_btn.setText("")
		self.img_lbl_1.setText("")
		self.shelf_name_lbl.setText(QCoreApplication.translate("ShelfPage", u"# ShelfName", None))
		self.add_new_album_btn.setText(QCoreApplication.translate("ShelfPage", u"Add new album", None))
		self.connect_album_btn.setText(QCoreApplication.translate("ShelfPage", u"Connect  album", None))
		self.disconnect_album_btn.setText(QCoreApplication.translate("ShelfPage", u"Disconnect  album", None))
	# retranslateUi

