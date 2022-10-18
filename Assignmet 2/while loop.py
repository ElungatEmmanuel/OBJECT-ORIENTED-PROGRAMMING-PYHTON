# A while loop that prints even numbers from the First 10 numbers
x=1
while x<11:
    # Use the if statement to validate the X values to see if they are divisible by 2 with out a remainder
    if x%2==0:
        # if the x values are divisible by 2 without any remainder then they will be printed
        print(x)
    x=x+1