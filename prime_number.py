num = int(input("Enter a number : "));
diviser = 2;
boolean = True;
while(diviser < num):
    if(num % diviser == 0):
        print("Not a prime");
        boolean = False;
        break;
    diviser = diviser + 1;

if(boolean == True):
    print("The Given number",num,"is Prime Number");
