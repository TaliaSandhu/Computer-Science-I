import random
def chorus():
    '''
    Prints the chorus of a song
    Args:
        None
    Returns:
        print: chorus
    '''
    print ("Oh, don't you dare look back " \
    "Just keep your eyes on me " \
    "I said, You're holding back " \
    "She said, Shut up and dance with me!" \
    "This woman is my destiny S" \
    "he said, Ooh-ooh-hoo " \
    "Shut up and dance with me.")
def sing_song():
    chorus()
    print ("We were victims of the night " \
    "The chemical, physical, kryptonite " \
    "Helpless to the bass and the fading light " \
    "Oh, we were bound to get together " \
    "Bound to get together " \
    "She took my arm " \
    "I don't know how it happened " \
    "We took the floor and she said")
    chorus()
def add(x, y):
    '''  
    Takes two numbers and adds them together
    Args:
        a (int): first number
        b (int): second number
    Returns:
        print: sum of x and y
    '''
    print(x+y)  
def print_list(array):
    '''  
    Takes a list and prints every individual element in the list
    Args:
        list (array)
    Returns:
        print elements in list
    '''
    for i in array:
        print(i)
def in_list(element, array):
    '''  
    Takes a list and an element and returns a boolean depending on if the item is in the list or not
    Args:
        element
        array
    Returns:
        true or false
    '''
    return element in array
def get_integer(order):
    '''  
    Takes anything and returns a boolean depending on if it's an integer
    Args:
        any parameter
    Returns:
        true or false
    Raises:
        valueError
    '''
    while True:
        try:
            number = int(input(f'Please enter your{order} number:'))
            return number
        except ValueError:
            print('Not an integer!!!!!')
def get_integers():
    '''  
    Asks user for two numbers and returns the two integers based on is_integer checking the input
    Args:
       num1
       num2
    Returns:
        num1, num2
    Raises:
        is_integer
    '''
    a = get_integer('first')
    b = get_integer('second')
    return a,b
   
def get_random ():
    '''  
    Uses get_integers and prints a random number between the two given integers
    Args:
        get_integers
    Returns:
        random number between two integers
    '''
    while True:
        a, b = get_integers()
        if a>b:
            print('Make sure your first number is less than your second')
        else:
            print(random.randint(a, b))
            break


def count_vowels(string):
    '''  
    Takes a string and returns the number of vowels in it
    Args:
        string
    Returns:
        integer
    '''
    count = 0
    vowels = ['a','e','i','o','u']
    for char in string:
        if char.lower() in vowels:
            count+=1
    return f"There are {count} vowels."
def subtract(x,y):
    '''  
    Takes two numbers and subtracts them
    Args:
        a (int): first number
        b (int): second number
    Returns:
        print: difference of x and y
    '''
    print(x-y)

def multiply(x,y):
    '''  
    Takes two numbers and multiplies them together
    Args:
        a (int): first number
        b (int): second number
    Returns:
        print: product of x and y
    '''
    print(x*y)

def divide(x,y):
    '''  
    Takes two numbers and divides them
    Args:
        a (int): first number
        b (int): second number
    Returns:
        print: quotient of x and y
    '''
    if y == 0:
        print('Cannot divide by zero. Please enter a new number')
    else:
        print(x/y)


def main():
    while True: #creates infinite loop
        option = input('What would you like to do? 1. Sing a song 2. Enter calculator mode 3. Experiment with lists 4. Count vowels')   #sets the input and asks user the question

        if option == "1":   #if user chooses first option
            sing_song() #calls function

        elif option == "2": #if user chooses second option
            operation = input('What would you like to do? Get a random number(random), +, -, *, /') #sets input and asks user a question
            if operation == 'random':   #if user chooses random option
                get_random()    #calls function

            elif operation in ['+', '-', '*', "/"]: #if the operation called is in this list
                a, b = get_integers()   #calls function

                if operation == '+':    #if operation is addition
                    add(a, b)   #calls function
                elif operation == '-':  #if operation is subtraction
                    subtract(a,b)   #calls function
                elif operation == '*':  #if operation is multiplication
                    multiply(a,b)   #calls function
                elif operation == '/':  #if operation is division
                    divide(a, b)    #calls function
            else:   #if user inputs anything else
                print ('Invalid Response')  #display message
        elif option == '3': #if user chooses option three
            which_function = input('What would you like to do? 1. Identify items in a list/print list or 2. Create your own list')  #sets input and asks user a question
            
            if which_function == '1':   #if user chooses option one
                desserts = ["ice cream", "brownie", "milkshake", "cake"]    #sets list
                print_list(desserts)    #prints list
                user_input1 = input('Enter a dessert to see if it is on the menu')  #sets input and displays message to user
                print(in_list(user_input1, desserts))   #uses in_list function to determine if user input is in list
            elif which_function == '2': #if user chooses option two
                user_list = input('Enter your list of items, separate each item using a space   ').split(' ')   #sets input and asks question, splitting up letters in answer
                print_list(user_list)   #prints user's input in list form
            else: #if user enters anything else
                print('Invalid Response')   #displays invalid response
                continue    #returns to start of code (first question)
        elif option == '4': #if user chooses option four
            user_input2 = input ('Enter a word')    #sets input and gives phrase for user to input response
            print(count_vowels(user_input2))    #displays amount of vowels in user's input using count_vowels function

        else:   #if user enters anything else
            print('Invalid response')   #displays invalid response

        play_again = input('Would you like to play again? y/n:  ').lower()  #sets input and asks user a question, checking lower case letters
        if play_again == 'no':  #if user answers no
            print('See you next time!') #displays message
            break   #breaks out of loop
        elif play_again == 'yes':   #if user answers yes
            continue    #return to beginning of code (first question)
        else:   #if user answers anything else
            print('Invalid response')   #display invalid response

        





        
       

       
        
        
    
    

main()