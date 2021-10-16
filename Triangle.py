def Triangle():
    a = float(input("Enter your first number: "))
    b = float(input("Enter your second number: "))
    c = float(input("Enter your third number: "))

    while True:
        if a+b>c:
            print("We have a triangle :)")
            break
        elif a+c>b:
            print("We have a triangle :)")
            break
        elif b+c>a:
            print("We have a triangle :)")
            break
        else:
            print("Error: We can not have a triangle!!")
    again()
def again():
    triangle_again = input("Do you want to give a number again?? y or n ===> ")
    if triangle_again.lower() == "y":
        Triangle()
    elif triangle_again.lower() == "n":
        print("see you later!!")
    else:
        again()
Triangle()