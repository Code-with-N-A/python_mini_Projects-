def name():
    try:
        a=int(input("Enter your number:- "))
        return a
    except ValueError:
        print("Enter veliid valu")
        return name()
b=name()
print(b,"yor valu")

