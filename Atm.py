class Atm(object):
    def __init__(self, atm_card_number, pin_number, money_left, user_name):
        self.atm_card_number = atm_card_number
        self.pin_number = pin_number
        self.money_left = money_left
        self.user_name = user_name

    def cash_widhdrawl(self):
        print("You just widhdrawed some money")
        print(" ")
        print("Thank you for coming, hope to see you again")

    def balance_inquiry(self, money_left):
        self.money_left = money_left
        print("So you have this much money left: " + str(self.money_left))
        print(" ")
        print("Thank you for coming, hope to see you again")

    def account_details(self, atm_card_number, pin_number, user_name):
        self.atm_card_number = atm_card_number
        self.pin_number = pin_number
        print("Name: " + str(self.user_name))
        print("Card Number: " + str(self.atm_card_number))
        print("Pin Number: " + str(self.pin_number))
        print(" ")
        print("Thank you for coming, hope to see you again")


# I have one user who's card number is 1346 and Pin Number is 1234
user1 = ['1346', 'Naman', '$14500', '1234']
card_number = input("What is your Card Number? ")

if str(card_number) == user1[0]:
    pin_number = input("Hello Naman. Welcome back! Please enter your Pin Number: ")

    if  str(pin_number) == user1[3]:
        user_name = user1[1]
        money_left = user1[2]
        user_name = Atm(card_number, pin_number, money_left, user_name)
        
        print(" ")
        print("1. Widhdraw")
        print("2. Balance Inquiry")
        print("3. Account Details (Card number and Pin number)")
        print(" ")
        question = input("What do you want to know or do from the above (1/2/3)? ")
        print(" ")

        if str(question) == '1':
            print(user_name.cash_widhdrawl())
            print(" ")
        elif str(question) == '2':
            print(user_name.balance_inquiry(money_left))
            print(" ")
        elif str(question) == '3':
            print(user_name.account_details(card_number, pin_number, user_name))
            print(" ")
        else:
            print("Please choose one option from the above by either typing 1/2 or 3 ")
            print(" ")
    else:
        print("Your entered Pin Number is incorrect. (How can you forget this XD)")

else:
    print("Sorry! You are not one of our users")