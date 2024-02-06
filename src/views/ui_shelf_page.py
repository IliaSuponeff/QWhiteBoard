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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QListWidget,
	QListWidgetItem, QPushButton, QSizePolicy, QStackedWidget,
	QVBoxLayout, QWidget)

class Ui_ShelfPage(object):
	def setupUi(self, ShelfPage):
		if not ShelfPage.objectName():
			ShelfPage.setObjectName(u"ShelfPage")
		ShelfPage.resize(717, 637)
		self.hLayout_2 = QHBoxLayout(ShelfPage)
		self.hLayout_2.setObjectName(u"hLayout_2")
		self.vLayout_1 = QVBoxLayout()
		self.vLayout_1.setObjectName(u"vLayout_1")
		self.hLayout_1 = QHBoxLayout()
		self.hLayout_1.setObjectName(u"hLayout_1")
		self.back_btn = QPushButton(ShelfPage)
		self.back_btn.setObjectName(u"back_btn")

		self.hLayout_1.addWidget(self.back_btn)

		self.add_new_album_btn = QPushButton(ShelfPage)
		self.add_new_album_btn.setObjectName(u"add_new_album_btn")

		self.hLayout_1.addWidget(self.add_new_album_btn)

		self.connect_album_btn = QPushButton(ShelfPage)
		self.connect_album_btn.setObjectName(u"connect_album_btn")

		self.hLayout_1.addWidget(self.connect_album_btn)

		self.disconnect_album_btn = QPushButton(ShelfPage)
		self.disconnect_album_btn.setObjectName(u"disconnect_album_btn")

		self.hLayout_1.addWidget(self.disconnect_album_btn)


		self.vLayout_1.addLayout(self.hLayout_1)

		self.albums_list = QListWidget(ShelfPage)
		self.albums_list.setObjectName(u"albums_list")

		self.vLayout_1.addWidget(self.albums_list)


		self.hLayout_2.addLayout(self.vLayout_1)

		self.albums_info_stack = QStackedWidget(ShelfPage)
		self.albums_info_stack.setObjectName(u"albums_info_stack")
		sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(3)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.albums_info_stack.sizePolicy().hasHeightForWidth())
		self.albums_info_stack.setSizePolicy(sizePolicy)
		self.albums_info_stack.setFrameShape(QFrame.StyledPanel)
		self.albums_info_stack.setFrameShadow(QFrame.Raised)
		self.empty_page = QWidget()
		self.empty_page.setObjectName(u"empty_page")
		self.albums_info_stack.addWidget(self.empty_page)

		self.hLayout_2.addWidget(self.albums_info_stack)


		self.retranslateUi(ShelfPage)

		QMetaObject.connectSlotsByName(ShelfPage)
	# setupUi

	def retranslateUi(self, ShelfPage):
		ShelfPage.setWindowTitle(QCoreApplication.translate("ShelfPage", u"Form", None))
		self.back_btn.setText("")
		self.add_new_album_btn.setText(QCoreApplication.translate("ShelfPage", u"Add new album", None))
		self.connect_album_btn.setText(QCoreApplication.translate("ShelfPage", u"Connect  album", None))
		self.disconnect_album_btn.setText(QCoreApplication.translate("ShelfPage", u"Disconnect  album", None))
	# retranslateUi

