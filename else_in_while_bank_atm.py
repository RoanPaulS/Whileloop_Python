Atm_pin = 123;
pin_try = 1;
remaining = 3;
while(pin_try<=3):
    user_pin = int(input("Enter Atm pin : "));
    if(user_pin == Atm_pin):
        print("Atm Pin Matches Successfully !");
        break;
    else:
        remaining = remaining -1;
        if(remaining !=0):
            print("You have entered incorrect pin , you have",remaining,"chances");
    pin_try = pin_try+1;

    
if(pin_try>3):
    print("You have entered wrong pin 3 times. Please contact your nearby bank");
