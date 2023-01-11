from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("550x655")
        self.root.title("STUDENT DETAILS")

        self.root.config(bg="Dark blue")
        self.namevalue = StringVar()
        self.studentIdvalue = StringVar()
        self.rollnovalue = StringVar()
        self.gendervalue = StringVar()
        self.coursevalue = StringVar()
        self.fathervalue = StringVar()
        self.contactvalue = StringVar()
        self.addressvalue = StringVar()
        self.cgpavalue = StringVar()
        self.semestervalue = StringVar()

        heading = Label(self.root, text="STUDENT DETAILS", font=("new time romans", 13, "bold"), bg="sky blue",fg="purple")
        heading.config(width=30, height=5)
        heading.grid(row=0, column=3, padx=5, pady=5)

        name_lbl = Label(self.root,text = "NAME",font=("new time romans", 10, "bold"),bg = 'sky blue',fg= "purple")
        name_lbl.grid(row =2,column =2,padx =5,pady =5)

        studentId_lbl = Label(self.root, text="STUDENT ID", font=("new time romans", 10, "bold"), bg='sky blue', fg="purple")
        studentId_lbl.grid(row =3,column =2,padx =5,pady =5)

        rollno_lbl = Label(self.root, text="ROLL NO", font=("new time romans", 10, "bold"), bg='sky blue',fg="purple")
        rollno_lbl.grid(row=4, column=2, padx=5, pady=5)

        gender_lbl = Label(self.root, text="GENDER", font=("new time romans", 10, "bold"), bg='sky blue', fg="purple")
        gender_lbl.grid(row=5, column=2, padx=5, pady=5)

        course_lbl = Label(self.root, text="COURSE", font=("new time romans", 10, "bold"), bg='sky blue',fg="purple")
        course_lbl.grid(row=6, column=2, padx=5, pady=5)

        semester_lbl = Label(self.root, text="SEMESTER", font=("new time romans", 10, "bold"), bg='sky blue', fg="purple")
        semester_lbl.grid(row=7, column=2, padx=5, pady=5)

        father_lbl = Label(self.root, text="FATHER", font=("new time romans", 10, "bold"), bg='sky blue',fg="purple")
        father_lbl.grid(row=8, column=2, padx=5, pady=5)

        CGPA_lbl = Label(self.root, text="CGPA", font=("new time romans", 10, "bold"), bg='sky blue',fg="purple")
        CGPA_lbl.grid(row=9, column=2, padx=5, pady=5)

        contact_lbl = Label(self.root, text="CONTACT NO", font=("new time romans", 10, "bold"), bg='sky blue', fg="purple")
        contact_lbl.grid(row=10, column=2, padx=5, pady=5)

        address_lbl = Label(self.root, text="ADDRESS", font=("new time romans", 10, "bold"), bg='sky blue', fg="purple")
        address_lbl.grid(row=11, column=2, padx=5, pady=5)



        self.nameentry = Entry(self.root,textvariable = self.namevalue)
        self.nameentry.grid(row=2, column=3)

        self.studentIdentry = Entry(self.root, textvariable=self.studentIdvalue)
        self.studentIdentry.grid(row=3, column=3)

        self.rollnoentry = Entry(self.root, textvariable=self.rollnovalue)
        self.rollnoentry.grid(row=4, column=3)

        self.genderentry = Entry(self.root, textvariable=self.gendervalue)
        self.genderentry.grid(row=5, column=3)

        self.courseentry = Entry(self.root, textvariable=self.coursevalue)
        self.courseentry.grid(row=6, column=3)

        self.semesterentry = Entry(self.root, textvariable=self.semestervalue)
        self.semesterentry.grid(row=7, column=3)

        self.fatherentry = Entry(self.root, textvariable=self.fathervalue)
        self.fatherentry.grid(row=8, column=3)

        self.cgpaentry = Entry(self.root, textvariable=self.cgpavalue)
        self.cgpaentry.grid(row=9, column=3)

        self.contactentry = Entry(self.root, textvariable=self.contactvalue)
        self.contactentry.grid(row=10, column=3)

        self.addressentry = Entry(self.root, textvariable=self.addressvalue)
        self.addressentry.grid(row=11, column=3)

        self.b_lbl = Label(self.root)
        self.b_lbl.place(x=0,y=500,width=550,height=25)

        self.savebutton = Button(self.b_lbl,text="Save",command=self.add_data,bg = "purple",fg = "sky blue")
        self.savebutton.place(x=0,y=0,width=275,height=25)

        self.addphotobutton = Button(self.b_lbl, text="ADD PHOTO",command=self.generate_dataset, bg="purple", fg="sky blue")
        self.addphotobutton.place(x=275, y=0, width=270, height=25)

    #**************************Function Declaration******************#

    def add_data(self):
        try:
            conn = mysql.connector.connect(host="localhost",username="root",password="Vaibhav1#",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.nameentry.get(),
                                                                                        self.studentIdentry.get(),
                                                                                        self.rollnoentry.get(),
                                                                                        self.genderentry.get(),
                                                                                        self.courseentry.get(),
                                                                                        self.fatherentry.get(),
                                                                                        self.contactentry.get(),
                                                                                        self.addressentry.get(),
                                                                                        self.cgpaentry.get(),
                                                                                        self.semesterentry.get()
                                                                                          ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","student details has been added successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #*******************Generate dataset or take photo samples********************#
    def generate_dataset(self):
        try:
            conn = mysql.connector.connect(host="localhost",username="root",password="Vaibhav1#",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from student")
            my_result = my_cursor.fetchall()
            id = 0
            for x in my_result:
                id+=1
            conn.close()
            #********************Load predefined data on face frontals from opencv***********#
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            def face_cropped(img):
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces=face_classifier.detectMultiScale(gray,1.3,5)

                for (x,y,w,h)in faces:
                    face_cropped=img[y:y+h,x:x+w]
                    return face_cropped
            cap = cv2.VideoCapture(0)
            img_id=0
            while True:
                ret,my_frame=cap.read()
                if face_cropped(my_frame) is not None:
                    img_id+=1
                    face=cv2.resize(face_cropped(my_frame),(450,450))
                    face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Cropped face",face)

                if cv2.waitKey(1)==13 or int(img_id)==100:
                    break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Generating dataset completed!!!!")
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)






if __name__ == '__main__':
    root = Tk()
    obj = student(root)
    root.mainloop()