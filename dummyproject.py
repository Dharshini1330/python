try:
    def _atm_():
        print("Welcome to INDIAN BANK")
    _setbalance_ = 10000
    user = input("Enter any one mode (withdraw / checkbalance / depositmoney): ").lower()

    if user == "withdraw":
        withdrawamount = int(input("Enter the amount to withdraw: "))
        if withdrawamount <= _setbalance_:
            _setbalance_ -= withdrawamount
            print("Amount withdrawn:", withdrawamount)
            print("Remaining balance:", _setbalance_)
        else:
            print("Insufficient balance!")

    elif user == "checkbalance":
        print("Your current balance is:", _setbalance_)

    elif user == "depositmoney":
        amt = int(input("Enter the amount to deposit: "))
        _setbalance_ += amt
        print("Amount deposited:", amt)
        print("Updated balance:", _setbalance_)

    else:
        print("Invalid input! Please choose a valid option.")


    _atm_()
except expection as e:
    print(e)

    
