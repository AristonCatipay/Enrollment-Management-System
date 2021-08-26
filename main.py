import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
import mysql.connector as mc
from ULTfinale_design import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)


        self.ui.stackedWidget_2.setCurrentWidget(self.ui.OLD_STUDENT)

        self.ui.pushButton_6.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.OLD_STUDENT))
        self.ui.pushButton_7.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.NEW_STUDENT))
        self.ui.pushButton_8.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.ENROLLED_))
        self.ui.pushButton_9.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.GRADE_SEC))
        self.ui.pushButton_10.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.SCHEDULE_))
        self.ui.pushButton_11.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.SUBJECT_))
        self.ui.pushButton_12.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.TEACHER_))
        self.ui.pushButton_13.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.DEPARTMENT_))
        

    def show(self):
        self.main_win.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MyMainWindow()
    main_win.show()
    sys.exit(app.exec_())
