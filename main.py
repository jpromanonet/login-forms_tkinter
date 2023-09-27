# Import tkinter
from tkinter import *
from tkinter import messagebox

# Creating the window
root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

# Let's apply the login image
login_img = PhotoImage(file='./assets/login.png')
Label(root, image=login_img, bg="white").place(x=50, y=50)

# Login component
frame = Frame(root, width = 350, height = 350, bg = "red")
frame.place(x = 480, y = 70)

heading = Label(frame, text = "Sign In", fg = "#57a1f8", bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

user = Entry(frame, width=25,fg='black',border=2,bg="white", font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)

# Running the app
root.mainloop()