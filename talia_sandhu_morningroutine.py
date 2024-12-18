print ("Alarm goes off")                                                    #display message
while True:                                                                 #infinite loop
    wake_up = input ("Wake up? yes/no: ")                                   #setting the input/asking the question (two options)
    if wake_up == "no":                                                     #conditional loop if user answers no
        print ("Oversleep")                                                 #display message                 
        break                                                               #break out of while true loop (skips to after the else)
    elif wake_up == "yes":                                                  #mutually exclusive to the if, this one is if the user answers yes
        while True:                                                         #while true in the while true, only asks these questions if the answer is yes to the original question
            put_up_blinds = input ("Put up blinds? yes/no: ")               #setting the input/asking the question (two options)
            if put_up_blinds == "no":                                       #conditional loop if user answers no
                print ("Keep the room dark")                                #display message
                break                                                       #break out of inside while true loop (stays in the original one/skips to the second else)
            elif put_up_blinds == "yes":                                    #mutually exclusive to the if, this one is if the user answers yes
                break                                                       #break out of inside while true loop (skips to second else)
            else:                                                           #mutually exclusive to the if and elif, if answer isn't yes or no
                print ("invalid response")                                  #display message
        break                                                               #break out of outside while true look
    else:                                                                   #mutually exclusive to the yes and no, if user types in anything else
        print("invalid response")                                           #display message
print ("brush teeth")                                                       #display message
print("do skincare")                                                        #display message
while True:                                                                 #new infinite loop
    ask_alexa_the_weather = input ("Ask Alexa the weather? yes/no: ")       #setting input/asking question (two options)
    if ask_alexa_the_weather == "no":                                       #conditional loop if user answers no
        print ("wear anything")                                             #display message
        break                                                               #break out of while true loop, skip to picking out shirt
    elif ask_alexa_the_weather == "yes":                                    #mutually exclusive to the if, this one is if the user answers yes
    #EVERTHING AFTER THIS IS UNDER SAYING YES TO THIS QUESTION INCLUDING ALL WHILE TRUES UNTIL THE SHIRT ONE OUTSIDE THE LOOP
        while True:                                                         #new infinite loop
            will_it_get_above_65_degrees = input ("Will it get above 65 degrees? yes/no: ")                 #Setting input/asking the question (two options)
            if will_it_get_above_65_degrees == "yes":                                                       #conditional loop if user answers yes
                print ("Wear a skirt")                                                                      #display message
            #EVERYTHING AFTER THIS IS UNDER SAYING YES TO BOTH THIS QUESTION AND THE QUESTION BEFORE
                while True:                                                                                 #new infinite loop                                                                             
                    wear_a_blue_skirt = input ("Wear a blue skirt? yes/no: ")                               #setting input/asking the question (two options)
                    if wear_a_blue_skirt == "yes":                                                          #conditional loop if answer is yes
                        break                                                                               #break out of blue skirt while true, skip to shirt while true
                    elif wear_a_blue_skirt == "no":                                                         #mutually exclusive to the if, this one is if the user answers no
                        break                                                                               #break out of blue skirt while true, skip to black skirt while true
                    else:                                                                                   #mutually exclusive to the if and elif, every other answer
                        print ("invalid response")                                                          #display message
                while True:                                                                                 #new infinite loop if one before is "no"                                                                    
                    wear_a_black_skirt = input ("Wear a black skirt? yes/no: ")                             #setting input/asking the question (two options)
                    if wear_a_black_skirt == "yes":                                                         #conditional loop if answer is yes
                        break                                                                               #break ot of black skirt while true loop, skip to shirt
                    elif wear_a_black_skirt == "no":                                                        #mutually exclusive to the if, this one is if the user answers no
                        print ("Wear a grey skirt")                                                         #display message
                        break                                                                               #break out of black skirt while true, skip to shirt
                    else:                                                                                   #mutually exclusive to if and elif, every other answer
                        print ("invalid response")                                                          #display message                                              
                break                                                                                       #break out of BOTH while trues, skip to shirt
                
            elif will_it_get_above_65_degrees == "no":                                                      #mutually exclusive to the if (yes), this one is if user answers no
                print ("Wear pants")                                                                        #display message
                while True:                                                                                 #new infinite loop (under elif-no to 65 degrees)
                    wear_black_pants = input ("Wear black pants? yes/no: ")                                 #setting input/asking the question (two options)
                    if wear_black_pants == "yes":                                                           #conditional loop if answer is yes                                                           
                        break                                                                               #break out of pants while true, skip to sweater
                    elif wear_black_pants == "no":                                                          #mutually exclusive to the if, this one if if the user answers no
                        print ("Wear white pants")                                                          #display message
                        break                                                                               #break out of pants while true, skip to sweater
                    else:                                                                                   #mutually exclusive to the if and elif, every other answer
                        print ("invalid response")                                                          #display message
                while True:                                                                                 #new infinite loop under "no" elif                                                                         
                    wear_a_quarter_zip = input ("Wear a quarter zip? yes/no: ")                             #setting input/asking question (two options)
                    if wear_a_quarter_zip == "yes":                                                         #conditional loop if answer is yes                                                        
                        break                                                                               #break out of sweater while true, skip to shirt
                    elif wear_a_quarter_zip == "no":                                                        #mutually exclusive to the if, this one is if user answers no
                        print ("Wear a crewneck")                                                           #display message
                        break                                                                               #break out of sweater while true, skip to shirt
                    else:                                                                                   #mutually exclusive to the if and elif, every other answer
                        print("Invalid response")                                                           #display message
                break                                                                                       #break out of 65 degrees while true, skip to shirt
            else:                                                                                           #mutually exclusive to the if and elif of 65 degrees, every other answer
                print ("Invalid response")                                                                  #display message
        else:                                                                                               #mutually exclusive to the if and elif ask alexa the weather, every other answer
            print ("Invalid response")                                                                      #display message                                                            
        break                                                                                               #break out of ask alexa weather while true, skip to shirt
