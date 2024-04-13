# first github
# encode
def encode(password):
    if password.isdigit() or not len(password) != 8:
        raise ValueError("Password should be 8 digits long and contain only integers.")

    digit_pw = [int(digit) for digit in password]
    digit_encoded = [(digit + 3) % 10 for digit in password_digits]
    pw_encoded = [str(digit) for digit in encoded_digits]
    return ''.join(pw_encoded)
