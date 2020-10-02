from tkinter import *
import time
from tkinter import ttk
import datetime

msg1 = "Welcome to ShowBot's Hotel..."
msg2 = "Powered by ShowBot.."
msg3 = "Make an Order.."
msg4 = "Thank you for your Order.."
msg5 = "Thanks for Coming..."
msg6 = "Waiting for U R Nxt Visit..."
text1 = ""
n = 0

#=========================Calculator Functions=======================

def btn(numbers):
    global  operator
    operator = operator + str(numbers)
    txt_input.set(operator)

def Clear():
    global operator
    operator = ''
    txt_input.set('')
    Display.insert(0,'Start Calculating...')

def Equal():
    global operator
    sumup = float(eval(operator))
    txt_input.set(sumup)
    operator = ''

#===================================Total Function=================================
def TotalResult():
    #================Cost of Meal======================
    varme1 = Mealdicator.get()
    varme2 = Meal1.get()
    if varme1 =='Fried Rice          '+"\U0001f371":
       varme3 = (varme2*1.8)
       Cost.set(varme3)
    elif varme1 =='Curd Rice           '+"\U0001f35C":
        varme3 = (varme2*3.7)
        Cost.set(varme3)
    elif varme1 == 'Chinese Noodles     '+"\U0001f35C":
        varme3 = (varme2*1.2)
        Cost.set(varme3)
    elif varme1 == 'Chicken 65           '+"\U0001f357":
        varme3 = (varme2*0.9)
        Cost.set(varme3)
    elif varme1 == 'Burger              ' + "\U0001f354":
        varme3 = (varme2*1.01)
        Cost.set(varme3)
    else:
        varme3 = (varme2 * 0.0)
        Cost.set(varme3)

    # ================Cost of Drink======================
    vardi1 = Drinkdicator.get()
    vardi2 = Drink1.get()
    if vardi1 == 'Bottled Water       '+"\U0001F37E":
        vardi3 = (vardi2 * 1.8)
        Drinks.set(vardi3)
    elif vardi1 == 'Coca Cola           '+"\U0001F377":
        vardi3 = (vardi2 * 3.7)
        Drinks.set(vardi3)
    elif vardi1 == 'Pepsi               '+"\U0001F942":
        vardi3 = (vardi2 * 1.2)
        Drinks.set(vardi3)
    elif vardi1 == '7 up                '+"\U0001F37A":
        vardi3 = (vardi2 * 0.9)
        Drinks.set(vardi3)
    elif vardi1 == 'Thumps up           '+"\U0001F964":
        vardi3 = (vardi2 * 1.01)
        Drinks.set(vardi3)
    else:
        vardi3 = (vardi2 * 0.0)
        Drinks.set(vardi3)

    #======================Delivery Cost========================================
    num1 = float(Cost.get())
    num2 = float(Drinks.get())
    Delivery = (num1 + num2) * 0.2

    #======================Cost of Room==========================================
    room = v.get()
    null = 0.0

    rvip = 10.0 #============Cost of VIP room======================================
    rvip1 = Delivery/(10*0.5) #====VIP room with Delivery cost===================

    rnormal = 5.0 #=========Cost of Normal room====================================
    rnormal1 = Delivery/(5*2.5) #======Normal room with Delivery cost============

    if room == 1:
        if chkb1.get() == 1:
            Service_Charge.set(rvip1)
            RoomCost.set(10.0)
            DevCost.set(Delivery)
        else:
            Service_Charge.set(null)
            DevCost.set(null)
            RoomCost.set(10.0)
    elif room == 2:
        if chkb1.get() == 1:
            Service_Charge.set(rnormal)
            RoomCost.set(5.0)
            DevCost.set(Delivery)
        else:
            Service_Charge.set(null)
            DevCost.set(null)
            RoomCost.set(5.0)
    elif room == 3:
        if chkb1.get() == 1:
            Service_Charge.set(null)
            RoomCost.set(null)
            DevCost.set(null)
        else:
            Service_Charge.set(null)
            DevCost.set(null)
            RoomCost.set(null)

    #==================Total Result=========================
    num3 = float(DevCost.get())
    num4 = float(RoomCost.get())
    num5 = float(Service_Charge.get())

    MyTotal = num1+num2+num3+num4+num5
    Total.set(MyTotal)
    FinalTotal = "Total = $"+'\U0001F4C3',MyTotal

    num6 = Total.get()
    Display.delete(0,END)
    Display.insert(0,FinalTotal)

    if num6 == '0.0':
        Display.delete(0,END)
        Display.insert(0,'Make an order '+'\U0001F4DD')


