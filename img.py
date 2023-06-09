# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Img.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1443, 683)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Images/icon/annotation.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(231, 231, 231);")
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(1030, 0, 231, 20))
        self.toolButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton.setObjectName("toolButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, -20, 611, 661))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(229, 250, 230);")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(990, 450, 281, 181))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 279, 179))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1443, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.menuView.setFont(font)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.toolBar.setFont(font)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setStyleSheet("color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0.261364 rgba(85, 0, 127, 255), stop:0.778409 rgba(0, 170, 255, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.toolBar.setIconSize(QtCore.QSize(50, 50))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/Images/icon/open canva.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionOpen.setFont(font)
        self.actionOpen.setShortcutVisibleInContextMenu(True)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen_Directory = QtWidgets.QAction(MainWindow)
        self.actionOpen_Directory.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionOpen_Directory.setFont(font)
        self.actionOpen_Directory.setShortcutVisibleInContextMenu(True)
        self.actionOpen_Directory.setObjectName("actionOpen_Directory")
        self.actionChange_Save_Directory = QtWidgets.QAction(MainWindow)
        self.actionChange_Save_Directory.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionChange_Save_Directory.setFont(font)
        self.actionChange_Save_Directory.setShortcutVisibleInContextMenu(True)
        self.actionChange_Save_Directory.setObjectName("actionChange_Save_Directory")
        self.actionOpen_Annotation = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icon/Images/icon/open icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_Annotation.setIcon(icon2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionOpen_Annotation.setFont(font)
        self.actionOpen_Annotation.setShortcutVisibleInContextMenu(True)
        self.actionOpen_Annotation.setObjectName("actionOpen_Annotation")
        self.actionCopy_previous_Bounding_Boxes_in_the_current_image = QtWidgets.QAction(MainWindow)
        self.actionCopy_previous_Bounding_Boxes_in_the_current_image.setShortcutVisibleInContextMenu(True)
        self.actionCopy_previous_Bounding_Boxes_in_the_current_image.setObjectName("actionCopy_previous_Bounding_Boxes_in_the_current_image")
        self.actionOpen_Recent = QtWidgets.QAction(MainWindow)
        self.actionOpen_Recent.setShortcutVisibleInContextMenu(True)
        self.actionOpen_Recent.setObjectName("actionOpen_Recent")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/Images/icon/Save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionSave.setFont(font)
        self.actionSave.setShortcutVisibleInContextMenu(True)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icon/Images/icon/save icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As.setIcon(icon4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionSave_As.setFont(font)
        self.actionSave_As.setShortcutVisibleInContextMenu(True)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionClose = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icon/Images/icon/close icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionClose.setFont(font)
        self.actionClose.setShortcutVisibleInContextMenu(True)
        self.actionClose.setObjectName("actionClose")
        self.actionReset_All = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Icon/Images/icon/reset icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReset_All.setIcon(icon6)
        self.actionReset_All.setShortcutVisibleInContextMenu(True)
        self.actionReset_All.setObjectName("actionReset_All")
        self.actionDelete_current_image = QtWidgets.QAction(MainWindow)
        self.actionDelete_current_image.setIcon(icon5)
        self.actionDelete_current_image.setShortcutVisibleInContextMenu(True)
        self.actionDelete_current_image.setObjectName("actionDelete_current_image")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setIcon(icon5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionQuit.setFont(font)
        self.actionQuit.setShortcutVisibleInContextMenu(True)
        self.actionQuit.setObjectName("actionQuit")
        self.actionCreate_RectBox = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Icons/Images/icon/boundingboxes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreate_RectBox.setIcon(icon7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionCreate_RectBox.setFont(font)
        self.actionCreate_RectBox.setObjectName("actionCreate_RectBox")
        self.actionEdit_Label = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Icon/Images/icon/edit label.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_Label.setIcon(icon8)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionEdit_Label.setFont(font)
        self.actionEdit_Label.setObjectName("actionEdit_Label")
        self.actionDuplicate_RectBox = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Icon/Images/icon/dupicate icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDuplicate_RectBox.setIcon(icon9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionDuplicate_RectBox.setFont(font)
        self.actionDuplicate_RectBox.setObjectName("actionDuplicate_RectBox")
        self.actionDelete_RectBox = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/Icon/Images/icon/remove icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete_RectBox.setIcon(icon10)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionDelete_RectBox.setFont(font)
        self.actionDelete_RectBox.setShortcutVisibleInContextMenu(True)
        self.actionDelete_RectBox.setObjectName("actionDelete_RectBox")
        self.actionBox_Line_Square = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Icon/Images/icon/pencil icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBox_Line_Square.setIcon(icon11)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionBox_Line_Square.setFont(font)
        self.actionBox_Line_Square.setShortcutVisibleInContextMenu(True)
        self.actionBox_Line_Square.setObjectName("actionBox_Line_Square")
        self.actionDraw_Square = QtWidgets.QAction(MainWindow)
        self.actionDraw_Square.setShortcutVisibleInContextMenu(True)
        self.actionDraw_Square.setObjectName("actionDraw_Square")
        self.actionAuto_Save_Mode = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/Icon/icon/hide icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAuto_Save_Mode.setIcon(icon12)
        self.actionAuto_Save_Mode.setObjectName("actionAuto_Save_Mode")
        self.actionSingle_Class_Mode = QtWidgets.QAction(MainWindow)
        self.actionSingle_Class_Mode.setObjectName("actionSingle_Class_Mode")
        self.actionDisplay_Labels = QtWidgets.QAction(MainWindow)
        self.actionDisplay_Labels.setObjectName("actionDisplay_Labels")
        self.actionShow_Hide_Label_panel = QtWidgets.QAction(MainWindow)
        self.actionShow_Hide_Label_panel.setShortcutVisibleInContextMenu(True)
        self.actionShow_Hide_Label_panel.setObjectName("actionShow_Hide_Label_panel")
        self.actionAdvanced_Mode = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/Icon/Images/icon/advance icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdvanced_Mode.setIcon(icon13)
        self.actionAdvanced_Mode.setShortcutVisibleInContextMenu(True)
        self.actionAdvanced_Mode.setObjectName("actionAdvanced_Mode")
        self.actionHide_RectBox = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/Icon/Images/icon/hide icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHide_RectBox.setIcon(icon14)
        self.actionHide_RectBox.setShortcutVisibleInContextMenu(True)
        self.actionHide_RectBox.setObjectName("actionHide_RectBox")
        self.actionShow_RectBox = QtWidgets.QAction(MainWindow)
        self.actionShow_RectBox.setIcon(icon14)
        self.actionShow_RectBox.setShortcutVisibleInContextMenu(True)
        self.actionShow_RectBox.setObjectName("actionShow_RectBox")
        self.actionZoom_In = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/Icon/Images/icon/zoom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_In.setIcon(icon15)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionZoom_In.setFont(font)
        self.actionZoom_In.setShortcutVisibleInContextMenu(True)
        self.actionZoom_In.setObjectName("actionZoom_In")
        self.actionZoom_Out = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/Icon/Images/icon/zoom out icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_Out.setIcon(icon16)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionZoom_Out.setFont(font)
        self.actionZoom_Out.setShortcutVisibleInContextMenu(True)
        self.actionZoom_Out.setObjectName("actionZoom_Out")
        self.actionOrginal_Size = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/Icon/Images/icon/origibal icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOrginal_Size.setIcon(icon17)
        self.actionOrginal_Size.setShortcutVisibleInContextMenu(True)
        self.actionOrginal_Size.setObjectName("actionOrginal_Size")
        self.actionFit_Window = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/Icon/Images/icon/fit window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFit_Window.setIcon(icon18)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionFit_Window.setFont(font)
        self.actionFit_Window.setShortcutVisibleInContextMenu(True)
        self.actionFit_Window.setObjectName("actionFit_Window")
        self.actionFit_Width = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/Icon/Images/icon/fit width.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFit_Width.setIcon(icon19)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionFit_Width.setFont(font)
        self.actionFit_Width.setShortcutVisibleInContextMenu(True)
        self.actionFit_Width.setObjectName("actionFit_Width")
        self.actionBrighten = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/Icon/Images/icon/brighten icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBrighten.setIcon(icon20)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionBrighten.setFont(font)
        self.actionBrighten.setShortcutVisibleInContextMenu(True)
        self.actionBrighten.setObjectName("actionBrighten")
        self.actionDarken = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/Icon/Images/icon/darken icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDarken.setIcon(icon21)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionDarken.setFont(font)
        self.actionDarken.setShortcutVisibleInContextMenu(True)
        self.actionDarken.setObjectName("actionDarken")
        self.actionOriginal_Brightness = QtWidgets.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/Icon/Images/icon/original brightnes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOriginal_Brightness.setIcon(icon22)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionOriginal_Brightness.setFont(font)
        self.actionOriginal_Brightness.setShortcutVisibleInContextMenu(True)
        self.actionOriginal_Brightness.setObjectName("actionOriginal_Brightness")
        self.actionNext_Image = QtWidgets.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/Icons/Images/icon/next image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNext_Image.setIcon(icon23)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionNext_Image.setFont(font)
        self.actionNext_Image.setShortcutVisibleInContextMenu(True)
        self.actionNext_Image.setObjectName("actionNext_Image")
        self.actionPrevious_Image = QtWidgets.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/Icons/Images/icon/previous image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrevious_Image.setIcon(icon24)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionPrevious_Image.setFont(font)
        self.actionPrevious_Image.setShortcutVisibleInContextMenu(True)
        self.actionPrevious_Image.setObjectName("actionPrevious_Image")
        self.actionYOLO = QtWidgets.QAction(MainWindow)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/Icons/Images/icon/Yolo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionYOLO.setIcon(icon25)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionYOLO.setFont(font)
        self.actionYOLO.setShortcutVisibleInContextMenu(True)
        self.actionYOLO.setObjectName("actionYOLO")
        self.actionAction_Save_Mode = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        self.actionAction_Save_Mode.setFont(font)
        self.actionAction_Save_Mode.setObjectName("actionAction_Save_Mode")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpen_Directory)
        self.menuFile.addAction(self.actionChange_Save_Directory)
        self.menuFile.addAction(self.actionOpen_Annotation)
        self.menuFile.addAction(self.actionCopy_previous_Bounding_Boxes_in_the_current_image)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionReset_All)
        self.menuFile.addAction(self.actionDelete_current_image)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionCreate_RectBox)
        self.menuEdit.addAction(self.actionEdit_Label)
        self.menuEdit.addAction(self.actionDuplicate_RectBox)
        self.menuEdit.addAction(self.actionDelete_RectBox)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionBox_Line_Square)
        self.menuEdit.addAction(self.actionDraw_Square)
        self.menuView.addAction(self.actionAction_Save_Mode)
        self.menuView.addAction(self.actionSingle_Class_Mode)
        self.menuView.addAction(self.actionDisplay_Labels)
        self.menuView.addAction(self.actionShow_Hide_Label_panel)
        self.menuView.addAction(self.actionAdvanced_Mode)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionHide_RectBox)
        self.menuView.addAction(self.actionShow_RectBox)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionZoom_In)
        self.menuView.addAction(self.actionZoom_Out)
        self.menuView.addAction(self.actionOrginal_Size)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionFit_Window)
        self.menuView.addAction(self.actionFit_Width)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionBrighten)
        self.menuView.addAction(self.actionDarken)
        self.menuView.addAction(self.actionOriginal_Brightness)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionOpen_Directory)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionChange_Save_Directory)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionNext_Image)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPrevious_Image)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionYOLO)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCreate_RectBox)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDuplicate_RectBox)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDelete_RectBox)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionZoom_In)
        self.toolBar.addAction(self.actionZoom_Out)
        self.toolBar.addAction(self.actionFit_Window)
        self.toolBar.addAction(self.actionFit_Width)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionBrighten)
        self.toolBar.addAction(self.actionDarken)
        self.toolBar.addAction(self.actionOriginal_Brightness)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AnnotationTool"))
        self.toolButton.setText(_translate("MainWindow", "Box Labels"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setIconText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open File"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionOpen_Directory.setText(_translate("MainWindow", "Open Directory"))
        self.actionOpen_Directory.setIconText(_translate("MainWindow", "Open Dir"))
        self.actionOpen_Directory.setStatusTip(_translate("MainWindow", "Open Directory"))
        self.actionOpen_Directory.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionChange_Save_Directory.setText(_translate("MainWindow", "Change Save Directory"))
        self.actionChange_Save_Directory.setIconText(_translate("MainWindow", "Change Save Dir"))
        self.actionChange_Save_Directory.setStatusTip(_translate("MainWindow", "Change default Saved Annotate Dir"))
        self.actionChange_Save_Directory.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionOpen_Annotation.setText(_translate("MainWindow", "Open Annotation"))
        self.actionOpen_Annotation.setStatusTip(_translate("MainWindow", "Open an Annotation file"))
        self.actionOpen_Annotation.setShortcut(_translate("MainWindow", "Ctrl+Shift+O"))
        self.actionCopy_previous_Bounding_Boxes_in_the_current_image.setText(_translate("MainWindow", "Copy previous Bounding Boxes in the current image"))
        self.actionOpen_Recent.setText(_translate("MainWindow", "Open Recent"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save the label to a file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionSave_As.setStatusTip(_translate("MainWindow", "Save the labels to different file"))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setStatusTip(_translate("MainWindow", "Close the curret file"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionReset_All.setText(_translate("MainWindow", "Reset All"))
        self.actionReset_All.setStatusTip(_translate("MainWindow", "Reset All"))
        self.actionDelete_current_image.setText(_translate("MainWindow", "Delete current image"))
        self.actionDelete_current_image.setStatusTip(_translate("MainWindow", "Delete the current image"))
        self.actionDelete_current_image.setShortcut(_translate("MainWindow", "Ctrl+Shift+D"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setStatusTip(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionCreate_RectBox.setText(_translate("MainWindow", "Create RectBox"))
        self.actionCreate_RectBox.setStatusTip(_translate("MainWindow", "Draw a new box"))
        self.actionCreate_RectBox.setShortcut(_translate("MainWindow", "W"))
        self.actionEdit_Label.setText(_translate("MainWindow", "Edit Label"))
        self.actionEdit_Label.setStatusTip(_translate("MainWindow", "Modify the label of selected box"))
        self.actionEdit_Label.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionDuplicate_RectBox.setText(_translate("MainWindow", "Duplicate RectBox"))
        self.actionDuplicate_RectBox.setStatusTip(_translate("MainWindow", "Create a duplicate of selected box"))
        self.actionDuplicate_RectBox.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionDelete_RectBox.setText(_translate("MainWindow", "Delete RectBox"))
        self.actionDelete_RectBox.setStatusTip(_translate("MainWindow", "Remove the box"))
        self.actionDelete_RectBox.setShortcut(_translate("MainWindow", "Del"))
        self.actionBox_Line_Square.setText(_translate("MainWindow", "Box Line Color"))
        self.actionBox_Line_Square.setStatusTip(_translate("MainWindow", "Choose Box line color"))
        self.actionBox_Line_Square.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionDraw_Square.setText(_translate("MainWindow", "Draw Square"))
        self.actionDraw_Square.setShortcut(_translate("MainWindow", "Ctrl+Shift+R"))
        self.actionAuto_Save_Mode.setText(_translate("MainWindow", "Auto Save Mode"))
        self.actionSingle_Class_Mode.setText(_translate("MainWindow", "Single Class Mode"))
        self.actionSingle_Class_Mode.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionDisplay_Labels.setText(_translate("MainWindow", "Display Labels"))
        self.actionDisplay_Labels.setShortcut(_translate("MainWindow", "Ctrl+Shift+P"))
        self.actionShow_Hide_Label_panel.setText(_translate("MainWindow", "Show/Hide Label panel"))
        self.actionShow_Hide_Label_panel.setShortcut(_translate("MainWindow", "Ctrl+Shift+L"))
        self.actionAdvanced_Mode.setText(_translate("MainWindow", "Advanced Mode"))
        self.actionAdvanced_Mode.setStatusTip(_translate("MainWindow", "Switch to Advance Mode"))
        self.actionAdvanced_Mode.setShortcut(_translate("MainWindow", "Ctrl+Shift+A"))
        self.actionHide_RectBox.setText(_translate("MainWindow", "Hide RectBox"))
        self.actionHide_RectBox.setStatusTip(_translate("MainWindow", "Hide all bounding Boxes"))
        self.actionHide_RectBox.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionShow_RectBox.setText(_translate("MainWindow", "Show RectBox"))
        self.actionShow_RectBox.setStatusTip(_translate("MainWindow", "Show all bounding Boxes"))
        self.actionShow_RectBox.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionZoom_In.setText(_translate("MainWindow", "Zoom In"))
        self.actionZoom_In.setStatusTip(_translate("MainWindow", "Increase Zoom level"))
        self.actionZoom_In.setShortcut(_translate("MainWindow", "Ctrl++"))
        self.actionZoom_Out.setText(_translate("MainWindow", "Zoom Out"))
        self.actionZoom_Out.setStatusTip(_translate("MainWindow", "Decrease Zoom level"))
        self.actionZoom_Out.setShortcut(_translate("MainWindow", "Ctrl+-"))
        self.actionOrginal_Size.setText(_translate("MainWindow", "Orginal Size"))
        self.actionOrginal_Size.setStatusTip(_translate("MainWindow", "Zoom to Orginal Size"))
        self.actionOrginal_Size.setShortcut(_translate("MainWindow", "Ctrl+="))
        self.actionFit_Window.setText(_translate("MainWindow", "Fit Window"))
        self.actionFit_Window.setStatusTip(_translate("MainWindow", "Zoom follows window size"))
        self.actionFit_Window.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionFit_Width.setText(_translate("MainWindow", "Fit Width"))
        self.actionFit_Width.setStatusTip(_translate("MainWindow", "Zoom follows window width"))
        self.actionFit_Width.setShortcut(_translate("MainWindow", "Ctrl+Shift+F"))
        self.actionBrighten.setText(_translate("MainWindow", "Brighten"))
        self.actionBrighten.setStatusTip(_translate("MainWindow", "Increase Image Brightness"))
        self.actionBrighten.setShortcut(_translate("MainWindow", "Ctrl+Shift+Num++"))
        self.actionDarken.setText(_translate("MainWindow", "Darken"))
        self.actionDarken.setStatusTip(_translate("MainWindow", "Decrease Image Brightness"))
        self.actionDarken.setShortcut(_translate("MainWindow", "Ctrl+Shift+Num+-"))
        self.actionOriginal_Brightness.setText(_translate("MainWindow", "Original Brightness"))
        self.actionOriginal_Brightness.setStatusTip(_translate("MainWindow", "Restore Original Brightness"))
        self.actionOriginal_Brightness.setShortcut(_translate("MainWindow", "Ctrl+Shift+="))
        self.actionNext_Image.setText(_translate("MainWindow", "Next Image"))
        self.actionNext_Image.setToolTip(_translate("MainWindow", "Open Next Image"))
        self.actionNext_Image.setStatusTip(_translate("MainWindow", "Open Next Image"))
        self.actionNext_Image.setShortcut(_translate("MainWindow", "D"))
        self.actionPrevious_Image.setText(_translate("MainWindow", "Previous Image"))
        self.actionPrevious_Image.setToolTip(_translate("MainWindow", "Previous Image"))
        self.actionPrevious_Image.setStatusTip(_translate("MainWindow", "Previous Image"))
        self.actionPrevious_Image.setShortcut(_translate("MainWindow", "A"))
        self.actionYOLO.setText(_translate("MainWindow", "Annotation"))
        self.actionYOLO.setToolTip(_translate("MainWindow", "Verify Image"))
        self.actionYOLO.setStatusTip(_translate("MainWindow", "Verify Image"))
        self.actionAction_Save_Mode.setText(_translate("MainWindow", "Action Save Mode"))
import Res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
