"""main customers adding there"""
import uuid 
main_cust = { 
}
class All_Customer:
    __number = 0
    def __init__(self,name,l_name, age):
        self.name = name 
        self.l_name = l_name
        self.age = age
        self.id = uuid.uuid4()
    def get_info(self):
        print(f"Name -- {self.name}\n"
              f"Last Name -- {self.l_name}\n"
              f"Age -- {self.age}\n"
              f"Id --- {self.id}")
    @classmethod
    def number_cust(cls):
        cls.__number += 1
        return cls.__number

customer = All_Customer("gojo", 'satoru',29)
customer.get_info()
print(customer.number_cust())
# def get_name():
#     for customer in main_cust.keys():
#         return customer
# print(get_name())
