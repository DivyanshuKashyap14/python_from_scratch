a=int(input("n="))
try:
    print(10/a)
except ZeroDivisionError:
    print("cant divide by 0")
print("division done")
