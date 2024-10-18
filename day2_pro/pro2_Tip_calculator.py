bill = int(input("Enter your total bill:"))


tip = int(input("How much tip would you like to give? ['10','20','more']$:"))
cgst =sgst = (bill*6)/100
gst =cgst+sgst

total_bill= round(float(bill+tip+gst),2)
per_person = int (input("Enter How many people to split the bill:"))
split = total_bill/per_person

print("------------------------------RESTAURANT BILL------------------------------")
print(f"\t\t Total Bill:{bill}")
print(f"\t\t Tip:{tip}")
print(f"\t\t TAX:{gst}")
print(f"\t\t Total Bill+TAX+Tip:{total_bill}")
print(f"\t\t Split among{per_person}:{split}")
print("-------------------------------PROGRAM EXECUTED-------------------------------")