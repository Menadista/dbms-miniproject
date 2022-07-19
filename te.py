from tkinter import Tk, Canvas, Frame, Label, Entry, Button, W, E, Listbox, END

import psycopg2

root = Tk()
root.title("Zomato")


def save_new_customer(id, name, address, number, email, un, pw):
    conn = psycopg2.connect(dbname="zomato", user="postgres",
                            password="postgres", host="localhost", port="5432")
    cursor = conn.cursor()
    query = '''INSERT INTO customer(customer_id, complete_name, address, contact_number, email_address, username, 
    password) VALUES (%s, %s, %s, %s, %s, %s, %s) '''
    cursor.execute(query, (id, name, address, number, email, un, pw))
    print("successfully data inserted")
    cursor.execute('''select * from customer''')
    conn.commit()
    conn.close()


def update_customer(id, name, address, number, email, un, pw):
    conn = psycopg2.connect(dbname="zomato", user="postgres",
                            password="postgres", host="localhost", port="5432")
    cursor = conn.cursor()
    query = '''UPDATE customer SET complete_name= %s, address= %s, contact_number= %s, email_address= 
    %s, username= %s, password= %s where customer_id= %s '''
    cursor.execute(query, (name, address, number, email, un, pw, id))
    print("successfully Data Updated")
    conn.commit()
    cursor.execute('''select * from customer''')
    conn.close()
    # refresh with new customers


def search(order_id):
    conn = psycopg2.connect(dbname="zomato", user="postgres",
                            password="postgres", host="localhost", port="5432")
    cursor = conn.cursor()
    query = '''SELECT * FROM order_ where order_id= %s'''
    cursor.execute(query, order_id)

    row = cursor.fetchone()
    print(row)
    display_search_result(row)

    conn.commit()
    conn.close()


def display_search_result(row):
    listbox = Listbox(frame, width=20, height=1)
    listbox.grid(row=9, columnspan=4, sticky=W + E)
    listbox.insert(END, row)


def display_food_list():
    conn = psycopg2.connect(dbname="zomato", user="postgres",
                            password="postgres", host="localhost", port="5432")
    cursor = conn.cursor()
    query = '''SELECT food_name FROM food_list'''
    cursor.execute(query)

    row = cursor.fetchall()

    listbox = Listbox(frame, width=20, height=5)
    listbox.grid(row=10, columnspan=4, sticky=W + E)
    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()


# Canva
canvas = Canvas(root, height=600, width=600)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text="Add/Update a User")
label.grid(row=0, column=1)

# Name Input
label = Label(frame, text="Name")
label.grid(row=1, column=0)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1)
entry_name.focus()

# ID
label = Label(frame, text="ID")
label.grid(row=1, column=2)

entry_id = Entry(frame)
entry_id.grid(row=1, column=3)

# Number
label = Label(frame, text="Age")
label.grid(row=2, column=0)

entry_number = Entry(frame)
entry_number.grid(row=2, column=1)

# email
label = Label(frame, text="Email ID")
label.grid(row=2, column=2)

entry_email = Entry(frame)
entry_email.grid(row=2, column=3)

# Username
label = Label(frame, text="Username")
label.grid(row=2, column=4)

entry_username = Entry(frame)
entry_username.grid(row=2, column=5)

# Address
label = Label(frame, text="Address")
label.grid(row=3, column=0)

entry_address = Entry(frame)
entry_address.grid(row=3, column=1)

# Password
label = Label(frame, text="Password")
label.grid(row=3, column=2)

entry_password = Entry(frame, show="*")
entry_password.grid(row=3, column=3)

# Button
button = Button(frame, text="Add",
                command=lambda: save_new_customer(entry_id.get(), entry_name.get(), entry_address.get(),
                                                  entry_number.get(), entry_email.get(), entry_username.get(),
                                                  entry_password.get()))
button.grid(row=4, column=1, sticky=W + E)

button = Button(frame, text="Update",
                command=lambda: update_customer(entry_id.get(), entry_name.get(), entry_address.get(),
                                                entry_number.get(), entry_email.get(), entry_username.get(),
                                                entry_password.get()))
button.grid(row=4, column=2, sticky=W + E)

# Search
label = Label(frame, text="Search Data")
label.grid(row=5, column=1)

label = Label(frame, text="Search By ID")
label.grid(row=6, column=0)

id_search = Entry(frame)
id_search.grid(row=6, column=1)

button = Button(frame, text="Search", command=lambda: search(id_search.get()))
button.grid(row=6, column=2)

display_food_list()
root.mainloop()
