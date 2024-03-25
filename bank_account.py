class BankAccount:
    def __init__(self, account_number, firstname, lastname, time_zone_offset, balance):
        self.__account_number = account_number
        self.__firstname = firstname
        self.__lastname = lastname
        self.__balance = balance
        self.__time_zone_offset = time_zone_offset

    def do_deposit(self, amount):
        transaction_time = get_time_with_offset(self.__time_zone_offset)
        ConfirmantionNumber.transaction_id += 1
        if amount < 0:
            return ConfirmantionNumber("X",self.__account_number, transaction_time, amount)
        self.__balance += amount
        return ConfirmantionNumber("D",self.__account_number, transaction_time, amount)
    
 
    def do_withdrawal(self, amount):
        transaction_time = get_time_with_offset(self.__time_zone_offset)
        ConfirmantionNumber.transaction_id += 1
        if amount < 0:
            return ConfirmantionNumber("X",self.__account_number, transaction_time, amount)
        self.__balance -= amount
        return ConfirmantionNumber("W",self.__account_number, transaction_time, amount)   

    def add_interest_rate(self, rate):
         transaction_time = get_time_with_offset(self.__time_zone_offset)
         interest = self.__balance * rate  
         self.__balance += interest
         return ConfirmantionNumber("I", self.__account_number, transaction_time, interest)


class ConfirmantionNumber:
    transaction_id = 0

    def __init__(self, transaction_type, account_number, transaction_time, inc_number):
        self.__transaction_type = transaction_type
        self.__account_number = account_number
        self.__transaction_time = transaction_time
        self.__inc_number = inc_number

    def return_confirmation_number(self):
        return '-'.join([str(self.__transaction_type), str(self.__account_number), str(self.__transaction_time), str(ConfirmantionNumber.transaction_id)])



def get_time_with_offset(preferred_offset_hours):
    from datetime import datetime, timedelta
    
    utc_now = datetime.utcnow()

    offset = timedelta(hours=preferred_offset_hours)

    preferred_time = utc_now + offset

    return preferred_time

account = BankAccount("123456789", "has", "asaturyan", -7, 1000)
dep_conf = account.do_deposit(500)
print(dep_conf.return_confirmation_number())
withdraw_conf = account.do_withdrawal(40)
print(withdraw_conf.return_confirmation_number())