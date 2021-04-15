# portable-fortnight
import requests
from tkinter import *
from tkinter import scrolledtext
import json
import sys
import tkinter.messagebox as tkMessageBox

def errormesg(msg):
    tkMessageBox.showinfo("Error", msg)
    
def convert():
    try:
        l3.config(text="")
        fromval=e1.get().upper()
        toval=e2.get().upper()
        am=e3.get()
        #Validation
        if fromval in options and fromval in options:
            r=requests.get("https://free.currencyconverterapi.com/api/v5/convert?q="+fromval+"_"+toval+"&compact=y")
            if r.status_code != 200:
                errormesg("Currency Converter API Server seems to be down. Try again later!")
                return
            #print(r.json())
            #print(r.status_code)
            jsonf=r.json()
            am1=jsonf[fromval+"_"+toval]["val"]
            if am=="":
                dis=str(1)+" "+str(fromval)+" = "+str("{0:.2f}".format(am1))+" "+str(toval)
            else:
                ans="{0:.2f}".format(float(am1)*float(am))
                #print(ans)
                dis=str(am)+" "+str(fromval)+" = "+str(ans)+" "+str(toval)
            l3.config(text=dis)

        else:
            errormesg("An Error Occured, Please check the data entered and try again")
            return
        
    except:
        errormesg("An Error Occured, Please check the data entered and try again")


def help():
    def close1():
        w2.destroy()
    w2=Tk()
    w2.title("Currencies available")
    txt=scrolledtext.ScrolledText(w2,width=40,height=10)
    txt.grid(column=0,row=0)
    txt.insert(INSERT,hstr)
    b4=Button(w2,text="OK",command=close1)
    b4.grid(column=0,row=1)
    w2.mainloop()

    
#Main
options=[]

try:
    r=requests.get("https://free.currencyconverterapi.com/api/v5/currencies")
    if r.status_code != 200:
        errormesg("Currency Converter API Server seems to be down. Try again later!")
    options=list(r.json()["results"].keys())
    options.sort()
    hstr=""
    for i in options:
        hstr=hstr+"\n"+i+"-"+r.json()["results"][i]["currencyName"]
    #print(hstr)
except:
    errormesg("Currency Converter API Server seems to be down. Try again later!")
    
w=Tk()
w.title("Currency Converter")


l1=Label(w,text="From")
l1.grid(column=0,row=0)


e1=Entry(w)
e1.grid(column=1,row=0)

l2=Label(w,text="To")
l2.grid(column=0,row=1)

e2=Entry(w)
e2.grid(column=1,row=1)

l3=Label(w,text="Amount")
l3.grid(column=0,row=2)

e3=Entry(w)
e3.grid(column=1,row=2)



b1=Button(w,text="Convert",command=convert)
b1.grid(column=1,row=3)

b1=Button(w,text="Help",command=help)
b1.grid(column=0,row=3)

b1=Button(w,text="Exit",command=exit)
b1.grid(column=2,row=3)


l3=Label(w,bg="#98fb98")
l3.grid(column=1,row=4)



w.mainloop()
