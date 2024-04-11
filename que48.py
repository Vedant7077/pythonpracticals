class person:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
class employee(person):
    def __init__(self,name,age,address,designation,company_name,salary):
        super().__init__(name,age,address)
        self.designation = designation
        self.company_name = company_name
        self.salary = salary
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)
        print("Designation:", self.designation)
        print("Company Name:", self.company_name)
        print("Salary:", self.salary)

emp = employee("Alice", 30, "123 Main St", "Manager", "ABC Inc.", 50000)
emp.display()