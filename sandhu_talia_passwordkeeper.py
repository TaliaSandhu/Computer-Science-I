import random
import csv

def export_to_csv(filename, headers, *arrays):
    '''
    Exports parallel arrays to a CSV file.

    Args:
        filename (str): The name of the CSV file to create.
        headers (list): A list of header names for each column.
        *arrays: Variable number of array arguments (lists or tuples).
               All arrays must have the same length.
    '''
    if not arrays:                                                                  #if no array is given
        raise ValueError("At least one array must be provided.")                    #acknoledges an error and controls it
    
    num_rows = len(arrays[0])                                                       #creates the number of rows using the number of elements in the first array

    for arr in arrays:                                                              #checking that for every array
        if len(arr) != num_rows:                                                    #the lengths are all the same
            raise ValueError("All arrays must have the same length.")               #controls error if lengths are different
    
    with open(filename, 'w', newline='') as csvfile:                                #open the file in writing mode
        csvwriter = csv.writer(csvfile)                                             #creates writer to write data in file
        csvwriter.writerow(headers)                                                 #writes the first row as headers

        for i in range(num_rows):                                                   #for the number of rows
            row = [arr[i] for arr in arrays]                                        #creates each row of data using the elements in the arrays
            csvwriter.writerow(row)                                                 #writes each row of data to the csv file

def add_entry(websites, usernames, passwords):
    '''
    Adds an entry to the parallel array of websites, usernames, and passwords
    Args:
        websites (list): the list of websites
        usernames (list): the list of usernames
        passwords (list): the list of passwords
    Returns:
        parallel array: newly added to array of websites, usernames, and passwords
    '''
    enter_website = input("Please enter a website ")
    enter_username = input("Please enter a username ")
    enter_password = input("Please enter a password (press 'g' to generate) ")

    if enter_password.lower() == "g":
        enter_password = generate_password()
    websites.append(enter_website)    #add website to websites
    usernames.append(enter_username)  #add username to usernames
    passwords.append(enter_password)  #add password to passwords

def print_entry(website, username, password):
    '''
    Takes a website, username, and password and prints them neatly in an f-string
    Args:
        website (str): entry from list of websites
        username (str): entry from list of websites
        password (str): entry from list of passwords
    Returns:
        print: f string of website, username, and password
    '''
    print(f'''
Website: {website}
Username: {username}
Password: {password}
    ''')

def print_entries(websites, usernames, passwords):
    '''
    Takes and prints websites, usernames, and passwords in an f string
    Args:
        websites (list): the list of websites
        usernames (list): the list of usernames
        passwords (list): the list of passwords
    Returns:
        print: f string of websites, usernames, and passwords
    '''
    for i in range(len(websites)):
        print_entry(websites[i], usernames[i], passwords[i])

def get_index(websites):
    '''
    Takes list of websites and returns index of website in list
    Args:
        websites (list): the list of websites
    Returns:
        int: index website in given list of websites
    '''
    while True: #forever loop:
        web = input('please enter a website from your archive') #prompt user for a website

        if web in websites: #if website in websites:
            return websites.index(web) #return the index of website in websites
        else:
            print('Website does not exist in your archive')

def change_entry(index, entry_list):
    '''
    Changes an entry
    Args:
        websites (list): the list of websites
        usernames (list): the list of usernames
        passwords (list): the list of passwords
    Returns:
        parallel array: updates given entry
    '''
    entry_list[index] = input('Enter new website: ')

def delete_entry(websites, usernames, passwords):
    '''
    Deletes an entry
    Args:
        websites (list): the list of websites
        usernames (list): the list of usernames
        passwords (list): the list of passwords
    Returns:
        parallel array: updates lists with deleted entry
    '''
    index = get_index(websites)
    websites.pop(index)
    usernames.pop(index)
    passwords.pop(index)

def get_password_length():
    '''
    Gets a length for the password
    Args:
        None
    Returns:
        int: length
    Raises:
        ValueError
    '''
    while True:
        try:
            length = int(input('Please enter desired password length: '))

            if length < 4:
                print('Length must be at least 4')
                continue
            return length
        except ValueError:
            print('Please enter an integer')

