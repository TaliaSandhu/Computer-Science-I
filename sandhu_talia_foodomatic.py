#Author: Talia Sandhu
#Description: A code that asks which foods you would like to order, which drinks you would like to order, and then checks for errors and adds up the total.
#Date: 4/7/25
#Bugs: None
#Challenges: Drinks, drink prices, check for value error, calculating total price of food, calculating total price of drinks
#Sources: None

import random   #access random library

mains = ["cauliflower", "tilapia fillet", "pork loin", "salmon", "potatoes", "three color squash", "eggplant", "steak", "baguette"]    #set the list of main dishes 
prices = [20, 25, 28, 30, 18, 20, 22, 30, 20]   #set the list of main dish prices 
flairs = ["with balsamico", "with garlic and olive oil", "with minted yogurt", "with chutney", "with salad", "with salsa", "over sticky rice", "au jus", "with basmati rice"]  #set the list of flairs 
drinks = ["sprite", "coca-cola", "ginger ale", "shirley temple", "water", "lemonade"]  #set the list of drinks 
drinks_prices = [3, 3, 3, 4, 2, 3]   #set the list of drink prices 

while True:
    try:   #if there is an error
        items = int(input("How many menu items would you like to order?"))  #set the input and ask question 
    except ValueError: #if there is an error with the value
        print("Enter an integer") #asks user to enter an integer
        continue #restart

    total = 0   #set total money spent to zero

    for i in range(int(items)):    #turning the answer of the question into an integer 
        main = random.choice(mains)    #picking a random item from list 
        flair = random.choice(flairs)    #picking a random item from list
        price = prices[mains.index(main)]    #matching indexes in the parallel arrays of mains and prices
        total+=price   #add price to total
        print(main, flair, price)  #display the main then flair then price in the same line 

    print(f"Your total is: ${total}")   #tell the user the new total price

    drink = input("Would you like to order drinks? yes/no")    #set the input and ask question      
    if drink == "yes": #if the user answers yes 
        answer = input("How many drinks would you like to order?") #set the input and ask question 
        for i in range(int(answer)):   #turning the answer of question into an integer 
            drink = random.choice(drinks)  #picking a random item from list 
            drink_price = drinks_prices[drinks.index(drink)]   #matching indexes in the parallel arrays of drink prices and drinks
            total+=drink_price 
            print(drink, drink_price)  #display the drink then price in the same line 

        print(f"Your total is: ${total}")   #tell the user the new total price
    if drink == "no": #if the user answers no
        quit   #exit code 