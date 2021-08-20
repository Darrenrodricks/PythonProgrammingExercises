# Define a function that can accept two strings as input and print the string with longer length in console. If two
# strings have the same length, then the function should print all strings line by line.

def length_tester(s1, s2):
    a = int(len(s1))
    b = int(len(s2))
    if a > b:
        print(s1 + " is the longer input")
    elif b > a:
        print(s2 + " is the longer input")
    elif b == a:
        print("both inputs have the same length")


length_tester("one","three")

