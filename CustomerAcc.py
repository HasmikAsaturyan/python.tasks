class Customer_Account:
    def __init__(self,customer_id, customer_name, account_balance):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.account_balance = account_balance
        self.transaclog = TransactionLog()

    def deposit(self,amount):
        self.account_balance += amount
        self.transaclog.log_transaction(f"+{amount}")

    def withdraw(self,amount):
        self.account_balance -= amount
        self.transaclog.log_transaction(f"-{amount}")


    def balace(self):
        return self.account_balance
    
    def get_transaction_log(self):
        self.transaclog.display()
    
class TransactionLog:
    def __init__(self):
        self.transaction = []

    def log_transaction(self, transaction_details):
        self.transaction.append(transaction_details)

    def display(self):
        print(self.transaction)


customer1 = Customer_Account(1,"tom",500)
customer1.deposit(400)
customer1.get_transaction_log()
print(customer1.balace())
customer1.withdraw(100)
customer1.get_transaction_log()
print(customer1.balace())
