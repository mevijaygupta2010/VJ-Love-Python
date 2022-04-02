#This Program is used to Calculate the Split based on Tip & Number of People Split is done
print("welcome to the tip calculator.")
total_bill=float(input("what was the total Bill?"))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15?"))
total_ppl=int(input("How many people to split the bill?"))
total_bill_with_tip= total_bill + total_bill * (tip/100)
split=round(total_bill_with_tip/total_ppl,2)
#print(f"Each person should Pay: ${split}")
print("Each person should pay ${:.2f}".format(split))