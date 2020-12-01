from tkinter import*
from tkinter import messagebox
class Login_system:
    def __init__(self, root):
        self.root = root
        self.root.title("System")

        #self.bgpic = PhotoImage(file =  "image/bg.jpg")
        #self.userpic = PhotoImage(file = "images/man-user.jpg")
        #self.passpic = PhotoImage(file = "images/password.jpg")

        self.username = StringVar()
        self.password = StringVar()

        title = Label(self.root, text ="Payroll System", font =( "Ariel", 40), bg= "grey")
        title.place(x = 0, y = 0, relwidth = 1)

        FrameL = Frame(self.root, bg = "grey")
        FrameL.place(x = 450, y = 150)

        luser = Label(FrameL, text = "Input username", compound = LEFT, font =( "times new roman", 10)).grid(row = 1, column = 0, padx = 20, pady = 10)
        user = Entry(FrameL, bd="5", textvariable = self.username, relief=GROOVE, font=("", 15)).grid(row=1, column=1, padx=20)
        luser = Label(FrameL, text = "Input username", compound = LEFT, font =( "times new roman", 10)).grid(row = 2, column = 0, padx = 20, pady = 10)
        password = Entry(FrameL, bd="5", textvariable = self.password, relief=GROOVE, font=("", 15)).grid(row=2, column=1, padx=20)

        log = Button(FrameL, text = "Login", width = 15,command = self.login,  font =( "times new roman", 10), bg = "grey").grid(row = 3, column = 1, pady = 10)

    def login(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Invalid", "Please try again.")
        elif self.username.get() == "admin" and self.password.get() =="admin":
            messagebox.showinfo("successful", f"welcome {self.username.get()}")
        else:
            messagebox.showerror("Error","Invalid username or password")


root = Tk()
object = Login_system(root)
root.mainloop()
