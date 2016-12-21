# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setBaseSize(QtCore.QSize(640, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        self._mainTabs = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._mainTabs.sizePolicy().hasHeightForWidth())
        self._mainTabs.setSizePolicy(sizePolicy)
        self._mainTabs.setTabPosition(QtWidgets.QTabWidget.South)
        self._mainTabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self._mainTabs.setIconSize(QtCore.QSize(24, 24))
        self._mainTabs.setElideMode(QtCore.Qt.ElideNone)
        self._mainTabs.setUsesScrollButtons(True)
        self._mainTabs.setDocumentMode(False)
        self._mainTabs.setTabsClosable(False)
        self._mainTabs.setMovable(False)
        self._mainTabs.setTabBarAutoHide(False)
        self._mainTabs.setObjectName("_mainTabs")
        self._tabEditor = QtWidgets.QWidget()
        self._tabEditor.setObjectName("_tabEditor")
        self.verticalLayout = QtWidgets.QVBoxLayout(self._tabEditor)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self._editorPanel = QtWidgets.QToolBox(self._tabEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._editorPanel.sizePolicy().hasHeightForWidth())
        self._editorPanel.setSizePolicy(sizePolicy)
        self._editorPanel.setMinimumSize(QtCore.QSize(0, 0))
        self._editorPanel.setMaximumSize(QtCore.QSize(200, 16777215))
        self._editorPanel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self._editorPanel.setObjectName("_editorPanel")
        self._pageScene = QtWidgets.QWidget()
        self._pageScene.setGeometry(QtCore.QRect(0, 0, 103, 343))
        self._pageScene.setObjectName("_pageScene")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self._pageScene)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self._buttonResetScene = QtWidgets.QPushButton(self._pageScene)
        self._buttonResetScene.setObjectName("_buttonResetScene")
        self.verticalLayout_2.addWidget(self._buttonResetScene)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self._editorPanel.addItem(self._pageScene, "")
        self._pageObstacles = QtWidgets.QWidget()
        self._pageObstacles.setGeometry(QtCore.QRect(0, 0, 103, 343))
        self._pageObstacles.setObjectName("_pageObstacles")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self._pageObstacles)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self._buttonDrawObstacle = QtWidgets.QPushButton(self._pageObstacles)
        self._buttonDrawObstacle.setCheckable(True)
        self._buttonDrawObstacle.setChecked(False)
        self._buttonDrawObstacle.setAutoDefault(False)
        self._buttonDrawObstacle.setDefault(False)
        self._buttonDrawObstacle.setFlat(False)
        self._buttonDrawObstacle.setObjectName("_buttonDrawObstacle")
        self.verticalLayout_3.addWidget(self._buttonDrawObstacle)
        self._checkSnapToGrid = QtWidgets.QCheckBox(self._pageObstacles)
        self._checkSnapToGrid.setChecked(False)
        self._checkSnapToGrid.setTristate(False)
        self._checkSnapToGrid.setObjectName("_checkSnapToGrid")
        self.verticalLayout_3.addWidget(self._checkSnapToGrid)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self._editorPanel.addItem(self._pageObstacles, "")
        self.verticalLayout.addWidget(self._editorPanel)
        self._mainTabs.addTab(self._tabEditor, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self._mainTabs.addTab(self.widget, "")
        self.gridLayout.addWidget(self._mainTabs, 0, 0, 2, 1)
        self._sceneFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._sceneFrame.sizePolicy().hasHeightForWidth())
        self._sceneFrame.setSizePolicy(sizePolicy)
        self._sceneFrame.setMinimumSize(QtCore.QSize(400, 400))
        self._sceneFrame.setBaseSize(QtCore.QSize(300, 300))
        self._sceneFrame.setFrameShape(QtWidgets.QFrame.Box)
        self._sceneFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self._sceneFrame.setLineWidth(2)
        self._sceneFrame.setObjectName("_sceneFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self._sceneFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout.addWidget(self._sceneFrame, 0, 2, 2, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self._mainTabs.setCurrentIndex(0)
        self._editorPanel.setCurrentIndex(0)
        self._editorPanel.layout().setSpacing(6)
        self._buttonResetScene.clicked.connect(MainWindow.resetScene)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self._buttonResetScene.setText(_translate("MainWindow", "Reset Scene"))
        self._editorPanel.setItemText(self._editorPanel.indexOf(self._pageScene), _translate("MainWindow", "Scene"))
        self._buttonDrawObstacle.setText(_translate("MainWindow", "Draw Obstacle"))
        self._checkSnapToGrid.setText(_translate("MainWindow", "Snap To Grid"))
        self._editorPanel.setItemText(self._editorPanel.indexOf(self._pageObstacles), _translate("MainWindow", "Obstacles"))
        self._mainTabs.setTabText(self._mainTabs.indexOf(self._tabEditor), _translate("MainWindow", "Editor"))
        self._mainTabs.setTabText(self._mainTabs.indexOf(self.widget), _translate("MainWindow", "Selecton"))
