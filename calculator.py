import tkinter as tk
from tkinter.messagebox import *
import math as m
font = ('Areal',18,'bold')

# Important Function
def clrbtn():
    ex = textField.get()
    ex = ex[0:len(ex)-1]
    textField.delete(0,"end")
    textField.insert(0,ex)
    return  
    


def ACbtn():
    textField.delete(0,"end")
    return




def click_btn_function(event):
    print("btn clicked")
    b =event.widget
    text = b['text']
    print(text)
    if text == 'x':
        textField.insert('end',"*")
        return
    if text == '=':
        try:
            ex = textField.get()
            answer = eval(ex)
            textField.delete(0,"end")
            textField.insert(0,answer)
        except Exception as e:
            print("Error..",e)
            showerror("Error..",e)
        return
        

        
    
    textField.insert('end',text)
 
root = tk.Tk()
root.title("CALCULATOR")
root.geometry("450x400")
root.minsize(250,200)
root.maxsize(700,600)
headingLable = tk.Label(root, text= " MY CALCULATOR", font=font)
headingLable.pack(side="top")
# Text field
textField = tk.Entry(root,font=font,justify="center")
textField.pack(side="top",pady=10,fill="x",padx=10)
# Frame
buttonFrame = tk.Frame(root)
buttonFrame.pack(side="top")
# Adding Button
temp = 1
for i in range(0,3):
    for j in range(0,3):
        btn = tk.Button(buttonFrame,text=str(temp),font=font,width=6,relief="ridge",activebackground="gray",activeforeground="white")
        btn.grid(row=i,column=j,padx=5,pady=5)
        temp = temp+1
        btn.bind('<Button-1>',click_btn_function)


zerobtn = tk.Button(buttonFrame,text='0',font=font,width=6,relief="ridge",activebackground="gray",activeforeground="white")
zerobtn.grid(row=3,column=0,padx=5,pady=5)

dotbtn = tk.Button(buttonFrame,text='.',font=font,width=6,relief="ridge",activebackground="gray",activeforeground="white")
dotbtn.grid(row=3,column=1,padx=5,pady=5)

equalbtn = tk.Button(buttonFrame,text='=',font=font,width=6,relief="ridge",activebackground="gray",activeforeground="white")
equalbtn.grid(row=3,column=2,padx=5,pady=5)

plusbtn = tk.Button(buttonFrame,text='+',font=font,width=6,relief="ridge",activebackground="gray",activeforeground="white")
plusbtn.grid(row=0,column=3,padx=5,pady=5)


minusbtn = tk.Button(buttonFrame,text='-',font=font,width=6,relief="ridge",activebackground="gray",activeforeground="white")
minusbtn.grid(row=1,column=3,padx=5,pady=5)

multyplybtn = tk.Button(buttonFrame,text='x',font=font,width=6,relief="ridge",activebackground="gray",activeforeground="white")
multyplybtn.grid(row=2,column=3,padx=5,pady=5)

dividebtn = tk.Button(buttonFrame,text='/',font=font,width=6,relief="ridge",activebackground="gray",activeforeground="white")
dividebtn.grid(row=3,column=3,padx=5,pady=5)


ACbtn = tk.Button(buttonFrame,text='AC',font=font,width=6,relief="ridge",activebackground="gray",activeforeground="white",command=ACbtn)
ACbtn.grid(row=4,column=0,padx=5,pady=5)

percntbtn = tk.Button(buttonFrame,text='%',font=font,width=6,relief="ridge",activebackground="gray",activeforeground="white")
percntbtn.grid(row=4,column=1,padx=5,pady=5)

zrbtn = tk.Button(buttonFrame,text='00',font=font,width=6,relief="ridge",activebackground="gray",activeforeground="white")
zrbtn.grid(row=4,column=2,padx=5,pady=5)

clrbtn = tk.Button(buttonFrame,text="⌫",font=font,width=6,relief="ridge",activebackground="gray",activeforeground="white",command=clrbtn)
clrbtn.grid(row=4,column=3,padx=5,pady=5)       

 # Binding all buttons
plusbtn.bind('<Button-1>',click_btn_function)    
minusbtn.bind('<Button-1>',click_btn_function)    
multyplybtn.bind('<Button-1>',click_btn_function)    
dividebtn.bind('<Button-1>',click_btn_function)    
equalbtn.bind('<Button-1>',click_btn_function)    
    
    
zerobtn.bind('<Button-1>',click_btn_function)    
    
