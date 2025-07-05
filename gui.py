import tkinter as tk
from tkinter import messagebox
from customer import All_Customer
from data import load_customers, save_customers

customers = load_customers()

def add_customer():
    name = name_entry.get()
    lname = lname_entry.get()
    money = money_entry.get()

    if not name or not lname or not money.isdigit():
        messagebox.showerror("Error", "Enter valid name, last name, and money!")
        return

    cust = All_Customer(name, lname, int(money))
    customers.append(cust)
    save_customers(customers)
    messagebox.showinfo("Success", f"Customer {name} {lname} added!")
    update_list()

def update_list():
    listbox.delete(0, tk.END)
    for c in customers:
        listbox.insert(tk.END, f"{c.name} {c.l_name} | ${c.money}")

root = tk.Tk()
root.title("Customer Manager")
root.geometry("400x400")

tk.Label(root, text="First Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Last Name").pack()
lname_entry = tk.Entry(root)
lname_entry.pack()

tk.Label(root, text="Money").pack()
money_entry = tk.Entry(root)
money_entry.pack()

tk.Button(root, text="Add Customer", command=add_customer).pack(pady=10)

tk.Label(root, text="Customer List").pack()
listbox = tk.Listbox(root, width=40)
listbox.pack()

update_list()
root.mainloop()
