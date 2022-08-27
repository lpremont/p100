class Atm:
    def _init_(self,cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def check_balance(self):
        print('Your balance is $50000')

    def cashWithdrawal(self,amount):
        newAmount = 50000-amount
        print('You have withdrawn amount:'+str(amount)+'Your remaining balance is:'+str(newAmount))


def main():
    CardNumber = input("insert your card number:- ")
    pinNumber  = input("enter your pin number:- ")

    new_user =  Atm(CardNumber ,pinNumber)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.withdrawl")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number")

if __name__ == "__main__":
    main()