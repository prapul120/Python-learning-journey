# Validate user input exercise
# 1. Username is no more than 12 character
# 2. Username must not contain spaces
# 3. Username must not contain digits

# Prapul brain 🧠
'''
uname = input("Enter your username: ")

ulen = len(uname)
uname = uname.replace(" ","")
udig = uname.isalpha()

if ulen > 12 :
    print("User name must be less than 12 character")
elif udig == False :
    print("User name must contain only characters")
else:
    print(uname)
'''

# Bro code brain 🧠

username = input("Enter a username: ")



if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain number")
else:
    print(f"Welcome {username}")

# Prapul 30% Brocode 70%