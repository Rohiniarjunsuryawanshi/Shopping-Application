print("Welcome to the shopping application")

print("""
1. Electronics
2. Clothing
3. Groceries
4. Exit
""")

choice=int(input("Enter your choice :"))

if choice==1:
    print("""
    1. Mobile 📱 (25000)
    2. Laptop 💻 (50000)
    3. Headphones 🎧 (2000)
    4. Exit
""")
    choice1=int(input("Enter your choice :"))
    if choice1==1:
        price=25000
        print("you have selected mobile and price is Rs:",price)
    elif choice1==2:
       price=50000
       print("you have selected labtop and price is Rs:",price)
    elif choice1==3:
           price=2000
           print("you have selected headphones and price is Rs:",price)   
    elif choice1==4:
         print("Thank you for shopping with us")
    else:
         print("Invalid choice")

elif choice==2:
    print("""
     1. t-shirt 👕 (500)
     2. shorts 🩳 (300)
     3. jeans 👖 (800)
     4. Exit
     """)
    choice2=int(input("Enter your choice :"))
    if choice2==1:
         price=500
         print("you have selected t-shiet and price is Rs:",price)
    elif choice2==2:
         price=300
         print("you have selected shorts and price is Rs:",price)
    elif choice2==3:
         price=800
         print("you have selected jeans and price is Rs:",price)   
    elif choice2==4:
         print("Thank you for shopping with us")
    else:
         print("Invalid choice")   


elif choice==3:
    print("""
     1. rice 1kg 🍚 (50)
     2. milk 1Ltr 🍶 (40)
     3. suger 1kg 🍬 (30)
     4. Exit
     """)
    choice3=int(input("Enter your choice :"))
    if choice3==1:
         price=50
         print("you have selected rice and price is Rs:",price)
    elif choice3==2:
         price=40
         print("you have selected milk and price is Rs:",price)
    elif choice3==3:
         price=30
         print("you have selected suger and price is Rs:",price)   
    elif choice3==4:
         print("Thank you for shopping with us")
    else:
         print("Invalid choice")   

elif choice==4:
     print("Thank you for shopping with us")         

else:
     print("Invalid choice")           
   
quantity=int(input("Enter the quantity :"))

total=price*quantity

if total>30000:
     discount=total*0.20
     print("Youhavee got 20% discount")
elif total>15000:
      discount=total*0.10
      print("Youhavee got 10% discount")    
else:
     discount=0
     print("You have got no discount")

finalAmount=total-discount

print("You got discount :",discount)
print("Your final amount is Rs:",finalAmount)
print("Thank you for shopping with us and visit again.....😊!")