import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush, QFont, QRegExpValidator
from datetime import date
from PyQt5.QtCore import QRegExp
import os, glob


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.setGeometry(700, 200, 750, 650)
        self.setFixedSize(750, 650)
        self.setWindowTitle("Accepted Students List| insert data.")
        self.setToolTip("hey mate!")
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(current_dir, 'img/icon.ico')
        background_path = os.path.join(current_dir, 'img/background.png')
        self.setWindowIcon(QIcon(icon_path))
        oImage = QPixmap(background_path)
        sImage = oImage.scaled(self.size())  
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        self.initUI()
        custom_font = QFont('Arial', 11)
        self.setFont(custom_font)
        
        self.names = []

    def initUI(self):
        regex = QRegExp("[^\\s]*")
        validator = QRegExpValidator(regex)
        self.lblFname = QtWidgets.QLabel(self)
        self.lblFname.setText("Enter first Name of student: ")
        self.lblFname.move(50, 70)
        self.lblFname.resize(260, 22)

        self.lblLname = QtWidgets.QLabel(self)
        self.lblLname.setText("Enter last name of student: ")
        self.lblLname.move(50, 110)
        self.lblLname.resize(260, 22)

        self.lblGfname = QtWidgets.QLabel(self)
        self.lblGfname.setText("Enter Grand_F name of student: ")
        self.lblGfname.move(50, 150)
        self.lblGfname.resize(260, 22)

        self.lblGrade = QtWidgets.QLabel(self)
        self.lblGrade.setText("Enter students grade: ")
        self.lblGrade.move(50, 70)
        self.lblGrade.resize(260, 22)
        self.lblGrade.hide()

        self.txt_Fname = QtWidgets.QLineEdit(self)
        self.txt_Fname.move(310, 70)
        self.txt_Fname.resize(250, 22)
        self.txt_Fname.setValidator(validator)

        self.txt_Lname = QtWidgets.QLineEdit(self)
        self.txt_Lname.move(310, 110)
        self.txt_Lname.resize(250, 22)
        self.txt_Lname.setValidator(validator)

        self.txt_GFname = QtWidgets.QLineEdit(self)
        self.txt_GFname.move(320, 150)
        self.txt_GFname.resize(250, 22)
        self.txt_GFname.setValidator(validator)

        self.txt_Grade = QtWidgets.QComboBox(self)
        self.txt_Grade.move(250, 70)
        self.txt_Grade.resize(150, 22)
        for i in range(1, 13):
            self.txt_Grade.addItem(str(i))
        self.txt_Grade.hide()
        
        
        self.btn_nexts = QtWidgets.QPushButton(self)
        self.btn_nexts.setText('Next student')
        self.btn_nexts.clicked.connect(self.nextStudent)
        self.btn_nexts.move(130, 210)
        self.btn_nexts.resize(150, 42)

        self.btn_done = QtWidgets.QPushButton(self)
        self.btn_done.setText('Done')
        self.btn_done.clicked.connect(self.done)
        self.btn_done.move(350, 210)
        self.btn_done.resize(150, 42)

         
        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText('Save')
        self.btn_save.clicked.connect(self.save)
        self.btn_save.move(150, 120)
        self.btn_save.resize(130, 32)
        self.btn_save.hide()

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText('RESULT: ')
        self.lbl_result.move(50, 280)
        self.lbl_result.resize(600, 60)
        rfont = QFont()
        rfont.setPointSize(10)  
        self.lbl_result.setFont(rfont)

        self.btn_clear = QtWidgets.QPushButton('Clear files', self)
        self.btn_clear.clicked.connect(self.clear_directory)
        self.btn_clear.setToolTip('Clear all lists from drive!')

        self.btn_back = QtWidgets.QPushButton('Back', self)
        self.btn_back.clicked.connect(self.back)
        self.btn_back.setToolTip('Add more students')
        self.btn_back.hide()

    
    def event(self, event):
        if event.type() == QtCore.QEvent.KeyPress:
            if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
                self.focusNextPrevChild(True)
        return super().event(event)   
         

    def nextStudent(self):
         
         name = f"{self.txt_Fname.text()} {self.txt_Lname.text()} {self.txt_GFname.text()}"
         name = name.title()
         sname = name.split()
         cname = len(sname)
         
         if cname == 3:
             self.names.append(name.strip())
    
             self.txt_Fname.clear()
             self.txt_Lname.clear()
             self.txt_GFname.clear()
             self.lbl_result.setText(f'{name} added sucessfully.')
         else:
             self.lbl_result.setText("Please add names in all the spaces provided.")

    def back(self):
        self.lblGrade.hide()
        self.txt_Grade.hide()
        self.btn_save.hide()
        self.btn_nexts.show()
        self.btn_done.show()
        self.lblFname.show()
        self.lblLname.show()
        self.lblGfname.show()
        self.txt_Fname.show()
        self.txt_Lname.show()
        self.txt_GFname.show()
        self.btn_clear.show()
        self.btn_back.hide()

    def done(self):
         # Checks if the QLineEdit txt_grade and txt_year fields are empty or not before taking action.
        if not self.txt_Fname.text().strip() or not self.txt_Lname.text().strip() or not self.txt_GFname.text().strip():
            if not self.names:
                self.lbl_result.setText(' Please add a list of students first! thank you!')
            else:
                self.lblGrade.show()
                self.txt_Grade.show()
                self.btn_save.show()
                self.btn_nexts.hide()
                self.btn_done.hide()
                self.lblFname.hide()
                self.lblLname.hide()
                self.lblGfname.hide()
                self.txt_Fname.hide()
                self.txt_Lname.hide()
                self.txt_GFname.hide()
                self.btn_clear.hide()
                self.btn_back.show()

                count = 0
                #counts total students added in the list
                for names in self.names:
                    count+=1

                self.lbl_result.setText(f'A total of {count} students were added to the list.')
        else:
            self.lbl_result.setText(f"If you still have a students name laying around \n in the boxes press 'Next student' one more time")

    def save(self):
        Year = date.today().year
        grade_text = self.txt_Grade.currentText()

        if grade_text != "":
            directory = "C://lists"
            #chacks if the directory c://lists exists or not if it doesnt it will create on if exists it creates a .txt file with all the accepted students names from variable self.names with \n and saves it.
            if not os.path.exists(directory):
                os.makedirs(directory)

            with open(f'{directory}/{Year}_{grade_text}.txt','a') as file:
                file.close()

            textFile = open(f'{directory}/{Year}_{grade_text}.txt', 'w')
            content = '\n'.join(self.names)
            textFile.writelines(content)
            self.lbl_result.setText(' File created successfully! in the directory "C://lists" :)')
        

    def clear_directory(self):
        #clears all list files created previously if they exist, if they dont itt prints a message saying no files found.
        if not os.listdir('C://lists'):
            self.lbl_result.setText(' No files found in lists -folder- :)')
        # Perform some action
        else:
            files = glob.glob('C://lists/*')
            fcount = 0
            for f in files:
                os.remove(f)
                fcount += 1
            self.lbl_result.setText(f' {fcount} Files removed successfully! :)')
           
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
window()