def Convert():
    var2 = indicator.get()
    var3 = var1.get()
    if var2 == 'India':
        Display.delete(0,END)
        var4 = ('Yuan',(var3*6.88))
        Display.insert(0,var4)
    elif var2 == 'France':
        Display.delete(0,END)
        var4 = ('Euro',(var3*0.81))
        Display.insert(0,var4)
    elif var2 == 'Ghana':
        Display.delete(0,END)
        var4 = ('Cedi',(var3*4.88))
        Display.insert(0,var4)
    elif var2 == 'Mexico':
        Display.delete(0,END)
        var4 = ('MXN',(var3*18.90))
        Display.insert(0,var4)
    elif var2 == 'Nigeria':
        Display.delete(0,END)
        var4 = ('Naira',(var3*361.01))
        Display.insert(0,var4)
    elif var2 == 'USA':
        Display.delete(0,END)
        var4 = ('USD',(var3*1.00))
        Display.insert(0,var4)
    else:
        Display.delete(0,END)
        Display.insert(0,'Error:Select a country!')

    #============================Reset Button======================

'''def scroll():
    for line in Line:
        for c in line:
            print(c, end='')
            sys.stdout.flush()
            sleep(0.1)
        print('')'''

def Hotel():
    Display.delete(0,END)
    Display.insert(0,'Hotel Management Sys.')

def Powered():
    Display.delete(0, END)
    Display.insert(0, 'Powered by ShowBot...')

def Reset():
    Display.delete(0, END)
    Display.insert(0, 'System Resetting.. '+"\U0001f50D")
    Display.after(2000,Hotel)
    Display.after(4000,Powered)
    Display.after(6000,Rest)

def Rest():
    Clear()
    Display.delete(0,END)
    Display.insert(0,'Hello! Welcome')
    Mealdicator.set(value='Delicious Meal')
    Drinkdicator.set(value='Fresh Drink')
    indicator.set(value='Choose a Country')
    txtQtyofMeal.delete(0,END)
    txtQtyofMeal.insert(0,0)
    txtQtyofDrink.delete(0,END)
    txtQtyofDrink.insert(0,0)
    txtAmount.delete(0,END)
    txtAmount.insert(0,0)
    RoomCost.set(0.0)
    Total.set(0.0)
    Service_Charge.set(0.0)
    Drinks.set(0.0)
    Cost.set(0.0)
    chkb1.set(0)
    v.set(3)
    DevCost.set(0.0)

#==========================Clear Button========================
def ClearScreen():
    Display.delete(0,END)
    RoomCost.set('')
    Total.set('')
    Service_Charge.set('')
    Drinks.set('')
    Cost.set('')
    DevCost.set('')

#===============================Exit===========================
def Stop():
    root.destroy()

def Exit():
    Display.delete(0,END)
    Display.insert(0,'Thanks for Coming  '+'\U0001F91D')
    Display.after(3000,Stop)

#============================Time================================
def tick():
    d = datetime.datetime.now()
    Today = '{:%B %d, %Y}'.format(d)

    mytime = time.strftime('%I:%M:%S%p')
    lblInfo.config(text=('\U0001F570 '+mytime+'\U0001F4C5'+Today+"\U0001f514"))
    lblInfo.after(200,tick)

#=================================Scroll Function===============
def display():
    global text1, n, msg1
    for t in range(len(msg1)):
        for k in range(t):
            text1 += ' '
        for g in range(len(msg1) - t):
            text1 += msg1[g]
        text1 = text1.strip()
        f2.update()
        f2.after(200)
        text1 = text1.strip()
        scroll_text.set('')
        scroll_text.set(text1)
        text1 = ''
    scroll_text.set('')
    txtscroll.after(200,display)

