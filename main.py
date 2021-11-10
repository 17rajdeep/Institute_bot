import tkinter
from tkinter import *
from tkinter import filedialog
root = Tk()
root.title('the bot')
root.geometry('300x400')
root.config(bg="#77ACF1")
botr= tkinter.StringVar()
adms =tkinter.StringVar()
def adm():
    labl2.insert(END,"your willingness to join kiet\nis being looked after\nwe will get back to you")
def back():
    root.destroy()
greet={
    "hi":"hello, ask me anything about kiet",
    "hello":"hello, ask me anything about kiet",
}
quits={
    "bye":"bye!thanks for visiting",
    "goodbye":"bye!thanks for visiting",
    "quit":"bye!thanks for visiting",
}
courses = {
    "courses":"1.AID\n 2.CSM\n 3.CSD\n 4.CAI\n 5.CSC",
    "what are the courses offered":"1.AID\n 2.CSM\n 3.CSD\n 4.CAI\n 5.CSC",
    "courses available":"1.AID\n 2.CSM\n 3.CSD\n 4.CAI\n 5.CSC",
    "course":"1.AID\n 2.CSM\n 3.CSD\n 4.CAI\n 5.CSC",
    "courses offered":"1.AID\n 2.CSM\n 3.CSD\n 4.CAI\n 5.CSC",
    "more about aid":"scientific methodologies, processes, and techniques drawn from different domains like statistics, cognitive science, and computing and information science to extract knowledge \nfrom structured data and unstructured data.",
    "more about csm":"Machine learning is the study of computer algorithms that can improve automatically through experience and by the use of data. It is seen as a part of artificial intelligence.",
    "more about csd":"Data science is an interdisciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from noisy,\n structured and unstructured data, and apply knowledge\n and actionable insights from data across a broad range \nof application domains.",
    "more about cai":"Artificial intelligence is a technology which enables a machine to simulate human behavior. Machine learning is a subset of AI which allows a machine\n to automatically learn from past data without programming \nexplicitly. The goal of AI is to make a smart computer system \nlike humans to solve complex problems",
    "more about csc":"Cyber security is the application of technologies, processes and controls to protect systems, networks, programs, devices and data from cyber attacks"
}

fee_inp={
    "what is the fee structure":"1.college fee=1.05 lakhs\n2.transport fee= 12k to 18k\n3.hostel fee= 40k with food",
    "fee":"1.college fee=1.05 lakhs\n2.transport fee= 12k to 18k\n3.hostel fee= 40k with food",
    "courses fee":"1.college fee=1.05 lakhs\n2.transport fee= 12k to 18k\n3.hostel fee= 40k with food"

}
campus={
    "campus":"1.KIET\n2.KIET+\n3.KIET WOMENS",
    "how many campus are there":"1.KIET\n2.KIET+\n3.KIET WOMENS",
    "different campus":"1.KIET\n2.KIET+\n3.KIET WOMENS",
    "extra curricular":"1.games\n2.NCC\n3.NSS\n4.TOASTMASTERS",
    "what are the extra curricular":"1.games\n2.NCC\n3.NSS\n4.TOASTMASTERS",


}
admission={

    "admission":"please enter your name",
    "i want to take admission":"please enter your name",
    "i want to join kiet":"please enter your name"

}
placements = {
    "is their any placements in your college":"yes every year soo many students are placed in top mnc companies",
    "how many compines are visited to your college every year":"in between 35 to 40 companies are visited to the college",
    "name some top companies visited to the college":"companies like TCS,WIPRO,HCL,COGNIZENT,ACCENTURE ect",
    "what is the highest package of last year":"last year one student got 18lacks per annum",
    "average salary package":"average salary is 4.5lac to 5lack per annum",
    "minimum salary package per anum":"3lack to 3.6lacks per annum",
    "what are the available courses to get admission":"1.AID\n 2.CSM\n 3.CAI\n 4.CSD\n 5.CSC",
    "overall how many seats are their in these branches":"overall 1050 seats are their",
    "in a branch how many seats are their":"in a branch 180 seats are their",
    #"in a branch how many conviner seats are their":"overall 120 conviner seats are available ",
    "in a branch how many management seats are their":"60 seats are available in management "
}
global labl2,user_inp,count,ent1
count=0
def outpp():

        if user_inp in courses.keys():
            labl2.delete('1.0', END)
            labl2.insert(INSERT,courses[user_inp]+"\nto know more about courses type\nmore about course name")
        elif user_inp in fee_inp.keys():
            labl2.delete('1.0', END)
            labl2.insert(END,fee_inp[user_inp])
        elif user_inp in campus.keys():
            labl2.delete('1.0', END)
            labl2.insert(END,campus[user_inp])
        elif user_inp in admission.keys():
            labl2.delete('1.0', END)
            adm()
        elif user_inp in greet.keys():
            labl2.delete('1.0', END)
            labl2.insert(END,greet[user_inp])
        elif user_inp in quits.keys():
            labl2.delete('1.0', END)
            labl2.insert(END,quits[user_inp])
            back()

        else:
            labl2.delete('1.0', END)
            labl2.insert(END,"Sorry did not get it\ntry again!!! ")

def inp():

    global user_inp,ent1
    user_inp = str(botr.get())
    ent1.delete(0,"end")
    outpp()

lbl=lbl1= Label(root,text="YOU:")
lbl.place(x=10, y=370)
ent1=Entry(root,textvariable=botr,width = 30)
ent1.place(x= 50,y=370)

lbl1= Label(root,text="BOT:")
lbl1.place(x=20, y=100)
labl2 = Text(root,height=15,width=25)
labl2.insert('end',"hello i am Panda!\n you can ask me \nanything about kiet")

labl2.place(x=80,y=100)

subt=Button(root,text="submit",bg="yellow",fg="black",command=inp)
subt.place(x=240,y=370)





root.mainloop()


