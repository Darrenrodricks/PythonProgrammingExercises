# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the first 5 elements in the list.
def square_list_FirstFive():
    l = list()
    for i in range(1, 21):
        l.append(i ** 2)
    print(l[:5])

square_list_FirstFive()