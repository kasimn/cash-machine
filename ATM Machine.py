#Welcome to the Python ATM Machine

Pin = 2367
balance = 1000

pin = input("Enter the four digit pin: ")


if pin == "2367":
    print("Pin correct")
else:
    print("Pin incorrect")
    exit()


def show_balance():
    print(f"Your balance is currently: {balance}")
    return balance

def deposit():
    amount=float(input("Enter the amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"Deposited {amount}. New balance {balance}.")
        return balace

def withdraw():
    amount = float(input("Enter the amount to withdraw: "))
    if 0 < amount <=balance:
        balance -= amount
        print(f"Withdraw {amount}. New balance {balance}.")
        return balace
      

#balance = 0
is_active = True
running = True
while running:
    print("1.banking program")
    print("2.show balance")
    print("3.deposit")
    print("4.withdraw")
    print("5.exit")
    choice = input("enter your choice")
    
    if choice == '1':
          print("you are now currently in the banking program. please choose an action.") 
    elif choice == '2':
        show_balance()
    elif choice == '3':
        deposit()
    elif choice =='4':
        withdraw()
    if choice == "5":
        print("Exit the program,")
        running = False
    else:
        print("invalid choice. Please choose a Valid option. ") 



