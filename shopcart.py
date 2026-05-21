snacks=["chips","chocolate","juice","biscuit","sandwich"]
prices=[20,50,30,10,70]
cart=[]
snacks
bill=[]
prices
while true:
 print("\n=====SNACK MENU====")
for i in range(len(snacks)):
 print(i+1,".",snacks[i],"-Rs.",prices[i])
choiuce=int(input("choose your snack number:"))
if choice<=1 and choice<= len(snacks):
 cart.append(snacks[choice-1])
 bill.append(prices[choice-1])
 print(snacks[choice-1],"added to cart successfully!")
else:
 print("invalid choice!")
 continue

 more=input("do you want to add more snacks?(yes/no:")
if more.lower()!="yes":
    
 break
print("\n======YOUR SNACK CART=========")
for i in range(len(cart)):
 print(cart[i],"-Rs.",bill[i])
 print("-------------------")
 print("Total snacks bought:",len(cart))
 print("total amount   :Rs.",sum(bill))
 print("------------------")
confirm=input("confirm order?(yes/no:")
if confirm.lower()=="Yes":
 print("orderplaced successfully!")
 print("enjoy your snacks")
else:
 print("order cancelled")
                        
                    
                    
                    
