import datetime
import tkinter as tk
window=tk.Tk()
window.geometry("620x780")
window.title("AGE CALCULATOR APP")
name=tk.Label(text="NAME")
name.grid(column=0,row=1)
nameEntry=tk.Entry()
nameEntry.grid(column=1,row=1)
year=tk.Label(text="YEAR")
year.grid(column=0,row=2)
yearEntry=tk.Entry()
yearEntry.grid(column=1,row=2)
month=tk.Label(text="MONTH")
month.grid(column=0,row=3)
monthEntry=tk.Entry()
monthEntry.grid(column=1,row=3)
date=tk.Label(text="DATE")
date.grid(column=0,row=4)
dateEntry=tk.Entry()
dateEntry.grid(column=1,row=4)
def getinput():
    
    name=nameEntry.get()
    

    p=person(name,datetime.date(int(yearEntry.get()),int(monthEntry.get()),
                                int(dateEntry.get())))

    textArea=tk.Text(master=window,height=15,width=40)
    textArea.grid(column=1,row=6)

    answer=" hey{p}!!!!!,you are {age} years old!!!".format(p=name,age=p.age())
    textArea.insert(tk.END,answer)

             


class person:
    def __init__(self,name,birthdate):
        self.name=name
        self.birthdate=birthdate

    def age(self):
        today=datetime.date.today()
        age=today.year-self.birthdate.year
        return age
        



button=tk.Button(window,text="calculateage",command=getinput,bg="pink")
button.grid(column=1,row=5)
window.mainloop()
























