# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\QT\Food2019\userhome.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets
from FOODCNN import CNN
from details import Details


class UserHome(object):
    def browsefile(self):
        try:
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File","E:\\A PROJECTS\\2019\\Python\\Food 2019\\Source Code\\Food", "*.jpg")
            print(fileName)
            self.image.setText(fileName)
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)
    
    def detectiondef(self):
        try:
            fname = self.image.text()
            c=CNN()
            tagetimage=fname
            foodname=c.detect(tagetimage)
            
            print(foodname,'----------')

            number = self.spinBox.text()
            number=float(number)    
            cal=Details.getCal(foodname)
            cal=float(cal)
            cal=cal*number
            print(cal)
            
            self.foodname.setText(str(foodname))
            self.calories.setText(str(cal))

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)




    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(802, 559)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 811, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(0, 0, 941, 541))
        self.frame.setStyleSheet("background-image: url(calorieu.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 941, 541))
        self.frame_2.setStyleSheet("background-image: url(calorie2.jpg);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(230, 220, 380, 280))
        self.frame_3.setStyleSheet("background-image: url(wbg.png);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(30, 0, 321, 50))
        self.label.setStyleSheet("font: 20pt \"Rage Italic\";")
        self.label.setObjectName("label")
        self.image = QtWidgets.QLineEdit(self.frame_3)
        self.image.setGeometry(QtCore.QRect(10, 60, 310, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.image.setFont(font)
        self.image.setStyleSheet("")
        self.image.setText("")
        self.image.setObjectName("image")
        self.detection = QtWidgets.QPushButton(self.frame_3)
        self.detection.setGeometry(QtCore.QRect(270, 100, 90, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.detection.setFont(font)
        self.detection.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 208, 131);")
        self.detection.setObjectName("detection")



        #############################################
        self.detection.clicked.connect(self.detectiondef)

        
        self.browse = QtWidgets.QPushButton(self.frame_3)
        self.browse.setGeometry(QtCore.QRect(330, 60, 40, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.browse.setFont(font)
        self.browse.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 208, 131);")
        self.browse.setObjectName("browse")



        #############################################
        self.browse.clicked.connect(self.browsefile)


        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 141, 51))
        self.label_2.setStyleSheet("\n"
"font: 75 14pt \"Microsoft YaHei UI Light\";\n"
"\n"
"color: rgb(36, 36, 36);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(10, 230, 140, 51))
        self.label_3.setStyleSheet("\n"
"font: 75 14pt \"Microsoft YaHei UI Light\";\n"
"\n"
"color: rgb(36, 36, 36);")
        self.label_3.setObjectName("label_3")
        self.spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox.setGeometry(QtCore.QRect(200, 100, 60, 30))
        self.spinBox.setMaximum(9999)
        self.spinBox.setObjectName("spinBox")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 180, 51))
        self.label_4.setStyleSheet("\n"
"font: 75 12pt \"Microsoft YaHei UI Light\";\n"
"\n"
"color: rgb(36, 36, 36);")
        self.label_4.setObjectName("label_4")
        self.foodname = QtWidgets.QLabel(self.frame_3)
        self.foodname.setGeometry(QtCore.QRect(160, 180, 240, 30))
        self.foodname.setStyleSheet("\n"
"font: 75 14pt \"Microsoft YaHei UI Light\";\n"
"\n"
"color: rgb(36, 36, 36);")
        self.foodname.setObjectName("foodname")
        self.calories = QtWidgets.QLabel(self.frame_3)
        self.calories.setGeometry(QtCore.QRect(160, 240, 240, 40))
        self.calories.setStyleSheet("\n"
"font: 75 14pt \"Microsoft YaHei UI Light\";\n"
"\n"
"color: rgb(36, 36, 36);")
        self.calories.setObjectName("calories")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "User Home"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Home"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Image Upload</p></body></html>"))
        self.image.setToolTip(_translate("Dialog", "Food Image Upload"))
        self.image.setPlaceholderText(_translate("Dialog", "Food Detection"))
        self.detection.setText(_translate("Dialog", "Detection"))
        self.browse.setText(_translate("Dialog", "----"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Food Result:</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Calories:</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Enter No. of Grams:</span></p></body></html>"))
        self.foodname.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Non</span></p></body></html>"))
        self.calories.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Non</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Upload Food Image"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UserHome()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