while True:                                                                                                 #new infinite loop
    print ("Pick out shirt color")                                                                          #display message
    wear_navy_shirt = input ("Wear a navy shirt? yes/no: ")                                                 #setting input/asking question (two answers)
    if wear_navy_shirt == "no":                                                                             #conditional loop if answer is no
        print ("Wear white shirt")                                                                          #display message
        break                                                                                               #break out of shirt while true, skip to socks
    elif wear_navy_shirt == "yes":                                                                          #mutually exclusive to the if, this one is if user answers yes
        break                                                                                               #break out of shirt while true, skip to socks
    else:                                                                                                   #mutually exclusive to the if and elif, every other answer
        print ("Invalid response")                                                                          #display message
else:                                                                                                       #mutually exclusive to if and elif, every other response of other while true
    print ("Invalid response")                                                                              #display message
print ("Put on socks")                                                                                      #display message
print ("Put on shoes")                                                                                      #display message
while True:                                                                                                 #new infinite loop
    remember_to_fill_water = input ("Remember to fill water bottle? yes/no: ")                              #setting input/asking question (two answers)
    if remember_to_fill_water == "no":                                                                      #conditional statement if answer is no
        print ("Be dehydrated")                                                                             #display message
        break                                                                                               #break out of water while true, skip to breakfast
    elif remember_to_fill_water == "yes":                                                                   #mutually exclusive to the if, this one is if user answers yes
        break                                                                                               #break out of water while true, skip to breakfast
    else:                                                                                                   #mutually exclusive to if and elif, every other answer
        print("Invalid response")                                                                           #display message
    break                                                                                                   #break out of water while true, skip to breakfast
while True:                                                                                                 #new infinite loop
    eat_breakfast_at_home = input ("Eat breakfast at home? yes/no: ")                                       #setting input/asking question (two answers)
    if eat_breakfast_at_home == "no":                                                                       #conditional statement if user answers no
        print ("Eat breakfast at school")                                                                   #display message
        break                                                                                               #break out of breakfast while true, skip to prints                                                              
    elif eat_breakfast_at_home == "yes":                                                                    #mutually exclusive to if, this one is if user answers yes                                                        
        print ("Eat breakfast")                                                                             #display message
        break                                                                                               #break out of breakfast while true, skip to prints
    else:                                                                                                   #mutually exclusive to if and elif, every other answer
        print("Invalid response")                                                                           #display message
print ("Go to school")                                                                                      #display message
print ("Morning routine done!")                                                                             #display message





                    
                    
    
            

                
                
        
            



    

