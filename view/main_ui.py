# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 331)
        MainWindow.setStyleSheet("QWidget #centralwidget {\n"
"    background-color: #0F2333;\n"
"}\n"
"\n"
"QLabel#questionLabel {\n"
"    color: #FCFCFC;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#savePushButton {\n"
"    background-color: #E50058;\n"
"    color: #FCFCFC;\n"
"    border-radius: 10px;\n"
"    min-width: 75px;\n"
"    min-height: 25px;\n"
"    font: 15px;\n"
"}\n"
"\n"
"QPushButton#savePushButton:disabled {\n"
"    background-color:#0F2333;\n"
"    color:#0F2333\n"
"}\n"
"\n"
"QPushButton#savePushButton:enabled {\n"
"    background-color: #E50058;\n"
"    color: #FCFCFC;\n"
"}\n"
"\n"
"QPushButton#savePushButton:hover {\n"
"    background-color: #FF740F;\n"
"}\n"
"\n"
"QPushButton#savePushButton:pressed {\n"
"    background-color:#FFBE36;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#volumePushButton {\n"
"    background-color: #E50058;\n"
"    color: #FCFCFC;\n"
"    border-radius: 10px;\n"
"    min-width: 50px;\n"
"    min-height: 25px;\n"
"    font: 15px;\n"
"}\n"
"\n"
"QPushButton#volumePushButton:hover {\n"
"    background-color: #FF740F;\n"
"}\n"
"\n"
"QPushButton#volumePushButton:pressed {\n"
"    background-color:#FFBE36;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #E50058;\n"
"    color: #FCFCFC;\n"
"    border-radius: 10px;\n"
"    min-width: 100px;\n"
"    min-height: 25px;\n"
"    font: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FF740F;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:#FFBE36;\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: rgb(255,255,255);\n"
"    border-radius: 10px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.savePushButton = QtWidgets.QPushButton(self.widget)
        self.savePushButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savePushButton.sizePolicy().hasHeightForWidth())
        self.savePushButton.setSizePolicy(sizePolicy)
        self.savePushButton.setObjectName("savePushButton")
        self.horizontalLayout_3.addWidget(self.savePushButton)
        self.questionLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.questionLabel.setFont(font)
        self.questionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.questionLabel.setObjectName("questionLabel")
        self.horizontalLayout_3.addWidget(self.questionLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.volumePushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volumePushButton.sizePolicy().hasHeightForWidth())
        self.volumePushButton.setSizePolicy(sizePolicy)
        self.volumePushButton.setMinimumSize(QtCore.QSize(50, 25))
        self.volumePushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/view/logos/volume-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.volumePushButton.setIcon(icon)
        self.volumePushButton.setIconSize(QtCore.QSize(21, 21))
        self.volumePushButton.setObjectName("volumePushButton")
        self.horizontalLayout_3.addWidget(self.volumePushButton)
        spacerItem1 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.responseTextEdit = QtWidgets.QPlainTextEdit(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.responseTextEdit.setFont(font)
        self.responseTextEdit.setObjectName("responseTextEdit")
        self.horizontalLayout_2.addWidget(self.responseTextEdit)
        self.horizontalLayout.addWidget(self.widget_3, 0, QtCore.Qt.AlignBottom)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SkipPushButton = QtWidgets.QPushButton(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.SkipPushButton.setFont(font)
        self.SkipPushButton.setObjectName("SkipPushButton")
        self.verticalLayout_2.addWidget(self.SkipPushButton)
        self.recordPushButton = QtWidgets.QPushButton(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.recordPushButton.setFont(font)
        self.recordPushButton.setObjectName("recordPushButton")
        self.verticalLayout_2.addWidget(self.recordPushButton)
        self.previousPushButton = QtWidgets.QPushButton(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.previousPushButton.setFont(font)
        self.previousPushButton.setObjectName("previousPushButton")
        self.verticalLayout_2.addWidget(self.previousPushButton)
        self.submitPushButton = QtWidgets.QPushButton(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.submitPushButton.setFont(font)
        self.submitPushButton.setObjectName("submitPushButton")
        self.verticalLayout_2.addWidget(self.submitPushButton)
        self.createBibliographyButton = QtWidgets.QPushButton(self.widget_4)
        self.createBibliographyButton.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.createBibliographyButton.setFont(font)
        self.createBibliographyButton.setObjectName("createBibliographyButton")
        self.verticalLayout_2.addWidget(self.createBibliographyButton)
        self.horizontalLayout.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.savePushButton.setText(_translate("MainWindow", "Save"))
        self.questionLabel.setText(_translate("MainWindow", "What is your name?"))
        self.SkipPushButton.setText(_translate("MainWindow", "Skip"))
        self.recordPushButton.setText(_translate("MainWindow", "Record"))
        self.previousPushButton.setText(_translate("MainWindow", "Previous"))
        self.submitPushButton.setText(_translate("MainWindow", "Submit"))
        self.createBibliographyButton.setText(_translate("MainWindow", "Create"))
import logos_rc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
