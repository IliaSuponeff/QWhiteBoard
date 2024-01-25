# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
	QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
	QVBoxLayout, QWidget)

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		if not MainWindow.objectName():
			MainWindow.setObjectName(u"MainWindow")
		MainWindow.resize(800, 600)
		self.central_widget = QWidget(MainWindow)
		self.central_widget.setObjectName(u"central_widget")
		self.vLayout_1 = QVBoxLayout(self.central_widget)
		self.vLayout_1.setObjectName(u"vLayout_1")
		self.hLayout_1 = QHBoxLayout()
		self.hLayout_1.setObjectName(u"hLayout_1")
		self.app_icon_lbl = QLabel(self.central_widget)
		self.app_icon_lbl.setObjectName(u"app_icon_lbl")
		self.app_icon_lbl.setAlignment(Qt.AlignCenter)

		self.hLayout_1.addWidget(self.app_icon_lbl)

		self.app_name_lbl = QLabel(self.central_widget)
		self.app_name_lbl.setObjectName(u"app_name_lbl")
		self.app_name_lbl.setTextFormat(Qt.MarkdownText)
		self.app_name_lbl.setAlignment(Qt.AlignCenter)

		self.hLayout_1.addWidget(self.app_name_lbl)

		self.hSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.hLayout_1.addItem(self.hSpacer)

		self.settings_btn = QPushButton(self.central_widget)
		self.settings_btn.setObjectName(u"settings_btn")
		self.settings_btn.setIconSize(QSize(32, 32))
		self.settings_btn.setFlat(False)

		self.hLayout_1.addWidget(self.settings_btn)


		self.vLayout_1.addLayout(self.hLayout_1)

		self.pages_stack_widget = QStackedWidget(self.central_widget)
		self.pages_stack_widget.setObjectName(u"pages_stack_widget")
		self.page = QWidget()
		self.page.setObjectName(u"page")
		self.pages_stack_widget.addWidget(self.page)
		self.page_2 = QWidget()
		self.page_2.setObjectName(u"page_2")
		self.pages_stack_widget.addWidget(self.page_2)

		self.vLayout_1.addWidget(self.pages_stack_widget)

		MainWindow.setCentralWidget(self.central_widget)

		self.retranslateUi(MainWindow)

		self.settings_btn.setDefault(False)


		QMetaObject.connectSlotsByName(MainWindow)
	# setupUi

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
		self.app_icon_lbl.setText("")
		self.app_name_lbl.setText(QCoreApplication.translate("MainWindow", u"# Title", None))
		self.settings_btn.setText("")
	# retranslateUi

