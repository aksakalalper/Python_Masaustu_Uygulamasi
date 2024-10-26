import sys #komut satırından uygulama açmak için import edildi.
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setWindowTitle("Uygulama") #pencere ismi verildi.
        self.setGeometry(200,200,500,500) #uygulama pencere boyutu ayarlandi.
        self.setWindowIcon(QIcon("icon.png")) #icon ayarlandi.
        self.initUI()

    def initUI(self):
        self.labelName=QtWidgets.QLabel(self) #etiket ismi verildi.
        self.labelName.setText("isim: ") #isim atandı.
        self.labelName.move(60,30) #isim taşındı.
        self.textName=QtWidgets.QLineEdit(self) #texbox eklendi
        self.textName.move(150,30)

        self.labelSurnam=QtWidgets.QLabel(self) #etiket ismi verildi.
        self.labelSurnam.setText("soyisim: ") #isim atandı.
        self.labelSurnam.move(60,70) #isim taşındı
        self.textSurname=QtWidgets.QLineEdit(self)  #texbox eklendi
        self.textSurname.move(150,70)

        self.buttonSave=QtWidgets.QPushButton(self)
        self.buttonSave.setText("Kaydet")
        self.buttonSave.move(150,120)
        self.buttonSave.clicked.connect(self.clicked)
    
    def clicked(self):
        print(f"Butona basildi. isim {self.textName.text()},soyisim {self.textSurname.text()}.")

def window():
    ## Atamalar yapilir
    app=QApplication(sys.argv) #sistem argümanı eklendi.
    win=MyWindow() #pencere şeklindeki uygulamanın ataması yapıldı.
    win.show() #pencere gösterildi.
    sys.exit(app.exec_()) #exit tuşuna basınca uygulamadan çıkılır.

window()