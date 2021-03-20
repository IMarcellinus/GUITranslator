'''
By: Marcellinus :D
'''
import gui
import sys
import googletrans
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox

class Main(QtWidgets.QMainWindow, gui.Ui_Form):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.setupUi(self)
        self.textEdit.clear()
        self.tambah_bahasa()

        self.pushButton.clicked.connect(self.translate)
        self.pushButton_2.clicked.connect(self.clear)
        self.pushButton_3.clicked.connect(self.exit)

    # Fungsi pilih bahasa
    def tambah_bahasa(self):
        for x in googletrans.LANGUAGES.values():
            self.comboBox.addItem(x.capitalize())
            self.comboBox_2.addItem(x.capitalize())

    # Fungsi translate
    def translate(self):
        try:
            text_1 = self.textEdit.toPlainText()
            lang_1 = self.comboBox.currentText()
            lang_2 = self.comboBox_2.currentText()

            translator = googletrans.Translator()
            translate = translator.translate(text_1, src=lang_1, dest=lang_2)
            self.textEdit_2.setText(translate.text)
            self.textEdit_3.setText(translate.pronunciation)

        except Exception:
            self.pesan_eror()

    # Fungsi Error
    def pesan_eror(self):
        msg = QMessageBox()
        msg.setWindowTitle('Wrong Input')
        msg.setText('Ketik anda kosong!')
        msg.setIcon(QMessageBox.Warning)

        x = msg.exec_()
    
    # Fungsi Reset/Clear
    def clear(self):
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()
    
    # Fungsi Exit
    def exit(self):
        sys.exit()

if __name__ == "__main__":
    a = QtWidgets.QApplication(sys.argv)
    app = Main()
    app.show()
    a.exec_()
