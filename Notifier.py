from tkinter import*
from PIL import Image,ImageTk
from plyer import notification
import time
from tkinter import messagebox

t=Tk()
t.title("Work Reminder-app")
t.geometry("500x300")
img = Image.open("png.jpg")
tkimage = ImageTk.PhotoImage(img)

#get details 
def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time =  time1.get()

    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "All Fields are required!")
    else:
        int_time = int(float(get_time))
        min_to_sec = int_time * 60
        messagebox.showinfo("notifier set", "set notification?")

        time.sleep(min_to_sec)

        notification.notify(title=get_title,
                    message=get_msg,
                    app_icon="alarm.ico",
                    app_name ="notifier",
                    timeout=10)

img_label = Label(t,image=tkimage).grid()

#label1
t_label = Label(t,text="Title to notify", font=("poppins",10))
t_label.place(x=12,y=70)

#entry1
title = Entry(t,width="25", font=("poppins",13))
title.place(x=123,y=70)

#label2
m_label = Label(t,text="Display message", font=("poppins",10))
m_label.place(x=12,y=120)

#entry2
msg = Entry(t,width="40", font=("poppins",13))
msg.place(x=123,y=128,height=30)

#label3
time_label = Label(t,text="Set time", font=("poppins",10))
time_label.place(x=12,y=175)

#entry3
time1 = Entry(t, width="5", font=("poppins",13))
time1.place(x=123,y=175)

#label4
time_min_label = Label(t,text="min", font=("poppins",10))
time_min_label.place(x=175,y=180)

#button
but = Button(t,text="SET NOTIFICATIION", font=("poppins",10,'bold'), fg="#ffffff",bg="#528DFF",width=20,
             relief="raised",
             command=get_details)
but.place(x=170, y=230)

t.resizable(0,0)
t.mainloop()