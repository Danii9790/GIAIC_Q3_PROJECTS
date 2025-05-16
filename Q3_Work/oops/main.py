class BankAccount:
    def __init__(self,account_holder,balance=0):
        self.account_holder=account_holder
        self.__balance=balance #Private variable using encapsulation

    def deposit(self,amount):
        if amount > 0:
            self.__balance +=amount
            print(f"[+] Deposited : {amount}")
        else:
            print(f"[!] Invalid deposit amount")
    def withdraw(self,amount):
        if 0 < amount <=self.__balance:
            self.__balance -= amount
            print(f"[-] {amount} Withdraw.")
        else:
            print(f"[!] Insufficient balance or invalid amount.")
    def get_balance(self):
        return self.__balance
    # (__str__) object ko readable banata hn 
    def __str__(self): #Polymorphism (method overriding)
        return f"Holder : {self.account_holder} , Balance : {self.__balance}"
# Inheritance
class SavingAccount(BankAccount):
    def __init__(self, account_holder, balance=0,interest_rate=0.05):
        # (super()) is used to call the parent class function into the child function
        # parent (BankAccount) constructor call
        super().__init__(account_holder, balance) # Inheriting parent class
        self.interest_rate=interest_rate

    def apply_interest(self):
        interest=self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"[📈] Interest Applied : {interest}")

# Polymorphism : overriding __str__ again
    def __str__(self):
        return f"[SavingAccount] {self.account_holder} | Balance : {self.get_balance()} | Interest : {self.interest_rate} "
        
        
def main():

    print("💸 ACCOUNT")
    acc1=BankAccount("Daniyal",1000)
    acc1.deposit(500)
    acc1.withdraw(200)
    print(acc1)
    # Child class Object (Inheritance + Polymorphism)
    print("💸 SAVING ACCOUNT ")
    acc2=SavingAccount("Ahmed",1000,0.10)
    acc2.deposit(500)
    acc2.apply_interest()
    acc2.withdraw(700)
    print(acc2)   #Polymorphism __str__


if __name__=="__main__":
    main()