def generate_password():
    '''
    Randomly generates a secure password for the user
    Args:
        None
    Returns:
        str: generated password
    '''
    length = get_password_length()
    characters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!-@#$%^&*()-_=+?')

    while True:
        pwd = ''.join(random.sample(characters, length)) 
        
        if check_security(pwd, length, False):
            break
    print(f'The generated password is {pwd}')
    return pwd

def check_security(pwd, length, display):
    '''
    Checks the security of a given password
    Args:
        pwd (str): given password
        length (int): secure length
        display (bool): whether to print security message
    Returns:
        bool: True/False depending on security of password
    '''
    if len(pwd) < length or pwd.lower() == pwd or pwd.upper() == pwd or not any(char.isdigit() for char in pwd) or not any(char in pwd for char in list('!@#$%^&*()-_=+?~')):
        if display:
            print(f'{pwd} is not secure')
        return False
    else:
        if display:
            print(f'{pwd} is secure')
        return True

def main():
    websites = []
    usernames = []
    passwords = []

    add_entry(websites, usernames, passwords)  

    options = '''
1. Add another entry
2. See all of your entries
3. See where a website is in your list of websites
4. See username and password of specific website
5. Change an entry
6. Delete an entry
7. Export websites, usernames, and passwords to a csv file to see in excel
8. Generate a password
    '''

    while True:                                                                                                                    #forever loop
        option = input('What would you like to do? (Press "q" to quit, "o" to see the options): ').lower()  

        if option == "q":                                                                                                           #if user enters q
            break                                                                                                                   #break out of loop
        elif option == "o":                                                                                                         #if user enters o
            print(options)                                                                                                          #display options
        elif option == "1":                                                                                                         #if user enters 1
            add_entry(websites, usernames, passwords)                                                                               #calls add_entry using websites, usernames, and passwords lists
        elif option == "2":                                                                                                         #if user enters 2
            print_entries(websites, usernames, passwords)                                                                           #calls print_entries using websites, usernames, and passworlds lists
        elif option == "3":                                                                                                         #if user enters 3
            print(f'That is the {get_index(websites) + 1} website')                                                                 #displaying get_index using websites list
        elif option == "4":                                                                                                         #if user enters 4
            index = get_index(websites)                                                                                             #set index to the output of get_index using websites lists
            print_entry(websites[index], usernames[index], passwords[index])                                                        #call print entry using the indexes from websites, usernames, and passwords list
        elif option == "5":                                                                                                         #if user enters 5
            change = input("Would you like to change a website, username and/or password? w/u/p (enter all that apply): ").lower()  #sets input and asks question
            index = get_index(websites)

            if "w" in change:                                                                                                       #if user enters w
                print(change_entry(index, websites))                                                                                #display and call change_entry function for websites
            if "u" in change:                                                                                                       #if user enters u
                print(change_entry(index, usernames))                                                                               #display and call change_entry function for usernames
            if "p" in change:                                                                                                       #if user enters p
                print(change_entry(index, passwords))                                                                               #display and call change_entry function for passwords
        elif option == "6":                                                                                                         #if user enters 6
            delete_entry(websites, usernames, passwords)            
        elif option == "7":                                                                                                         #if user enters 7
            filename = input('Enter filename for csv: ')                                                                            #sets input and prompts user
            export_to_csv(filename+".csv", ["Website", "Username", "Password"], websites, usernames, passwords)                     #calls export_to_csv function and names the file and fills in information using websites, usernames, and passwords lists
            print(f'Data successfully exported to {filename}.csv')
        elif option == "8":
            pwd = generate_password()
            store = input(f'Do you want to store this for a specific entry? y/n ').lower()

            if store == "y":
                index = get_index(websites)
                passwords[index] = pwd
        elif option == "9":
            pwd = input('Enter password to check (or "p" to get a specific password from your entries) ')

            if pwd.lower() == "p":
                index = get_index(websites)
                pwd = passwords[index]
            length = get_password_length()
            check_security(pwd, length, True)
        else:   #if user enters anything else
            print("invalid")    #display invalid message
    
main()