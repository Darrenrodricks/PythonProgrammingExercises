def area():
    return 5/0

try:
    area()
except ZeroDivisionError:
    print("There was a Zero Division Error")
finally:
    print("Done")
    