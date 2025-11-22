from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from pymongo import *


root=Tk()
root.title("Doubt App")
root.geometry("500x400+400+70")
f=("Calibri",33,"bold")
root.config(bg="orange")

def save():
	con=None
	try:
		con=MongoClient("localhost",27017)
		db=con["doubt_23july24"]
		coll=db["Students"]

		name=ent_name.get()
		phone=int(ent_phone.get())
		doubt=st_doubt.get(1.0,END)
		
		record={"name":name,"phone":phone,"doubt":doubt}
		coll.insert_one(record)	
		showinfo("Details saved","we will get back to you")
		ent_name.delete(0,END)
		ent_phone.delete(0,END)
		st_doubt.delete(1.0,END)
		
		ent_name.focus()
	except Exception as e:
		print("issue",e)
	finally:
		if con is not None:
			con.close()

lab_header=Label(root,text="Welcome to Doubt App",font=f,bg="purple")
lab_name=Label(root,text="Enter name",font=f,bg="orange")
ent_name=Entry(root,font=f)
lab_phone=Label(root,text="phone number",font=f,bg="orange")
ent_phone=Entry(root,font=f)
lab_doubt=Label(root,text="Ask your Doubt",font=f,bg="orange")
ent_doubt=Entry(root,font=f)
st_doubt=ScrolledText(root,font=f,width=20,height=5)
btn_submit=Button(root,text="Submit",font=f,command=save,bg="green")

lab_header.place(x=500, y=20)
lab_name.place(x=400, y=100)
ent_name.place(x=650, y=100) 
lab_phone.place(x=360, y=200)
ent_phone.place(x=650, y=200) 
lab_doubt.place(x=350, y=300)
st_doubt.place(x=650, y=300)  
btn_submit.place(x=630, y=690)

root.mainloop()