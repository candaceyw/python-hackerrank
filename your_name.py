# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
#
# Hello firstname lastname! You just delved into python.
#
# Input Format
#
# The first line contains the first name, and the second line contains the last name.
#


def print_full_name(a, b):
    firstname = a
    lastname = b
    print(f'Hello {firstname} {lastname}! You just delved into python.')

if __name__ == '__main__':