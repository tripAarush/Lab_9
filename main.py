# My name is Aarush Tripathi
# first github
def encode(password):
    if not password.isdigit() or len(password) != 8:
        raise ValueError("Password should be 8 digits long and contain only integers.")

    digit_pw = [int(digit) for digit in password]
    digit_encoded = [(digit + 3) % 10 for digit in digit_pw]
    pw_encoded = [str(digit) for digit in digit_encoded]
    return ''.join(pw_encoded)

def decode(encoded_password):
    decoded_password = ""
    for char in encoded_password:
        if char.isdigit():
            decoded_digit = (int(char) - 3) % 10
            decoded_password += str(decoded_digit)
        else:
            print("Error: Encoded password must contain only integers.")
            return ""
    return decoded_password
    
def main():
    encoded = 0
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        option = int(input("Please enter an option:"))
        if option == 1:
            pw = input("Please enter your password to encode:")
            encoded = encode(pw)
            print("Your password has been encoded and stored!")
        elif option == 2:
            print("The encoded password is", encoded, "and the original password is", pw)
        elif option == 3:
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
