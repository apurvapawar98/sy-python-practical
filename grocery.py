print("****grocery shop billing calculator")

rice_qty = float(input("enter qty of rice (in kg):"))
rice_price_per_kg = 50
rice_total = rice_qty * rice_price_per_kg

sugar_qty = float(input("enter qty of sugar (in kg):"))
sugar_price_per_kg = 40
sugar_total = sugar_qty * sugar_price_per_kg

dal_qty = float(input("enter qty of dal (in kg):"))
dal_price_per_kg = 30
dal_total = dal_qty * dal_price_per_kg

print("***bill details***")
print("rice :",rice_total)
print("sugar :",sugar_total)
print("dal :",dal_total)

total_bill = sugar_total + rice_total + dal_total
print("total bill :",total_bill)

discount = 0
if total_bill >=1000:
    print("discount:",discount)
    discount = total_bill * 0.10

elif total_bill >= 500:

  discount = total_bill * 0.05
  print("discount:",discount)


else:
    print("No discount")
    final_bill = total_bill - discount
    print("final bill:",final_bill)
