# In this File using for All the Program runs
#First Import the Packages
import calendar
import datetime
import json
import os
from expences import Expences as ex
from main import GET as get

def mainFunction():
    k = 0
    value = object
    while True:
        allFunctions = ["1). Add Expense",
                        "2). View All Expenses",
                        "3). View Spending",
                        "4). Delete Expense",
                        "5). Exit"]

        if k < 0:
            print("\n" + "--------------------------------Welcome to the Expences Tracker---------------------------------" + "\n")
        else:
            print("\n" + "--------------------------------Welcome Back to the Expences Tracker---------------------------------" + "\n")
            k += 1
        for i in allFunctions:
            print(i)

        print("Enter the Number to Continue: ", end="")
        mainChoice = input()

        if mainChoice == "1":
            # In this Run when user click the 1st Choice that is add to spends
            if mainChoice == "1":
                # First take the Amount from the User

                try:
                    print("Enter the Amount(Rs.) : ", end="")
                    amount = int(input())
                except ValueError as e:
                    print(e)
                    break


                # Second take the Description from the User
                print("Enter the Description: ",end="")
                des = input()

                # In here i have to calculate the Id
                idValue = 0
                if os.path.exists("detail.json") == True:

                    with open('detail.json', "r") as file:
                        data = json.load(file)

                    if len(data) == 0:
                        idValue = 0
                    else:
                        idValue = data[len(data) - 1]["id"]+1
                else:
                    idValue = 0

                # get the Date from the user
                try:
                    print("Enter the year: ", end="")
                    year = int(input())

                    if year <= datetime.datetime.now().year:
                        print("Enter the Month: ", end="")
                        month = int(input())

                        if month > 0 or month <= 12:
                            print("\n" + calendar.month(year, month) + "\n")

                            print("Enter the Day : ", end="")
                            day = int(input())

                            if calendar.monthrange(year, month)[1] >= day:
                                myObject = ex(idValue, amount, des, f"{year}-{month:02d}-{day:02d}")
                                value = myObject
                                myObject.add_Expences()
                except ValueError as e:
                    print(e)
                    break

        elif mainChoice == "2" or mainChoice == "3":
            #in this block run when user wants to see the all spends or Filter Spends by adding details
            myObject_01 = get(mainChoice)

        elif mainChoice == "4":
            #In this block run when the user wants to delete the exist spends in the list
            ex.delete_Expences(value)
        elif mainChoice == '5':
            #When User Clicks the 5 that means they need to exit from this Application
            print("\n"+"-------------------------Thank You---------------------------------------")
            break
        else:
            print("Please Enter the Right Number!")

        print("\nDo You Want to Continue(y/n): ",end="")
        again_Choice = input()

        if again_Choice == "Y" or again_Choice =="y":
            continue
        else:
            print("\n"+"-------------------------Thank You---------------------------------------")
            break












mainFunction()
