# Assignment : 04 => Class Variables and class Methods
class Bank:
    bank_name="Old bank"
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name=name

b1=Bank()
print(b1.bank_name)
Bank.change_bank_name("New bank")
print(b1.bank_name)    

