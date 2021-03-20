import tkinter as tk
import requests
import datetime



form1_height = 400
form1_width = 300

root = tk.Tk()

def create_balance():
	root.withdraw()

	#creating a new window to enter basic parameters of the new balance
	new_balance = tk.Toplevel()
	var = ''

	new_canvas = tk.Canvas(new_balance, height=form1_height, width=form1_width)
	new_canvas.pack()

	new_label = tk.Label(new_balance, text="Fill out the form below to create a new balance sheet:")
	new_label.place(relx=0.02, rely=0.02)

	new_frame = tk.Frame(new_balance)
	new_frame.place(relx=0.05, rely=0.1, relwidth=0.95, relheight=0.9)

	new_title_label = tk.Label(new_frame, text="Title:")
	new_title_label.place(rely=0)
	new_title_entry = tk.Entry(new_frame)
	new_title_entry.place(rely=0.06, relwidth=0.95)

	new_type_label = tk.Label(new_frame, text="Type:")
	new_type_label.place(rely=0.15)
	new_type1 = tk.Radiobutton(new_frame, text="Weekly", value="weekly", variable=str(var))
	new_type1.place(rely=0.21)
	new_type2 = tk.Radiobutton(new_frame, text="Bi-weekly", value="biweekly", variable=str(var))
	new_type2.place(rely=0.26)
	new_type3 = tk.Radiobutton(new_frame, text="Monthly", value="monthly", variable=str(var))
	new_type3.place(rely=0.32)
	new_type3.invoke()

	new_description_label = tk.Label(new_frame, text="Description:")
	new_description_label.place(rely=0.42)
	new_description_entry = tk.Text(new_frame)
	new_description_entry.place(rely=0.48, relwidth=0.95, relheight=0.25)

	new_button = tk.Button(new_frame, text="Create", command= lambda: modify_db('add'))
	new_button.place(relx= 0.4, rely=0.8)

	#adicionar funcionalidade para pedir dados em nova tela, criar e abrir este balanço.
	

def modify_db(action):
	if action == "add":
		time_stamp = datetime.datetime.now()
		newwindow = tk.Toplevel()
		another = tk.Canvas(newwindow, height=form1_height, width=form1_width)
		another.pack()
		anotherentry = tk.Label(another, text=time_stamp)
		anotherentry.pack()


		pass
	elif action == "update":
		pass
	elif action == "delete":
		pass
	else:
		pass


def open_balance():
	print(data)
	pass
	#adicionar funcionalidade para abrir um balanço existente depois de mostrar uma lista dos existentes

def delete_balance():
	pass
	#adicionar funcionalidade para mostrar os balanços existentes e confirmar se quer mesmo deletar


canvas = tk.Canvas(root, height=form1_height, width=form1_width)
canvas.pack()

frame = tk.Frame(root)
frame.place(relx=0.2, rely=0.1, relwidth=0.8, relheight=0.8)

label_mainpage = tk.Label(frame, text='Create, open or delete a balance below:')
label_mainpage.place(rely=0)

create_button = tk.Button(frame,text='Create', command=create_balance, height=3, width=25)
create_button.place(rely=0.1)

open_button = tk.Button(frame,text='Open', command=open_balance, height=3, width=25)
open_button.place(rely=0.35)

delete_button = tk.Button(frame,text='Delete', command=delete_balance, height=3, width=25)
delete_button.place(rely=0.60)

root.mainloop()


'''
Infrastructure
app.py
images/images files (styling)
data/json files (storage)


Screens organization
welcome screen:
	- Create new balance
		- Name, type (weekly, bi-weekly, monthly), description
		- Button (create)
			- creates a registry in json file
			- opens interface without any data

	- Open existing balance
		- list balances
		- show open button
			- opens interface with data

	- Delete Balance
		- show available balances
			- confirm exclusion
'''