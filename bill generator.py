
Bill = int(input("how much is your meal ?"))
tax = float(input("what is the tax in your provience, in percentage ?"))
tip_wish = input("want to tip us ?😊 (yes/no)")
if tip_wish == "yes" or tip_wish=="YES" or tip_wish=="Yes":
   tip =  int(input('enter tip amount'))
   print("Thank you 😘.")    
else:
    tip_wish = 0
    print("thank you.")
tax_amount= (Bill*tax)/100
total_payable_amount= (Bill + tax_amount+ tip)

print("Your Final Bill is rs.", total_payable_amount," Includes Taxes and Tip." )
print("Thank You For Visiting Us❤️.")





