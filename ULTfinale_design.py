
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import mysql.connector as mc

mydb = mc.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "enrollment_system",
    auth_plugin='mysql_native_password',
    buffered = True
)
mycursor = mydb.cursor() 
if mydb.is_connected():
    print ("Enrollment System is connected to MySQL.")


class Ui_MainWindow(object):
        # NEW STUDENT FORM ---------------------------------------------
        def Inserting_NewStudentForm(self):
                StudentID = self.Student_IDLE.text()
                StudentFirstname = self.Student_FirstnameLE.text()
                StudentLastname = self.Student_LastnameLE.text()
                StudentMiddlename = self.Student_MiddlenameLE.text()
                StudentAge = self.Student_AgeLE.text()
                StudentGender = self.Student_GenderLE.text()
                StudentBLKAndLOT = self.Student_BLKAndLot.text()
                StudentStreet = self.Student_Street.text()
                StudentSubdivision = self.Student_SubdivisionLE.text()
                StudentBarangay = self.Student_BarangayLE.text()
                StudentCity = self.Student_CityLE.text()
                StudentContactNo = self.Student_Contact_NoLE.text()
                StudentClassification = self.Student_ClassificationLE.text()
                StudentisGrades = self.Student_isGradesLE.text()
                StudentisForm136 = self.Student_isForm136LE.text()
                StudentisForm137 = self.Student_isForm137LE.text()
                StudentisBirthCertificate = self.Student_isBirthCertificateLE.text()
                StudentisResidency = self.Student_isResidencyLE.text()
                Student_Class_ID = self.Student_ClassID_FKLE.text()
                StudentGrade = self.Student_Grade_2LE.text()
                StudentGradeasInt= int(StudentGrade)
                StudentSection = self.Student_Section_2LE.text()

                self.Student_IDLE.clear()
                self.Student_FirstnameLE.clear()
                self.Student_LastnameLE.clear()
                self.Student_MiddlenameLE.clear()
                self.Student_AgeLE.clear()
                self.Student_GenderLE.clear()
                self.Student_BLKAndLot.clear()
                self.Student_Street.clear()
                self.Student_SubdivisionLE.clear()
                self.Student_BarangayLE.clear()
                self.Student_CityLE.clear()
                self.Student_Contact_NoLE.clear()
                self.Student_ClassID_FKLE.clear()
                self.Student_Grade_2LE.clear()
                self.Student_Section_2LE.clear()

                HomeroomGrade = 0
                MathGrade = 0 
                HekasiGrade = 0 
                FilipinoGrade = 0 
                EspGrade = 0
                EnglishGrade = 0
                ScienceGrade = 0

                InsertItemStudent = "INSERT INTO STUDENTS (Student_ID, Student_Firstname, Student_Lastname, Student_Middlename, Student_Age, Student_Gender,BLK_And_Lot,Street,Subdivision,Barangay,City,Student_Contact_No,Student_Classification,isGrades,isForm136,isForm137,isBirthCertificate,isResidency,Class_ID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                Itemstobeinserted = (StudentID,StudentFirstname,StudentLastname,StudentMiddlename,StudentAge,StudentGender,StudentBLKAndLOT,StudentStreet,StudentSubdivision,StudentBarangay,StudentCity,StudentContactNo,StudentClassification,StudentisGrades,StudentisForm136,StudentisForm137,StudentisBirthCertificate,StudentisResidency,Student_Class_ID)
                mycursor.execute(InsertItemStudent,Itemstobeinserted)
                mydb.commit()
                print("Successful")

                if (StudentGradeasInt == 1):
                        if (StudentSection == "Masipag"):
                                InsertintoSection = "INSERT INTO section_masipag (Student_ID,HOMEROOM_Grade,MATH_Grade,SCIENCE_Grade,HEKASI_Grade,FILIPINO_Grade,ENGLISH_Grade,ESP_Grade,Class_ID,Student_IDCPY)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                Itemstobeinserted = (StudentID,HomeroomGrade,MathGrade,ScienceGrade,HekasiGrade,FilipinoGrade,EnglishGrade,EspGrade,Student_Class_ID,StudentID)
                                mycursor.execute(InsertintoSection,Itemstobeinserted)
                                mydb.commit()
                                print("Enrolling Student to Section Masipag is Successful!")
                                
                        elif (StudentSection == "Masunurin"):
                                InsertintoSection = "INSERT INTO section_masunurin (Student_ID,HOMEROOM_Grade,MATH_Grade,SCIENCE_Grade,HEKASI_Grade,FILIPINO_Grade,ENGLISH_Grade,ESP_Grade,Class_ID,Student_IDCPY)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                Itemstobeinserted = (StudentID,HomeroomGrade,MathGrade,ScienceGrade,HekasiGrade,FilipinoGrade,EnglishGrade,EspGrade,Student_Class_ID,StudentID)
                                mycursor.execute(InsertintoSection,Itemstobeinserted)
                                mydb.commit()
                                print("Enrolling Student to Section Masunurin is Successful!")
                                
                        else:
                                print("Enrolling Student to Grade 1 is unsuccessful!")
                elif (StudentGradeasInt == 2):
                        if (StudentSection == "Uranium"):
                                InsertintoSection = "INSERT INTO section_uranium (Student_ID,HOMEROOM_Grade,MATH_Grade,SCIENCE_Grade,HEKASI_Grade,FILIPINO_Grade,ENGLISH_Grade,ESP_Grade,Class_ID,Student_IDCPY)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                Itemstobeinserted = (StudentID,HomeroomGrade,MathGrade,ScienceGrade,HekasiGrade,FilipinoGrade,EnglishGrade,EspGrade,Student_Class_ID,StudentID)
                                mycursor.execute(InsertintoSection,Itemstobeinserted)
                                mydb.commit()
                                print("Enrolling Student to Section Uranium is Successful!")
                                
                        elif (StudentSection == "Xenon"):
                                InsertintoSection = "INSERT INTO section_xenon (Student_ID,HOMEROOM_Grade,MATH_Grade,SCIENCE_Grade,HEKASI_Grade,FILIPINO_Grade,ENGLISH_Grade,ESP_Grade,Class_ID,Student_IDCPY)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                Itemstobeinserted = (StudentID,HomeroomGrade,MathGrade,ScienceGrade,HekasiGrade,FilipinoGrade,EnglishGrade,EspGrade,Student_Class_ID,StudentID)
                                mycursor.execute(InsertintoSection,Itemstobeinserted)
                                mydb.commit()
                                print("Enrolling Student to Section Xenon is Successful!")
                                
                        else:
                                print("Enrolling Student to Grade 2 is unsuccessful!")
                elif (StudentGradeasInt == 3):
                        if (StudentSection == "Sampaguita"):
                                InsertintoSection = "INSERT INTO section_sampaguita (Student_ID,HOMEROOM_Grade,MATH_Grade,SCIENCE_Grade,HEKASI_Grade,FILIPINO_Grade,ENGLISH_Grade,ESP_Grade,Class_ID,Student_IDCPY)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                Itemstobeinserted = (StudentID,HomeroomGrade,MathGrade,ScienceGrade,HekasiGrade,FilipinoGrade,EnglishGrade,EspGrade,Student_Class_ID,StudentID)
                                mycursor.execute(InsertintoSection,Itemstobeinserted)
                                mydb.commit()
                                print("Enrolling Student to Section Sampaguita is Successful!")
                                
                        elif (StudentSection == "Sunflower"):
                                InsertintoSection = "INSERT INTO section_sunflower (Student_ID,HOMEROOM_Grade,MATH_Grade,SCIENCE_Grade,HEKASI_Grade,FILIPINO_Grade,ENGLISH_Grade,ESP_Grade,Class_ID,Student_IDCPY)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                Itemstobeinserted = (StudentID,HomeroomGrade,MathGrade,ScienceGrade,HekasiGrade,FilipinoGrade,EnglishGrade,EspGrade,Student_Class_ID,StudentID)
                                mycursor.execute(InsertintoSection,Itemstobeinserted)
                                mydb.commit()
                                print("Enrolling Student to Section Sunflower is Successful!")
                                
                        else:
                                print("Enrolling Student to Grade 3 is unsuccessful!")
                elif (StudentGradeasInt == 4):
                        if (StudentSection == "Diamond"):
                                InsertintoSection = "INSERT INTO section_diamond (Student_ID,HOMEROOM_Grade,MATH_Grade,SCIENCE_Grade,HEKASI_Grade,FILIPINO_Grade,ENGLISH_Grade,ESP_Grade,Class_ID,Student_IDCPY)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                Itemstobeinserted = (StudentID,HomeroomGrade,MathGrade,ScienceGrade,HekasiGrade,FilipinoGrade,EnglishGrade,EspGrade,Student_Class_ID,StudentID)
                                mycursor.execute(InsertintoSection,Itemstobeinserted)
                                mydb.commit()
                                print("Enrolling Student to Section Diamond is Successful!")
                        elif (StudentSection == "Ruby"):
                                InsertintoSection = "INSERT INTO section_ruby (Student_ID,HOMEROOM_Grade,MATH_Grade,SCIENCE_Grade,HEKASI_Grade,FILIPINO_Grade,ENGLISH_Grade,ESP_Grade,Class_ID,Student_IDCPY)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                Itemstobeinserted = (StudentID,HomeroomGrade,MathGrade,ScienceGrade,HekasiGrade,FilipinoGrade,EnglishGrade,EspGrade,Student_Class_ID,StudentID)
                                mycursor.execute(InsertintoSection,Itemstobeinserted)
                                mydb.commit()
                                print("Enrolling Student to Section Ruby is Successful!")
                                
                        else:
                                print("Enrolling Student to Grade 4 is unsuccessful!")
                elif (StudentGradeasInt == 5):
                        if (StudentSection == "Narra"):
                                InsertintoSection = "INSERT INTO section_narra (Student_ID,HOMEROOM_Grade,MATH_Grade,SCIENCE_Grade,HEKASI_Grade,FILIPINO_Grade,ENGLISH_Grade,ESP_Grade,Class_ID,Student_IDCPY)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                Itemstobeinserted = (StudentID,HomeroomGrade,MathGrade,ScienceGrade,HekasiGrade,FilipinoGrade,EnglishGrade,EspGrade,Student_Class_ID,StudentID)
                                mycursor.execute(InsertintoSection,Itemstobeinserted)
                                mydb.commit()
                                print("Enrolling Student to Section Narra is Successful!")
                                
                        else: 
                                print("Enrolling Student to Grade 5 is unsuccessful!")
                elif (StudentGradeasInt == 6):
                        if (StudentSection == "Rizal"):
                                InsertintoSection = "INSERT INTO section_rizal (Student_ID,HOMEROOM_Grade,MATH_Grade,SCIENCE_Grade,HEKASI_Grade,FILIPINO_Grade,ENGLISH_Grade,ESP_Grade,Class_ID,Student_IDCPY)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                Itemstobeinserted = (StudentID,HomeroomGrade,MathGrade,ScienceGrade,HekasiGrade,FilipinoGrade,EnglishGrade,EspGrade,Student_Class_ID,StudentID)
                                mycursor.execute(InsertintoSection,Itemstobeinserted)
                                mydb.commit()
                                print("Enrolling Student to Section Rizal is Successful!")
                        else:
                                print("Enrolling Student to Grade 6 is unsuccessful!")
                else:
                        print("Enrolling student is unsuccessful")
        
        def Show_Table_Students(self):
                try:
                        ShowTableStudent = 'SELECT * FROM STUDENTS WHERE Student_Classification = "NEW STUDENT"'
                        mycursor.execute(ShowTableStudent)
                        mydb.commit()
                        print("Displaying New Student Table is Successful")
                        recordsinstudent = mycursor.fetchall() 

                        # We set how many Rows and Columns our table is going to have. 
                        # We will also set the names of the Headers of tables that we have. 
                        self.NewStudents_Table.setRowCount(len(recordsinstudent))
                        self.NewStudents_Table.setColumnCount(19)
                        self.NewStudents_Table.setHorizontalHeaderLabels(["STUDENT ID","FIRSTNAME","LASTNAME","MIDDLENAME","AGE","GENDER","BLK AND LOT","STREET","SUBDIVISION","BARANGAY","CITY","CONTACT NO","CLASSIFICATION","GRADES","FORM136","FORM137","BIRTHCERTIFICATE","RESIDENCY","CLASS ID"])
                        
                        # header_settings set the Headers to Fit the size of the table.
                        header_settings = self.NewStudents_Table.horizontalHeader()
                        header_settings.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                        header_settings.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(9, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(10, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(11, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(12, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(13, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(14, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(15, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(16, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(17, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(18, QtWidgets.QHeaderView.ResizeToContents)


                        # This will iterate over the records in the (recordsinstudent) and will set the values to specific columns.
                        for i, (Student_ID, Student_Firstname, Student_Lastname, Student_Middlename, Student_Age, Student_Gender,BLK_And_Lot,Street,Subdivision,Barangay,City,Student_Contact_No,Student_Classification,isGrades,isForm136,isForm137,isBirthCertificate,isResidency,Class_ID) in enumerate(recordsinstudent):
                                new_Student_ID = str(Student_ID)
                                new_Student_Age = str(Student_Age)
                                new_Student_Contact_No = str(Student_Contact_No)        
                                new_isGrades= str(isGrades)
                                new_isForm136= str(isForm136)
                                new_isForm137= str(isForm137)
                                new_isBirthCertificate= str(isBirthCertificate)
                                new_isResidency= str(isResidency)
                                new_Student_Class_ID= str(Class_ID)
                        
                                item_Student_ID = QTableWidgetItem(new_Student_ID)
                                item_Student_Firstname = QTableWidgetItem(Student_Firstname)
                                item_Student_Lastname = QTableWidgetItem(Student_Lastname)
                                item_Student_Middleinitial = QTableWidgetItem(Student_Middlename)
                                item_Student_Age = QTableWidgetItem(new_Student_Age)
                                item_Student_Gender = QTableWidgetItem(Student_Gender)
                                item_Student_BLK_And_Lot = QTableWidgetItem(BLK_And_Lot)
                                item_Student_Street = QTableWidgetItem(Street)
                                item_Student_Subdivision = QTableWidgetItem(Subdivision)
                                item_Student_Barangay = QTableWidgetItem(Barangay)
                                item_Student_City = QTableWidgetItem(City)
                                item_Student_Contact_No = QTableWidgetItem(new_Student_Contact_No)
                                item_Student_Classification = QTableWidgetItem(Student_Classification)
                                item_isGrades = QTableWidgetItem(new_isGrades)
                                item_isForm136 = QTableWidgetItem(new_isForm136)
                                item_isForm137 = QTableWidgetItem(new_isForm137)
                                item_isBirthCertificate = QTableWidgetItem(new_isBirthCertificate)
                                item_isResidency = QTableWidgetItem(new_isResidency)
                                item_Student_Class_ID = QTableWidgetItem(new_Student_Class_ID)
                                self.NewStudents_Table.setItem(i, 0, item_Student_ID)
                                self.NewStudents_Table.setItem(i, 1, item_Student_Firstname)
                                self.NewStudents_Table.setItem(i, 2, item_Student_Lastname)
                                self.NewStudents_Table.setItem(i, 3, item_Student_Middleinitial)
                                self.NewStudents_Table.setItem(i, 4, item_Student_Age)
                                self.NewStudents_Table.setItem(i, 5, item_Student_Gender)
                                self.NewStudents_Table.setItem(i, 6, item_Student_BLK_And_Lot)
                                self.NewStudents_Table.setItem(i, 7, item_Student_Street)
                                self.NewStudents_Table.setItem(i, 8, item_Student_Subdivision)
                                self.NewStudents_Table.setItem(i, 9, item_Student_Barangay)
                                self.NewStudents_Table.setItem(i, 10, item_Student_City)
                                self.NewStudents_Table.setItem(i, 11, item_Student_Contact_No)
                                self.NewStudents_Table.setItem(i, 12, item_Student_Classification)
                                self.NewStudents_Table.setItem(i, 13, item_isGrades)
                                self.NewStudents_Table.setItem(i, 14, item_isForm136)
                                self.NewStudents_Table.setItem(i, 15, item_isForm137)
                                self.NewStudents_Table.setItem(i, 16, item_isBirthCertificate)
                                self.NewStudents_Table.setItem(i, 17, item_isResidency)
                                self.NewStudents_Table.setItem(i, 18, item_Student_Class_ID)
                                self.NewStudents_Table.show()
                except mc.Error as e:
                        print("Error in Showing Data")
        # OLD STUDENT FORM ---------------------------------------------
        def Inserting_OldStudentForm(self):
                StudentID = self.newStudent_IDLE.text()
                StudentNewGrade = int(self.Student_NewGradeLE.text())
                StudentNewSection = str(self.Student_NewSectionLE.text())
                StudentOldSection = str(self.Student_OldSectionLE.text())

                if (StudentOldSection == "Masipag"):
                        DeletionQuery = "DELETE FROM section_masipag WHERE Student_ID = %s AND Student_IDCPY=%s"
                        Itemstobedeleted = (StudentID,StudentID)
                        mycursor.execute(DeletionQuery,Itemstobedeleted)
                        mydb.commit()
                        print("Deleting Record From Section Masipag is Successful")
                elif (StudentOldSection == "Masunurin"):
                        DeletionQuery = "DELETE FROM section_masunurin WHERE Student_ID = %s AND Student_IDCPY=%s"
                        Itemstobedeleted = (StudentID,StudentID)
                        mycursor.execute(DeletionQuery,Itemstobedeleted)
                        mydb.commit()
                        print("Deleting Record From Section Masunurin is Successful")
                elif (StudentOldSection == "Uranium"):
                        DeletionQuery = "DELETE FROM section_uranium WHERE Student_ID = %s AND Student_IDCPY=%s"
                        Itemstobedeleted = (StudentID,StudentID)
                        mycursor.execute(DeletionQuery,Itemstobedeleted)
                        mydb.commit()
                        print("Deleting Record From Section Uranium is Successful")
                elif (StudentOldSection == "Xenon"):
                        DeletionQuery = "DELETE FROM section_xenon WHERE Student_ID = %s AND Student_IDCPY=%s"
                        Itemstobedeleted = (StudentID,StudentID)
                        mycursor.execute(DeletionQuery,Itemstobedeleted)
                        mydb.commit()
                        print("Deleting Record From Section Xenon is Successful")
                elif (StudentOldSection == "Sampaguita"):
                        DeletionQuery = "DELETE FROM section_sampaguita WHERE Student_ID = %s AND Student_IDCPY=%s"
                        Itemstobedeleted = (StudentID,StudentID)
                        mycursor.execute(DeletionQuery,Itemstobedeleted)
                        mydb.commit()
                        print("Deleting Record From Section Sampaguita is Successful")
                elif (StudentOldSection == "Sunflower"):
                        DeletionQuery = "DELETE FROM section_sunflower WHERE Student_ID = %s AND Student_IDCPY=%s"
                        Itemstobedeleted = (StudentID,StudentID)
                        mycursor.execute(DeletionQuery,Itemstobedeleted)
                        mydb.commit()
                        print("Deleting Record From Section Sunflower is Successful")
                elif (StudentOldSection == "Diamond"):
                        DeletionQuery = "DELETE FROM section_diamond WHERE Student_ID = %s AND Student_IDCPY=%s"
                        Itemstobedeleted = (StudentID,StudentID)
                        mycursor.execute(DeletionQuery,Itemstobedeleted)
                        mydb.commit()
                        print("Deletion is Successful")
                elif (StudentOldSection == "Ruby"):
                        DeletionQuery = "DELETE FROM section_ruby WHERE Student_ID = %s AND Student_IDCPY=%s"
                        Itemstobedeleted = (StudentID,StudentID)
                        mycursor.execute(DeletionQuery,Itemstobedeleted)
                        mydb.commit()
                        print("Deleting Record From Section Ruby is Successful")
                elif (StudentOldSection == "Narra"):
                        DeletionQuery = "DELETE FROM section_narra WHERE Student_ID = %s AND Student_IDCPY=%s"
                        Itemstobedeleted = (StudentID,StudentID)
                        mycursor.execute(DeletionQuery,Itemstobedeleted)
                        mydb.commit()
                        print("Deleting Record From Section Narra is Successful")
                elif (StudentOldSection == "Rizal"):
                        DeletionQuery = "DELETE FROM section_rizal WHERE Student_ID = %s AND Student_IDCPY=%s"
                        Itemstobedeleted = (StudentID,StudentID)
                        mycursor.execute(DeletionQuery,Itemstobedeleted)
                        mydb.commit()
                        print("Deleting Record From Section Rizal is Successful")
                else:
                        print("Delition of Previous Section Failed!")

                HomeroomGrade = 0
                MathGrade = 0 
                HekasiGrade = 0 
                FilipinoGrade = 0 
                EspGrade = 0
                EnglishGrade = 0
                ScienceGrade = 0
                TurningintoanOldStudent = "OLD STUDENT"

                if (StudentNewGrade == 1):
                        if (StudentNewSection == "Masipag"):
                                Class_ID = 1
                                UpdateQuery = "UPDATE STUDENTS SET Class_ID = %s,Student_Classification = %s WHERE Student_ID = %s"
                                Itemstobeinserted = (Class_ID,TurningintoanOldStudent,StudentID)
                                mycursor.execute(UpdateQuery,Itemstobeinserted)
                                mydb.commit()
                                print("Changing the Class ID of the Student is Successful")

                                AddtoSectionQuery = "INSERT INTO Section_Masipag (Student_ID,HOMEROOM_Grade,MATH_Grade,SCIENCE_Grade,HEKASI_Grade,FILIPINO_Grade,ENGLISH_Grade,ESP_Grade,Class_ID,Student_IDCPY)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                ItemstobeinsertedinSection = (StudentID,HomeroomGrade,MathGrade,ScienceGrade,HekasiGrade,FilipinoGrade,EnglishGrade,EspGrade,Class_ID,StudentID)
                                mycursor.execute(AddtoSectionQuery,ItemstobeinsertedinSection)
                                mydb.commit()
                                print("Successful")
                        elif (StudentNewSection == "Masunurin"):
                                Class_ID = 2
                                UpdateQuery = "UPDATE STUDENTS SET Class_ID = %s,Student_Classification = %s WHERE Student_ID = %s"
                                Itemstobeinserted = (Class_ID,TurningintoanOldStudent,StudentID)
                                mycursor.execute(UpdateQuery,Itemstobeinserted)
                                mydb.commit()
                                print("Successful")

                                AddtoSectionQuery = "INSERT INTO Section_Masunurin (Student_ID,HOMEROOM_Grade,MATH_Grade,SCIENCE_Grade,HEKASI_Grade,FILIPINO_Grade,ENGLISH_Grade,ESP_Grade,Class_ID,Student_IDCPY)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                ItemstobeinsertedinSection = (StudentID,HomeroomGrade,MathGrade,ScienceGrade,HekasiGrade,FilipinoGrade,EnglishGrade,EspGrade,Class_ID,StudentID)
                                mycursor.execute(AddtoSectionQuery,ItemstobeinsertedinSection)
                                mydb.commit()
                                print("Successful")
                        else: 
                                print("Invalid input in Section!")
                elif (StudentNewGrade == 2): 
                        if (StudentNewSection == "Uranium"):
                                Class_ID = 3
                                UpdateQuery = "UPDATE STUDENTS SET Class_ID = %s,Student_Classification = %s WHERE Student_ID = %s"
                                Itemstobeinserted = (Class_ID,TurningintoanOldStudent,StudentID)
                                mycursor.execute(UpdateQuery,Itemstobeinserted)
                                mydb.commit()
                                print("Successful")

                                AddtoSectionQuery = "INSERT INTO Section_Uranium (Student_ID,HOMEROOM_Grade,MATH_Grade,SCIENCE_Grade,HEKASI_Grade,FILIPINO_Grade,ENGLISH_Grade,ESP_Grade,Class_ID,Student_IDCPY)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                ItemstobeinsertedinSection = (StudentID,HomeroomGrade,MathGrade,ScienceGrade,HekasiGrade,FilipinoGrade,EnglishGrade,EspGrade,Class_ID,StudentID)
                                mycursor.execute(AddtoSectionQuery,ItemstobeinsertedinSection)
                                mydb.commit()
                                print("Successful")
                        elif (StudentNewSection == "Xenon"):
                                Class_ID = 4
                                UpdateQuery = "UPDATE STUDENTS SET Class_ID = %s,Student_Classification = %s WHERE Student_ID = %s"
                                Itemstobeinserted = (Class_ID,TurningintoanOldStudent,StudentID)
                                mycursor.execute(UpdateQuery,Itemstobeinserted)
                                mydb.commit()
                                print("Successful")

                                AddtoSectionQuery = "INSERT INTO Section_Xenon VALUES (Student_ID,HOMEROOM_Grade,MATH_Grade,SCIENCE_Grade,HEKASI_Grade,FILIPINO_Grade,ENGLISH_Grade,ESP_Grade,Class_ID,Student_IDCPY)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                ItemstobeinsertedinSection = (StudentID,HomeroomGrade,MathGrade,ScienceGrade,HekasiGrade,FilipinoGrade,EnglishGrade,EspGrade,Class_ID,StudentID)
                                mycursor.execute(AddtoSectionQuery,ItemstobeinsertedinSection)
                                mydb.commit()
                                print("Successful")
                        else: 
                                print("Invalid input in Section!")
                elif (StudentNewGrade == 3): 
                        if (StudentNewSection == "Sampaguita"):
                                Class_ID = 5
                                UpdateQuery = "UPDATE STUDENTS SET Class_ID = %s,Student_Classification = %s WHERE Student_ID = %s"
                                Itemstobeinserted = (Class_ID,TurningintoanOldStudent,StudentID)
                                mycursor.execute(UpdateQuery,Itemstobeinserted)
                                mydb.commit()
                                print("Successful")

                                AddtoSectionQuery = "INSERT INTO Section_Sampaguita (Student_ID,HOMEROOM_Grade,MATH_Grade,SCIENCE_Grade,HEKASI_Grade,FILIPINO_Grade,ENGLISH_Grade,ESP_Grade,Class_ID,Student_IDCPY)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                ItemstobeinsertedinSection = (StudentID,HomeroomGrade,MathGrade,ScienceGrade,HekasiGrade,FilipinoGrade,EnglishGrade,EspGrade,Class_ID,StudentID)
                                mycursor.execute(AddtoSectionQuery,ItemstobeinsertedinSection)
                                mydb.commit()
                                print("Successful")
                        elif (StudentNewSection == "Sunflower"):
                                Class_ID = 6
                                UpdateQuery = "UPDATE STUDENTS SET Class_ID = %s,Student_Classification = %s WHERE Student_ID = %s"
                                Itemstobeinserted = (Class_ID,TurningintoanOldStudent,StudentID)
                                mycursor.execute(UpdateQuery,Itemstobeinserted)
                                mydb.commit()
                                print("Successful")

                                AddtoSectionQuery = "INSERT INTO Section_Sunflower (Student_ID,HOMEROOM_Grade,MATH_Grade,SCIENCE_Grade,HEKASI_Grade,FILIPINO_Grade,ENGLISH_Grade,ESP_Grade,Class_ID,Student_IDCPY)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                ItemstobeinsertedinSection = (StudentID,HomeroomGrade,MathGrade,ScienceGrade,HekasiGrade,FilipinoGrade,EnglishGrade,EspGrade,Class_ID,StudentID)
                                mycursor.execute(AddtoSectionQuery,ItemstobeinsertedinSection)
                                mydb.commit()
                                print("Successful")
                        else: 
                                print("Invalid input in Section!")
                elif (StudentNewGrade == 4): 
                        if (StudentNewSection == "Diamond"):
                                Class_ID = 7
                                UpdateQuery = "UPDATE STUDENTS SET Class_ID = %s,Student_Classification = %s WHERE Student_ID = %s"
                                Itemstobeinserted = (Class_ID,TurningintoanOldStudent,StudentID)
                                mycursor.execute(UpdateQuery,Itemstobeinserted)
                                mydb.commit()
                                print("Successful")

                                AddtoSectionQuery = "INSERT INTO Section_Diamond (Student_ID,HOMEROOM_Grade,MATH_Grade,SCIENCE_Grade,HEKASI_Grade,FILIPINO_Grade,ENGLISH_Grade,ESP_Grade,Class_ID,Student_IDCPY)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                ItemstobeinsertedinSection = (StudentID,HomeroomGrade,MathGrade,ScienceGrade,HekasiGrade,FilipinoGrade,EnglishGrade,EspGrade,Class_ID,StudentID)
                                mycursor.execute(AddtoSectionQuery,ItemstobeinsertedinSection)
                                mydb.commit()
                                print("Successful")
                        elif (StudentNewSection == "Ruby"):
                                Class_ID = 8
                                UpdateQuery = "UPDATE STUDENTS SET Class_ID = %s,Student_Classification = %s WHERE Student_ID = %s"
                                Itemstobeinserted = (Class_ID,TurningintoanOldStudent,StudentID)
                                mycursor.execute(UpdateQuery,Itemstobeinserted)
                                mydb.commit()
                                print("Successful")

                                AddtoSectionQuery = "INSERT INTO Section_Ruby (Student_ID,HOMEROOM_Grade,MATH_Grade,SCIENCE_Grade,HEKASI_Grade,FILIPINO_Grade,ENGLISH_Grade,ESP_Grade,Class_ID,Student_IDCPY)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                ItemstobeinsertedinSection = (StudentID,HomeroomGrade,MathGrade,ScienceGrade,HekasiGrade,FilipinoGrade,EnglishGrade,EspGrade,Class_ID,StudentID)
                                mycursor.execute(AddtoSectionQuery,ItemstobeinsertedinSection)
                                mydb.commit()
                                print("Successful")
                        else: 
                                print("Invalid input in Section!")
                elif (StudentNewGrade == 5): 
                        if (StudentNewSection == "Narra"):
                                Class_ID = 9
                                UpdateQuery = "UPDATE STUDENTS SET Class_ID = %s,Student_Classification = %s WHERE Student_ID = %s"
                                Itemstobeinserted = (Class_ID,TurningintoanOldStudent,StudentID)
                                mycursor.execute(UpdateQuery,Itemstobeinserted)
                                mydb.commit() 
                                print("Successful")

                                AddtoSectionQuery = "INSERT INTO Section_Narra (Student_ID,HOMEROOM_Grade,MATH_Grade,SCIENCE_Grade,HEKASI_Grade,FILIPINO_Grade,ENGLISH_Grade,ESP_Grade,Class_ID,Student_IDCPY)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                ItemstobeinsertedinSection = (StudentID,HomeroomGrade,MathGrade,ScienceGrade,HekasiGrade,FilipinoGrade,EnglishGrade,EspGrade,Class_ID,StudentID)
                                mycursor.execute(AddtoSectionQuery,ItemstobeinsertedinSection)
                                mydb.commit()
                                print("Successful")
                        else: 
                                print("Invalid input in Section!")    
                elif (StudentNewGrade == 6): 
                        if (StudentNewSection == "Rizal"):
                                Class_ID = 10
                                UpdateQuery = "UPDATE STUDENTS SET Class_ID = %s,Student_Classification = %s WHERE Student_ID = %s"
                                Itemstobeinserted = (Class_ID,TurningintoanOldStudent,StudentID)
                                mycursor.execute(UpdateQuery,Itemstobeinserted)
                                mydb.commit() 
                                print("Successful")

                                AddtoSectionQuery = "INSERT INTO Section_Rizal (Student_ID,HOMEROOM_Grade,MATH_Grade,SCIENCE_Grade,HEKASI_Grade,FILIPINO_Grade,ENGLISH_Grade,ESP_Grade,Class_ID,Student_IDCPY)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                ItemstobeinsertedinSection = (StudentID,HomeroomGrade,MathGrade,ScienceGrade,HekasiGrade,FilipinoGrade,EnglishGrade,EspGrade,Class_ID,StudentID)
                                mycursor.execute(AddtoSectionQuery,ItemstobeinsertedinSection)
                                mydb.commit()
                                print("Successful")
                        else: 
                                print("Invalid input in Section!") 
                else: 
                        print("Invalid input in Grades!")
        
        def Show_Table_OldStudents(self):
                try:    
                        ShowTableStudent = 'SELECT * FROM STUDENTS WHERE Student_Classification ="OLD STUDENT";'
                        mycursor.execute(ShowTableStudent)
                        mydb.commit()
                        print("Displaying Student Table is Successful")
                        recordsinstudent = mycursor.fetchall() 


                        # We set how many Rows and Columns our table is going to have. 
                        # We will also set the names of the Headers of tables that we have. 
                        self.OldStudents_Table.setRowCount(len(recordsinstudent))
                        self.OldStudents_Table.setColumnCount(19)
                        self.OldStudents_Table.setHorizontalHeaderLabels(["STUDENT ID","FIRSTNAME","LASTNAME","MIDDLENAME","AGE","GENDER","BLK AND LOT","STREET","SUBDIVISION","BARANGAY","CITY","CONTACT NO","CLASSIFICATION","GRADES","FORM136","FORM137","BIRTHCERTIFICATE","RESIDENCY","CLASS ID"])
                        
                        # header_settings set the Headers to Fit the size of the table.
                        header_settings = self.OldStudents_Table.horizontalHeader()
                        header_settings.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                        header_settings.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(9, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(10, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(11, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(12, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(13, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(14, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(15, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(16, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(17, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(18, QtWidgets.QHeaderView.ResizeToContents)


                        # This will iterate over the records in the (recordsinstudent) and will set the values to specific columns.
                        for i, (Student_ID, Student_Firstname, Student_Lastname, Student_Middleinitial, Student_Age, Student_Gender,BLK_And_Lot,Street,Subdivision,Barangay,City,Student_Contact_No,Student_Classification,isGrades,isForm136,isForm137,isBirthCertificate,isResidency,Class_ID) in enumerate(recordsinstudent):
                                new_Student_ID = str(Student_ID)
                                new_Student_Age = str(Student_Age)
                                new_isGrades= str(isGrades)
                                new_isForm136= str(isForm136)
                                new_isForm137= str(isForm137)
                                new_isBirthCertificate= str(isBirthCertificate)
                                new_isResidency= str(isResidency)
                                new_Student_Class_ID= str(Class_ID)
                        
                                item_Student_ID = QTableWidgetItem(new_Student_ID)
                                item_Student_Firstname = QTableWidgetItem(Student_Firstname)
                                item_Student_Lastname = QTableWidgetItem(Student_Lastname)
                                item_Student_Middleinitial = QTableWidgetItem(Student_Middleinitial)
                                item_Student_Age = QTableWidgetItem(new_Student_Age)
                                item_Student_Gender = QTableWidgetItem(Student_Gender)
                                item_Student_BLK_And_Lot = QTableWidgetItem(BLK_And_Lot)
                                item_Student_Street = QTableWidgetItem(Street)
                                item_Student_Subdivision = QTableWidgetItem(Subdivision)
                                item_Student_Barangay = QTableWidgetItem(Barangay)
                                item_Student_City = QTableWidgetItem(City)
                                new_Student_Contact_No = str(Student_Contact_No)
                                item_Student_Contact_No = QTableWidgetItem(new_Student_Contact_No)
                                item_Student_Classification = QTableWidgetItem(Student_Classification)
                                item_isGrades = QTableWidgetItem(new_isGrades)
                                item_isForm136 = QTableWidgetItem(new_isForm136)
                                item_isForm137 = QTableWidgetItem(new_isForm137)
                                item_isBirthCertificate = QTableWidgetItem(new_isBirthCertificate)
                                item_isResidency = QTableWidgetItem(new_isResidency)
                                item_Student_Class_ID = QTableWidgetItem(new_Student_Class_ID)
                                self.OldStudents_Table.setItem(i, 0, item_Student_ID)
                                self.OldStudents_Table.setItem(i, 1, item_Student_Firstname)
                                self.OldStudents_Table.setItem(i, 2, item_Student_Lastname)
                                self.OldStudents_Table.setItem(i, 3, item_Student_Middleinitial)
                                self.OldStudents_Table.setItem(i, 4, item_Student_Age)
                                self.OldStudents_Table.setItem(i, 5, item_Student_Gender)
                                self.OldStudents_Table.setItem(i, 6, item_Student_BLK_And_Lot)
                                self.OldStudents_Table.setItem(i, 7, item_Student_Street)
                                self.OldStudents_Table.setItem(i, 8, item_Student_Subdivision)
                                self.OldStudents_Table.setItem(i, 9, item_Student_Barangay)
                                self.OldStudents_Table.setItem(i, 10, item_Student_City)
                                self.OldStudents_Table.setItem(i, 11, item_Student_Contact_No)
                                self.OldStudents_Table.setItem(i, 12, item_Student_Classification)
                                self.OldStudents_Table.setItem(i, 13, item_isGrades)
                                self.OldStudents_Table.setItem(i, 14, item_isForm136)
                                self.OldStudents_Table.setItem(i, 15, item_isForm137)
                                self.OldStudents_Table.setItem(i, 16, item_isBirthCertificate)
                                self.OldStudents_Table.setItem(i, 17, item_isResidency)
                                self.OldStudents_Table.setItem(i, 18, item_Student_Class_ID)
                                self.OldStudents_Table.show()
                except mc.Error as e:
                        print("Error in Showing Data")

        # START TAB 3 --------------------------------
        def Show_Student_Schedule(self):
                try:
                        Start = 0
                        End = 0
                        SectionName = ""
                        StudentDummy = 0
                        
                        DataneededbyQuery = (Start,End,SectionName)
                        StudentID = self.Student_IDSEARCHLE.text()

                        RetrievingtheClassID = "SELECT * FROM STUDENTS WHERE STUDENT_ID = %s AND STUDENT_ID > %s"
                        StudentIDData = (StudentID,StudentDummy)
                        mycursor.execute(RetrievingtheClassID,StudentIDData)
                        mydb.commit()
                        Class_ID  = mycursor.fetchone()[18]
                        print("Retriving Class ID is Successful")

                        if (Class_ID == 1):
                                Start = 101 
                                End = 107
                                SectionName = "Masipag"
                                DataneededbyQuery = (Start,End,SectionName)
                        elif (Class_ID == 2):
                                Start = 1012
                                End = 1072
                                SectionName = "Masunurin"
                                DataneededbyQuery = (Start,End,SectionName)
                        elif (Class_ID == 3):
                                Start = 201
                                End = 207
                                SectionName = "Uranium"
                                DataneededbyQuery = (Start,End,SectionName)
                        elif (Class_ID == 4):
                                Start = 2012
                                End = 2072
                                SectionName = "Xenon"
                                DataneededbyQuery = (Start,End,SectionName)
                        elif (Class_ID == 5):
                                Start = 301
                                End = 307
                                SectionName = "Sampaguita"
                                DataneededbyQuery = (Start,End,SectionName)
                        elif (Class_ID == 6):
                                Start = 3012
                                End = 3072
                                SectionName = "Sunflower"
                                DataneededbyQuery = (Start,End,SectionName)
                        elif (Class_ID == 7):
                                Start = 401
                                End = 407
                                SectionName = "Diamond"
                                DataneededbyQuery = (Start,End,SectionName)
                        elif (Class_ID == 8):
                                Start = 4012
                                End = 4072
                                SectionName = "Ruby"
                                DataneededbyQuery = (Start,End,SectionName)
                        elif (Class_ID == 9):
                                Start = 501
                                End = 507
                                SectionName = "Narra"
                                DataneededbyQuery = (Start,End,SectionName)
                        elif (Class_ID == 10):
                                Start = 601
                                End = 607
                                SectionName = "Rizal"
                                DataneededbyQuery = (Start,End,SectionName)
                        else: 
                                print("Query Failed")


                        ShowStudentSchedule = """SELECT C.Section_Name,SCH.Schedule_Code,S.SUBJECT_ID,S.SUBJECT_NAME,S.SUBJECT_CODE,S.SUBJECT_TIME,S.TEACHER_ID,T.Teacher_Firstname,T.Teacher_Lastname,T.Teacher_Middleinitial,DEP.Department_Name
                                                        FROM SUBJECT AS S,TEACHER AS T,SCHEDULE AS SCH,DEPARTMENT AS DEP,CLASS AS C
                                                        WHERE (S.TEACHER_ID = T.TEACHER_ID) AND (SCH.Subject_ID = S.Subject_ID) AND (T.Department_ID = DEP.Department_ID)
                                                        AND S.SUBJECT_ID BETWEEN %s AND %s AND C.Section_Name= %s;"""
                        mycursor.execute(ShowStudentSchedule,DataneededbyQuery)
                        mydb.commit()
                        print("Displaying Student Schedule is Successful")
                        studentschedule = mycursor.fetchall() 

                        # We set how many Rows and Columns our table is going to have. 
                        # We will also set the names of the Headers of tables that we have. 
                        self.StudentSchedule_Table.setRowCount(len(studentschedule))
                        self.StudentSchedule_Table.setColumnCount(11)
                        self.StudentSchedule_Table.setHorizontalHeaderLabels(["SECTION NAME","SCHED CODE","SUBJECT ID","SUBJECT NAME","CODE","TIME","TEACHER ID","TEACHER FIRSTNAME","TEACHER LASTNAME","TEACHER MIDDLE NAME","DEPARTMENT"])
                        
                        # header_settings set the Headers to Fit the size of the table.
                        header_settings = self.StudentSchedule_Table.horizontalHeader()
                        header_settings.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                        header_settings.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(9, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(10, QtWidgets.QHeaderView.ResizeToContents)
                        


                        # This will iterate over the records in the (recordsinstudent) and will set the values to specific columns.
                        for i, (Section_Name,Schedule_Code,SUBJECT_ID,SUBJECT_NAME,SUBJECT_CODE,SUBJECT_TIME,TEACHER_ID,Teacher_Firstname,Teacher_Lastname,Teacher_Middleinitial,Department_Name) in enumerate(studentschedule):
                                newScheduleCode = str(Schedule_Code) 
                                newSubjectID = str(SUBJECT_ID)
                                newSubjectCode = str(SUBJECT_CODE)


                        
                                item_Section_Name = QTableWidgetItem(Section_Name)
                                item_Schedule_Code = QTableWidgetItem(newScheduleCode)
                                item_Subject_ID = QTableWidgetItem(newSubjectID)
                                item_Subject_Name = QTableWidgetItem(SUBJECT_NAME)
                                item_Subject_Code  = QTableWidgetItem(newSubjectCode)
                                item_Subject_Time = QTableWidgetItem(SUBJECT_TIME)
                                item_Teacher_ID = QTableWidgetItem(TEACHER_ID)
                                item_Teacher_Firstname = QTableWidgetItem(Teacher_Firstname)
                                item_Teacher_Lastname  = QTableWidgetItem(Teacher_Lastname)
                                item_Teacher_Middleinitial = QTableWidgetItem(Teacher_Middleinitial)
                                item_Department_Name = QTableWidgetItem(Department_Name)
                                
                                self.StudentSchedule_Table.setItem(i, 0, item_Section_Name)
                                self.StudentSchedule_Table.setItem(i, 1, item_Schedule_Code)
                                self.StudentSchedule_Table.setItem(i, 2, item_Subject_ID)
                                self.StudentSchedule_Table.setItem(i, 3, item_Subject_Name)
                                self.StudentSchedule_Table.setItem(i, 4, item_Subject_Code)
                                self.StudentSchedule_Table.setItem(i, 5, item_Subject_Time)
                                self.StudentSchedule_Table.setItem(i, 6, item_Teacher_ID)
                                self.StudentSchedule_Table.setItem(i, 7, item_Teacher_Firstname)
                                self.StudentSchedule_Table.setItem(i, 8, item_Teacher_Lastname)
                                self.StudentSchedule_Table.setItem(i, 9, item_Teacher_Middleinitial)
                                self.StudentSchedule_Table.setItem(i, 10, item_Department_Name)
                                self.StudentSchedule_Table.show()
                except: 
                        print("Error")

        def Show_Section_Schedule(self):
                try:    
                        Section = self.ScheduleSection_SEARCHLE.text()
                        if (Section == "Masipag"):
                                Start = 101 
                                End = 107
                                Section = "Masipag"
                                DataneededbyQuery = (Start,End,Section)
                                print("Finding the Schedule_Code is Successful")
                        elif (Section == "Masunurin"):
                                Start = 1012 
                                End = 1072
                                Section = "Masunurin"
                                DataneededbyQuery = (Start,End,Section)
                                print("Finding the Schedule_Code is Successful")
                        elif (Section == "Uranium"):
                                Start = 201
                                End = 207
                                Section = "Uranium"
                                DataneededbyQuery = (Start,End,Section)
                                print("Finding the Schedule_Code is Successful")
                        elif (Section == "Xenon"):
                                Start = 2012 
                                End = 2072
                                Section = "Xenon"
                                DataneededbyQuery = (Start,End,Section)
                                print("Finding the Schedule_Code is Successful")
                        elif (Section == "Sampaguita"):
                                Start = 301 
                                End = 307
                                Section = "Sampaguita"
                                DataneededbyQuery = (Start,End,Section)
                                print("Finding the Schedule_Code is Successful")
                        elif (Section == "Sunflower"):
                                Start = 3012 
                                End = 3072
                                Section = "Sunflower"
                                DataneededbyQuery = (Start,End,Section)
                                print("Finding the Schedule_Code is Successful")
                        elif (Section == "Diamond"):
                                Start = 401 
                                End = 402
                                Section = "Diamond"
                                DataneededbyQuery = (Start,End,Section)
                                print("Finding the Schedule_Code is Successful")
                        elif (Section == "Ruby"):
                                Start = 4012 
                                End = 4072
                                Section = "Ruby"
                                DataneededbyQuery = (Start,End,Section)
                                print("Finding the Schedule_Code is Successful")
                        elif (Section == "Narra"):
                                Start = 501
                                End = 507
                                Section = "Narra"
                                DataneededbyQuery = (Start,End,Section)
                                print("Finding the Schedule_Code is Successful")
                        elif (Section == "Rizal"):
                                Start = 601 
                                End = 607
                                Section = "Rizal"
                                DataneededbyQuery = (Start,End,Section)
                                print("Finding the Schedule_Code is Successful")
                        else: 
                                print("The Schedule_Code given does not exist.")
                        

                        ShowSectionSchedule = """SELECT C.Section_Name,SCH.Schedule_Code,S.SUBJECT_ID,S.SUBJECT_NAME,S.SUBJECT_CODE,S.SUBJECT_TIME,S.TEACHER_ID,T.Teacher_Firstname,T.Teacher_Lastname,T.Teacher_Middleinitial,DEP.Department_Name
                                                        FROM SUBJECT AS S,TEACHER AS T,SCHEDULE AS SCH,DEPARTMENT AS DEP,CLASS AS C
                                                        WHERE (S.TEACHER_ID = T.TEACHER_ID) AND (SCH.Subject_ID = S.Subject_ID) AND (T.Department_ID = DEP.Department_ID)
                                                        AND S.SUBJECT_ID BETWEEN %s AND %s AND C.Section_Name= %s;"""
                        mycursor.execute(ShowSectionSchedule,DataneededbyQuery)
                        mydb.commit()
                        sectionschedule = mycursor.fetchall()
                        print("Displaying Student Schedule is Successful")

                        # We set how many Rows and Columns our table is going to have. 
                        # We will also set the names of the Headers of tables that we have. 
                        self.SectionSchedule_Table.setRowCount(len(sectionschedule))
                        self.SectionSchedule_Table.setColumnCount(11)
                        self.SectionSchedule_Table.setHorizontalHeaderLabels(["SECTION NAME","SCHED CODE","SUBJECT ID","SUBJECT NAME","CODE","TIME","TEACHER ID","TEACHER FIRSTNAME","TEACHER LASTNAME","TEACHER MIDDLE NAME","DEPARTMENT"])
                        
                        # header_settings set the Headers to Fit the size of the table.
                        header_settings = self.SectionSchedule_Table.horizontalHeader()
                        header_settings.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                        header_settings.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(9, QtWidgets.QHeaderView.ResizeToContents)
                        header_settings.setSectionResizeMode(10, QtWidgets.QHeaderView.ResizeToContents)
                        


                        # This will iterate over the records in the (recordsinstudent) and will set the values to specific columns.
                        for i, (Section_Name,ScheduleCode,SUBJECT_ID,SUBJECT_NAME,SUBJECT_CODE,SUBJECT_TIME,TEACHER_ID,Teacher_Firstname,Teacher_Lastname,Teacher_Middleinitial,Department_Name) in enumerate(sectionschedule):
                                newScheduleCode = str(ScheduleCode) 
                                newSubjectID = str(SUBJECT_ID)
                                newSubjectCode = str(SUBJECT_CODE)


                        
                                item_Section_Name = QTableWidgetItem(Section_Name)
                                item_Schedule_Code = QTableWidgetItem(newScheduleCode)
                                item_Subject_ID = QTableWidgetItem(newSubjectID)
                                item_Subject_Name = QTableWidgetItem(SUBJECT_NAME)
                                item_Subject_Code  = QTableWidgetItem(newSubjectCode)
                                item_Subject_Time = QTableWidgetItem(SUBJECT_TIME)
                                item_Teacher_ID = QTableWidgetItem(TEACHER_ID)
                                item_Teacher_Firstname = QTableWidgetItem(Teacher_Firstname)
                                item_Teacher_Lastname  = QTableWidgetItem(Teacher_Lastname)
                                item_Teacher_Middleinitial = QTableWidgetItem(Teacher_Middleinitial)
                                item_Department_Name = QTableWidgetItem(Department_Name)
                                
                                self.SectionSchedule_Table.setItem(i, 0, item_Section_Name)
                                self.SectionSchedule_Table.setItem(i, 1, item_Schedule_Code)
                                self.SectionSchedule_Table.setItem(i, 2, item_Subject_ID)
                                self.SectionSchedule_Table.setItem(i, 3, item_Subject_Name)
                                self.SectionSchedule_Table.setItem(i, 4, item_Subject_Code)
                                self.SectionSchedule_Table.setItem(i, 5, item_Subject_Time)
                                self.SectionSchedule_Table.setItem(i, 6, item_Teacher_ID)
                                self.SectionSchedule_Table.setItem(i, 7, item_Teacher_Firstname)
                                self.SectionSchedule_Table.setItem(i, 8, item_Teacher_Lastname)
                                self.SectionSchedule_Table.setItem(i, 9, item_Teacher_Middleinitial)
                                self.SectionSchedule_Table.setItem(i, 10, item_Department_Name)
                                self.SectionSchedule_Table.show()
                except: 
                        print("Error!")
        # TEACHER ---------------------------------------------------------
        def Show_Specific_Teacher_Record(self):
                try:
                        SpecificTeacher = self.Teacher_Specific_SearchLE.text()
                        self.Teacher_Specific_SearchLE.clear()
                        ShowSpecificTeacher = "SELECT * FROM TEACHER WHERE Teacher_ID =" + SpecificTeacher
                        mycursor.execute(ShowSpecificTeacher,SpecificTeacher)
                        mydb.commit
                        print("Successful")
                        recordofteacher = mycursor.fetchall()

                        # We set how many Rows and Columns our table is going to have.
                        # We will also set the names of the Headers of tables that we have. 
                        self.Show_Specific_Teacher_RecordTBL.setRowCount(len(recordofteacher))
                        self.Show_Specific_Teacher_RecordTBL.setColumnCount(5)
                        self.Show_Specific_Teacher_RecordTBL.setHorizontalHeaderLabels(["TEACHER ID","FIRSTNAME","LASTNAME","MIDDLENAME","DEPARTMENT ID"])

                        for i, (Teacher_ID,Teacher_Firstname,Teacher_Lastname,Teacher_Middleinitial,Department_ID) in enumerate(recordofteacher):
                                string_Teacher_ID = str(Teacher_ID)
                                string_Department_ID = str(Department_ID)

                                item_in_Teacher_ID = QTableWidgetItem(string_Teacher_ID)
                                item_in_Teacher_Firstname = QTableWidgetItem(Teacher_Firstname)
                                item_in_Teacher_Lastname = QTableWidgetItem(Teacher_Lastname)
                                item_in_Teacher_Middleinitial = QTableWidgetItem(Teacher_Middleinitial)
                                item_in_Department_ID = QTableWidgetItem(string_Department_ID)

                                self.Show_Specific_Teacher_RecordTBL.setItem(i, 0, item_in_Teacher_ID)
                                self.Show_Specific_Teacher_RecordTBL.setItem(i, 1, item_in_Teacher_Firstname)
                                self.Show_Specific_Teacher_RecordTBL.setItem(i, 2, item_in_Teacher_Lastname)
                                self.Show_Specific_Teacher_RecordTBL.setItem(i, 3, item_in_Teacher_Middleinitial)
                                self.Show_Specific_Teacher_RecordTBL.setItem(i, 4, item_in_Department_ID)
                                self.Show_Specific_Teacher_RecordTBL.show()
                except:
                        print("Error!")
        
        def Show_All_Teacher_Record(self):
                try:
                        ShowSpecificTeacher = """SELECT * FROM TEACHER"""
                        mycursor.execute(ShowSpecificTeacher)
                        mydb.commit
                        print("Successful")
                        recordofteacher = mycursor.fetchall()

                        # We set how many Rows and Columns our table is going to have.
                        # We will also set the names of the Headers of tables that we have. 
                        self.Show_All_Teacher_RecordTBL.setRowCount(len(recordofteacher))
                        self.Show_All_Teacher_RecordTBL.setColumnCount(5)
                        self.Show_All_Teacher_RecordTBL.setHorizontalHeaderLabels(["TEACHER ID","FIRSTNAME","LASTNAME","MIDDLENAME","DEPARTMENT ID"])

                        for i, (Teacher_ID,Teacher_Firstname,Teacher_Lastname,Teacher_Middleinitial,Department_ID) in enumerate(recordofteacher):
                                string_Teacher_ID = str(Teacher_ID)
                                string_Department_ID = str(Department_ID)

                                item_in_Teacher_ID = QTableWidgetItem(string_Teacher_ID)
                                item_in_Teacher_Firstname = QTableWidgetItem(Teacher_Firstname)
                                item_in_Teacher_Lastname = QTableWidgetItem(Teacher_Lastname)
                                item_in_Teacher_Middleinitial = QTableWidgetItem(Teacher_Middleinitial)
                                item_in_Department_ID = QTableWidgetItem(string_Department_ID)

                                self.Show_All_Teacher_RecordTBL.setItem(i, 0, item_in_Teacher_ID)
                                self.Show_All_Teacher_RecordTBL.setItem(i, 1, item_in_Teacher_Firstname)
                                self.Show_All_Teacher_RecordTBL.setItem(i, 2, item_in_Teacher_Lastname)
                                self.Show_All_Teacher_RecordTBL.setItem(i, 3, item_in_Teacher_Middleinitial)
                                self.Show_All_Teacher_RecordTBL.setItem(i, 4, item_in_Department_ID)
                                self.Show_All_Teacher_RecordTBL.show()
                except:
                        print("Error!")


        # DEPARTMENT --------------------------------------------------------------------
        def Show_Table_Department(self):
                try:
                        ShowTableDepartment = """SELECT * FROM Department"""
                        mycursor.execute(ShowTableDepartment)
                        mydb.commit
                        print("Successful")
                        recordsindepartment = mycursor.fetchall() 
                        
                        # We set how many Rows and Columns our table is going to have.
                        # We will also set the names of the Headers of tables that we have. 
                        self.Departmenttableselector.setRowCount(len(recordsindepartment))
                        self.Departmenttableselector.setColumnCount(2)
                        self.Departmenttableselector.setHorizontalHeaderLabels(["ID","Department Name"])

                        # header_settings set the Headers to Fit the size of the table.
                        header_settings = self.Departmenttableselector.horizontalHeader()
                        header_settings.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                        header_settings.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

                        for i, (Department_ID,Department_Name) in enumerate(recordsindepartment):
                                string_Department_ID = str(Department_ID)

                                item_in_Department_ID = QTableWidgetItem(string_Department_ID)
                                item_in_Department_Name = QTableWidgetItem(Department_Name)

                                self.Departmenttableselector.setItem(i, 0, item_in_Department_ID)
                                self.Departmenttableselector.setItem(i, 1, item_in_Department_Name)
                                self.Departmenttableselector.show()
                except:
                        print("Error!")
        
        def Add_Item_in_Department(self):
                try:
                        DepartmentID = self.Department_IDLE.text()
                        self.Department_IDLE.clear()
                        DepartmentName = self.Department_NameLE.text()
                        self.Department_NameLE.clear()

                        InsertItemDepartment = "INSERT INTO Department(Department_ID,Department_Name) VALUES (%s,%s)"
                        Itemstobeinserted = (DepartmentID,DepartmentName)

                        mycursor.execute(InsertItemDepartment,Itemstobeinserted)
                        mydb.commit()
                        print("Successful")
                except:
                        print("Error!")

        def Delete_Item_in_Department(self):
                DepartmentID = self.Department_IDLE.text()
                self.Department_IDLE.clear()
                DepartmentName= self.Department_NameLE.text()
                self.Department_NameLE.clear()

                DeleteItemDepartment = "DELETE FROM Department WHERE Department_ID=%s AND Department_Name=%s"
                Itemstobedeleted = (DepartmentID,DepartmentName)

                mycursor.execute(DeleteItemDepartment,Itemstobedeleted)
                mydb.commit()
                print("Successful")

        def Update_Item_in_Department(self):
                DepartmentID = self.Department_IDLE.text()
                self.Department_IDLE.clear()
                DepartmentName = self.Department_NameLE.text()
                self.Department_NameLE.clear()

                UpdateIteminDepartment = "UPDATE department set Department_Name = %s WHERE Department_ID = %s"
                Itemstobeupdated = (DepartmentName,DepartmentID)

                mycursor.execute(UpdateIteminDepartment,Itemstobeupdated)
                mydb.commit()
                print("Succesful")

        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1135, 699)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
                self.tabWidget.setGeometry(QtCore.QRect(0, 70, 1141, 601))
                self.tabWidget.setObjectName("tabWidget")
                self.tab = QtWidgets.QWidget()
                self.tab.setObjectName("tab")
                self.label = QtWidgets.QLabel(self.tab)
                self.label.setGeometry(QtCore.QRect(450, 10, 221, 41))
                font = QtGui.QFont()
                font.setPointSize(15)
                self.label.setFont(font)
                self.label.setObjectName("label")
                self.Student_IDLA = QtWidgets.QLabel(self.tab)
                self.Student_IDLA.setGeometry(QtCore.QRect(20, 70, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_IDLA.setFont(font)
                self.Student_IDLA.setObjectName("Student_IDLA")
                self.Student_FirstnameLA = QtWidgets.QLabel(self.tab)
                self.Student_FirstnameLA.setGeometry(QtCore.QRect(20, 90, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_FirstnameLA.setFont(font)
                self.Student_FirstnameLA.setObjectName("Student_FirstnameLA")
                self.Student_LastnameLA = QtWidgets.QLabel(self.tab)
                self.Student_LastnameLA.setGeometry(QtCore.QRect(20, 110, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_LastnameLA.setFont(font)
                self.Student_LastnameLA.setObjectName("Student_LastnameLA")
                self.Student_MiddlenameLA = QtWidgets.QLabel(self.tab)
                self.Student_MiddlenameLA.setGeometry(QtCore.QRect(20, 130, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_MiddlenameLA.setFont(font)
                self.Student_MiddlenameLA.setObjectName("Student_MiddlenameLA")
                self.Student_AgeLA = QtWidgets.QLabel(self.tab)
                self.Student_AgeLA.setGeometry(QtCore.QRect(20, 150, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_AgeLA.setFont(font)
                self.Student_AgeLA.setObjectName("Student_AgeLA")
                self.Student_GenderLA = QtWidgets.QLabel(self.tab)
                self.Student_GenderLA.setGeometry(QtCore.QRect(20, 170, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_GenderLA.setFont(font)
                self.Student_GenderLA.setObjectName("Student_GenderLA")
                self.Student_BLKAndLotLA = QtWidgets.QLabel(self.tab)
                self.Student_BLKAndLotLA.setGeometry(QtCore.QRect(20, 190, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_BLKAndLotLA.setFont(font)
                self.Student_BLKAndLotLA.setObjectName("Student_BLKAndLotLA")
                self.Student_StreetLA = QtWidgets.QLabel(self.tab)
                self.Student_StreetLA.setGeometry(QtCore.QRect(20, 210, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_StreetLA.setFont(font)
                self.Student_StreetLA.setObjectName("Student_StreetLA")
                self.Student_SubdivisionLA = QtWidgets.QLabel(self.tab)
                self.Student_SubdivisionLA.setGeometry(QtCore.QRect(20, 230, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_SubdivisionLA.setFont(font)
                self.Student_SubdivisionLA.setObjectName("Student_SubdivisionLA")
                self.Student_BarangayLA = QtWidgets.QLabel(self.tab)
                self.Student_BarangayLA.setGeometry(QtCore.QRect(20, 250, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_BarangayLA.setFont(font)
                self.Student_BarangayLA.setObjectName("Student_BarangayLA")
                self.Student_CityLA = QtWidgets.QLabel(self.tab)
                self.Student_CityLA.setGeometry(QtCore.QRect(20, 270, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_CityLA.setFont(font)
                self.Student_CityLA.setObjectName("Student_CityLA")
                self.Student_Contact_NoLA = QtWidgets.QLabel(self.tab)
                self.Student_Contact_NoLA.setGeometry(QtCore.QRect(20, 290, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_Contact_NoLA.setFont(font)
                self.Student_Contact_NoLA.setObjectName("Student_Contact_NoLA")
                self.Student_ClassificationLA = QtWidgets.QLabel(self.tab)
                self.Student_ClassificationLA.setGeometry(QtCore.QRect(20, 310, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_ClassificationLA.setFont(font)
                self.Student_ClassificationLA.setObjectName("Student_ClassificationLA")
                self.Student_isGradesLA = QtWidgets.QLabel(self.tab)
                self.Student_isGradesLA.setGeometry(QtCore.QRect(20, 330, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_isGradesLA.setFont(font)
                self.Student_isGradesLA.setObjectName("Student_isGradesLA")
                self.Student_isForm136LA = QtWidgets.QLabel(self.tab)
                self.Student_isForm136LA.setGeometry(QtCore.QRect(20, 350, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_isForm136LA.setFont(font)
                self.Student_isForm136LA.setObjectName("Student_isForm136LA")
                self.Student_isForm137LA = QtWidgets.QLabel(self.tab)
                self.Student_isForm137LA.setGeometry(QtCore.QRect(20, 370, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_isForm137LA.setFont(font)
                self.Student_isForm137LA.setObjectName("Student_isForm137LA")
                self.Student_isBirthCertificateLA = QtWidgets.QLabel(self.tab)
                self.Student_isBirthCertificateLA.setGeometry(QtCore.QRect(20, 390, 150, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_isBirthCertificateLA.setFont(font)
                self.Student_isBirthCertificateLA.setObjectName("Student_isBirthCertificateLA")
                self.Student_isResidencyLA = QtWidgets.QLabel(self.tab)
                self.Student_isResidencyLA.setGeometry(QtCore.QRect(20, 410, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_isResidencyLA.setFont(font)
                self.Student_isResidencyLA.setObjectName("Student_isResidencyLA")
                self.Student_ClassID_FKLA = QtWidgets.QLabel(self.tab)
                self.Student_ClassID_FKLA.setGeometry(QtCore.QRect(20, 430, 150, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_ClassID_FKLA.setFont(font)
                self.Student_ClassID_FKLA.setObjectName("Student_ClassID_FKLA")
                self.Student_Grade_2LA = QtWidgets.QLabel(self.tab)
                self.Student_Grade_2LA.setGeometry(QtCore.QRect(20, 450, 150, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_Grade_2LA.setFont(font)
                self.Student_Grade_2LA.setObjectName("Student_Grade_2LA")
                self.Student_Section_2LA = QtWidgets.QLabel(self.tab)
                self.Student_Section_2LA.setGeometry(QtCore.QRect(20, 470, 150, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_Section_2LA.setFont(font)
                self.Student_Section_2LA.setObjectName("Student_Section_2LA")

                self.Student_IDLE = QtWidgets.QLineEdit(self.tab)
                self.Student_IDLE.setGeometry(QtCore.QRect(175, 70, 201, 21))
                self.Student_IDLE.setObjectName("Student_IDLE")
                self.Student_FirstnameLE = QtWidgets.QLineEdit(self.tab)
                self.Student_FirstnameLE.setGeometry(QtCore.QRect(175, 90, 201, 21))
                self.Student_FirstnameLE.setObjectName("Student_FirstnameLE")
                self.Student_LastnameLE = QtWidgets.QLineEdit(self.tab)
                self.Student_LastnameLE.setGeometry(QtCore.QRect(175, 110, 201, 21))
                self.Student_LastnameLE.setObjectName("Student_LastnameLE")
                self.Student_MiddlenameLE = QtWidgets.QLineEdit(self.tab)
                self.Student_MiddlenameLE.setGeometry(QtCore.QRect(175, 130, 201, 21))
                self.Student_MiddlenameLE.setObjectName("Student_MiddlenameLE")
                self.Student_AgeLE = QtWidgets.QLineEdit(self.tab)
                self.Student_AgeLE.setGeometry(QtCore.QRect(175, 150, 201, 21))
                self.Student_AgeLE.setObjectName("Student_AgeLE")
                self.Student_GenderLE = QtWidgets.QLineEdit(self.tab)
                self.Student_GenderLE.setGeometry(QtCore.QRect(175, 170, 201, 21))
                self.Student_GenderLE.setObjectName("Student_GenderLE")
                self.Student_BLKAndLot = QtWidgets.QLineEdit(self.tab)
                self.Student_BLKAndLot.setGeometry(QtCore.QRect(175, 190, 201, 21))
                self.Student_BLKAndLot.setObjectName("Student_BLKAndLot")
                self.Student_Street = QtWidgets.QLineEdit(self.tab)
                self.Student_Street.setGeometry(QtCore.QRect(175, 210, 201, 21))
                self.Student_Street.setObjectName("Student_Street")
                self.Student_SubdivisionLE = QtWidgets.QLineEdit(self.tab)
                self.Student_SubdivisionLE.setGeometry(QtCore.QRect(175, 230, 201, 21))
                self.Student_SubdivisionLE.setObjectName("Student_SubdivisionLE")
                self.Student_BarangayLE = QtWidgets.QLineEdit(self.tab)
                self.Student_BarangayLE.setGeometry(QtCore.QRect(175, 250, 201, 21))
                self.Student_BarangayLE.setObjectName("Student_BarangayLE")
                self.Student_CityLE = QtWidgets.QLineEdit(self.tab)
                self.Student_CityLE.setGeometry(QtCore.QRect(175, 270, 201, 21))
                self.Student_CityLE.setObjectName("Student_CityLE")
                self.Student_Contact_NoLE = QtWidgets.QLineEdit(self.tab)
                self.Student_Contact_NoLE.setGeometry(QtCore.QRect(175, 290, 201, 21))
                self.Student_Contact_NoLE.setObjectName("Student_Contact_NoLE")
                self.Student_ClassificationLE = QtWidgets.QLineEdit(self.tab)
                self.Student_ClassificationLE.setGeometry(QtCore.QRect(175, 310, 201, 21))
                self.Student_ClassificationLE.setObjectName("Student_ClassificationLE")
                self.Student_isGradesLE = QtWidgets.QLineEdit(self.tab)
                self.Student_isGradesLE.setGeometry(QtCore.QRect(175, 330, 201, 21))
                self.Student_isGradesLE.setObjectName("Student_isGradesLE")
                self.Student_isForm136LE = QtWidgets.QLineEdit(self.tab)
                self.Student_isForm136LE.setGeometry(QtCore.QRect(175, 350, 201, 21))
                self.Student_isForm136LE.setObjectName("Student_isForm136LE")
                self.Student_isForm137LE = QtWidgets.QLineEdit(self.tab)
                self.Student_isForm137LE.setGeometry(QtCore.QRect(175, 370, 201, 21))
                self.Student_isForm137LE.setObjectName("Student_isForm137LE")
                self.Student_isBirthCertificateLE = QtWidgets.QLineEdit(self.tab)
                self.Student_isBirthCertificateLE.setGeometry(QtCore.QRect(175, 390, 201, 21))
                self.Student_isBirthCertificateLE.setObjectName("Student_isBirthCertificateLE")
                self.Student_isResidencyLE = QtWidgets.QLineEdit(self.tab)
                self.Student_isResidencyLE.setGeometry(QtCore.QRect(175, 410, 201, 21))
                self.Student_isResidencyLE.setObjectName("Student_isResidencyLE")
                self.Student_ClassID_FKLE = QtWidgets.QLineEdit(self.tab)
                self.Student_ClassID_FKLE.setGeometry(QtCore.QRect(175, 430, 201, 21))
                self.Student_ClassID_FKLE.setObjectName("Student_ClassID_FKLE")
                self.Student_Grade_2LE = QtWidgets.QLineEdit(self.tab)
                self.Student_Grade_2LE.setGeometry(QtCore.QRect(175, 450, 201, 21))
                self.Student_Grade_2LE.setObjectName("Student_GradeLE")
                self.Student_Section_2LE = QtWidgets.QLineEdit(self.tab)
                self.Student_Section_2LE.setGeometry(QtCore.QRect(175, 470, 201, 21))
                self.Student_Section_2LE.setObjectName("Student_Section_2LE")

                self.NewStudents_Table = QtWidgets.QTableWidget(self.tab)
                self.NewStudents_Table.setGeometry(QtCore.QRect(430, 70, 680, 300))
                self.NewStudents_Table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
                self.NewStudents_Table.resizeColumnsToContents()
                self.NewStudents_Table.resizeRowsToContents()
                self.NewStudents_Table.setObjectName("NewStudent_Table")
                self.NewStudents_Table.setColumnCount(19)
                self.NewStudents_Table.setRowCount(0)

                item = QtWidgets.QTableWidgetItem()
                self.NewStudents_Table.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.NewStudents_Table.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.NewStudents_Table.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.NewStudents_Table.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.NewStudents_Table.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                self.NewStudents_Table.setHorizontalHeaderItem(5, item)
                item = QtWidgets.QTableWidgetItem()
                self.NewStudents_Table.setHorizontalHeaderItem(6, item)
                item = QtWidgets.QTableWidgetItem()
                self.NewStudents_Table.setHorizontalHeaderItem(7, item)
                item = QtWidgets.QTableWidgetItem()
                self.NewStudents_Table.setHorizontalHeaderItem(8, item)
                item = QtWidgets.QTableWidgetItem()
                self.NewStudents_Table.setHorizontalHeaderItem(9, item)
                item = QtWidgets.QTableWidgetItem()
                self.NewStudents_Table.setHorizontalHeaderItem(10, item)
                item = QtWidgets.QTableWidgetItem()
                self.NewStudents_Table.setHorizontalHeaderItem(11, item)
                item = QtWidgets.QTableWidgetItem()
                self.NewStudents_Table.setHorizontalHeaderItem(12, item)
                item = QtWidgets.QTableWidgetItem()
                self.NewStudents_Table.setHorizontalHeaderItem(13, item)
                item = QtWidgets.QTableWidgetItem()
                self.NewStudents_Table.setHorizontalHeaderItem(14, item)
                item = QtWidgets.QTableWidgetItem()
                self.NewStudents_Table.setHorizontalHeaderItem(15, item)
                item = QtWidgets.QTableWidgetItem()
                self.NewStudents_Table.setHorizontalHeaderItem(16, item)
                item = QtWidgets.QTableWidgetItem()
                self.NewStudents_Table.setHorizontalHeaderItem(17, item)
                item = QtWidgets.QTableWidgetItem()
                self.NewStudents_Table.setHorizontalHeaderItem(18, item)

                self.NewStudentEnrollmentPB = QtWidgets.QPushButton(self.tab)
                self.NewStudentEnrollmentPB.setGeometry(QtCore.QRect(130, 520, 75, 23))
                self.NewStudentEnrollmentPB.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.NewStudentEnrollmentPB.setObjectName("NewStudentEnrollmentPB")
                self.NewStudentEnrollmentPB.clicked.connect(self.Inserting_NewStudentForm)



                self.ViewFormOldStudentPB = QtWidgets.QPushButton(self.tab)
                self.ViewFormOldStudentPB.setGeometry(QtCore.QRect(630, 390, 75, 23))
                self.ViewFormOldStudentPB.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.ViewFormOldStudentPB.setObjectName("Show_Table_NewStudentPB")
                self.ViewFormOldStudentPB.clicked.connect(self.Show_Table_Students)

                self.label_30 = QtWidgets.QLabel(self.tab)
                self.label_30.setGeometry(QtCore.QRect(580, 450, 531, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_30.setFont(font)
                self.label_30.setObjectName("label_30")
                self.label_31 = QtWidgets.QLabel(self.tab)
                self.label_31.setGeometry(QtCore.QRect(700, 470, 531, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_31.setFont(font)
                self.label_31.setObjectName("label_31")
                self.label_32 = QtWidgets.QLabel(self.tab)
                self.label_32.setGeometry(QtCore.QRect(510, 430, 531, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_32.setFont(font)
                self.label_32.setObjectName("label_32")
                self.label_33 = QtWidgets.QLabel(self.tab)
                self.label_33.setGeometry(QtCore.QRect(480, 30, 121, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_33.setFont(font)
                self.label_33.setObjectName("label_33")

                # OLD Student Tab -----------------------------------------------------------------------------------------------------
                self.tabWidget.addTab(self.tab, "")
                self.tab_2 = QtWidgets.QWidget()
                self.tab_2.setObjectName("tab_2")
                self.label_11 = QtWidgets.QLabel(self.tab_2)
                self.label_11.setGeometry(QtCore.QRect(440, 20, 201, 41))
                font = QtGui.QFont()
                font.setPointSize(15)
                self.label_11.setFont(font)
                self.label_11.setObjectName("label_11")

                self.Student_ID_2LA = QtWidgets.QLabel(self.tab_2)
                self.Student_ID_2LA.setGeometry(QtCore.QRect(20, 160, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_ID_2LA.setFont(font)
                self.Student_ID_2LA.setObjectName("Student_ID_2LA")
                self.Student_NewGradeLA = QtWidgets.QLabel(self.tab_2)
                self.Student_NewGradeLA.setGeometry(QtCore.QRect(20, 190, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_NewGradeLA.setFont(font)
                self.Student_NewGradeLA.setObjectName("Student_NewGradeLA")
                self.Student_NewSectionLA = QtWidgets.QLabel(self.tab_2)
                self.Student_NewSectionLA.setGeometry(QtCore.QRect(20, 220, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_NewSectionLA.setFont(font)
                self.Student_NewSectionLA.setObjectName("Student_NewSectionLA")
                self.Student_OldSectionLA = QtWidgets.QLabel(self.tab_2)
                self.Student_OldSectionLA.setGeometry(QtCore.QRect(20, 250, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Student_OldSectionLA.setFont(font)
                self.Student_OldSectionLA.setObjectName("Student_OldSectionLA")
                

                self.newStudent_IDLE = QtWidgets.QLineEdit(self.tab_2)
                self.newStudent_IDLE.setGeometry(QtCore.QRect(140, 160, 201, 21))
                self.newStudent_IDLE.setObjectName("newStudent_IDLE")
                self.Student_NewGradeLE = QtWidgets.QLineEdit(self.tab_2)
                self.Student_NewGradeLE.setGeometry(QtCore.QRect(140, 190, 201, 21))
                self.Student_NewGradeLE.setObjectName("Student_NewGradeLE")
                self.Student_NewSectionLE = QtWidgets.QLineEdit(self.tab_2)
                self.Student_NewSectionLE.setGeometry(QtCore.QRect(140, 220, 201, 21))
                self.Student_NewSectionLE.setObjectName("Student_NewSectionLE")
                self.Student_OldSectionLE = QtWidgets.QLineEdit(self.tab_2)
                self.Student_OldSectionLE.setGeometry(QtCore.QRect(140, 250, 201, 21))
                self.Student_OldSectionLE.setObjectName("Student_OldSectionLE")
                self.label_23 = QtWidgets.QLabel(self.tab_2)
                self.label_23.setGeometry(QtCore.QRect(470, 40, 121, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_23.setFont(font)
                self.label_23.setObjectName("label_23")


                self.OldStudents_Table = QtWidgets.QTableWidget(self.tab_2)
                self.OldStudents_Table.setGeometry(QtCore.QRect(400, 150, 721, 171))
                self.OldStudents_Table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
                self.OldStudents_Table.resizeColumnsToContents()
                self.OldStudents_Table.resizeRowsToContents()
                self.OldStudents_Table.setObjectName("OldStudents_Table")
                self.OldStudents_Table.setColumnCount(19)
                self.OldStudents_Table.setRowCount(0)

                item = QtWidgets.QTableWidgetItem()
                self.OldStudents_Table.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.OldStudents_Table.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.OldStudents_Table.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.OldStudents_Table.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.OldStudents_Table.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                self.OldStudents_Table.setHorizontalHeaderItem(5, item)
                item = QtWidgets.QTableWidgetItem()
                self.OldStudents_Table.setHorizontalHeaderItem(6, item)
                item = QtWidgets.QTableWidgetItem()
                self.OldStudents_Table.setHorizontalHeaderItem(7, item)
                item = QtWidgets.QTableWidgetItem()
                self.OldStudents_Table.setHorizontalHeaderItem(8, item)
                item = QtWidgets.QTableWidgetItem()
                self.OldStudents_Table.setHorizontalHeaderItem(9, item)
                item = QtWidgets.QTableWidgetItem()
                self.OldStudents_Table.setHorizontalHeaderItem(10, item)
                item = QtWidgets.QTableWidgetItem()
                self.OldStudents_Table.setHorizontalHeaderItem(11, item)
                item = QtWidgets.QTableWidgetItem()
                self.OldStudents_Table.setHorizontalHeaderItem(12, item)
                item = QtWidgets.QTableWidgetItem()
                self.OldStudents_Table.setHorizontalHeaderItem(13, item)
                item = QtWidgets.QTableWidgetItem()
                self.OldStudents_Table.setHorizontalHeaderItem(14, item)
                item = QtWidgets.QTableWidgetItem()
                self.OldStudents_Table.setHorizontalHeaderItem(15, item)
                item = QtWidgets.QTableWidgetItem()
                self.OldStudents_Table.setHorizontalHeaderItem(16, item)
                item = QtWidgets.QTableWidgetItem()
                self.OldStudents_Table.setHorizontalHeaderItem(17, item)
                item = QtWidgets.QTableWidgetItem()
                self.OldStudents_Table.setHorizontalHeaderItem(18, item)
                



                self.OldStudentEnrollmentPB = QtWidgets.QPushButton(self.tab_2)
                self.OldStudentEnrollmentPB.setGeometry(QtCore.QRect(170, 530, 75, 23))
                self.OldStudentEnrollmentPB.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.OldStudentEnrollmentPB.setObjectName("OldStudentEnrollmentPB")
                self.OldStudentEnrollmentPB.clicked.connect(self.Inserting_OldStudentForm)

                self.Show_Table_OldStudentPB = QtWidgets.QPushButton(self.tab_2)
                self.Show_Table_OldStudentPB.setGeometry(QtCore.QRect(680, 330, 75, 23))
                self.Show_Table_OldStudentPB.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.Show_Table_OldStudentPB.setObjectName("Show_Table_OldStudentPB")
                self.Show_Table_OldStudentPB.clicked.connect(self.Show_Table_OldStudents)



                self.label_27 = QtWidgets.QLabel(self.tab_2)
                self.label_27.setGeometry(QtCore.QRect(490, 400, 531, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_27.setFont(font)
                self.label_27.setObjectName("label_27")
                self.label_28 = QtWidgets.QLabel(self.tab_2)
                self.label_28.setGeometry(QtCore.QRect(560, 420, 531, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_28.setFont(font)
                self.label_28.setObjectName("label_28")
                self.label_29 = QtWidgets.QLabel(self.tab_2)
                self.label_29.setGeometry(QtCore.QRect(670, 440, 531, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_29.setFont(font)
                self.label_29.setObjectName("label_29")
                self.tabWidget.addTab(self.tab_2, "")

                # Start Tab 3 --------------------------------------------------------
                self.tab_3 = QtWidgets.QWidget()
                self.tab_3.setObjectName("tab_3")
                self.StudentSchedule_Table = QtWidgets.QTableWidget(self.tab_3)
                self.StudentSchedule_Table.setGeometry(QtCore.QRect(10, 150, 491, 191))
                self.StudentSchedule_Table.setObjectName("StudentSchedule_Table")
                self.StudentSchedule_Table.setColumnCount(10)
                self.StudentSchedule_Table.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.StudentSchedule_Table.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.StudentSchedule_Table.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.StudentSchedule_Table.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.StudentSchedule_Table.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.StudentSchedule_Table.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                self.StudentSchedule_Table.setHorizontalHeaderItem(5, item)
                item = QtWidgets.QTableWidgetItem()
                self.StudentSchedule_Table.setHorizontalHeaderItem(6, item)
                item = QtWidgets.QTableWidgetItem()
                self.StudentSchedule_Table.setHorizontalHeaderItem(7, item)
                item = QtWidgets.QTableWidgetItem()
                self.StudentSchedule_Table.setHorizontalHeaderItem(8, item)
                item = QtWidgets.QTableWidgetItem()
                self.StudentSchedule_Table.setHorizontalHeaderItem(9, item)

                
                self.SectionSchedule_Table = QtWidgets.QTableWidget(self.tab_3)
                self.SectionSchedule_Table.setGeometry(QtCore.QRect(520, 150, 551, 191))
                self.SectionSchedule_Table.setObjectName("Section_ScheduleTable")
                self.SectionSchedule_Table.setColumnCount(9)
                self.SectionSchedule_Table.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.SectionSchedule_Table.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.SectionSchedule_Table.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.SectionSchedule_Table.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.SectionSchedule_Table.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.SectionSchedule_Table.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                self.SectionSchedule_Table.setHorizontalHeaderItem(5, item)
                item = QtWidgets.QTableWidgetItem()
                self.SectionSchedule_Table.setHorizontalHeaderItem(6, item)
                item = QtWidgets.QTableWidgetItem()
                self.SectionSchedule_Table.setHorizontalHeaderItem(7, item)
                item = QtWidgets.QTableWidgetItem()
                self.SectionSchedule_Table.setHorizontalHeaderItem(8, item)

                self.Student_IDSEARCHLA = QtWidgets.QLabel(self.tab_3)
                self.Student_IDSEARCHLA.setGeometry(QtCore.QRect(40, 120, 81, 16))
                self.Student_IDSEARCHLA.setObjectName("Student_IDSEARCHLA")
                self.Student_IDSEARCHLE = QtWidgets.QLineEdit(self.tab_3)
                self.Student_IDSEARCHLE.setGeometry(QtCore.QRect(120, 120, 201, 20))
                self.Student_IDSEARCHLE.setObjectName("Student_IDSEARCHLE")
                self.Student_IDSEARCHPB = QtWidgets.QPushButton(self.tab_3)
                self.Student_IDSEARCHPB.setGeometry(QtCore.QRect(340, 118, 75, 23))
                self.Student_IDSEARCHPB.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.Student_IDSEARCHPB.setObjectName("Student_IDSEARCHPB")
                self.Student_IDSEARCHPB.clicked.connect(self.Show_Student_Schedule)


                self.ScheduleSection_SEARCHLA = QtWidgets.QLabel(self.tab_3)
                self.ScheduleSection_SEARCHLA.setGeometry(QtCore.QRect(520, 120, 101, 16))
                self.ScheduleSection_SEARCHLA.setObjectName("Schedule_CodeSEARCHLA")
                self.ScheduleSection_SEARCHLE = QtWidgets.QLineEdit(self.tab_3)
                self.ScheduleSection_SEARCHLE.setGeometry(QtCore.QRect(610, 120, 201, 20))
                self.ScheduleSection_SEARCHLE.setObjectName("Schedule_CodeSEARCHLE")
                self.ScheduleSection_SEARCHPB = QtWidgets.QPushButton(self.tab_3)
                self.ScheduleSection_SEARCHPB.setGeometry(QtCore.QRect(820, 118, 75, 23))
                self.ScheduleSection_SEARCHPB.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.ScheduleSection_SEARCHPB.setObjectName("ScheduleSection_SEARCHPB")
                self.ScheduleSection_SEARCHPB.clicked.connect(self.Show_Section_Schedule)


                self.label_163 = QtWidgets.QLabel(self.tab_3)
                self.label_163.setGeometry(QtCore.QRect(470, 20, 221, 16))
                font = QtGui.QFont()
                font.setPointSize(15)
                self.label_163.setFont(font)
                self.label_163.setObjectName("label_163")
                self.label_164 = QtWidgets.QLabel(self.tab_3)
                self.label_164.setGeometry(QtCore.QRect(530, 40, 131, 16))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.label_164.setFont(font)
                self.label_164.setObjectName("label_164")
                self.tabWidget.addTab(self.tab_3, "")

                # Start Tab 4 --------------------------------------------------------

                
                self.tab_4 = QtWidgets.QWidget()
                self.tab_4.setObjectName("tab_4")
                self.frame = QtWidgets.QFrame(self.tab_4)
                self.frame.setGeometry(QtCore.QRect(0, 0, 131, 571))
                self.frame.setStyleSheet("background-color: rgb(209, 209, 209);")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.pushButton_6 = QtWidgets.QPushButton(self.frame)
                self.pushButton_6.setGeometry(QtCore.QRect(0, 0, 131, 81))
                self.pushButton_6.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_6.setObjectName("pushButton_6")
                self.pushButton_7 = QtWidgets.QPushButton(self.frame)
                self.pushButton_7.setGeometry(QtCore.QRect(0, 80, 131, 71))
                self.pushButton_7.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_7.setObjectName("pushButton_7")
                self.pushButton_8 = QtWidgets.QPushButton(self.frame)
                self.pushButton_8.setGeometry(QtCore.QRect(0, 150, 131, 71))
                self.pushButton_8.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_8.setObjectName("pushButton_8")
                self.pushButton_9 = QtWidgets.QPushButton(self.frame)
                self.pushButton_9.setGeometry(QtCore.QRect(0, 220, 131, 71))
                self.pushButton_9.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_9.setObjectName("pushButton_9")
                self.pushButton_10 = QtWidgets.QPushButton(self.frame)
                self.pushButton_10.setGeometry(QtCore.QRect(0, 290, 131, 71))
                self.pushButton_10.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_10.setObjectName("pushButton_10")
                self.pushButton_11 = QtWidgets.QPushButton(self.frame)
                self.pushButton_11.setGeometry(QtCore.QRect(0, 360, 131, 71))
                self.pushButton_11.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_11.setObjectName("pushButton_11")
                self.pushButton_12 = QtWidgets.QPushButton(self.frame)
                self.pushButton_12.setGeometry(QtCore.QRect(0, 430, 131, 71))
                self.pushButton_12.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_12.setObjectName("pushButton_12")
                self.pushButton_13 = QtWidgets.QPushButton(self.frame)
                self.pushButton_13.setGeometry(QtCore.QRect(0, 500, 131, 71))
                self.pushButton_13.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_13.setObjectName("pushButton_13")
                self.stackedWidget_2 = QtWidgets.QStackedWidget(self.tab_4)
                self.stackedWidget_2.setGeometry(QtCore.QRect(130, 0, 1001, 571))
                self.stackedWidget_2.setObjectName("stackedWidget_2")
                self.OLD_STUDENT = QtWidgets.QWidget()
                self.OLD_STUDENT.setObjectName("OLD_STUDENT")
                self.label_56 = QtWidgets.QLabel(self.OLD_STUDENT)
                self.label_56.setGeometry(QtCore.QRect(30, 260, 41, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_56.setFont(font)
                self.label_56.setObjectName("label_56")
                self.lineEdit_45 = QtWidgets.QLineEdit(self.OLD_STUDENT)
                self.lineEdit_45.setGeometry(QtCore.QRect(120, 140, 161, 21))
                self.lineEdit_45.setObjectName("lineEdit_45")
                self.lineEdit_46 = QtWidgets.QLineEdit(self.OLD_STUDENT)
                self.lineEdit_46.setGeometry(QtCore.QRect(120, 380, 161, 21))
                self.lineEdit_46.setObjectName("lineEdit_46")
                self.lineEdit_47 = QtWidgets.QLineEdit(self.OLD_STUDENT)
                self.lineEdit_47.setGeometry(QtCore.QRect(120, 300, 161, 21))
                self.lineEdit_47.setObjectName("lineEdit_47")
                self.label_57 = QtWidgets.QLabel(self.OLD_STUDENT)
                self.label_57.setGeometry(QtCore.QRect(10, 100, 81, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_57.setFont(font)
                self.label_57.setObjectName("label_57")
                self.label_58 = QtWidgets.QLabel(self.OLD_STUDENT)
                self.label_58.setGeometry(QtCore.QRect(10, 220, 81, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_58.setFont(font)
                self.label_58.setObjectName("label_58")
                self.label_59 = QtWidgets.QLabel(self.OLD_STUDENT)
                self.label_59.setGeometry(QtCore.QRect(0, 380, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_59.setFont(font)
                self.label_59.setObjectName("label_59")
                self.lineEdit_48 = QtWidgets.QLineEdit(self.OLD_STUDENT)
                self.lineEdit_48.setGeometry(QtCore.QRect(120, 220, 161, 21))
                self.lineEdit_48.setObjectName("lineEdit_48")
                self.pushButton_42 = QtWidgets.QPushButton(self.OLD_STUDENT)
                self.pushButton_42.setGeometry(QtCore.QRect(630, 410, 75, 23))
                self.pushButton_42.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_42.setObjectName("pushButton_42")
                self.label_60 = QtWidgets.QLabel(self.OLD_STUDENT)
                self.label_60.setGeometry(QtCore.QRect(10, 180, 81, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_60.setFont(font)
                self.label_60.setObjectName("label_60")
                self.lineEdit_49 = QtWidgets.QLineEdit(self.OLD_STUDENT)
                self.lineEdit_49.setGeometry(QtCore.QRect(120, 100, 161, 21))
                self.lineEdit_49.setObjectName("lineEdit_49")
                self.pushButton_43 = QtWidgets.QPushButton(self.OLD_STUDENT)
                self.pushButton_43.setGeometry(QtCore.QRect(110, 470, 75, 23))
                self.pushButton_43.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_43.setObjectName("pushButton_43")
                self.label_61 = QtWidgets.QLabel(self.OLD_STUDENT)
                self.label_61.setGeometry(QtCore.QRect(20, 300, 51, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_61.setFont(font)
                self.label_61.setObjectName("label_61")
                self.lineEdit_50 = QtWidgets.QLineEdit(self.OLD_STUDENT)
                self.lineEdit_50.setGeometry(QtCore.QRect(120, 420, 161, 21))
                self.lineEdit_50.setObjectName("lineEdit_50")
                self.tableWidget_10 = QtWidgets.QTableWidget(self.OLD_STUDENT)
                self.tableWidget_10.setGeometry(QtCore.QRect(390, 190, 571, 191))
                self.tableWidget_10.setObjectName("tableWidget_10")
                self.tableWidget_10.setColumnCount(8)
                self.tableWidget_10.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_10.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_10.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_10.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_10.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_10.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_10.setHorizontalHeaderItem(5, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_10.setHorizontalHeaderItem(6, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_10.setHorizontalHeaderItem(7, item)
                self.label_62 = QtWidgets.QLabel(self.OLD_STUDENT)
                self.label_62.setGeometry(QtCore.QRect(20, 140, 81, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_62.setFont(font)
                self.label_62.setObjectName("label_62")
                self.label_63 = QtWidgets.QLabel(self.OLD_STUDENT)
                self.label_63.setGeometry(QtCore.QRect(0, 420, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_63.setFont(font)
                self.label_63.setObjectName("label_63")
                self.label_64 = QtWidgets.QLabel(self.OLD_STUDENT)
                self.label_64.setGeometry(QtCore.QRect(20, 340, 61, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_64.setFont(font)
                self.label_64.setObjectName("label_64")
                self.lineEdit_51 = QtWidgets.QLineEdit(self.OLD_STUDENT)
                self.lineEdit_51.setGeometry(QtCore.QRect(120, 180, 161, 21))
                self.lineEdit_51.setObjectName("lineEdit_51")
                self.lineEdit_52 = QtWidgets.QLineEdit(self.OLD_STUDENT)
                self.lineEdit_52.setGeometry(QtCore.QRect(120, 340, 161, 21))
                self.lineEdit_52.setObjectName("lineEdit_52")
                self.lineEdit_53 = QtWidgets.QLineEdit(self.OLD_STUDENT)
                self.lineEdit_53.setGeometry(QtCore.QRect(120, 260, 161, 21))
                self.lineEdit_53.setObjectName("lineEdit_53")
                self.pushButton_44 = QtWidgets.QPushButton(self.OLD_STUDENT)
                self.pushButton_44.setGeometry(QtCore.QRect(290, 140, 61, 23))
                self.pushButton_44.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_44.setObjectName("pushButton_44")
                self.pushButton_45 = QtWidgets.QPushButton(self.OLD_STUDENT)
                self.pushButton_45.setGeometry(QtCore.QRect(290, 180, 61, 23))
                self.pushButton_45.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_45.setObjectName("pushButton_45")
                self.pushButton_46 = QtWidgets.QPushButton(self.OLD_STUDENT)
                self.pushButton_46.setGeometry(QtCore.QRect(290, 220, 61, 23))
                self.pushButton_46.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_46.setObjectName("pushButton_46")
                self.pushButton_47 = QtWidgets.QPushButton(self.OLD_STUDENT)
                self.pushButton_47.setGeometry(QtCore.QRect(290, 260, 61, 23))
                self.pushButton_47.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_47.setObjectName("pushButton_47")
                self.pushButton_48 = QtWidgets.QPushButton(self.OLD_STUDENT)
                self.pushButton_48.setGeometry(QtCore.QRect(290, 300, 61, 23))
                self.pushButton_48.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_48.setObjectName("pushButton_48")
                self.pushButton_49 = QtWidgets.QPushButton(self.OLD_STUDENT)
                self.pushButton_49.setGeometry(QtCore.QRect(290, 340, 61, 23))
                self.pushButton_49.setStyleSheet("")
                self.pushButton_49.setObjectName("pushButton_49")
                self.pushButton_50 = QtWidgets.QPushButton(self.OLD_STUDENT)
                self.pushButton_50.setGeometry(QtCore.QRect(290, 380, 61, 23))
                self.pushButton_50.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_50.setObjectName("pushButton_50")
                self.pushButton_51 = QtWidgets.QPushButton(self.OLD_STUDENT)
                self.pushButton_51.setGeometry(QtCore.QRect(290, 420, 61, 23))
                self.pushButton_51.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_51.setObjectName("pushButton_51")
                self.label_76 = QtWidgets.QLabel(self.OLD_STUDENT)
                self.label_76.setGeometry(QtCore.QRect(350, 40, 131, 16))
                font = QtGui.QFont()
                font.setPointSize(15)
                self.label_76.setFont(font)
                self.label_76.setObjectName("label_76")
                self.label_162 = QtWidgets.QLabel(self.OLD_STUDENT)
                self.label_162.setGeometry(QtCore.QRect(390, 160, 81, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_162.setFont(font)
                self.label_162.setObjectName("label_162")
                self.lineEdit_135 = QtWidgets.QLineEdit(self.OLD_STUDENT)
                self.lineEdit_135.setGeometry(QtCore.QRect(500, 160, 161, 21))
                self.lineEdit_135.setObjectName("lineEdit_135")
                self.pushButton_160 = QtWidgets.QPushButton(self.OLD_STUDENT)
                self.pushButton_160.setGeometry(QtCore.QRect(680, 160, 75, 23))
                self.pushButton_160.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_160.setObjectName("pushButton_160")
                self.stackedWidget_2.addWidget(self.OLD_STUDENT)
                self.NEW_STUDENT = QtWidgets.QWidget()
                self.NEW_STUDENT.setObjectName("NEW_STUDENT")
                self.lineEdit_63 = QtWidgets.QLineEdit(self.NEW_STUDENT)
                self.lineEdit_63.setGeometry(QtCore.QRect(130, 340, 201, 16))
                self.lineEdit_63.setObjectName("lineEdit_63")
                self.lineEdit_61 = QtWidgets.QLineEdit(self.NEW_STUDENT)
                self.lineEdit_61.setGeometry(QtCore.QRect(130, 190, 201, 16))
                self.lineEdit_61.setObjectName("lineEdit_61")
                self.lineEdit_56 = QtWidgets.QLineEdit(self.NEW_STUDENT)
                self.lineEdit_56.setGeometry(QtCore.QRect(130, 160, 201, 16))
                self.lineEdit_56.setObjectName("lineEdit_56")
                self.label_70 = QtWidgets.QLabel(self.NEW_STUDENT)
                self.label_70.setGeometry(QtCore.QRect(10, 160, 81, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_70.setFont(font)
                self.label_70.setObjectName("label_70")
                self.label_67 = QtWidgets.QLabel(self.NEW_STUDENT)
                self.label_67.setGeometry(QtCore.QRect(20, 340, 71, 21))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_67.setFont(font)
                self.label_67.setObjectName("label_67")
                self.pushButton_53 = QtWidgets.QPushButton(self.NEW_STUDENT)
                self.pushButton_53.setGeometry(QtCore.QRect(220, 410, 75, 23))
                self.pushButton_53.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_53.setObjectName("pushButton_53")
                self.pushButton_52 = QtWidgets.QPushButton(self.NEW_STUDENT)
                self.pushButton_52.setGeometry(QtCore.QRect(30, 410, 75, 23))
                self.pushButton_52.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_52.setObjectName("pushButton_52")
                self.lineEdit_57 = QtWidgets.QLineEdit(self.NEW_STUDENT)
                self.lineEdit_57.setGeometry(QtCore.QRect(130, 100, 201, 16))
                self.lineEdit_57.setObjectName("lineEdit_57")
                self.lineEdit_55 = QtWidgets.QLineEdit(self.NEW_STUDENT)
                self.lineEdit_55.setGeometry(QtCore.QRect(130, 280, 201, 16))
                self.lineEdit_55.setObjectName("lineEdit_55")
                self.label_72 = QtWidgets.QLabel(self.NEW_STUDENT)
                self.label_72.setGeometry(QtCore.QRect(10, 100, 81, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_72.setFont(font)
                self.label_72.setObjectName("label_72")
                self.label_66 = QtWidgets.QLabel(self.NEW_STUDENT)
                self.label_66.setGeometry(QtCore.QRect(10, 310, 111, 21))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_66.setFont(font)
                self.label_66.setObjectName("label_66")
                self.lineEdit_62 = QtWidgets.QLineEdit(self.NEW_STUDENT)
                self.lineEdit_62.setGeometry(QtCore.QRect(130, 130, 201, 16))
                self.lineEdit_62.setObjectName("lineEdit_62")
                self.lineEdit_54 = QtWidgets.QLineEdit(self.NEW_STUDENT)
                self.lineEdit_54.setGeometry(QtCore.QRect(130, 370, 201, 16))
                self.lineEdit_54.setObjectName("lineEdit_54")
                self.label_73 = QtWidgets.QLabel(self.NEW_STUDENT)
                self.label_73.setGeometry(QtCore.QRect(20, 370, 61, 21))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_73.setFont(font)
                self.label_73.setObjectName("label_73")
                self.label_71 = QtWidgets.QLabel(self.NEW_STUDENT)
                self.label_71.setGeometry(QtCore.QRect(10, 130, 81, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_71.setFont(font)
                self.label_71.setObjectName("label_71")
                self.lineEdit_58 = QtWidgets.QLineEdit(self.NEW_STUDENT)
                self.lineEdit_58.setGeometry(QtCore.QRect(130, 310, 201, 16))
                self.lineEdit_58.setObjectName("lineEdit_58")
                self.label_74 = QtWidgets.QLabel(self.NEW_STUDENT)
                self.label_74.setGeometry(QtCore.QRect(20, 250, 61, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_74.setFont(font)
                self.label_74.setObjectName("label_74")
                self.lineEdit_60 = QtWidgets.QLineEdit(self.NEW_STUDENT)
                self.lineEdit_60.setGeometry(QtCore.QRect(130, 220, 201, 16))
                self.lineEdit_60.setObjectName("lineEdit_60")
                self.label_65 = QtWidgets.QLabel(self.NEW_STUDENT)
                self.label_65.setGeometry(QtCore.QRect(30, 280, 51, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_65.setFont(font)
                self.label_65.setObjectName("label_65")
                self.tableWidget_11 = QtWidgets.QTableWidget(self.NEW_STUDENT)
                self.tableWidget_11.setGeometry(QtCore.QRect(450, 250, 461, 171))
                self.tableWidget_11.setObjectName("tableWidget_11")
                self.tableWidget_11.setColumnCount(11)
                self.tableWidget_11.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_11.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_11.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_11.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_11.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_11.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_11.setHorizontalHeaderItem(5, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_11.setHorizontalHeaderItem(6, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_11.setHorizontalHeaderItem(7, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_11.setHorizontalHeaderItem(8, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_11.setHorizontalHeaderItem(9, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_11.setHorizontalHeaderItem(10, item)
                self.label_69 = QtWidgets.QLabel(self.NEW_STUDENT)
                self.label_69.setGeometry(QtCore.QRect(30, 190, 81, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_69.setFont(font)
                self.label_69.setObjectName("label_69")
                self.label_68 = QtWidgets.QLabel(self.NEW_STUDENT)
                self.label_68.setGeometry(QtCore.QRect(20, 220, 81, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_68.setFont(font)
                self.label_68.setObjectName("label_68")
                self.lineEdit_59 = QtWidgets.QLineEdit(self.NEW_STUDENT)
                self.lineEdit_59.setGeometry(QtCore.QRect(130, 250, 201, 16))
                self.lineEdit_59.setObjectName("lineEdit_59")
                self.pushButton_54 = QtWidgets.QPushButton(self.NEW_STUDENT)
                self.pushButton_54.setGeometry(QtCore.QRect(130, 410, 75, 23))
                self.pushButton_54.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_54.setObjectName("pushButton_54")
                self.pushButton_55 = QtWidgets.QPushButton(self.NEW_STUDENT)
                self.pushButton_55.setGeometry(QtCore.QRect(340, 100, 75, 21))
                self.pushButton_55.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_55.setObjectName("pushButton_55")
                self.pushButton_56 = QtWidgets.QPushButton(self.NEW_STUDENT)
                self.pushButton_56.setGeometry(QtCore.QRect(340, 130, 75, 21))
                self.pushButton_56.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_56.setObjectName("pushButton_56")
                self.pushButton_57 = QtWidgets.QPushButton(self.NEW_STUDENT)
                self.pushButton_57.setGeometry(QtCore.QRect(340, 160, 75, 21))
                self.pushButton_57.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_57.setObjectName("pushButton_57")
                self.pushButton_58 = QtWidgets.QPushButton(self.NEW_STUDENT)
                self.pushButton_58.setGeometry(QtCore.QRect(340, 190, 75, 21))
                self.pushButton_58.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_58.setObjectName("pushButton_58")
                self.pushButton_59 = QtWidgets.QPushButton(self.NEW_STUDENT)
                self.pushButton_59.setGeometry(QtCore.QRect(340, 220, 75, 21))
                self.pushButton_59.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_59.setObjectName("pushButton_59")
                self.pushButton_60 = QtWidgets.QPushButton(self.NEW_STUDENT)
                self.pushButton_60.setGeometry(QtCore.QRect(340, 250, 75, 21))
                self.pushButton_60.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_60.setObjectName("pushButton_60")
                self.pushButton_61 = QtWidgets.QPushButton(self.NEW_STUDENT)
                self.pushButton_61.setGeometry(QtCore.QRect(340, 280, 75, 21))
                self.pushButton_61.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_61.setObjectName("pushButton_61")
                self.pushButton_62 = QtWidgets.QPushButton(self.NEW_STUDENT)
                self.pushButton_62.setGeometry(QtCore.QRect(340, 310, 75, 21))
                self.pushButton_62.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_62.setObjectName("pushButton_62")
                self.pushButton_63 = QtWidgets.QPushButton(self.NEW_STUDENT)
                self.pushButton_63.setGeometry(QtCore.QRect(340, 340, 75, 21))
                self.pushButton_63.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_63.setObjectName("pushButton_63")
                self.pushButton_64 = QtWidgets.QPushButton(self.NEW_STUDENT)
                self.pushButton_64.setGeometry(QtCore.QRect(340, 370, 75, 21))
                self.pushButton_64.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_64.setObjectName("pushButton_64")
                self.label_75 = QtWidgets.QLabel(self.NEW_STUDENT)
                self.label_75.setGeometry(QtCore.QRect(350, 20, 191, 31))
                font = QtGui.QFont()
                font.setPointSize(15)
                self.label_75.setFont(font)
                self.label_75.setObjectName("label_75")
                self.pushButton_83 = QtWidgets.QPushButton(self.NEW_STUDENT)
                self.pushButton_83.setGeometry(QtCore.QRect(660, 430, 75, 23))
                self.pushButton_83.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_83.setObjectName("pushButton_83")
                self.pushButton_84 = QtWidgets.QPushButton(self.NEW_STUDENT)
                self.pushButton_84.setGeometry(QtCore.QRect(800, 100, 75, 21))
                self.pushButton_84.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_84.setObjectName("pushButton_84")
                self.lineEdit_74 = QtWidgets.QLineEdit(self.NEW_STUDENT)
                self.lineEdit_74.setGeometry(QtCore.QRect(590, 100, 201, 16))
                self.lineEdit_74.setObjectName("lineEdit_74")
                self.label_93 = QtWidgets.QLabel(self.NEW_STUDENT)
                self.label_93.setGeometry(QtCore.QRect(470, 100, 81, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_93.setFont(font)
                self.label_93.setObjectName("label_93")
                self.label_94 = QtWidgets.QLabel(self.NEW_STUDENT)
                self.label_94.setGeometry(QtCore.QRect(470, 130, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_94.setFont(font)
                self.label_94.setObjectName("label_94")
                self.lineEdit_75 = QtWidgets.QLineEdit(self.NEW_STUDENT)
                self.lineEdit_75.setGeometry(QtCore.QRect(590, 130, 201, 16))
                self.lineEdit_75.setObjectName("lineEdit_75")
                self.pushButton_85 = QtWidgets.QPushButton(self.NEW_STUDENT)
                self.pushButton_85.setGeometry(QtCore.QRect(800, 130, 75, 21))
                self.pushButton_85.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_85.setObjectName("pushButton_85")
                self.lineEdit_76 = QtWidgets.QLineEdit(self.NEW_STUDENT)
                self.lineEdit_76.setGeometry(QtCore.QRect(130, 70, 201, 16))
                self.lineEdit_76.setObjectName("lineEdit_76")
                self.label_95 = QtWidgets.QLabel(self.NEW_STUDENT)
                self.label_95.setGeometry(QtCore.QRect(10, 70, 81, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_95.setFont(font)
                self.label_95.setObjectName("label_95")
                self.pushButton_86 = QtWidgets.QPushButton(self.NEW_STUDENT)
                self.pushButton_86.setGeometry(QtCore.QRect(800, 160, 75, 21))
                self.pushButton_86.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_86.setObjectName("pushButton_86")
                self.label_96 = QtWidgets.QLabel(self.NEW_STUDENT)
                self.label_96.setGeometry(QtCore.QRect(470, 160, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_96.setFont(font)
                self.label_96.setObjectName("label_96")
                self.lineEdit_77 = QtWidgets.QLineEdit(self.NEW_STUDENT)
                self.lineEdit_77.setGeometry(QtCore.QRect(590, 160, 201, 16))
                self.lineEdit_77.setObjectName("lineEdit_77")
                self.lineEdit_78 = QtWidgets.QLineEdit(self.NEW_STUDENT)
                self.lineEdit_78.setGeometry(QtCore.QRect(590, 190, 201, 16))
                self.lineEdit_78.setObjectName("lineEdit_78")
                self.label_97 = QtWidgets.QLabel(self.NEW_STUDENT)
                self.label_97.setGeometry(QtCore.QRect(470, 190, 81, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_97.setFont(font)
                self.label_97.setObjectName("label_97")
                self.pushButton_87 = QtWidgets.QPushButton(self.NEW_STUDENT)
                self.pushButton_87.setGeometry(QtCore.QRect(800, 190, 75, 21))
                self.pushButton_87.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_87.setObjectName("pushButton_87")
                self.stackedWidget_2.addWidget(self.NEW_STUDENT)
                self.ENROLLED_ = QtWidgets.QWidget()
                self.ENROLLED_.setObjectName("ENROLLED_")
                self.label_53 = QtWidgets.QLabel(self.ENROLLED_)
                self.label_53.setGeometry(QtCore.QRect(20, 70, 111, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_53.setFont(font)
                self.label_53.setObjectName("label_53")
                self.label_54 = QtWidgets.QLabel(self.ENROLLED_)
                self.label_54.setGeometry(QtCore.QRect(20, 100, 111, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_54.setFont(font)
                self.label_54.setObjectName("label_54")
                self.label_55 = QtWidgets.QLabel(self.ENROLLED_)
                self.label_55.setGeometry(QtCore.QRect(20, 130, 111, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_55.setFont(font)
                self.label_55.setObjectName("label_55")
                self.lineEdit_42 = QtWidgets.QLineEdit(self.ENROLLED_)
                self.lineEdit_42.setGeometry(QtCore.QRect(120, 70, 113, 16))
                self.lineEdit_42.setObjectName("lineEdit_42")
                self.lineEdit_43 = QtWidgets.QLineEdit(self.ENROLLED_)
                self.lineEdit_43.setGeometry(QtCore.QRect(120, 100, 113, 16))
                self.lineEdit_43.setObjectName("lineEdit_43")
                self.lineEdit_44 = QtWidgets.QLineEdit(self.ENROLLED_)
                self.lineEdit_44.setGeometry(QtCore.QRect(120, 130, 113, 16))
                self.lineEdit_44.setObjectName("lineEdit_44")
                self.pushButton_40 = QtWidgets.QPushButton(self.ENROLLED_)
                self.pushButton_40.setGeometry(QtCore.QRect(250, 130, 75, 23))
                self.pushButton_40.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_40.setObjectName("pushButton_40")
                self.pushButton_41 = QtWidgets.QPushButton(self.ENROLLED_)
                self.pushButton_41.setGeometry(QtCore.QRect(140, 160, 75, 23))
                self.pushButton_41.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_41.setObjectName("pushButton_41")
                self.label_77 = QtWidgets.QLabel(self.ENROLLED_)
                self.label_77.setGeometry(QtCore.QRect(400, 10, 191, 31))
                font = QtGui.QFont()
                font.setPointSize(15)
                self.label_77.setFont(font)
                self.label_77.setObjectName("label_77")
                self.tableWidget_29 = QtWidgets.QTableWidget(self.ENROLLED_)
                self.tableWidget_29.setGeometry(QtCore.QRect(480, 70, 211, 131))
                self.tableWidget_29.setObjectName("tableWidget_29")
                self.tableWidget_29.setColumnCount(2)
                self.tableWidget_29.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_29.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_29.setHorizontalHeaderItem(1, item)
                self.tableWidget_30 = QtWidgets.QTableWidget(self.ENROLLED_)
                self.tableWidget_30.setGeometry(QtCore.QRect(720, 70, 211, 131))
                self.tableWidget_30.setObjectName("tableWidget_30")
                self.tableWidget_30.setColumnCount(2)
                self.tableWidget_30.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_30.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_30.setHorizontalHeaderItem(1, item)
                self.pushButton_162 = QtWidgets.QPushButton(self.ENROLLED_)
                self.pushButton_162.setGeometry(QtCore.QRect(250, 100, 75, 23))
                self.pushButton_162.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_162.setObjectName("pushButton_162")
                self.tableWidget_31 = QtWidgets.QTableWidget(self.ENROLLED_)
                self.tableWidget_31.setGeometry(QtCore.QRect(30, 350, 421, 151))
                self.tableWidget_31.setObjectName("tableWidget_31")
                self.tableWidget_31.setColumnCount(5)
                self.tableWidget_31.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_31.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_31.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_31.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_31.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_31.setHorizontalHeaderItem(4, item)
                self.pushButton_163 = QtWidgets.QPushButton(self.ENROLLED_)
                self.pushButton_163.setGeometry(QtCore.QRect(340, 100, 75, 23))
                self.pushButton_163.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_163.setObjectName("pushButton_163")
                self.pushButton_164 = QtWidgets.QPushButton(self.ENROLLED_)
                self.pushButton_164.setGeometry(QtCore.QRect(340, 130, 75, 23))
                self.pushButton_164.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_164.setObjectName("pushButton_164")
                self.pushButton_165 = QtWidgets.QPushButton(self.ENROLLED_)
                self.pushButton_165.setGeometry(QtCore.QRect(540, 220, 75, 23))
                self.pushButton_165.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_165.setObjectName("pushButton_165")
                self.pushButton_166 = QtWidgets.QPushButton(self.ENROLLED_)
                self.pushButton_166.setGeometry(QtCore.QRect(790, 220, 75, 23))
                self.pushButton_166.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_166.setObjectName("pushButton_166")
                self.tableWidget_32 = QtWidgets.QTableWidget(self.ENROLLED_)
                self.tableWidget_32.setGeometry(QtCore.QRect(480, 350, 421, 151))
                self.tableWidget_32.setObjectName("tableWidget_32")
                self.tableWidget_32.setColumnCount(5)
                self.tableWidget_32.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_32.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_32.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_32.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_32.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_32.setHorizontalHeaderItem(4, item)
                self.lineEdit_136 = QtWidgets.QLineEdit(self.ENROLLED_)
                self.lineEdit_136.setGeometry(QtCore.QRect(130, 320, 113, 16))
                self.lineEdit_136.setObjectName("lineEdit_136")
                self.label_165 = QtWidgets.QLabel(self.ENROLLED_)
                self.label_165.setGeometry(QtCore.QRect(30, 320, 111, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_165.setFont(font)
                self.label_165.setObjectName("label_165")
                self.label_166 = QtWidgets.QLabel(self.ENROLLED_)
                self.label_166.setGeometry(QtCore.QRect(30, 290, 111, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_166.setFont(font)
                self.label_166.setObjectName("label_166")
                self.lineEdit_137 = QtWidgets.QLineEdit(self.ENROLLED_)
                self.lineEdit_137.setGeometry(QtCore.QRect(130, 290, 113, 16))
                self.lineEdit_137.setObjectName("lineEdit_137")
                self.lineEdit_138 = QtWidgets.QLineEdit(self.ENROLLED_)
                self.lineEdit_138.setGeometry(QtCore.QRect(580, 320, 113, 16))
                self.lineEdit_138.setText("")
                self.lineEdit_138.setObjectName("lineEdit_138")
                self.label_167 = QtWidgets.QLabel(self.ENROLLED_)
                self.label_167.setGeometry(QtCore.QRect(480, 320, 111, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_167.setFont(font)
                self.label_167.setObjectName("label_167")
                self.label_168 = QtWidgets.QLabel(self.ENROLLED_)
                self.label_168.setGeometry(QtCore.QRect(480, 290, 111, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_168.setFont(font)
                self.label_168.setObjectName("label_168")
                self.lineEdit_139 = QtWidgets.QLineEdit(self.ENROLLED_)
                self.lineEdit_139.setGeometry(QtCore.QRect(580, 290, 113, 16))
                self.lineEdit_139.setText("")
                self.lineEdit_139.setObjectName("lineEdit_139")
                self.pushButton_167 = QtWidgets.QPushButton(self.ENROLLED_)
                self.pushButton_167.setGeometry(QtCore.QRect(260, 290, 75, 21))
                self.pushButton_167.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_167.setObjectName("pushButton_167")
                self.pushButton_169 = QtWidgets.QPushButton(self.ENROLLED_)
                self.pushButton_169.setGeometry(QtCore.QRect(700, 290, 75, 21))
                self.pushButton_169.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_169.setObjectName("pushButton_169")
                self.pushButton_170 = QtWidgets.QPushButton(self.ENROLLED_)
                self.pushButton_170.setGeometry(QtCore.QRect(700, 320, 75, 21))
                self.pushButton_170.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_170.setObjectName("pushButton_170")
                self.stackedWidget_2.addWidget(self.ENROLLED_)
                self.GRADE_SEC = QtWidgets.QWidget()
                self.GRADE_SEC.setObjectName("GRADE_SEC")
                self.label_49 = QtWidgets.QLabel(self.GRADE_SEC)
                self.label_49.setGeometry(QtCore.QRect(20, 70, 151, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_49.setFont(font)
                self.label_49.setObjectName("label_49")
                self.label_50 = QtWidgets.QLabel(self.GRADE_SEC)
                self.label_50.setGeometry(QtCore.QRect(20, 90, 151, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_50.setFont(font)
                self.label_50.setObjectName("label_50")
                self.label_51 = QtWidgets.QLabel(self.GRADE_SEC)
                self.label_51.setGeometry(QtCore.QRect(20, 130, 151, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_51.setFont(font)
                self.label_51.setObjectName("label_51")
                self.label_52 = QtWidgets.QLabel(self.GRADE_SEC)
                self.label_52.setGeometry(QtCore.QRect(20, 150, 151, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_52.setFont(font)
                self.label_52.setObjectName("label_52")
                self.lineEdit_38 = QtWidgets.QLineEdit(self.GRADE_SEC)
                self.lineEdit_38.setGeometry(QtCore.QRect(180, 70, 131, 16))
                self.lineEdit_38.setObjectName("lineEdit_38")
                self.lineEdit_39 = QtWidgets.QLineEdit(self.GRADE_SEC)
                self.lineEdit_39.setGeometry(QtCore.QRect(180, 90, 131, 16))
                self.lineEdit_39.setObjectName("lineEdit_39")
                self.lineEdit_40 = QtWidgets.QLineEdit(self.GRADE_SEC)
                self.lineEdit_40.setGeometry(QtCore.QRect(180, 130, 131, 16))
                self.lineEdit_40.setObjectName("lineEdit_40")
                self.lineEdit_41 = QtWidgets.QLineEdit(self.GRADE_SEC)
                self.lineEdit_41.setGeometry(QtCore.QRect(180, 150, 131, 16))
                self.lineEdit_41.setObjectName("lineEdit_41")
                self.pushButton_35 = QtWidgets.QPushButton(self.GRADE_SEC)
                self.pushButton_35.setGeometry(QtCore.QRect(30, 180, 75, 23))
                self.pushButton_35.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_35.setObjectName("pushButton_35")
                self.pushButton_36 = QtWidgets.QPushButton(self.GRADE_SEC)
                self.pushButton_36.setGeometry(QtCore.QRect(120, 180, 75, 23))
                self.pushButton_36.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_36.setObjectName("pushButton_36")
                self.pushButton_37 = QtWidgets.QPushButton(self.GRADE_SEC)
                self.pushButton_37.setGeometry(QtCore.QRect(320, 90, 75, 16))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.pushButton_37.setFont(font)
                self.pushButton_37.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_37.setObjectName("pushButton_37")
                self.pushButton_38 = QtWidgets.QPushButton(self.GRADE_SEC)
                self.pushButton_38.setGeometry(QtCore.QRect(320, 130, 75, 16))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.pushButton_38.setFont(font)
                self.pushButton_38.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_38.setObjectName("pushButton_38")
                self.pushButton_39 = QtWidgets.QPushButton(self.GRADE_SEC)
                self.pushButton_39.setGeometry(QtCore.QRect(320, 150, 75, 16))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.pushButton_39.setFont(font)
                self.pushButton_39.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_39.setObjectName("pushButton_39")
                self.tableWidget_9 = QtWidgets.QTableWidget(self.GRADE_SEC)
                self.tableWidget_9.setGeometry(QtCore.QRect(420, 90, 381, 101))
                self.tableWidget_9.setObjectName("tableWidget_9")
                self.tableWidget_9.setColumnCount(5)
                self.tableWidget_9.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_9.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_9.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_9.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_9.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_9.setHorizontalHeaderItem(4, item)
                self.label_78 = QtWidgets.QLabel(self.GRADE_SEC)
                self.label_78.setGeometry(QtCore.QRect(320, 10, 221, 31))
                font = QtGui.QFont()
                font.setPointSize(15)
                self.label_78.setFont(font)
                self.label_78.setObjectName("label_78")
                self.pushButton_75 = QtWidgets.QPushButton(self.GRADE_SEC)
                self.pushButton_75.setGeometry(QtCore.QRect(210, 180, 75, 23))
                self.pushButton_75.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_75.setObjectName("pushButton_75")
                self.lineEdit_68 = QtWidgets.QLineEdit(self.GRADE_SEC)
                self.lineEdit_68.setGeometry(QtCore.QRect(550, 60, 131, 16))
                self.lineEdit_68.setObjectName("lineEdit_68")
                self.label_87 = QtWidgets.QLabel(self.GRADE_SEC)
                self.label_87.setGeometry(QtCore.QRect(410, 60, 151, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_87.setFont(font)
                self.label_87.setObjectName("label_87")
                self.pushButton_76 = QtWidgets.QPushButton(self.GRADE_SEC)
                self.pushButton_76.setGeometry(QtCore.QRect(700, 60, 75, 16))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.pushButton_76.setFont(font)
                self.pushButton_76.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_76.setObjectName("pushButton_76")
                self.lineEdit_71 = QtWidgets.QLineEdit(self.GRADE_SEC)
                self.lineEdit_71.setGeometry(QtCore.QRect(120, 290, 201, 20))
                self.lineEdit_71.setObjectName("lineEdit_71")
                self.label_89 = QtWidgets.QLabel(self.GRADE_SEC)
                self.label_89.setGeometry(QtCore.QRect(20, 250, 81, 16))
                self.label_89.setObjectName("label_89")
                self.pushButton_78 = QtWidgets.QPushButton(self.GRADE_SEC)
                self.pushButton_78.setGeometry(QtCore.QRect(770, 260, 75, 23))
                self.pushButton_78.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_78.setObjectName("pushButton_78")
                self.label_88 = QtWidgets.QLabel(self.GRADE_SEC)
                self.label_88.setGeometry(QtCore.QRect(460, 290, 101, 16))
                self.label_88.setObjectName("label_88")
                self.label_90 = QtWidgets.QLabel(self.GRADE_SEC)
                self.label_90.setGeometry(QtCore.QRect(20, 290, 101, 16))
                self.label_90.setObjectName("label_90")
                self.tableWidget_15 = QtWidgets.QTableWidget(self.GRADE_SEC)
                self.tableWidget_15.setGeometry(QtCore.QRect(10, 320, 411, 191))
                self.tableWidget_15.setObjectName("tableWidget_15")
                self.tableWidget_15.setColumnCount(8)
                self.tableWidget_15.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_15.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_15.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_15.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_15.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_15.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_15.setHorizontalHeaderItem(5, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_15.setHorizontalHeaderItem(6, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_15.setHorizontalHeaderItem(7, item)
                self.lineEdit_70 = QtWidgets.QLineEdit(self.GRADE_SEC)
                self.lineEdit_70.setGeometry(QtCore.QRect(120, 250, 201, 20))
                self.lineEdit_70.setObjectName("lineEdit_70")
                self.tableWidget_16 = QtWidgets.QTableWidget(self.GRADE_SEC)
                self.tableWidget_16.setGeometry(QtCore.QRect(430, 320, 491, 191))
                self.tableWidget_16.setObjectName("tableWidget_16")
                self.tableWidget_16.setColumnCount(8)
                self.tableWidget_16.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_16.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_16.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_16.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_16.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_16.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_16.setHorizontalHeaderItem(5, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_16.setHorizontalHeaderItem(6, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_16.setHorizontalHeaderItem(7, item)
                self.lineEdit_69 = QtWidgets.QLineEdit(self.GRADE_SEC)
                self.lineEdit_69.setGeometry(QtCore.QRect(560, 290, 201, 20))
                self.lineEdit_69.setObjectName("lineEdit_69")
                self.pushButton_77 = QtWidgets.QPushButton(self.GRADE_SEC)
                self.pushButton_77.setGeometry(QtCore.QRect(340, 250, 75, 23))
                self.pushButton_77.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_77.setObjectName("pushButton_77")
                self.pushButton_79 = QtWidgets.QPushButton(self.GRADE_SEC)
                self.pushButton_79.setGeometry(QtCore.QRect(340, 290, 75, 23))
                self.pushButton_79.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_79.setObjectName("pushButton_79")
                self.pushButton_80 = QtWidgets.QPushButton(self.GRADE_SEC)
                self.pushButton_80.setGeometry(QtCore.QRect(770, 290, 75, 23))
                self.pushButton_80.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_80.setObjectName("pushButton_80")
                self.label_91 = QtWidgets.QLabel(self.GRADE_SEC)
                self.label_91.setGeometry(QtCore.QRect(460, 260, 101, 16))
                self.label_91.setObjectName("label_91")
                self.lineEdit_72 = QtWidgets.QLineEdit(self.GRADE_SEC)
                self.lineEdit_72.setGeometry(QtCore.QRect(560, 260, 201, 20))
                self.lineEdit_72.setObjectName("lineEdit_72")
                self.lineEdit_73 = QtWidgets.QLineEdit(self.GRADE_SEC)
                self.lineEdit_73.setGeometry(QtCore.QRect(180, 110, 131, 16))
                self.lineEdit_73.setObjectName("lineEdit_73")
                self.label_92 = QtWidgets.QLabel(self.GRADE_SEC)
                self.label_92.setGeometry(QtCore.QRect(20, 110, 151, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_92.setFont(font)
                self.label_92.setObjectName("label_92")
                self.pushButton_81 = QtWidgets.QPushButton(self.GRADE_SEC)
                self.pushButton_81.setGeometry(QtCore.QRect(320, 110, 75, 16))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.pushButton_81.setFont(font)
                self.pushButton_81.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_81.setObjectName("pushButton_81")
                self.pushButton_82 = QtWidgets.QPushButton(self.GRADE_SEC)
                self.pushButton_82.setGeometry(QtCore.QRect(570, 200, 75, 23))
                self.pushButton_82.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_82.setObjectName("pushButton_82")
                self.stackedWidget_2.addWidget(self.GRADE_SEC)
                self.SCHEDULE_ = QtWidgets.QWidget()
                self.SCHEDULE_.setObjectName("SCHEDULE_")
                self.label_46 = QtWidgets.QLabel(self.SCHEDULE_)
                self.label_46.setGeometry(QtCore.QRect(30, 70, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_46.setFont(font)
                self.label_46.setObjectName("label_46")
                self.label_47 = QtWidgets.QLabel(self.SCHEDULE_)
                self.label_47.setGeometry(QtCore.QRect(30, 100, 111, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_47.setFont(font)
                self.label_47.setObjectName("label_47")
                self.label_48 = QtWidgets.QLabel(self.SCHEDULE_)
                self.label_48.setGeometry(QtCore.QRect(30, 130, 111, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_48.setFont(font)
                self.label_48.setObjectName("label_48")
                self.lineEdit_35 = QtWidgets.QLineEdit(self.SCHEDULE_)
                self.lineEdit_35.setGeometry(QtCore.QRect(160, 70, 151, 16))
                self.lineEdit_35.setObjectName("lineEdit_35")
                self.lineEdit_36 = QtWidgets.QLineEdit(self.SCHEDULE_)
                self.lineEdit_36.setGeometry(QtCore.QRect(160, 100, 151, 16))
                self.lineEdit_36.setObjectName("lineEdit_36")
                self.lineEdit_37 = QtWidgets.QLineEdit(self.SCHEDULE_)
                self.lineEdit_37.setGeometry(QtCore.QRect(160, 130, 151, 16))
                self.lineEdit_37.setObjectName("lineEdit_37")
                self.pushButton_31 = QtWidgets.QPushButton(self.SCHEDULE_)
                self.pushButton_31.setGeometry(QtCore.QRect(50, 170, 75, 23))
                self.pushButton_31.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_31.setObjectName("pushButton_31")
                self.pushButton_32 = QtWidgets.QPushButton(self.SCHEDULE_)
                self.pushButton_32.setGeometry(QtCore.QRect(150, 170, 75, 23))
                self.pushButton_32.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_32.setObjectName("pushButton_32")
                self.pushButton_33 = QtWidgets.QPushButton(self.SCHEDULE_)
                self.pushButton_33.setGeometry(QtCore.QRect(330, 100, 75, 21))
                self.pushButton_33.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_33.setObjectName("pushButton_33")
                self.pushButton_34 = QtWidgets.QPushButton(self.SCHEDULE_)
                self.pushButton_34.setGeometry(QtCore.QRect(330, 130, 75, 21))
                self.pushButton_34.setObjectName("pushButton_34")
                self.tableWidget_8 = QtWidgets.QTableWidget(self.SCHEDULE_)
                self.tableWidget_8.setGeometry(QtCore.QRect(440, 70, 311, 141))
                self.tableWidget_8.setObjectName("tableWidget_8")
                self.tableWidget_8.setColumnCount(3)
                self.tableWidget_8.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_8.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_8.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_8.setHorizontalHeaderItem(2, item)
                self.label_79 = QtWidgets.QLabel(self.SCHEDULE_)
                self.label_79.setGeometry(QtCore.QRect(360, 20, 191, 31))
                font = QtGui.QFont()
                font.setPointSize(15)
                self.label_79.setFont(font)
                self.label_79.setObjectName("label_79")
                self.pushButton_71 = QtWidgets.QPushButton(self.SCHEDULE_)
                self.pushButton_71.setGeometry(QtCore.QRect(240, 170, 75, 23))
                self.pushButton_71.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_71.setObjectName("pushButton_71")
                self.tableWidget_12 = QtWidgets.QTableWidget(self.SCHEDULE_)
                self.tableWidget_12.setGeometry(QtCore.QRect(220, 350, 441, 141))
                self.tableWidget_12.setObjectName("tableWidget_12")
                self.tableWidget_12.setColumnCount(4)
                self.tableWidget_12.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_12.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_12.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_12.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_12.setHorizontalHeaderItem(3, item)
                self.lineEdit_66 = QtWidgets.QLineEdit(self.SCHEDULE_)
                self.lineEdit_66.setGeometry(QtCore.QRect(330, 280, 151, 16))
                self.lineEdit_66.setObjectName("lineEdit_66")
                self.label_85 = QtWidgets.QLabel(self.SCHEDULE_)
                self.label_85.setGeometry(QtCore.QRect(200, 280, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_85.setFont(font)
                self.label_85.setObjectName("label_85")
                self.lineEdit_67 = QtWidgets.QLineEdit(self.SCHEDULE_)
                self.lineEdit_67.setGeometry(QtCore.QRect(330, 310, 151, 16))
                self.lineEdit_67.setObjectName("lineEdit_67")
                self.label_86 = QtWidgets.QLabel(self.SCHEDULE_)
                self.label_86.setGeometry(QtCore.QRect(200, 310, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_86.setFont(font)
                self.label_86.setObjectName("label_86")
                self.pushButton_72 = QtWidgets.QPushButton(self.SCHEDULE_)
                self.pushButton_72.setGeometry(QtCore.QRect(500, 280, 75, 21))
                self.pushButton_72.setObjectName("pushButton_72")
                self.pushButton_73 = QtWidgets.QPushButton(self.SCHEDULE_)
                self.pushButton_73.setGeometry(QtCore.QRect(500, 310, 75, 21))
                self.pushButton_73.setObjectName("pushButton_73")
                self.pushButton_74 = QtWidgets.QPushButton(self.SCHEDULE_)
                self.pushButton_74.setGeometry(QtCore.QRect(390, 500, 75, 21))
                self.pushButton_74.setObjectName("pushButton_74")
                self.stackedWidget_2.addWidget(self.SCHEDULE_)
                self.SUBJECT_ = QtWidgets.QWidget()
                self.SUBJECT_.setObjectName("SUBJECT_")
                self.label_41 = QtWidgets.QLabel(self.SUBJECT_)
                self.label_41.setGeometry(QtCore.QRect(20, 70, 81, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_41.setFont(font)
                self.label_41.setObjectName("label_41")
                self.label_42 = QtWidgets.QLabel(self.SUBJECT_)
                self.label_42.setGeometry(QtCore.QRect(20, 100, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_42.setFont(font)
                self.label_42.setObjectName("label_42")
                self.label_43 = QtWidgets.QLabel(self.SUBJECT_)
                self.label_43.setGeometry(QtCore.QRect(20, 130, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_43.setFont(font)
                self.label_43.setObjectName("label_43")
                self.label_44 = QtWidgets.QLabel(self.SUBJECT_)
                self.label_44.setGeometry(QtCore.QRect(20, 160, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_44.setFont(font)
                self.label_44.setObjectName("label_44")
                self.label_45 = QtWidgets.QLabel(self.SUBJECT_)
                self.label_45.setGeometry(QtCore.QRect(20, 190, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_45.setFont(font)
                self.label_45.setObjectName("label_45")
                self.lineEdit_30 = QtWidgets.QLineEdit(self.SUBJECT_)
                self.lineEdit_30.setGeometry(QtCore.QRect(130, 70, 121, 16))
                self.lineEdit_30.setObjectName("lineEdit_30")
                self.lineEdit_31 = QtWidgets.QLineEdit(self.SUBJECT_)
                self.lineEdit_31.setGeometry(QtCore.QRect(130, 100, 121, 16))
                self.lineEdit_31.setObjectName("lineEdit_31")
                self.lineEdit_32 = QtWidgets.QLineEdit(self.SUBJECT_)
                self.lineEdit_32.setGeometry(QtCore.QRect(130, 130, 121, 16))
                self.lineEdit_32.setObjectName("lineEdit_32")
                self.lineEdit_33 = QtWidgets.QLineEdit(self.SUBJECT_)
                self.lineEdit_33.setGeometry(QtCore.QRect(130, 160, 121, 16))
                self.lineEdit_33.setObjectName("lineEdit_33")
                self.lineEdit_34 = QtWidgets.QLineEdit(self.SUBJECT_)
                self.lineEdit_34.setGeometry(QtCore.QRect(130, 190, 121, 16))
                self.lineEdit_34.setObjectName("lineEdit_34")
                self.pushButton_25 = QtWidgets.QPushButton(self.SUBJECT_)
                self.pushButton_25.setGeometry(QtCore.QRect(40, 220, 75, 23))
                self.pushButton_25.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_25.setObjectName("pushButton_25")
                self.pushButton_26 = QtWidgets.QPushButton(self.SUBJECT_)
                self.pushButton_26.setGeometry(QtCore.QRect(130, 220, 75, 23))
                self.pushButton_26.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_26.setObjectName("pushButton_26")
                self.pushButton_27 = QtWidgets.QPushButton(self.SUBJECT_)
                self.pushButton_27.setGeometry(QtCore.QRect(270, 100, 75, 20))
                self.pushButton_27.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_27.setObjectName("pushButton_27")
                self.pushButton_28 = QtWidgets.QPushButton(self.SUBJECT_)
                self.pushButton_28.setGeometry(QtCore.QRect(270, 130, 75, 20))
                self.pushButton_28.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_28.setObjectName("pushButton_28")
                self.pushButton_29 = QtWidgets.QPushButton(self.SUBJECT_)
                self.pushButton_29.setGeometry(QtCore.QRect(270, 160, 75, 20))
                self.pushButton_29.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_29.setObjectName("pushButton_29")
                self.pushButton_30 = QtWidgets.QPushButton(self.SUBJECT_)
                self.pushButton_30.setGeometry(QtCore.QRect(270, 190, 75, 20))
                self.pushButton_30.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_30.setObjectName("pushButton_30")
                self.tableWidget_7 = QtWidgets.QTableWidget(self.SUBJECT_)
                self.tableWidget_7.setGeometry(QtCore.QRect(380, 130, 451, 121))
                self.tableWidget_7.setObjectName("tableWidget_7")
                self.tableWidget_7.setColumnCount(6)
                self.tableWidget_7.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_7.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_7.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_7.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_7.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_7.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_7.setHorizontalHeaderItem(5, item)
                self.label_80 = QtWidgets.QLabel(self.SUBJECT_)
                self.label_80.setGeometry(QtCore.QRect(420, 20, 191, 31))
                font = QtGui.QFont()
                font.setPointSize(15)
                self.label_80.setFont(font)
                self.label_80.setObjectName("label_80")
                self.pushButton_68 = QtWidgets.QPushButton(self.SUBJECT_)
                self.pushButton_68.setGeometry(QtCore.QRect(230, 220, 75, 23))
                self.pushButton_68.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_68.setObjectName("pushButton_68")
                self.tableWidget_14 = QtWidgets.QTableWidget(self.SUBJECT_)
                self.tableWidget_14.setGeometry(QtCore.QRect(120, 310, 631, 161))
                self.tableWidget_14.setObjectName("tableWidget_14")
                self.tableWidget_14.setColumnCount(6)
                self.tableWidget_14.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_14.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_14.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_14.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_14.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_14.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_14.setHorizontalHeaderItem(5, item)
                self.lineEdit_65 = QtWidgets.QLineEdit(self.SUBJECT_)
                self.lineEdit_65.setGeometry(QtCore.QRect(490, 100, 121, 16))
                self.lineEdit_65.setObjectName("lineEdit_65")
                self.label_84 = QtWidgets.QLabel(self.SUBJECT_)
                self.label_84.setGeometry(QtCore.QRect(390, 100, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_84.setFont(font)
                self.label_84.setObjectName("label_84")
                self.pushButton_69 = QtWidgets.QPushButton(self.SUBJECT_)
                self.pushButton_69.setGeometry(QtCore.QRect(620, 100, 75, 20))
                self.pushButton_69.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_69.setObjectName("pushButton_69")
                self.pushButton_161 = QtWidgets.QPushButton(self.SUBJECT_)
                self.pushButton_161.setGeometry(QtCore.QRect(400, 480, 75, 23))
                self.pushButton_161.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_161.setObjectName("pushButton_161")
                self.pushButton_171 = QtWidgets.QPushButton(self.SUBJECT_)
                self.pushButton_171.setGeometry(QtCore.QRect(620, 70, 75, 20))
                self.pushButton_171.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_171.setObjectName("pushButton_171")
                self.label_169 = QtWidgets.QLabel(self.SUBJECT_)
                self.label_169.setGeometry(QtCore.QRect(390, 70, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_169.setFont(font)
                self.label_169.setObjectName("label_169")
                self.lineEdit_140 = QtWidgets.QLineEdit(self.SUBJECT_)
                self.lineEdit_140.setGeometry(QtCore.QRect(490, 70, 121, 16))
                self.lineEdit_140.setObjectName("lineEdit_140")
                self.stackedWidget_2.addWidget(self.SUBJECT_)



        # Admin>Teacher-----------------------------------------
                self.TEACHER_ = QtWidgets.QWidget()
                self.TEACHER_.setObjectName("TEACHER_")
                self.label_36 = QtWidgets.QLabel(self.TEACHER_)
                self.label_36.setGeometry(QtCore.QRect(20, 100, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_36.setFont(font)
                self.label_36.setObjectName("label_36")
                self.label_37 = QtWidgets.QLabel(self.TEACHER_)
                self.label_37.setGeometry(QtCore.QRect(20, 130, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_37.setFont(font)
                self.label_37.setObjectName("label_37")
                self.label_38 = QtWidgets.QLabel(self.TEACHER_)
                self.label_38.setGeometry(QtCore.QRect(20, 160, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_38.setFont(font)
                self.label_38.setObjectName("label_38")
                self.label_39 = QtWidgets.QLabel(self.TEACHER_)
                self.label_39.setGeometry(QtCore.QRect(20, 190, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_39.setFont(font)
                self.label_39.setObjectName("label_39")
                self.label_40 = QtWidgets.QLabel(self.TEACHER_)
                self.label_40.setGeometry(QtCore.QRect(20, 220, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_40.setFont(font)
                self.label_40.setObjectName("label_40")
                self.lineEdit_25 = QtWidgets.QLineEdit(self.TEACHER_)
                self.lineEdit_25.setGeometry(QtCore.QRect(130, 100, 113, 20))
                self.lineEdit_25.setObjectName("lineEdit_25")
                self.lineEdit_26 = QtWidgets.QLineEdit(self.TEACHER_)
                self.lineEdit_26.setGeometry(QtCore.QRect(130, 130, 113, 20))
                self.lineEdit_26.setObjectName("lineEdit_26")
                self.lineEdit_27 = QtWidgets.QLineEdit(self.TEACHER_)
                self.lineEdit_27.setGeometry(QtCore.QRect(130, 160, 113, 20))
                self.lineEdit_27.setObjectName("lineEdit_27")
                self.lineEdit_28 = QtWidgets.QLineEdit(self.TEACHER_)
                self.lineEdit_28.setGeometry(QtCore.QRect(130, 190, 113, 20))
                self.lineEdit_28.setObjectName("lineEdit_28")
                self.lineEdit_29 = QtWidgets.QLineEdit(self.TEACHER_)
                self.lineEdit_29.setGeometry(QtCore.QRect(130, 220, 113, 20))
                self.lineEdit_29.setObjectName("lineEdit_29")
                self.pushButton_19 = QtWidgets.QPushButton(self.TEACHER_)
                self.pushButton_19.setGeometry(QtCore.QRect(10, 250, 75, 23))
                self.pushButton_19.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_19.setObjectName("pushButton_19")
                self.pushButton_20 = QtWidgets.QPushButton(self.TEACHER_)
                self.pushButton_20.setGeometry(QtCore.QRect(100, 250, 75, 23))
                self.pushButton_20.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_20.setObjectName("pushButton_20")
                self.pushButton_21 = QtWidgets.QPushButton(self.TEACHER_)
                self.pushButton_21.setGeometry(QtCore.QRect(260, 130, 75, 23))
                self.pushButton_21.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_21.setObjectName("pushButton_21")
                self.pushButton_22 = QtWidgets.QPushButton(self.TEACHER_)
                self.pushButton_22.setGeometry(QtCore.QRect(260, 160, 75, 23))
                self.pushButton_22.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_22.setObjectName("pushButton_22")
                self.pushButton_23 = QtWidgets.QPushButton(self.TEACHER_)
                self.pushButton_23.setGeometry(QtCore.QRect(260, 190, 75, 23))
                self.pushButton_23.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_23.setObjectName("pushButton_23")
                self.pushButton_24 = QtWidgets.QPushButton(self.TEACHER_)
                self.pushButton_24.setGeometry(QtCore.QRect(260, 220, 75, 23))
                self.pushButton_24.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_24.setObjectName("pushButton_24")

                self.Show_Specific_Teacher_RecordTBL = QtWidgets.QTableWidget(self.TEACHER_)
                self.Show_Specific_Teacher_RecordTBL.setGeometry(QtCore.QRect(390, 140, 491, 141))
                self.Show_Specific_Teacher_RecordTBL.setObjectName("Show_Specific_Teacher_RecordTBL")
                self.Show_Specific_Teacher_RecordTBL.setColumnCount(5)
                self.Show_Specific_Teacher_RecordTBL.setRowCount(1)
                item = QtWidgets.QTableWidgetItem()
                self.Show_Specific_Teacher_RecordTBL.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.Show_Specific_Teacher_RecordTBL.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.Show_Specific_Teacher_RecordTBL.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.Show_Specific_Teacher_RecordTBL.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.Show_Specific_Teacher_RecordTBL.setHorizontalHeaderItem(4, item)


                self.label_81 = QtWidgets.QLabel(self.TEACHER_)
                self.label_81.setGeometry(QtCore.QRect(410, 30, 191, 31))
                font = QtGui.QFont()
                font.setPointSize(15)
                self.label_81.setFont(font)
                self.label_81.setObjectName("label_81")
                self.pushButton_65 = QtWidgets.QPushButton(self.TEACHER_)
                self.pushButton_65.setGeometry(QtCore.QRect(200, 250, 75, 23))
                self.pushButton_65.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.pushButton_65.setObjectName("pushButton_65")

                self.Teacher_Specific_SearchLB = QtWidgets.QLabel(self.TEACHER_)
                self.Teacher_Specific_SearchLB.setGeometry(QtCore.QRect(390, 110, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Teacher_Specific_SearchLB.setFont(font)
                self.Teacher_Specific_SearchLB.setObjectName("Teacher_Specific_SearchLB")

                self.Teacher_Specific_SearchLE = QtWidgets.QLineEdit(self.TEACHER_)
                self.Teacher_Specific_SearchLE.setGeometry(QtCore.QRect(470, 110, 113, 20))
                self.Teacher_Specific_SearchLE.setObjectName("Teacher_Specific_SearchLE")

                self.Teacher_Specific_SearchPB = QtWidgets.QPushButton(self.TEACHER_)
                self.Teacher_Specific_SearchPB.setGeometry(QtCore.QRect(600, 110, 75, 23))
                self.Teacher_Specific_SearchPB.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.Teacher_Specific_SearchPB.setObjectName("Teacher_Specific_SearchPB")
                self.Teacher_Specific_SearchPB.clicked.connect(self.Show_Specific_Teacher_Record)

                self.Show_All_Teacher_RecordTBL = QtWidgets.QTableWidget(self.TEACHER_)
                self.Show_All_Teacher_RecordTBL.setGeometry(QtCore.QRect(200, 320, 511, 161))
                self.Show_All_Teacher_RecordTBL.setObjectName("Show_All_Teacher_RecordTBL")
                self.Show_All_Teacher_RecordTBL.setColumnCount(5)
                self.Show_All_Teacher_RecordTBL.setRowCount(5)
                item = QtWidgets.QTableWidgetItem()
                self.Show_All_Teacher_RecordTBL.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.Show_All_Teacher_RecordTBL.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.Show_All_Teacher_RecordTBL.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.Show_All_Teacher_RecordTBL.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.Show_All_Teacher_RecordTBL.setHorizontalHeaderItem(4, item)


                self.Show_All_Teacher_TablePB = QtWidgets.QPushButton(self.TEACHER_)
                self.Show_All_Teacher_TablePB.setGeometry(QtCore.QRect(410, 490, 75, 23))
                self.Show_All_Teacher_TablePB.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.Show_All_Teacher_TablePB.setObjectName("Show_All_Teacher_TablePB")
                self.Show_All_Teacher_TablePB.clicked.connect(self.Show_All_Teacher_Record)
                self.stackedWidget_2.addWidget(self.TEACHER_)

        # Department> Admin ------------------------------------------------------------
                self.DEPARTMENT_ = QtWidgets.QWidget()
                self.DEPARTMENT_.setObjectName("DEPARTMENT_")
                self.Department_IDLA = QtWidgets.QLabel(self.DEPARTMENT_)
                self.Department_IDLA.setGeometry(QtCore.QRect(30, 190, 121, 21))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Department_IDLA.setFont(font)
                self.Department_IDLA.setObjectName("Department_IDLA")
                self.Department_IDLE = QtWidgets.QLineEdit(self.DEPARTMENT_)
                self.Department_IDLE.setGeometry(QtCore.QRect(160, 190, 201, 20))
                self.Department_IDLE.setObjectName("Department_IDLE")

                self.Add_Item_in_DepartmentPB = QtWidgets.QPushButton(self.DEPARTMENT_)
                self.Add_Item_in_DepartmentPB.setGeometry(QtCore.QRect(60, 260, 75, 23))
                self.Add_Item_in_DepartmentPB.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.Add_Item_in_DepartmentPB.setObjectName("Add_Item_in_DepartmentPB")
                self.Add_Item_in_DepartmentPB.clicked.connect(self.Add_Item_in_Department)

                self.Department_NameLA = QtWidgets.QLabel(self.DEPARTMENT_)
                self.Department_NameLA.setGeometry(QtCore.QRect(30, 220, 121, 21))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Department_NameLA.setFont(font)
                self.Department_NameLA.setObjectName("Department_NameLA")

                self.Department_NameLE = QtWidgets.QLineEdit(self.DEPARTMENT_)
                self.Department_NameLE.setGeometry(QtCore.QRect(160, 220, 201, 20))
                self.Department_NameLE.setObjectName("Department_NameLE")


                self.Delete_Item_in_DepartmentPB = QtWidgets.QPushButton(self.DEPARTMENT_)
                self.Delete_Item_in_DepartmentPB.setGeometry(QtCore.QRect(170, 260, 75, 23))
                self.Delete_Item_in_DepartmentPB.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.Delete_Item_in_DepartmentPB.setObjectName("Delete_Item_in_DepartmentPB")
                self.Delete_Item_in_DepartmentPB.clicked.connect(self.Delete_Item_in_Department)
                

                self.Update_Item_in_DepartmentPB = QtWidgets.QPushButton(self.DEPARTMENT_)
                self.Update_Item_in_DepartmentPB.setGeometry(QtCore.QRect(280, 260, 75, 23))
                self.Update_Item_in_DepartmentPB.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.Update_Item_in_DepartmentPB.setObjectName("Update_Item_in_DepartmentPB")
                self.Update_Item_in_DepartmentPB.clicked.connect(self.Update_Item_in_Department)

                self.Departmenttableselector = QtWidgets.QTableWidget(self.DEPARTMENT_)
                self.Departmenttableselector.setGeometry(QtCore.QRect(510, 130, 300, 300))
                self.Departmenttableselector.setObjectName("Departmenttableselector")
                self.Departmenttableselector.verticalHeader().setDefaultSectionSize(50)
                self.Departmenttableselector.horizontalHeader().setDefaultSectionSize(150)
                self.Departmenttableselector.setColumnCount(2)
                self.Departmenttableselector.setRowCount(10)
                item = QtWidgets.QTableWidgetItem()
                self.Departmenttableselector.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.Departmenttableselector.setHorizontalHeaderItem(1, item)

                self.label_82 = QtWidgets.QLabel(self.DEPARTMENT_)
                self.label_82.setGeometry(QtCore.QRect(370, 40, 191, 31))
                font = QtGui.QFont()
                font.setPointSize(15)
                self.label_82.setFont(font)
                self.label_82.setObjectName("label_82")


                self.Show_Table_DepartmentPB = QtWidgets.QPushButton(self.DEPARTMENT_)
                self.Show_Table_DepartmentPB.setGeometry(QtCore.QRect(170, 300, 75, 23))
                self.Show_Table_DepartmentPB.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(181, 181, 181);\n"
        "}")
                self.Show_Table_DepartmentPB.setObjectName("Show_Table_DepartmentPB")
                self.Show_Table_DepartmentPB.clicked.connect(self.Show_Table_Department)


                self.stackedWidget_2.addWidget(self.DEPARTMENT_)
                self.tabWidget.addTab(self.tab_4, "")
                self.label_170 = QtWidgets.QLabel(self.centralwidget)
                self.label_170.setGeometry(QtCore.QRect(360, 0, 501, 41))
                font = QtGui.QFont()
                font.setPointSize(20)
                self.label_170.setFont(font)
                self.label_170.setObjectName("label_170")
                self.label_171 = QtWidgets.QLabel(self.centralwidget)
                self.label_171.setGeometry(QtCore.QRect(470, 20, 151, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_171.setFont(font)
                self.label_171.setObjectName("label_171")
                self.label_172 = QtWidgets.QLabel(self.centralwidget)
                self.label_172.setGeometry(QtCore.QRect(490, 50, 101, 21))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.label_172.setFont(font)
                self.label_172.setObjectName("label_172")
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 1135, 21))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                self.tabWidget.setCurrentIndex(3)
                self.stackedWidget_2.setCurrentIndex(0)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)



        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label.setText(_translate("MainWindow", "ENROLLMENT FORM:"))
                self.Student_IDLA.setText(_translate("MainWindow", "STUDENT ID:"))
                self.Student_FirstnameLA.setText(_translate("MainWindow", "FIRST NAME:"))
                self.Student_LastnameLA.setText(_translate("MainWindow", "LAST NAME:"))
                self.Student_MiddlenameLA.setText(_translate("MainWindow", "MIDDLE NAME:"))
                self.Student_AgeLA.setText(_translate("MainWindow", "AGE:"))
                self.Student_GenderLA.setText(_translate("MainWindow", "GENDER:"))
                self.Student_BLKAndLotLA.setText(_translate("MainWindow", "BLK AND LOT:"))
                self.Student_StreetLA.setText(_translate("MainWindow", "STREET:"))
                self.Student_SubdivisionLA.setText(_translate("MainWindow", "SUBDIVISION:"))
                self.Student_BarangayLA.setText(_translate("MainWindow","BARANGAY:"))
                self.Student_CityLA.setText(_translate("MainWindow","CITY:"))
                self.Student_Contact_NoLA.setText(_translate("MainWindow","CONTACT NO(+09):"))
                self.Student_ClassificationLA.setText(_translate("MainWindow","CLASSIFICATION:"))
                self.Student_ClassificationLE.setText(_translate("MainWindow","NEW STUDENT"))
                self.Student_isGradesLA.setText(_translate("MainWindow","GRADES:"))
                self.Student_isGradesLE.setText(_translate("MainWindow","1"))
                self.Student_isForm136LA.setText(_translate("MainWindow","FORM136:"))
                self.Student_isForm136LE.setText(_translate("MainWindow","1"))
                self.Student_isForm137LA.setText(_translate("MainWindow","FORM137:"))
                self.Student_isForm137LE.setText(_translate("MainWindow","1"))
                self.Student_isBirthCertificateLA.setText(_translate("MainWindow","BIRTH CERTIFICATE:"))
                self.Student_isBirthCertificateLE.setText(_translate("MainWindow","1"))
                self.Student_isResidencyLA.setText(_translate("MainWindow","RESIDENCY:"))
                self.Student_isResidencyLE.setText(_translate("MainWindow","FILIPINO"))
                self.Student_ClassID_FKLA.setText(_translate("MainWindow","CLASS ID:"))
                self.Student_Grade_2LA.setText(_translate("MainWindow", "CURRENT GRADE:"))
                self.Student_Section_2LA.setText(_translate("MainWindow", "CHOOSEN SECTION:"))
                self.NewStudentEnrollmentPB.setText(_translate("MainWindow", "SUBMIT"))
                self.ViewFormOldStudentPB.setText(_translate("MainWindow", "VIEW"))

                item = self.NewStudents_Table.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "STUDENT ID"))
                item = self.NewStudents_Table.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "FIRST NAME"))
                item = self.NewStudents_Table.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "LAST NAME"))
                item = self.NewStudents_Table.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "MIDDLE NAME"))
                item = self.NewStudents_Table.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "AGE"))
                item = self.NewStudents_Table.horizontalHeaderItem(5)
                item.setText(_translate("MainWindow", "GENDER"))
                item = self.NewStudents_Table.horizontalHeaderItem(6)
                item.setText(_translate("MainWindow", "BLK AND LOT"))
                item = self.NewStudents_Table.horizontalHeaderItem(7)
                item.setText(_translate("MainWindow", "STREET"))
                item = self.NewStudents_Table.horizontalHeaderItem(8)
                item.setText(_translate("MainWindow", "SUBDIVISION"))
                item = self.NewStudents_Table.horizontalHeaderItem(9)
                item.setText(_translate("MainWindow", "BARANGAY"))
                item = self.NewStudents_Table.horizontalHeaderItem(10)
                item.setText(_translate("MainWindow", "CITY"))
                item = self.NewStudents_Table.horizontalHeaderItem(11)
                item.setText(_translate("MainWindow", "CONTACT NO(+09)"))
                item = self.NewStudents_Table.horizontalHeaderItem(12)
                item.setText(_translate("MainWindow", "CLASSIFICATION"))
                item = self.NewStudents_Table.horizontalHeaderItem(13)
                item.setText(_translate("MainWindow", "NEW STUDENT"))
                item = self.NewStudents_Table.horizontalHeaderItem(14)
                item.setText(_translate("MainWindow", "FORM136"))
                item = self.NewStudents_Table.horizontalHeaderItem(15)
                item.setText(_translate("MainWindow", "FORM137"))
                item = self.NewStudents_Table.horizontalHeaderItem(16)
                item.setText(_translate("MainWindow", "BIRTH CERTIFICATE"))
                item = self.NewStudents_Table.horizontalHeaderItem(17)
                item.setText(_translate("MainWindow", "RESIDENCY"))
                item = self.NewStudents_Table.horizontalHeaderItem(18)
                item.setText(_translate("MainWindow", "CLASS ID"))

                self.label_30.setText(_translate("MainWindow", "WAIT FOR A FEW DAYS TO VERIFY YOUR ENROLLMENT FORM"))
                self.label_31.setText(_translate("MainWindow", "THANK YOU"))
                self.label_32.setText(_translate("MainWindow", "COPY YOUR ENROLLEMT FORM IN THE TABLE TO SEE YOUR SECTION SUBJECT AND ETC ."))
                self.label_33.setText(_translate("MainWindow", "FOR NEW STUDENT"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "NEW STUDENT"))


                # Start Tab 2 --------------------------------------------------
                self.label_11.setText(_translate("MainWindow", "ENROLLMENT FORM"))
                self.Student_ID_2LA.setText(_translate("MainWindow", "STUDENT ID:"))
                self.Student_NewGradeLA.setText(_translate("MainWindow", "NEW GRADE:"))
                self.Student_NewSectionLA.setText(_translate("MainWindow", "NEW SECTION:"))
                self.Student_OldSectionLA.setText(_translate("MainWindow", "OLD SECTION:"))
                item = self.OldStudents_Table.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "STUDENT ID"))
                item = self.OldStudents_Table.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "FIRST NAME"))
                item = self.OldStudents_Table.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "LAST NAME"))
                item = self.OldStudents_Table.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "MIDDLE NAME"))
                item = self.OldStudents_Table.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "AGE"))
                item = self.OldStudents_Table.horizontalHeaderItem(5)
                item.setText(_translate("MainWindow", "GENDER"))
                item = self.OldStudents_Table.horizontalHeaderItem(6)
                item.setText(_translate("MainWindow", "BLK AND LOT"))
                item = self.OldStudents_Table.horizontalHeaderItem(7)
                item.setText(_translate("MainWindow", "STREET"))
                item = self.OldStudents_Table.horizontalHeaderItem(8)
                item.setText(_translate("MainWindow", "SUBDIVISION"))
                item = self.OldStudents_Table.horizontalHeaderItem(9)
                item.setText(_translate("MainWindow", "BARANGAY"))
                item = self.OldStudents_Table.horizontalHeaderItem(10)
                item.setText(_translate("MainWindow", "CITY"))
                item = self.OldStudents_Table.horizontalHeaderItem(11)
                item.setText(_translate("MainWindow", "CONTACT NO(+09)"))
                item = self.OldStudents_Table.horizontalHeaderItem(12)
                item.setText(_translate("MainWindow", "CLASSIFICATION"))
                item = self.OldStudents_Table.horizontalHeaderItem(13)
                item.setText(_translate("MainWindow", "NEW STUDENT"))
                item = self.OldStudents_Table.horizontalHeaderItem(14)
                item.setText(_translate("MainWindow", "FORM136"))
                item = self.OldStudents_Table.horizontalHeaderItem(15)
                item.setText(_translate("MainWindow", "FORM137"))
                item = self.OldStudents_Table.horizontalHeaderItem(16)
                item.setText(_translate("MainWindow", "BIRTH CERTIFICATE"))
                item = self.OldStudents_Table.horizontalHeaderItem(17)
                item.setText(_translate("MainWindow", "RESIDENCY"))
                item = self.OldStudents_Table.horizontalHeaderItem(18)
                item.setText(_translate("MainWindow", "CLASS ID"))

                self.label_23.setText(_translate("MainWindow", "FOR OLD STUDENT"))
                self.OldStudentEnrollmentPB.setText(_translate("MainWindow", "SUBMIT"))
                self.Show_Table_OldStudentPB.setText(_translate("MainWindow", "VIEW"))
                self.label_27.setText(_translate("MainWindow", "COPY YOUR ENROLLEMT FORM IN THE TABLE TO SEE YOUR SECTION SUBJECT AND ETC ."))
                self.label_28.setText(_translate("MainWindow", "WAIT FOR A FEW DAYS TO VERIFY YOUR ENROLLMENT FORM"))
                self.label_29.setText(_translate("MainWindow", "THANK YOU"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "OLD STUDENT"))

                # End Tab 2 -----------------------------------------------------------
                item = self.StudentSchedule_Table.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "GRADE"))
                item = self.StudentSchedule_Table.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "SECTION"))
                item = self.StudentSchedule_Table.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "STDUENT  ID"))
                item = self.StudentSchedule_Table.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "SECTION"))
                item = self.StudentSchedule_Table.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "SUBJECT CODE"))
                item = self.StudentSchedule_Table.horizontalHeaderItem(5)
                item.setText(_translate("MainWindow", "SUBJECT NAME"))
                item = self.StudentSchedule_Table.horizontalHeaderItem(6)
                item.setText(_translate("MainWindow", "DATE"))
                item = self.StudentSchedule_Table.horizontalHeaderItem(7)
                item.setText(_translate("MainWindow", "TIME"))
                item = self.StudentSchedule_Table.horizontalHeaderItem(8)
                item.setText(_translate("MainWindow", "TEACHER"))
                item = self.StudentSchedule_Table.horizontalHeaderItem(9)
                item.setText(_translate("MainWindow", "DEPARTMENT"))


                item = self.SectionSchedule_Table.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "GRADE"))
                item = self.SectionSchedule_Table.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "SECTION"))
                item = self.SectionSchedule_Table.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "SCHEDULE CODE"))
                item = self.SectionSchedule_Table.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "SUBJECT NAME"))
                item = self.SectionSchedule_Table.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "SUBJECT DATE"))
                item = self.SectionSchedule_Table.horizontalHeaderItem(5)
                item.setText(_translate("MainWindow", "DATE"))
                item = self.SectionSchedule_Table.horizontalHeaderItem(6)
                item.setText(_translate("MainWindow", "TIME"))
                item = self.SectionSchedule_Table.horizontalHeaderItem(7)
                item.setText(_translate("MainWindow", "TEACHER"))
                item = self.SectionSchedule_Table.horizontalHeaderItem(8)
                item.setText(_translate("MainWindow", "DEPARTMENT"))
                self.Student_IDSEARCHLA.setText(_translate("MainWindow", "STUDENT ID"))
                self.Student_IDSEARCHPB.setText(_translate("MainWindow", "SEARCH"))
                self.ScheduleSection_SEARCHLA.setText(_translate("MainWindow", "SUBJECT CODE"))
                self.ScheduleSection_SEARCHPB.setText(_translate("MainWindow", "SEARCH"))
                self.label_163.setText(_translate("MainWindow", "ENROLLED STUDENT"))
                self.label_164.setText(_translate("MainWindow", "SCHEDULE"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "ENROLLED STUDENT"))
                self.pushButton_6.setText(_translate("MainWindow", "OLD STUDENT"))
                self.pushButton_7.setText(_translate("MainWindow", "NEW STUDENT"))
                self.pushButton_8.setText(_translate("MainWindow", "ENROLLED"))
                self.pushButton_9.setText(_translate("MainWindow", "GRADE AND SECTION"))
                self.pushButton_10.setText(_translate("MainWindow", "SCHEDULE"))
                self.pushButton_11.setText(_translate("MainWindow", "SUBJECT"))
                self.pushButton_12.setText(_translate("MainWindow", "TEACHER"))
                self.pushButton_13.setText(_translate("MainWindow", "DEPARTMENT"))
                self.label_56.setText(_translate("MainWindow", "AGE"))
                self.label_57.setText(_translate("MainWindow", "STUDENT _ID"))
                self.label_58.setText(_translate("MainWindow", "MIDDLE NAME"))
                self.label_59.setText(_translate("MainWindow", "EMAIL ACCOUNT"))
                self.pushButton_42.setText(_translate("MainWindow", "VIEW FORM"))
                self.label_60.setText(_translate("MainWindow", "FIRST NAME"))
                self.pushButton_43.setText(_translate("MainWindow", "SUBMIT"))
                self.label_61.setText(_translate("MainWindow", "GENDER"))
                item = self.tableWidget_10.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "STUDENT ID"))
                item = self.tableWidget_10.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "LAST NAME"))
                item = self.tableWidget_10.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "FIRST NAME"))
                item = self.tableWidget_10.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "MIDDLE NAME"))
                item = self.tableWidget_10.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "AGE"))
                item = self.tableWidget_10.horizontalHeaderItem(5)
                item.setText(_translate("MainWindow", "GENDER"))
                item = self.tableWidget_10.horizontalHeaderItem(6)
                item.setText(_translate("MainWindow", "ADDRESS"))
                item = self.tableWidget_10.horizontalHeaderItem(7)
                item.setText(_translate("MainWindow", "CLASSIFICATION"))
                self.label_62.setText(_translate("MainWindow", "LAST NAME"))
                self.label_63.setText(_translate("MainWindow", "CLASSIFICATION"))
                self.label_64.setText(_translate("MainWindow", "ADDRESS"))
                self.pushButton_44.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_45.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_46.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_47.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_48.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_49.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_50.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_51.setText(_translate("MainWindow", "UPDATE"))
                self.label_76.setText(_translate("MainWindow", "OLD STUDENT"))
                self.label_162.setText(_translate("MainWindow", "STUDENT _ID"))
                self.pushButton_160.setText(_translate("MainWindow", "SEARCH"))
                self.label_70.setText(_translate("MainWindow", "MIDDLE NAME"))
                self.label_67.setText(_translate("MainWindow", "FORM 137"))
                self.pushButton_53.setText(_translate("MainWindow", "VIEW"))
                self.pushButton_52.setText(_translate("MainWindow", "ADD"))
                self.label_72.setText(_translate("MainWindow", "LAST NAME"))
                self.label_66.setText(_translate("MainWindow", "CLASSFICATION"))
                self.label_73.setText(_translate("MainWindow", "FORM 136"))
                self.label_71.setText(_translate("MainWindow", "FIRST NAME"))
                self.label_74.setText(_translate("MainWindow", "ADDRESS"))
                self.label_65.setText(_translate("MainWindow", "EMAIL"))
                item = self.tableWidget_11.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "NEW ID"))
                item = self.tableWidget_11.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "LAST NAME"))
                item = self.tableWidget_11.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "FIRST NAME"))
                item = self.tableWidget_11.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "MIDDLE NAME"))
                item = self.tableWidget_11.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "AGE"))
                item = self.tableWidget_11.horizontalHeaderItem(5)
                item.setText(_translate("MainWindow", "GENDER"))
                item = self.tableWidget_11.horizontalHeaderItem(6)
                item.setText(_translate("MainWindow", "ADDRESS"))
                item = self.tableWidget_11.horizontalHeaderItem(7)
                item.setText(_translate("MainWindow", "EMAIL"))
                item = self.tableWidget_11.horizontalHeaderItem(8)
                item.setText(_translate("MainWindow", "CLASSIFICATION"))
                item = self.tableWidget_11.horizontalHeaderItem(9)
                item.setText(_translate("MainWindow", "FORM 137"))
                item = self.tableWidget_11.horizontalHeaderItem(10)
                item.setText(_translate("MainWindow", "FORM 136"))
                self.label_69.setText(_translate("MainWindow", "AGE"))
                self.label_68.setText(_translate("MainWindow", "GENDER"))
                self.pushButton_54.setText(_translate("MainWindow", "DELETE"))
                self.pushButton_55.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_56.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_57.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_58.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_59.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_60.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_61.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_62.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_63.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_64.setText(_translate("MainWindow", "UPDATE"))
                self.label_75.setText(_translate("MainWindow", "NEW STUDENT"))
                self.pushButton_83.setText(_translate("MainWindow", "VIEW ALL"))
                self.pushButton_84.setText(_translate("MainWindow", "SEARCH"))
                self.label_93.setText(_translate("MainWindow", "NEW ID"))
                self.label_94.setText(_translate("MainWindow", "LAST NAME"))
                self.pushButton_85.setText(_translate("MainWindow", "SEARCH"))
                self.label_95.setText(_translate("MainWindow", "NEW ID"))
                self.pushButton_86.setText(_translate("MainWindow", "SEARCH"))
                self.label_96.setText(_translate("MainWindow", "FIRST NAME"))
                self.label_97.setText(_translate("MainWindow", "MIDDLE NAME"))
                self.pushButton_87.setText(_translate("MainWindow", "SEARCH"))
                self.label_53.setText(_translate("MainWindow", "ENROLLED ID"))
                self.label_54.setText(_translate("MainWindow", "STUDENT ID"))
                self.label_55.setText(_translate("MainWindow", "NEW_ID"))
                self.pushButton_40.setText(_translate("MainWindow", "ADD"))
                self.pushButton_41.setText(_translate("MainWindow", "DELETE"))
                self.label_77.setText(_translate("MainWindow", "ENROLLED"))
                item = self.tableWidget_29.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "ENROLLED ID"))
                item = self.tableWidget_29.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "STUDENT ID"))
                item = self.tableWidget_30.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "NEW_ID"))
                item = self.tableWidget_30.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "STUDENT ID"))
                self.pushButton_162.setText(_translate("MainWindow", "ADD"))
                item = self.tableWidget_31.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "ENROLLED ID"))
                item = self.tableWidget_31.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "STUDENT ID"))
                item = self.tableWidget_31.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "FIRST NAME"))
                item = self.tableWidget_31.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "LAST NAME"))
                item = self.tableWidget_31.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "MIDDLE NAME"))
                self.pushButton_163.setText(_translate("MainWindow", "VIEW"))
                self.pushButton_164.setText(_translate("MainWindow", "VIEW"))
                self.pushButton_165.setText(_translate("MainWindow", "VIEW ALL"))
                self.pushButton_166.setText(_translate("MainWindow", "VIEW ALL"))
                item = self.tableWidget_32.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "ENROLLED ID"))
                item = self.tableWidget_32.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "NEW ID"))
                item = self.tableWidget_32.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "FIRST NAME"))
                item = self.tableWidget_32.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "LAST NAME"))
                item = self.tableWidget_32.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "MIDDLE NAME"))
                self.label_165.setText(_translate("MainWindow", "STUDENT ID"))
                self.label_166.setText(_translate("MainWindow", "ENROLLED ID"))
                self.label_167.setText(_translate("MainWindow", "NEW ID"))
                self.label_168.setText(_translate("MainWindow", "ENROLLED ID"))
                self.pushButton_167.setText(_translate("MainWindow", "SEARCH"))
                self.pushButton_169.setText(_translate("MainWindow", "SEARCH"))
                self.pushButton_170.setText(_translate("MainWindow", "SEARCH"))
                self.label_49.setText(_translate("MainWindow", "GRADE AND SECTION ID"))
                self.label_50.setText(_translate("MainWindow", "GRADE"))
                self.label_51.setText(_translate("MainWindow", "SCHEDULE ID"))
                self.label_52.setText(_translate("MainWindow", "ENROLLED ID"))
                self.pushButton_35.setText(_translate("MainWindow", "ADD"))
                self.pushButton_36.setText(_translate("MainWindow", "DELETE"))
                self.pushButton_37.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_38.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_39.setText(_translate("MainWindow", "UPDATE"))
                item = self.tableWidget_9.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "GRADE AND SEC ID"))
                item = self.tableWidget_9.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "SCHEDULE"))
                item = self.tableWidget_9.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "SECTION"))
                item = self.tableWidget_9.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "SCHEDULE ID"))
                item = self.tableWidget_9.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "GRADE"))
                self.label_78.setText(_translate("MainWindow", "GRADE AND SECTION"))
                self.pushButton_75.setText(_translate("MainWindow", "VIEW"))
                self.label_87.setText(_translate("MainWindow", "GRADE AND SECTION ID"))
                self.pushButton_76.setText(_translate("MainWindow", "SEARCH"))
                self.label_89.setText(_translate("MainWindow", "STUDENT   ID"))
                self.pushButton_78.setText(_translate("MainWindow", "SEARCH"))
                self.label_88.setText(_translate("MainWindow", "SUBJECT CODE"))
                self.label_90.setText(_translate("MainWindow", "NEW STUDENT ID"))
                item = self.tableWidget_15.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "GRADE"))
                item = self.tableWidget_15.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "SECTION"))
                item = self.tableWidget_15.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "SCHEDULE CODE"))
                item = self.tableWidget_15.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "SUBJECT CODE"))
                item = self.tableWidget_15.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "SUBJECT NAME"))
                item = self.tableWidget_15.horizontalHeaderItem(5)
                item.setText(_translate("MainWindow", "TIME"))
                item = self.tableWidget_15.horizontalHeaderItem(6)
                item.setText(_translate("MainWindow", "DATE"))
                item = self.tableWidget_15.horizontalHeaderItem(7)
                item.setText(_translate("MainWindow", "DEPARTMENT"))
                item = self.tableWidget_16.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "GRADE"))
                item = self.tableWidget_16.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "SECTION"))
                item = self.tableWidget_16.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "DATE"))
                item = self.tableWidget_16.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "SCHEDULE CODE"))
                item = self.tableWidget_16.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "SUBJECT NAME"))
                item = self.tableWidget_16.horizontalHeaderItem(5)
                item.setText(_translate("MainWindow", "SUBJECT DATE"))
                item = self.tableWidget_16.horizontalHeaderItem(6)
                item.setText(_translate("MainWindow", "TIME"))
                item = self.tableWidget_16.horizontalHeaderItem(7)
                item.setText(_translate("MainWindow", "DEPARTMENT"))
                self.pushButton_77.setText(_translate("MainWindow", "SEARCH"))
                self.pushButton_79.setText(_translate("MainWindow", "SEARCH"))
                self.pushButton_80.setText(_translate("MainWindow", "SEARCH"))
                self.label_91.setText(_translate("MainWindow", "SUBJECT CODE"))
                self.label_92.setText(_translate("MainWindow", "SECTION"))
                self.pushButton_81.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_82.setText(_translate("MainWindow", "VIEW"))
                self.label_46.setText(_translate("MainWindow", "SCHEDULE ID"))
                self.label_47.setText(_translate("MainWindow", "SCHEDULE CODE"))
                self.label_48.setText(_translate("MainWindow", "SUBEJCT ID"))
                self.pushButton_31.setText(_translate("MainWindow", "ADD"))
                self.pushButton_32.setText(_translate("MainWindow", "DELETE"))
                self.pushButton_33.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_34.setText(_translate("MainWindow", "UPDATE"))
                item = self.tableWidget_8.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "SCHEDULE ID"))
                item = self.tableWidget_8.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "SCHEDULE CODE"))
                item = self.tableWidget_8.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "SUBJECT ID"))
                self.label_79.setText(_translate("MainWindow", "SCHEDULE"))
                self.pushButton_71.setText(_translate("MainWindow", "VIEW"))
                item = self.tableWidget_12.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "SCHEDULE ID"))
                item = self.tableWidget_12.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "SCHEDULE CODE"))
                item = self.tableWidget_12.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "SUBJECT ID"))
                item = self.tableWidget_12.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "SUBJECT NAME"))
                self.label_85.setText(_translate("MainWindow", "SCHEDULE ID"))
                self.label_86.setText(_translate("MainWindow", "SCHEDULE CODE"))
                self.pushButton_72.setText(_translate("MainWindow", "SEARCH"))
                self.pushButton_73.setText(_translate("MainWindow", "SEARCH"))
                self.pushButton_74.setText(_translate("MainWindow", "VIEW"))
                self.label_41.setText(_translate("MainWindow", "SUBJECT ID"))
                self.label_42.setText(_translate("MainWindow", "SUBJECT NAME"))
                self.label_43.setText(_translate("MainWindow", "SUBJECT CODE"))
                self.label_44.setText(_translate("MainWindow", "DATE"))
                self.label_45.setText(_translate("MainWindow", "TEACHER ID"))
                self.pushButton_25.setText(_translate("MainWindow", "ADD"))
                self.pushButton_26.setText(_translate("MainWindow", "DELETE"))
                self.pushButton_27.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_28.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_29.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_30.setText(_translate("MainWindow", "UPDATE"))
                item = self.tableWidget_7.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "SUBJECT ID"))
                item = self.tableWidget_7.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "LAST NAME"))
                item = self.tableWidget_7.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "CODE"))
                item = self.tableWidget_7.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "DATE"))
                item = self.tableWidget_7.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "TEACHER ID"))
                item = self.tableWidget_7.horizontalHeaderItem(5)
                item.setText(_translate("MainWindow", "TEACHER NAME"))
                self.label_80.setText(_translate("MainWindow", "SUBJECT"))
                self.pushButton_68.setText(_translate("MainWindow", "VIEW"))
                item = self.tableWidget_14.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "SUBJECT ID"))
                item = self.tableWidget_14.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "SUBJECT NAME"))
                item = self.tableWidget_14.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "CODE"))
                item = self.tableWidget_14.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "DATE"))
                item = self.tableWidget_14.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "TEACHER ID"))
                item = self.tableWidget_14.horizontalHeaderItem(5)
                item.setText(_translate("MainWindow", "TEACHER NAME"))
                self.label_84.setText(_translate("MainWindow", "SUBJECT CODE"))
                self.pushButton_69.setText(_translate("MainWindow", "SEARCH"))
                self.pushButton_161.setText(_translate("MainWindow", "VIEW ALL"))
                self.pushButton_171.setText(_translate("MainWindow", "SEARCH"))
                self.label_169.setText(_translate("MainWindow", "SUBJECT ID"))
                self.label_36.setText(_translate("MainWindow", "TEACHER ID"))
                self.label_37.setText(_translate("MainWindow", "LAST NAME"))
                self.label_38.setText(_translate("MainWindow", "FIRST NAME"))
                self.label_39.setText(_translate("MainWindow", "MIDDLE NAME"))
                self.label_40.setText(_translate("MainWindow", "DEPARTMENT ID"))
                self.pushButton_19.setText(_translate("MainWindow", "ADD"))
                self.pushButton_20.setText(_translate("MainWindow", "DELETE"))
                self.pushButton_21.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_22.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_23.setText(_translate("MainWindow", "UPDATE"))
                self.pushButton_24.setText(_translate("MainWindow", "UPDATE"))



                item = self.Show_Specific_Teacher_RecordTBL.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "TEACHER ID"))
                item = self.Show_Specific_Teacher_RecordTBL.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "FIRSTNAME"))
                item = self.Show_Specific_Teacher_RecordTBL.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "LASTNAME"))
                item = self.Show_Specific_Teacher_RecordTBL.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "MIDDLENAME"))
                item = self.Show_Specific_Teacher_RecordTBL.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "DEPARTMENT ID"))

                self.label_81.setText(_translate("MainWindow", "TEACHER"))
                self.pushButton_65.setText(_translate("MainWindow", "VIEW"))
                self.Teacher_Specific_SearchLB.setText(_translate("MainWindow", "TEACHER ID"))
                self.Teacher_Specific_SearchPB.setText(_translate("MainWindow", "SEARCH"))
                item = self.Show_All_Teacher_RecordTBL.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "TEACHER ID"))
                item = self.Show_All_Teacher_RecordTBL.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "LAST NAME"))
                item = self.Show_All_Teacher_RecordTBL.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "FIRST NAME"))
                item = self.Show_All_Teacher_RecordTBL.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "MIDDLE NAME"))
                item = self.Show_All_Teacher_RecordTBL.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "DEPARTMENT"))
                self.Show_All_Teacher_TablePB.setText(_translate("MainWindow", "VIEW ALL"))
                self.Department_IDLA.setText(_translate("MainWindow", "DEPARTMENT ID"))
                self.Add_Item_in_DepartmentPB.setText(_translate("MainWindow", "ADD"))
                self.Department_NameLA.setText(_translate("MainWindow", "DEPARTMENT NAME"))
                self.Delete_Item_in_DepartmentPB.setText(_translate("MainWindow", "DELETE"))
                self.Update_Item_in_DepartmentPB.setText(_translate("MainWindow", "UPDATE"))
                item = self.Departmenttableselector.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "DEPARTMENT ID"))
                item = self.Departmenttableselector.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "DEPARTMENT NAME"))
                self.label_82.setText(_translate("MainWindow", "DEPARTMENT"))
                self.Show_Table_DepartmentPB.setText(_translate("MainWindow", "VIEW ALL"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "ADMIN"))
                self.label_170.setText(_translate("MainWindow", "CHINESE MEDICAL UNIVERSITY "))
                self.label_171.setText(_translate("MainWindow", "LABORATORY SCHOOL"))
                self.label_172.setText(_translate("MainWindow", "(MIDDLE SCHOOL)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
