import tkinter as tk
import datetime

class UserInterface:
    def __init__(self, master):
        self.master = master
        master.title("Number Selector")
        master.geometry("400x210")
        self.scrollbar1 = tk.Scale(master, from_=1, to=10, orient=tk.HORIZONTAL, command=self.on_scroll1, length=200, troughcolor='blue', sliderlength=30)
        self.scrollbar2 = tk.Scale(master, from_=1, to=10, orient=tk.HORIZONTAL, command=self.on_scroll2, length=200, troughcolor='blue', sliderlength=30)
        self.scrollbar1.pack()
        self.scrollbar2.pack()
        self.scale1 = tk.Label(master, text="", fg="blue")
        self.scale1.place(x=150,y=45)
        self.scale10 = tk.Label(master, text="", fg="red")
        self.scale10.place(x=350,y=45)
        self.value1 = tk.Label(master, text="Value 1: ")
        self.value2 = tk.Label(master, text="Value 2: ")
        self.timestamp1 = tk.Label(master, text="H Last updated: ")
        self.timestamp2 = tk.Label(master, text="N Last updated: ")
        self.textbox1 = tk.Text(master, height=3)
        self.textbox1.pack()
        self.textbox2.pack()
        self.update_labels()

    def update_labels(self):
        self.value1.config(text="Value 1: {}".format(self.scrollbar1.get()))
        self.value2.config(text="Value 2: {}".format(self.scrollbar2.get()))
        if self.scrollbar1.get() == 10 and self.scrollbar2.get() ==10:
            self.textbox1.pack()
        else:
            self.textbox1.pack_forget()

    def update_timestamp1(self):
        now1 = datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
        self.timestamp1.config(text="H Last updated: {}".format(now1))
        self.timestamp1.pack()
    def update_timestamp2(self):
        now2 = datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
        self.timestamp2.config(text="N Last updated: {}".format(now2))
        self.timestamp2.pack()
        
    def on_scroll1(self, value):
        self.update_labels()
        self.update_timestamp1()
        r = int(self.scrollbar1.get()/10 * 255)
        g = 0
        b = int((1 - self.scrollbar1.get()/10) * 255)
        color = f'#{r:02x}{g:02x}{b:02x}'
        self.scrollbar1.config(troughcolor=color)

    def on_scroll2(self, value):
        self.update_labels()
        self.update_timestamp2()
        r = int(self.scrollbar2.get()/10 * 255)
        g = 0
        b = int((1 - self.scrollbar2.get()/10) * 255)
        color = f'#{r:02x}{g:02x}{b:02x}'
        self.scrollbar2.config(troughcolor=color)
    

root = tk.Tk()
app = UserInterface(root)
root.mainloop()