root = Tk()
root.geometry('1600x800+0+0')
root.title("ShowBot's Hotel Management System")

#================================Window's Partition==============================
Tops = Frame(root, width=1600, height=100, bg='blue',relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

f3 = Frame(root, width=35, height=700, relief=SUNKEN)
f3.pack(side=LEFT)

f4 = Frame(root, width=100, height=700, relief=SUNKEN)
f4.pack(side=LEFT)

#===================================Main Screen==================================

txt_input = StringVar(value= "\U0001f637"+"\U0001f337" +"\U0001f64f" + "WELCOME" + "\U0001f64f"+"\U0001f337") # welcome note along with emoji

Display = Entry(Tops, font=('arial',97,'bold'),fg='white',bd=50,bg='blue',justify='right',textvariable=txt_input)
Display.grid(columnspan=4)

#==================================Date and time=================================

lblInfo = Label(f2,font=('arial',19,'bold'),fg='dark blue',bd=5,anchor=W)
lblInfo.grid(row=1,column=0,columnspan=4)
tick()

#==================================Row 1========================================
operator=''

btn7 = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='7',command=lambda:btn(7)).grid(row=2,column=0)
btn8 = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='8',command=lambda:btn(8)).grid(row=2,column=1)
btn9 = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='9',command=lambda:btn(9)).grid(row=2,column=2)
btnC = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='C',bg='green', command=Clear).grid(row=2,column=3)

#==================================Row 2========================================

btn4 = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='4',command=lambda:btn(4)).grid(row=3,column=0)
btn5 = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='5',command=lambda:btn(5)).grid(row=3,column=1)
btn6 = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='6',command=lambda:btn(6)).grid(row=3,column=2)
btnplus = Button(f2,padx=18,pady=5,bd=8,font=('arial',30,'bold'),text='+',bg='orange',command=lambda:btn('+')
                 ).grid(row=3,column=3)

#==================================Row 3========================================

btn1 = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='1',command=lambda:btn(1)).grid(row=4,column=0)
btn2 = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='2',command=lambda:btn(2)).grid(row=4,column=1)
btn3 = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='3',command=lambda:btn(3)).grid(row=4,column=2)
btnminus = Button(f2,padx=23,pady=5,bd=8,font=('arial',30,'bold'),text='-',bg='orange',command=lambda:btn('-')
                  ).grid(row=4,column=3)

#==================================Row 4========================================

btn0 = Button(f2,padx=15,pady=5,bd=8,font=('arial',30,'bold'),text='0',command=lambda:btn(0)).grid(row=5,column=0)
btndot = Button(f2,padx=21,pady=5,bd=8,font=('arial',30,'bold'),text='.',bg='orange',command=lambda:btn('.')
                ).grid(row=5,column=1)
btndivision = Button(f2,padx=20,pady=5,bd=8,font=('arial',30,'bold'),text='/',bg='orange',command=lambda:btn('/')
                     ).grid(row=5,column=2)
btnmultiply = Button(f2,padx=19,pady=5,bd=8,font=('arial',30,'bold'),text='x',bg='orange',command=lambda:btn('*')
                     ).grid(row=5,column=3)

#==================================Row 5========================================

btnequals = Button(f2,padx=64,pady=2,bd=8,font=('arial',30,'bold'),text='=',bg='green',command=Equal
                   ).grid(row=6,column=0,columnspan=2)
btnopenbracket = Button(f2,padx=19,pady=2,bd=8,font=('arial',30,'bold'),text='(',bg='orange',command=lambda:btn('(')
                        ).grid(row=6,column=2)
btnclosebracket = Button(f2,padx=23,pady=2,bd=8,font=('arial',30,'bold'),text=')',bg='orange',command=lambda:btn(')')
                         ).grid(row=6,column=3)

#================================Choose Meal===================================
Meal1 = IntVar()
Mealdicator = StringVar(value='Delicious Meals          '+ "\U0001f4DC")

lblMeal = Label(f1,font=('arial',16,'bold'),text='Choose Meal',bd=10,anchor=W)
lblMeal.grid(row=0,column=0)
txtMeal = ttk.Combobox(f1,font=('arial',16,'bold'),textvariable=Mealdicator)
txtMeal['values']=('Fried Rice          '+"\U0001f371","Curd Rice           "+"\U0001f35C","Chinese Noodles     "+"\U0001f35C","Chicken 65           "+"\U0001f357","Burger              " + "\U0001f354")
txtMeal.grid(row=0,column=1)

