class InsufficientFundsException(Exception):
    pass
class InvalidAmountException(Exception):
    pass

class ATM_Simulation:
    def __init__(self,balance):
        self.__balance=balance

    def balance(self):
        return (self.__balance)

    def withdraw(self,withdraw):
        try:

            if withdraw>self.__balance:
                raise InsufficientFundsException
            elif withdraw<=0:
                raise InvalidAmountException

            else:
                self.__balance-=withdraw
                return (self.__balance)

        except InsufficientFundsException:
            print("Insufficient Balance")
        except InvalidAmountException:
            print("Invalid amount entered")
    def deposit(self,deposit):
        self.deposit=deposit
        self.__balance+=deposit
        return (self.__balance)

    def simulation(self):
        while True:
            print("Enter your choices")
            print("Enter 1 for balance Enquiry")
            print("Enter 2 for withdraw amount")
            print("Enter 3 for Deposit amount")
            choice=int(input())
            if choice==1:
                print("your balance is",self.balance())
            elif choice==2:
                withdraw=int(input("Enter the amount to be withdraw:"))
                print("after withdraw your balance is",self.withdraw(withdraw))
            elif choice==3:
                deposit=int(input("Enter the amount to be deposited:"))
                print("After the deposit your balance is",self.deposit(deposit))
            else:
                print("Invalid choice")

balance=25000
atm=ATM_Simulation(balance)
atm.simulation()