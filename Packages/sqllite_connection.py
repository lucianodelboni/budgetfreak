import sqlite3

try:
	conn = sqlite3.connect(r"..\Data\balances.db")
	
	cur = conn.cursor()

	print("Connection has been successfully established!")

	conn.commit()

except Error as e:

	print(e)