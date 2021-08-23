# Please write a program to randomly print a integer number between 7 and 15 inclusive.
import random
print(random.sample([x for x in range(7, 16)], 1))