# Question: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program: 9 Then, the output should be: 11106

a = int(input("Please enter a single digit number: "))

print((a) + (a * 11) + (a * 111) + (a * 1111))
