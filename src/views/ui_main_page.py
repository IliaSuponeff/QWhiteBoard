# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_page.ui'
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
	QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
	QVBoxLayout, QWidget)

class Ui_MainPage(object):
	def setupUi(self, MainPage):
		if not MainPage.objectName():
			MainPage.setObjectName(u"MainPage")
		MainPage.resize(794, 623)
		self.hLayout_1 = QHBoxLayout(MainPage)
		self.hLayout_1.setObjectName(u"hLayout_1")
		self.list_tools_frame = QFrame(MainPage)
		self.list_tools_frame.setObjectName(u"list_tools_frame")
		sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(2)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.list_tools_frame.sizePolicy().hasHeightForWidth())
		self.list_tools_frame.setSizePolicy(sizePolicy)
		self.vLayout_1 = QVBoxLayout(self.list_tools_frame)
		self.vLayout_1.setObjectName(u"vLayout_1")
		self.hLayout_2 = QHBoxLayout()
		self.hLayout_2.setObjectName(u"hLayout_2")
		self.add_album_btn = QPushButton(self.list_tools_frame)
		self.add_album_btn.setObjectName(u"add_album_btn")

		self.hLayout_2.addWidget(self.add_album_btn)

		self.hSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.hLayout_2.addItem(self.hSpacer_1)


		self.vLayout_1.addLayout(self.hLayout_2)

		self.items_list_widget = QListWidget(self.list_tools_frame)
		self.items_list_widget.setObjectName(u"items_list_widget")
		sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		sizePolicy1.setHorizontalStretch(1)
		sizePolicy1.setVerticalStretch(0)
		sizePolicy1.setHeightForWidth(self.items_list_widget.sizePolicy().hasHeightForWidth())
		self.items_list_widget.setSizePolicy(sizePolicy1)

		self.vLayout_1.addWidget(self.items_list_widget)


		self.hLayout_1.addWidget(self.list_tools_frame)

		self.album_info_frame = QFrame(MainPage)
		self.album_info_frame.setObjectName(u"album_info_frame")
		sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		sizePolicy2.setHorizontalStretch(3)
		sizePolicy2.setVerticalStretch(0)
		sizePolicy2.setHeightForWidth(self.album_info_frame.sizePolicy().hasHeightForWidth())
		self.album_info_frame.setSizePolicy(sizePolicy2)
		self.album_info_frame.setFrameShape(QFrame.StyledPanel)
		self.album_info_frame.setFrameShadow(QFrame.Raised)

		self.hLayout_1.addWidget(self.album_info_frame)


		self.retranslateUi(MainPage)

		QMetaObject.connectSlotsByName(MainPage)
	# setupUi

	def retranslateUi(self, MainPage):
		MainPage.setWindowTitle(QCoreApplication.translate("MainPage", u"Form", None))
		self.add_album_btn.setText(QCoreApplication.translate("MainPage", u"Add album", None))
	# retranslateUi

