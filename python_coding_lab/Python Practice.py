
#Employee management System
# class Employee:
#     def __init__(self, emp_id, name, salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.salary = salary

#     def display(self):
#         print(self.emp_id, self.name, self.salary)

# employees = []

# employees.append(Employee(1, 'Jhon', 50000))
# employees.append(Employee(2, 'Sham', 40000))

# for emp in employees:
#     emp.display()

#Bank Account

Class BankAccount:
    def __int__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def winthdraw(self, amount):
        if amount <= balance:
            self.balance -= amount
    def show_balance(self):
        print(self.balance)

account = BankAccount()
account.deposit(30000)
account.winthdraw(5000)
account.show_balance()    