lblQtofMeal = Label(f1,font=('arial',16,'bold'),text='Qty. of Meal',bd=10,anchor=W)
lblQtofMeal.grid(row=1,column=0)
txtQtyofMeal = Entry(f1,font=('arial',16,'bold'),textvariable=Meal1,bd=10,insertwidth=4,bg='white',justify='right')
txtQtyofMeal.grid(row=1,column=1)

#================================Choose Drinks====================================
Drink1 = IntVar()
Drinkdicator = StringVar(value='Fresh Drinks              ' +"\U0001f4C3")

lblDrink = Label(f1,font=('arial',16,'bold'),text='Choose Drink',bd=10,anchor=W)
lblDrink.grid(row=2,column=0)
txtDrink = ttk.Combobox(f1,font=('arial',16,'bold'),textvariable=Drinkdicator)
txtDrink['values']=('Bottled Water       '+"\U0001F37E",'Coca Cola           '+"\U0001F377",'Pepsi               '+"\U0001F942",'7 up                '+"\U0001F37A",'Thumps up           '+"\U0001F964")
txtDrink.grid(row=2,column=1)

lblQtofDrink = Label(f1,font=('arial',16,'bold'),text='Qty. of Drink',bd=10,anchor=W)
lblQtofDrink.grid(row=3,column=0)
txtQtyofDrink = Entry(f1,font=('arial',16,'bold'),textvariable=Drink1,bd=10,insertwidth=4,bg='white',justify='right')
txtQtyofDrink.grid(row=3,column=1)

#==============================Order Delivery=====================================
chkb1 = IntVar()

lblHomeDev = Label(f1,font=('arial',16,'bold'),text='Order Delivery  '+'\U0001F424',bd=10,anchor=W)
lblHomeDev.grid(row=4,column=0)
check1 = Checkbutton(f1,text='Yes  '+'\U0001F511',variable=chkb1,font=('arial',16,'bold'))
check1.grid(row=4,column=1)

#==========================Book a Room============================================
v = IntVar()
v.set(3)

lblRoom = Label(f1,font=('arial',16,'bold'),text='Book a Room  '+'\U0001f6CC'+"\U0001f4BA",bd=10, anchor=W)
lblRoom.grid(row=5,column=0)
MyRadios = Radiobutton(f1,text='VIP',font=('arial',16,'bold'),variable=v,value=1)
MyRadios.grid(row=5,column=1,sticky=W)
MyRadios = Radiobutton(f1,text='Normal',font=('arial',16,'bold'),variable=v,value=2)
MyRadios.grid(row=5,column=1)
MyRadios = Radiobutton(f1,text='No',font=('arial',16,'bold'),variable=v,value=3)
MyRadios.grid(row=5,column=1,sticky=E)

#================================Cost Display Screens============================
Cost = StringVar()
lblMeal1 = Label(f1, font=('arial',16,'bold'),text='Cost of Meal  '+'\U0001F4B2',bd=16,anchor=W)
lblMeal1.grid(row=0,column=2)
txtMeal1 = Entry(f1,font=('arial',16,'bold'),textvariable=Cost,fg='white',bd=10,insertwidth=4,bg='blue',
                 justify='right')
txtMeal1.grid(row=0,column=3)

Drinks = StringVar()
lblDrink1 = Label(f1, font=('arial',16,'bold'),text='Cost of Drink  '+'\U0001F4B2',bd=16,anchor=W)
lblDrink1.grid(row=1,column=2)
txtDrink1 = Entry(f1,font=('arial',16,'bold'),textvariable=Drinks,fg='white',bd=10,insertwidth=4,bg='blue',
                  justify='right')
txtDrink1.grid(row=1,column=3)

DevCost = StringVar()
lblDev = Label(f1, font=('arial',16,'bold'),text='Delivery Cost  '+'\U0001F4B2',bd=16,anchor=W)
lblDev.grid(row=2,column=2)
txtDev = Entry(f1,font=('arial',16,'bold'),textvariable=DevCost,fg='white',bd=10,insertwidth=4,bg='blue',
               justify='right')
