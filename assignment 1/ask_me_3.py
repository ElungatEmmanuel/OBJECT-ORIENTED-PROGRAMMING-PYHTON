#Number two
username  = input("Hey gorgeous, What is your  name? ")
username  = username .title()
# print("Hello," , username )

if username  == "Jack" or username  == "Jackie":
    print("Hello, ", username )
    print("Goodbye," , username )
else:
    print("Hello, Stranger!!!")

age = int(input("How old are you please? "))
if age < 18:
    print("Your are below the age of working.")
elif age > 18 and age < 25:
    print("You are in a job-seeking age.")
elif age > 25 and age < 30:
    print("You should a job already.")
elif age > 30 and age < 60:
    print("You should retire.")
else:
    print("Goodbye,", username )
    print("You are" , age , "years old.")
    print("You are an alien in nature.")