zrbtn.bind('<Button-1>',click_btn_function)    
percntbtn.bind('<Button-1>',click_btn_function)    
dotbtn.bind('<Button-1>',click_btn_function)
def enterClick(event):
    print("hi")
    
    event.widget = equalbtn
    click_btn_function(event)

root.bind('<Return>',enterClick)


## For scientific Calculator

scFrame = tk.Frame(root)
sqrtbtn = tk.Button(scFrame,text='√',font=font,width=6,relief="ridge",activebackground="gray",activeforeground="white")
sqrtbtn.grid(row=0,column=0,padx=5,pady=5)

powbtn = tk.Button(scFrame,text='^',font=font,width=6,relief="ridge",activebackground="gray",activeforeground="white")
powbtn.grid(row=0,column=1,padx=5,pady=5)

radbtn = tk.Button(scFrame,text='rad',font=font,width=6,relief="ridge",activebackground="gray",activeforeground="white")
radbtn.grid(row=0,column=2,padx=5,pady=5)

factbtn = tk.Button(scFrame,text='!',font=font,width=6,relief="ridge",activebackground="gray",activeforeground="white")
factbtn.grid(row=0,column=3,padx=5,pady=5)

degbtn = tk.Button(scFrame,text='deg',font=font,width=6,relief="ridge",activebackground="gray",activeforeground="white")
degbtn.grid(row=1,column=0,padx=5,pady=5)

sinbtn = tk.Button(scFrame,text='sinθ',font=font,width=6,relief="ridge",activebackground="gray",activeforeground="white")
sinbtn.grid(row=1,column=1,padx=5,pady=5)

cosbtn = tk.Button(scFrame,text='cosθ',font=font,width=6,relief="ridge",activebackground="gray",activeforeground="white")
cosbtn.grid(row=1,column=2,padx=5,pady=5)

tanbtn = tk.Button(scFrame,text='tanθ',font=font,width=6,relief="ridge",activebackground="gray",activeforeground="white")
tanbtn.grid(row=1,column=3,padx=5,pady=5)
# Scientific function

normalcalc = True
# function for sc excution

def calculate_sc(event):
    print("click..")
    btn = event.widget
    text = btn["text"]
    print(text)
    answer = ''
    ex = textField.get()
    if text == "deg":
        print("Calulate degree")
        answer = str(m.degrees(float(ex)))
    elif text == "rad":
        print("Radian")
        answer = str(m.radians(float(ex)))  
    elif text == "!":
        print("Cal factorail")
        answer = str(m.factorial(int(ex)))

    elif text == "√":
        print("Cal Squareroot")
        answer = m.sqrt(int(ex))

    elif text == "^":
        print("Cal Power")
        base,paw=ex.split(",")
        print(base)
        print(paw)

        answer = m.pow(int(base),int(paw))

    elif text == "sinθ":
        print("Cal sinθ")
        answer = str(m.sin(m.radians(int(ex))))             

    elif text == "cosθ":
        print("Cal Cosθ")
        answer = str(m.cos(m.radians(int(ex))))
    elif text == "tanθ":
        print("Cal tanθ")    
        answer = str(m.tan(m.radians(int(ex))))
    textField.delete(0,"end")
    textField.insert(0,answer)

    
    
    
def sc_click():
    global normalcalc
    if normalcalc:
        #show Sc
        buttonFrame.pack_forget()
        #add sc frame
        scFrame.pack(side="top")
        buttonFrame.pack(side="top")
        # increase sc width

        root.geometry("450x550")

        print("Show sc")
        normalcalc = False
    else:
        print("Show normal")  
        scFrame.pack_forget()
        root.geometry("450x400")
        #show normal
        normalcalc = True  
    

#end Function

menubar = tk.Menu(root)

fontmenu = ('',13)
mode = tk.Menu(menubar,font=fontmenu, tearoff=0)

mode.add_checkbutton(label="Scientific Calculator",command=sc_click)

menubar.add_cascade(label="Mode",menu=mode)
root.config(menu=menubar)
# bind sc button
sqrtbtn.bind("<Button-1>",calculate_sc)
radbtn.bind("<Button-1>",calculate_sc)
powbtn.bind("<Button-1>",calculate_sc)
factbtn.bind("<Button-1>",calculate_sc)
sinbtn.bind("<Button-1>",calculate_sc)
cosbtn.bind("<Button-1>",calculate_sc)
tanbtn.bind("<Button-1>",calculate_sc)
degbtn.bind("<Button-1>",calculate_sc)
root.mainloop()