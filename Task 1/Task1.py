print("BPP Pizza Price Calculator")
print("==========================")
pizza_price = 12.0
delivery_charge = 2.5
app_discount =0.25
tuesday_discount = 0.5

def pizza_takeaway (pizza_count, tuesday_offer, app_used, delivery_necessity):
    pizza_price = 12.0
    delivery_charge = 2.5
    app_discount =0.25
    tuesday_discount = 0.5

    

#pizza counts
while True:
    try:
        pizza_count = int (input("Please enter the numbers of pizza you want to order:"))
        if pizza_count < 0:
            raise ValueError
        break
    except ValueError:
        print("Oops! Enter a valid number.")
    
#apply tuesday discount offer
while True:
    tuesday_offer = input("Is it Tuesday? Enter 'Y' for Yes or 'N' for No: ").strip().lower()

    if tuesday_offer == 'y':
        break
    elif tuesday_offer == 'n':
        break
    else:
        print("Please answer the question in 'y' or 'n'.")

    
#ordering via bpp app
while True:
    app_used = input ("Did the customer order via our new app? Enter 'Y' for Yes or 'N' for No: ").strip().lower()
    
    if app_used == 'y':
        break
    elif app_used == 'n':
        break
    else:
        print ("Please answer the question in 'y' or 'n'.")

#delivery required
while True: 
    delivery_necessity = input ("Do you want us to deliver your pizza? Enter 'Y' for Yes or 'N' for No: ").strip().lower()
    
    if delivery_necessity == 'y':
        break
    elif delivery_necessity == 'n':
        break
    else:
        print ("Please answer the question in 'y' or 'n'.")
        
        
#calculation

total_pizza_price = pizza_count * pizza_price

if tuesday_offer == 'y':
    total_pizza_price *= (1 - tuesday_discount)
        
if app_used == "Y":
    total_pizza_price *= (1 - app_discount)
    
if delivery_necessity == 'y' and pizza_count < 5:
    total_pizza_price += delivery_charge

if app_used == 'y':
    total_pizza_price *= (1 - app_discount)

    
print("\nTotal Price: £{0:.2f}.".format(total_pizza_price))

