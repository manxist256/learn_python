house_price = 1000000
buyer_credit = "BAD"

additional_amount = 0

if buyer_credit == "GOOD":
    additional_amount = (house_price * 10) / 100
else:
    additional_amount = (house_price * 20) / 100
print(house_price + additional_amount)