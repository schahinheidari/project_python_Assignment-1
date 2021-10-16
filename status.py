#Assignment 1 exercise 10
def status():
    name = input("Please enter your name: ")
    family = input("Please enter your family: ")

    score1 = float(input("Please enter your first grade: "))
    score2 = float(input("Please enter your second grade: "))
    score3 = float(input("Please enter your third grade: "))
    if  0 > score1 > 20:
        print("score1 is incorrect")
        exit
    if  0 > score2 > 20:
        print("score2 is incorrect")
        exit
    if  0 > score2 > 20:
        print("score3 is incorrect")
        exit    
    average = (score1 + score2 + score3) / 3
    print(name," ", family)
    print("Your average is :" , average)
    if 20 > average >= 17:
            print("your status is Great")
    elif 17 > average >= 12:
            print("your status is Normal")
    elif average > 20:
            print("The numbers entered are incorrect")
    else:
            print("FAIL !!")

status()
