# Hatlist--------
# Create a hat list using the Square Brackets Notations
hat=[1,2,3,4,5]
#Relace the middle value by first defining its index
hat[2]=int(input("Replace"))
# Use the Pop() function to remove the last vale from the List and this as well uses the Negative indexing 
print(hat)
hat.pop(-1)
# We shall use the Len key word to check for the Length of the list after removing one Value 
print("The size of the List is:",len(hat))
# We shall print the whole list after checking the Length and also removing the Values
print("Hat=",hat)