txtDev.grid(row=2,column=3)

RoomCost = StringVar()
lblRoom = Label(f1, font=('arial',16,'bold'),text='Cost of Room  '+'\U0001F4B2',bd=16,anchor=W)
lblRoom.grid(row=3,column=2)
txtRoom = Entry(f1,font=('arial',16,'bold'),textvariable=RoomCost,fg='white',bd=10,insertwidth=4,bg='blue',
                justify='right')
txtRoom.grid(row=3,column=3)

Service_Charge = StringVar()
lblService = Label(f1, font=('arial',16,'bold'),text='Service Fee  '+'\U0001F4B2',bd=16,anchor=W)
lblService.grid(row=4,column=2)
txtService = Entry(f1,font=('arial',16,'bold'),textvariable=Service_Charge,fg='white',bd=10,insertwidth=4,bg='blue',
                   justify='right')
txtService.grid(row=4,column=3)

Total = StringVar()
lblTotal = Label(f1, font=('arial',16,'bold'),text='Total Cost  '+'\U0001F4B0',bd=16,anchor=W)
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('arial',16,'bold'),textvariable=Total,fg='white',bd=10,insertwidth=4,bg='blue',
                 justify='right')
txtTotal.grid(row=5,column=3)

#====================================Currency Converter===================================
var1 = IntVar()
indicator = StringVar(value='Choose a Country')

lblCunCon = Label(f1,font=('arial',16,'bold italic'),text='-----------------------------------Currency Converter---------------------------------------',
                  bd=20,anchor=W)
lblCunCon.grid(row=6,column=0,columnspan=4)

lblCountry = Label(f1,font=('arial',16,'bold'),text='\U0001F4CC  '+'Nationality',bd=20,anchor=W)
lblCountry.grid(row=7,column=0)
txtCountry = ttk.Combobox(f1,font=('arial',16,'bold'),textvariable=indicator)
txtCountry['values'] = ('India','France','Ghana','Mexico','Nigeria','USA')
txtCountry.grid(row=7,column=1)

lblAmount = Label(f1,font=('arial',16,'bold'),text='Amount($)',bd=20,anchor=W)
lblAmount.grid(row=7,column=2)
txtAmount = Entry(f1,font=('arial',16,'bold'),textvariable=var1,bd=10,insertwidth=4,bg='white',justify='right')
txtAmount.grid(row=7,column=3)

#=======================================Control Buttons=========================================
btnConvert = Button(f1,padx=10,pady=4,bd=16,fg='white',font=('arial',16,'bold'),width=10,text='Convert',bg='orange',
                    command=Convert)
btnConvert.grid(row=8,column=2)

btnTotal = Button(f4,padx=10,pady=8,bd=16,fg='white',font=('arial',16,'bold'),width=10,text='Total     '+'\U0001F4B5',bg='orange',
                  command=TotalResult)
btnTotal.grid(row=0,column=0)

btnScreen = Button(f4,padx=10,pady=8,bd=16,fg='white',font=('arial',16,'bold'),width=10,text='Clear',bg='blue',
                   command=ClearScreen)
btnScreen.grid(row=1,column=0)

btnReset = Button(f4,padx=10,pady=8,bd=16,fg='white',font=('arial',16,'bold'),width=10,text='Reset',bg='green',
                  command=Reset)
btnReset.grid(row=2,column=0)

btnExit = Button(f4,padx=10,pady=8,bd=16,fg='white',font=('arial',16,'bold'),width=10,text='Exit',bg='red',
                 command=Exit)
btnExit.grid(row=3,column=0)

#========================================Logo=======================================================
# photo = PhotoImage(file='Screenshot (49).png')
# myphoto = Label(f1,image=photo)
# myphoto.grid(row=8,column=0)

#=====================================Scrollable Text===============================================
scroll_text = StringVar()
txtscroll = Entry(f2, textvariable=scroll_text, font=('arial',16,'bold'), fg='white', bd=10, bg='blue', width=32)
txtscroll.grid(row=0, column=0, columnspan=4)
display()

root.mainloop()