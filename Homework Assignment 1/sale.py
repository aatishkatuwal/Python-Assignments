retail_price = 99
quantity = int(input("Enter quantity: "))

if quantity >= 10 and quantity <= 19:
    discounted_rate = 0.1
elif quantity >= 20 and quantity <= 49:
    discounted_rate = 0.2
elif quantity >= 50 and quantity <= 99:
    discounted_rate = 0.3
elif quantity >=100:
    discounted_rate = 0.4
else:
    discounted_rate = 0

full_price = quantity * retail_price
discount_amount = full_price * discounted_rate
total_amount = full_price - discount_amount

print("Discount Amount: $", format(discount_amount, '.2f'))
print("Total Amount: $", format(total_amount, '.2f'))
