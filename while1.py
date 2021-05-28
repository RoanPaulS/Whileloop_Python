mind = 5;
match_not_found = True;
while match_not_found == True:
    guess = int(input("Enter a number between 1 and 10 : "));
    if(guess == mind):
        print("Your guess is correct");
        match_not_found = False;
    elif(guess > mind):
        print("Your guess is higher. Please Try one more time \n");
    else:
        print("Your guess is lower. Please Try one more time \n");
    
