# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
#
# Example: If the following n is given as input to the program:
#
# 5
#
# Then, the output of the program should be:
#
# 3.55

a = int(input("Please enter a value:"))
sum = 0.0

for i in range(1, a+1):
    sum += float(float(i) / (i + 1))

print(sum)