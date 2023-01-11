from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import student
from face_recognition import facedetect
from train import Train

class face_recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1550x800")
        self.root.title("Face Rrecognition System")

        img = Image.open(r"C:\Users\anshu\OneDrive\Desktop\face recognition\face recognition\bg_image.jpg")
        img = img.resize((1550,800),Image.ANTIALIAS)
        self.back_img = ImageTk.PhotoImage(img)

        bg_lbl = Label(self.root,image = self.back_img)
        bg_lbl.place(x=0,y=0,width=1530,height=800)

        title_lbl = Label(bg_lbl,text = "FACE RECOGNITION SYSTEM",font = ("new time romans", 13, "bold"),bg = "dark blue",fg = "sky blue")
        title_lbl.place(x=0,y=0,width = 1530,height = 35)

        img1 = Image.open(r"C:\Users\anshu\OneDrive\Desktop\face recognition\face recognition\student.png")
        img1 = img1.resize((200, 200), Image.ANTIALIAS)
        self.student_img = ImageTk.PhotoImage(img1)

        st_button = Button(bg_lbl,image=self.student_img,command=self.student_details)
        st_button.place(x = 250,y=250,width = 200,height=200)
        st_lbl = Label(bg_lbl,text="STUDENT DETAILS",bg = "purple",fg="sky blue")
        st_lbl.place(x=250,y=450,width=200,height=25)

        img2 = Image.open(r"C:\Users\anshu\OneDrive\Desktop\face recognition\face recognition\attendance.png")
        img2 = img2.resize((200, 200), Image.ANTIALIAS)
        self.attendance_img = ImageTk.PhotoImage(img2)

        at_button = Button(bg_lbl,image = self.attendance_img,command=self.face_detect)
        at_button.place(x= 500,y=250,width=200,height= 200)
        at_lbl = Label(bg_lbl, text="ATTENDANCE DETAILS", bg="purple", fg="sky blue")
        at_lbl.place(x=500, y=450, width=200, height=25)

        img3 = Image.open(r"C:\Users\anshu\OneDrive\Desktop\face recognition\face recognition\train.png")
        img3 = img3.resize((200, 200), Image.ANTIALIAS)
        self.train_img = ImageTk.PhotoImage(img3)

        train_button = Button(bg_lbl, image=self.train_img,command = self.trains)
        train_button.place(x=750, y=250, width=200, height=200)
        train_lbl = Label(bg_lbl, text="TRAIN DATA", bg="purple", fg="sky blue")
        train_lbl.place(x=750, y=450, width=200, height=25)

        img4 = Image.open(r"C:\Users\anshu\OneDrive\Desktop\face recognition\face recognition\exit.png")
        img4 = img4.resize((200, 200), Image.ANTIALIAS)
        self.exit_img = ImageTk.PhotoImage(img4)

        exit_button = Button(bg_lbl, image=self.exit_img,command = self.exit_c)
        exit_button.place(x=1000, y=250, width=200, height=200)
        exit_lbl = Label(bg_lbl, text="EXIT", bg="purple", fg="sky blue")
        exit_lbl.place(x=1000, y=450, width=200, height=25)


    # *******************function Buttons*******************#

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)

    def face_detect(self):
        self.new_window = Toplevel(self.root)
        self.app = facedetect(self.new_window)

    def trains(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def exit_c(self):
        quit()



if __name__ == '__main__':
    root = Tk()
    obj = face_recognition(root)
    root.mainloop()



