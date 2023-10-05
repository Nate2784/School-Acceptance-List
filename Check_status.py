import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush, QFont , QRegExpValidator
from PyQt5.QtCore import QRegExp
import os
path =  "C://lists"

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.setGeometry(700, 200, 650, 500)
        self.setFixedSize(750, 650)
        self.setWindowTitle("Accepted Students List| check status.")
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(current_dir, 'img/icon.ico')
        background_path = os.path.join(current_dir, 'img/background.png')
        self.setWindowIcon(QIcon(icon_path))
        oImage = QPixmap(background_path)
        sImage = oImage.scaled(self.size())  
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        custom_font = QFont('Arial', 11)
        self.setFont(custom_font)
        self.initUI()
    
    def initUI(self):
        regex = QRegExp("[^\\s]*")
        validator = QRegExpValidator(regex)
        self.lblYear = QtWidgets.QLabel(self)
        self.lblYear.setText("Enter year of registeration: ")
        self.lblYear.move(80, 50)
        self.lblYear.resize(250, 22)

        self.lblGrade = QtWidgets.QLabel(self)
        self.lblGrade.setText("Enter your grade: ")
        self.lblGrade.move(80, 90)
        self.lblGrade.resize(250, 22)


        self.txt_year = QtWidgets.QLineEdit(self)
        self.txt_year.move(310, 50)
        self.txt_year.resize(150, 22)
        self.txt_year.setValidator(validator)


        self.txt_Grade = QtWidgets.QLineEdit(self)
        self.txt_Grade.move(230, 90)
        self.txt_Grade.resize(150, 22)
        self.txt_year.setValidator(validator)

        self.lblFName = QtWidgets.QLabel(self)
        self.lblFName.setText("Enter your First name: ")
        self.lblFName.move(50, 50)
        self.lblFName.resize(250, 22)
        self.lblFName.hide()
         
        self.lblLName = QtWidgets.QLabel(self)
        self.lblLName.setText("Enter your last name: ")
        self.lblLName.move(50, 90)
        self.lblLName.resize(250, 22)
        self.lblLName.hide()

        self.lblGfName = QtWidgets.QLabel(self)
        self.lblGfName.setText("Enter your grand_f name: ")
        self.lblGfName.move(50, 130)
        self.lblGfName.resize(250, 22)
        self.lblGfName.hide()

        self.txt_Fname = QtWidgets.QLineEdit(self)
        self.txt_Fname.move(235, 50)
        self.txt_Fname.resize(250, 25)
        self.txt_Fname.setValidator(validator)
        self.txt_Fname.hide()

        self.txt_Lname = QtWidgets.QLineEdit(self)
        self.txt_Lname.move(235, 90)
        self.txt_Lname.resize(250, 25)
        self.txt_Lname.setValidator(validator)
        self.txt_Lname.hide()

        self.txt_Gfname = QtWidgets.QLineEdit(self)
        self.txt_Gfname.move(265, 130)
        self.txt_Gfname.resize(250, 25)
        self.txt_Gfname.setValidator(validator)
        self.txt_Gfname.hide()

        self.btn_stat = QtWidgets.QPushButton(self)
        self.btn_stat.setText('Check Status')
        self.btn_stat.clicked.connect(self.stat)
        self.btn_stat.move(230, 150)
        self.btn_stat.resize(130, 32)

        self.btn_check = QtWidgets.QPushButton(self)
        self.btn_check.setText('Check')
        self.btn_check.clicked.connect(self.check)
        self.btn_check.move(230, 180)
        self.btn_check.resize(130, 32)
        self.btn_check.hide()

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText('STATUS: ')
        self.lbl_result.move(50, 200)
        self.lbl_result.resize(600, 190)

    
    def stat(self):
    # Checks if the QLineEdit txt_grade and txt_year fields are empty or not
        if not self.txt_Grade.text().strip() or not self.txt_year.text().strip():
            self.lbl_result.setText("please fill the empty fields, \n and proceed clicking the button above")
        else:
            try:
                fList = open(f'{path}\{self.txt_year.text()}_{self.txt_Grade.text()}.txt', 'r')
                self.lblYear.hide()
                self.lblGrade.hide()
                self.txt_year.hide()
                self.txt_Grade.hide()
                self.btn_stat.hide()

                self.lblFName.show()
                self.lblLName.show()
                self.lblGfName.show()
                self.txt_Fname.show()
                self.txt_Lname.show()
                self.txt_Gfname.show()
                self.btn_check.show()
                self.lbl_result.clear()
            except:
                self.lbl_result.setText("Sorry for the inconvenience, the file you're trying to open \n doesn't exist :(")
            pass
        

    def check(self):
        # Checks if the QLineEdit txt_Fname, txt_Lname and txt_Gfname fields are empty or not
        if not self.txt_Fname.text().strip()  or not self.txt_Lname.text().strip() or not self.txt_Gfname.text().strip():
            self.lbl_result.setText('Please fill out all the fields with appropriate name.')
        else:
            fList = open(f'{path}\{self.txt_year.text()}_{self.txt_Grade.text()}.txt', 'r')
            Name = f"{self.txt_Fname.text()} {self.txt_Lname.text()} {self.txt_Gfname.text()}"
            Name = Name.title()

            #A flag used to check if a match or result has been found in flist
            found = False

            #Gets students names from the saved file line by line and stores it temporarily in line
            for line in fList:
                line = line.rstrip()
                # nested if compares if the input name is equal to the line we got from our file(line of saved name) if it's equal it congradulates the user for being accepted.
                if Name == line:
                    self.lbl_result.setText(f"Hello! {Name} congratulations  you've been accepted! :)")

                    found = True
                    break
                else:
                    self.lbl_result.setText(f"Checking if {Name}  is in the accepted list...")
                    continue
            # if a match wasn't found in the above code it tells them they're not accepted.
            if not found: 
                self.lbl_result.setText(f"sorry {Name}  is not found in the accepted list :(")
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
