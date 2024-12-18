import random                                                                                               #import random
user_name = input ("What is your name?: ")                                                                  #create variable and ask user their name
print ("Good luck,", user_name)                                                                             #print good luck with user's name in it
word_options = ['computer', 'science', 'programming', 'python', 'logic', 'board', 'game', 'conditional']    #create list of potential word options: computer, science, programming, python, logic, board, game, conditional
games = 0                                                                                                   #set games to 0
wins = 0                                                                                                    #set wins to 0
while True:                                                                                                 #create infinite loop
    word = random.choice(word_options)                                                                      #set word to a random option from word list
    letters = list(word)                                                                                    #create a list of letters from the word
    random.shuffle(letters)                                                                                 #shuffle the list of letters
    scrambled_word = ''.join(letters)                                                                       #make the list of letters into a single word
    turns = 5                                                                                               #set the amount of turns to 5
    while turns > 0:                                                                                        #create loop using amount of turns is > 0
        user_guess = input(f'Unscramble the word {scrambled_word}: ')                                       #display scrambled word and print text asking user for guess
        if user_guess == word:                                                                              #if the user guesses the word then
            print ('Congrats! You guessed the word!')                                                       #print text to congradulate them                                         
            wins += 1                                                                                       #add 1 to amount of wins
            break                                                                                           #break out of code
        while True:                                                                                         #create infinite loop
            user_rescramble = input ('would you like to  rescramble the word? y/n:  ')                      #ask user if they want to rescramble word
            if user_rescramble == 'n':                                                                      #if they say no then
                exit()                                                                                      #break out of code
            elif user_rescramble ==  'y':                                                                   #if they say yes then
                letters = list(word)                                                                        #create a list of letters from the word
                random.shuffle(letters)                                                                     #shuffle the list of letters
                scrambled_word = ''.join(letters)                                                           #make the list of letters into a single word
                break                                                                                       #break out of loop
            else:                                                                                           #if they say anything else then
                print ('Invalid response')                                                                  #print text to tell user it's invalid
        turns -= 1                                                                                          #subract 1 from amount of turns 
    answer = input (f'The real word is {word}')                                                             #set answer to the real word
    print(answer)                                                                                           #print text to tell user the answer (real word)                                                                
    games += 1                                                                                              #add 1 to amount of games                    
    while True:                                                                                             #create infinite loop
        play_again = input (f'{user_name} you have gotten {wins} out of {games} Would you like to play again? y/n:  ')  #print text with the user's name, how many times they won, out of how many games, and ask if they want to play again
        if play_again == 'n':                                                                               #if they say no then
            exit()                                                                                          #break out of whole code
        elif play_again == 'y':                                                                             #if user says yes then
            break                                                                                           #break out of loop
        else:                                                                                               #user says anything else then
            print ('invalid response, respond with y or n')                                                 #print text to tell user it's invalid and what to respond