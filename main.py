import random
import string


#intro function display intro to user
def intro():
    print("Welcome to the Password Generator App!")
    print("We're here to help you create strong and secure passwords.")
    print("For best results, we recommend using a password length of 8 characters or more.")
    print("\n")


def password_generator(char_len):
    #check point to warn user its advice to have a password with 8 characters or more
    if char_len < 8:
        print("We recommend using 8 characters or more to have strong password")

    # Declare the different character type
    lowercase_char = string.ascii_lowercase
    uppercase_char = string.ascii_uppercase
    numbers_char = string.digits
    special_char = string.punctuation

    #concatenate all character type into one variable
    all_char = lowercase_char + uppercase_char + numbers_char + special_char

    #Use list as a data structure
    password = []
    char_count = 0


    while char_count <= char_len:
        random_char = random.choice(all_char)
        password.append(random_char)
        char_count += 1

    #convert the list of random selected character to a string
    password_str = ''.join(password)
    return password_str



#run intro function - prewritten/ custom it to your liking
intro()


#user input
char_len = int(input("Enter the length of the password: "))
print("\n")
password = password_generator(char_len)
print("🤔 Thinking of a masterful password......")
print(f"Generated Password: {password}")





