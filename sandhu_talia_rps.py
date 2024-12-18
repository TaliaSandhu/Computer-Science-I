import random                                                                               #access random library
def colored_text(text, color_name, input_or_print):                                         #change color of inputs and prints
    colors = {                                                                              #different colors to be introduced
        'black': '\033[30m',                                                                #black color option
        'red': '\033[31m',                                                                  #red color option
        'green': '\033[32m',                                                                #green color option
        'yellow': '\033[33m',                                                               #yellow color option
        'blue': '\033[34m',                                                                 #blue color option
        'magenta': '\033[35m',                                                              #magenta color option
        'cyan': '\033[36m',                                                                 #cyan color option
        'white': '\033[37m',                                                                #white color option
        'reset': '\033[0m',                                                                 #reset to default color option
    }                                                                                       #close parenthesis
    color_code = colors.get(color_name.lower(), '\033[37m')                                 #default to white if color not found
    if input_or_print == "input":                                                           #input can be colored
        return input(f"{color_code}{text}\033[0m")                                          #print text with color and reset
    else:                                                                                   #other options
        print(f"{color_code}{text}\033[0m")                                                 #print text with color and reset

weapons = ['rock', 'paper', 'scissors']                                                     #list of weapons for rps
responses = ['yes','no','maybe','ask again later']                                          #list of responses for kyd

while True:                                                                                 #new infinite loop
    which_game = colored_text("Which game would you like to play? Rock Paper Scissors/Know Your Destiny (press 'q' to quit): ", "blue", "input")        #setting input/asking question/with color
    
    if which_game == "Rock Paper Scissors":                                                 #if user answers rps
        while True:                                                                         #new infinite loop
            try:                                                                            #try this answer
                rounds = int(colored_text("How many rounds?: ", "blue", "input"))           #setting input/asking question/with color
                break                                                                       #break out of while true loop
            except ValueError:                                                              #check answer above, if not an integer, then...
                colored_text("Please enter an integer", "red", "print")                     #print message in red
        user_score = 0                                                                      #set user score to 0
        bot_score = 0                                                                       #set bot score to 0
        score_limit = 5                                                                     #max amount of points is 5 per person/bot
        while rounds > 0 and user_score < score_limit and bot_score < score_limit:          #new infinite loop when 1 or more rounds
            bot_rps = random.choice(weapons)                                                #bot chooses weapon from list

            while True:                                                                     #new infinite loop
                user_rps = colored_text ("Choose your weapon (rock, paper, or scissors): ", "cyan", "input")        #setting input/asking question/with color
                if user_rps in weapons:                                                     #if user chooses a weapon from the list
                    break                                                                   #break out of while true loop
                elif user_rps == "quit":                                                    #if user enters quit
                    colored_text ("don't be a quitter", "magenta", "print")                 #print message in color
                elif user_rps == "help":                                                    #if user enters help
                    colored_text ("fine you can leave", "white", "print")                   #print message in color
                    rounds = 0                                                              #set rounds to 0
                    break                                                                   #break out of while true
                else:                                                                       #user enters anything else then...
                    colored_text ("invalid response", "red", "print")                       #print message in color
            if user_rps == bot_rps:
                colored_text("tie", "white", "print")
            elif bot_rps == "rock" and user_rps == "scissors":
                colored_text ("you lose", "red", "print")
                bot_score += 1
            elif bot_rps == "rock" and user_rps == "paper":
                colored_text ("you win", "green", "print")
                user_score += 1
            elif bot_rps == "paper" and user_rps == "rock":
                colored_text ("you lose", "red", "print")
                bot_score += 1
            elif bot_rps == "paper" and user_rps == "scissors":
                colored_text ("you win", "green", "print")
                user_score += 1
            elif bot_rps == "scissors" and user_rps == "paper":
                colored_text ("you lose", "red", "print")
                bot_rps += 1
            elif bot_rps == "scissors" and user_rps == "rock":
                colored_text ("you win", "green", "print")
                user_score += 1
            print(f"user:{user_score} - bot: {bot_score}")
            rounds -= 1
        if bot_score > user_score:
            colored_text ("Bot won this game", "cyan", "print")
        else:
            colored_text("You won this game!", "cyan", "print")
    elif which_game == "Know Your Destiny":
        while True:                                                                                 #infinite loop
            ask_multiple_questions = colored_text ("Will you be asking more than one question? yes/no: ", "blue", "input")  #setting input/asking question
            if ask_multiple_questions == "yes":                                                     #conditional statement if user answers yes
                while True:                                                                         #infinite loop within the if statement
                    ask_a_question = colored_text ("Ask any question (press 'q' to quit): ", "magenta", "input")                                  #setting input/asking question
                    if ask_a_question == "q":
                        break
                    elif "?" in ask_a_question:                                                       #conditional statement checking if there is a question mark in the user's input
                        print (random.choice(responses))                                            #displays one of the responses in the list at random
                        break
                    else:                                                                           #if there isn't a ? in the user's input...
                        print ("THAT'S NOT A QUESTION")                                             #display message
            elif ask_multiple_questions == "no":                                                    #conditional statement if user answers no 
                while True:                                                                         #infinite loop if user answers no
                    ask_a_question = colored_text ("Ask any question (press 'q' to quit): ", "magenta", "input")                                  #setting input/asking the question
                    if "?" in ask_a_question:                                                       #conditional statement checking if there is a question mark in the user's input                                  
                        print (random.choice(responses))                                            #displays one of the responses in the list at random
                        break
                    elif ask_a_question == "q":
                        break                                                                       #break out of loop (doesn't ask again)
                    else:                                                                           #if there isn't a ? in the user's input...
                        print ("THAT'S NOT A QUESTION")                                             #display message
                break                                                                               #break out of outside loop (doesn't ask first question again)
    elif which_game == "q":
        break
    else:
        colored_text ("invalid response", "red", "print")