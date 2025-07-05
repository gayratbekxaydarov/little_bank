from customer import All_Customer
from data import load_customers, save_customers, find_customer, delete_customer

customers = load_customers()

c1 = All_Customer("Gojo", "Satoru", 100)
customers.append(c1)
save_customers(customers)

found = find_customer(customers, "Gojo Satoru")
if found:
    found.get_info()

deleted = delete_customer(customers, "Gojo Satoru")
if deleted:
    print("Customer deleted.")

for c in customers:
    c.get_info()
