#exception
def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print("Error Zero")

print(spam(2))
print(spam(0)) #除数为0
