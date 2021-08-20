# Question: Write a program that computes the net amount of a bank account based a transaction log from console
# input. The transaction log format is shown as following: D 100 W 200 D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then, the output should be: 500
balance = 0
while True:
    s = input(
        "Please deposit or withdraw money.\nTo deposit enter 'D' followed by the amount you would like to deposit\n"
        "To withdraw enter 'W' followed by the amount you would like to withdraw\nPlease enter here: ")
    if s == "":
        break
    else:
        a = s.split(" ")
        x = a[0]
        if a[0] == "D":
            balance += int(a[1])
        elif a[0] == "W":
            balance -= int(a[1])
        else:
            pass

print("Your total account balance is: {}".format(balance))
