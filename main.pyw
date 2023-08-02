import sys
from PySide6 import QtWidgets
import design
from PySide6.QtGui import QPalette

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_Button.clicked.connect(self.start)

    def start(self):
        if self.encrypt_Button.isChecked() == True:
            self.text_out.setText(self.cipher())
        elif self.decipher_Button.isChecked() == True:
            self.text_out.setText(self.uncipher())

    eng_up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']
    eng_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    punctuation_marks = [' ', ',', '.', '?', '!', ',,,', '-', '_', '+', '-', '=', '\n', '*', '/', ':', ';', '\'', '\'', '(', ')', '[', ']', '{', '}' ]

    def cipher(self):
        stroke = self.text_in.toPlainText()
        bias = self.Shift_box.value()
        new_stroke = ''
        for symb in stroke:
            if symb in self.punctuation_marks:
                pass
            elif symb.isupper():
                try:
                    symb = self.eng_up[self.eng_up.index(symb) + bias]
                except IndexError:
                    symb = self.eng_up[self.eng_up.index(symb) + bias - len(self.eng_up)]
            else:
                try:
                    symb = self.eng_low[self.eng_low.index(symb) + bias]
                except IndexError:
                    symb = self.eng_low[self.eng_low.index(symb) + bias - len(self.eng_low)]
            new_stroke += symb
        return new_stroke

    def uncipher(self):
        stroke = self.text_in.toPlainText()
        bias = self.Shift_box.value()
        new_stroke = ''
        for symb in stroke:
            if symb in self.punctuation_marks:
                pass
            elif symb.isupper():
                try:
                    symb = self.eng_up[self.eng_up.index(symb) - bias]
                except IndexError:
                    symb = self.eng_up[self.eng_up.index(symb) - bias + len(self.eng_up)]
            else:
                try:
                    symb = self.eng_low[self.eng_low.index(symb) - bias]
                except IndexError:
                    symb = self.eng_low[self.eng_low.index(symb) - bias + len(self.eng_low)]
            new_stroke += symb
        return new_stroke

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()