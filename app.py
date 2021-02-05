import tkinter as tk
import requests

form1_height = 400
form1_width = 300

root = tk.Tk()

canvas = tk.Canvas(root, height=form1_height, width=form1_width)
canvas.pack()

frame = tk.Frame(root)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label_mainpage = tk.Label(frame, text='Create, open or delete a balance below:')
label_mainpage.pack()

create_button = tk.Button(frame,text='Create', height=3, width=25)
create_button.pack()

open_button = tk.Button(frame,text='Open', height=3, width=25)
open_button.pack()

delete_button = tk.Button(frame,text='Delete', height=3, width=25)
delete_button.pack()

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