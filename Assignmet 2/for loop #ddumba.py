# A programme that breaks when it reaches the @ symbol in an email
# Create a for loop 
for ch in "Timothy.ddumba@guild.org":
    # Use an if statement to check for the @ symbol in the email
    if ch=="@":
        # This will skip the @ symbol once it reaches it
        break
    print(ch ,end="")