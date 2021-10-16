def Input():
    a = float(input("Please enter your Weight in KG: "))
    b = float(input("Please enter your Height in CM: "))
    k = (b / 100) ** 2
    result = a / k
    print("Your BMI is: " , result)
    if result < 18.5:
        print("UNDERWEIGHT")
    elif 18.5 < result < 24.9:
        print("NORMAL")
    elif 25 < result < 29.9:
        print("OVERWEIGHT")
    elif 30 < result < 34.9:
        print("OBESE")
    elif result > 35:
        print("EXTREMLY OBESE")
    again()
    
def again():
    bode = input("Do you want to calculate again? y or n ===> ")
    if bode.lower() == "y":
        Input()
    elif bode.lower() == "n":
        print("see you then!!")
    else:
        again()

Input()    

