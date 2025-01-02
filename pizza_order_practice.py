print("Welcome to Python Pizza Deliveries! ")
print("Enter everything in smallcase.")
size = input("Which size of pizza would you like to have: small, medium or large? ")
pepperoni = input("Would you like to have pepperoni: yes or no? ")
extra_cheese = input("Would you like to have extra cheese: yes or no? ")
bill = 0
if size == "small":
    bill += 15
elif size == "medium":
    bill += 20
elif size == "large":
    bill +=25
else:
    print("You have entered something wrong")

if pepperoni == "yes":
    if size == "small":
        bill +=2
    else:
        bill +=3
    
if extra_cheese == "yes":
    bill += 1

print(f"Your final bill is: ${bill}")
    