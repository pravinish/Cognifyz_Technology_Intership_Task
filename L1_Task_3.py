import re

def is_valid_email(email):
    # Regular expression to check email format
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(email_regex, email):
        return True
    else:
        return False

def main():
    email = input("Enter an email address: ")
    
    if is_valid_email(email):
        print("Valid email address.")
    else:
        print("Invalid email address.")

if __name__ == "__main__":
    main()
