from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QWidget)
from designer import Ui_MainWindow
import sys
import json

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.pushButton.clicked.connect(self.registr)
        self.ui.pushButton_2.clicked.connect(self.vxod)
        self.ui.pushButton_3.clicked.connect(self.registr2)
        self.ui.pushButton_4.clicked.connect(self.vxod2)

    def registr(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def vxod(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def registr2(self):
        try:
             with open("base.json","r",encoding="utf-8") as f:
                    self.t = json.load(f)
        except(FileNotFoundError, json.JSONDecodeError):
            self.t = []
        

        self.new_user = {
            "name" : self.ui.lineEdit.text(),
            "password" : self.ui.lineEdit_2.text()
        }
        self.t.append(self.new_user)


        with open("base.json","w",encoding="utf-8") as f:
            json.dump(self.t,f,ensure_ascii=False,indent=4)

        self.ui.stackedWidget.setCurrentIndex(3)
    def vxod2(self):
        if not hasattr(self,"label"):
            self.label = QLabel(self)
            self.label.setText("Данного аккаунта не существует")
            self.label.setGeometry(10,180,261,61)
            font = self.label.font()
            font.setPointSize(13)
        self.label.hide()
        with open("base.json","r",encoding="utf-8") as f:
            self.t = json.load(f)

            self.name = self.ui.lineEdit_3.text()
            self.password = self.ui.lineEdit_4.text()

            for i in self.t:
                cur_name = i["name"]
                cur_password = i["password"]

                if self.name == cur_name and self.password == cur_password:
                    self.ui.stackedWidget.setCurrentIndex(4)
                    self.label.hide()
                    break
                else:
                    self.label.show()




if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())