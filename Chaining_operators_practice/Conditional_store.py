purchase_amount = float(input("Enter purchase amount: "))
discount = 0

if purchase_amount >= 50000:
    discount = 0.2
elif purchase_amount > 20000:
    discount = 0.1

amount_payable = purchase_amount - (purchase_amount * discount)

print("Amount payable: ", amount_payable)