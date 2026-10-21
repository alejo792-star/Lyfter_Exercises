class InsufficientFundsError(Exception):
    pass
try:
    balance = 100
    withdraw = float(input("gime the ammount: 💵"))
    if withdraw > balance:
        raise InsufficientFundsError("insufficient funds❌")
    balance -= withdraw
    print("transaccion compled✅")
    print(f"new bank amount : {balance}")
except ValueError as e:
    print(f"Error [ValueError]: this is no a ammount: {e}")
except InsufficientFundsError as e:
    print(f"Error bank: {e}")
print("end program")    

