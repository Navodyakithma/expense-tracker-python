# First we need to Import the Packages
import calendar
import datetime
import json

class GET:
    # First take the Input From the User

    def __init__(self,number):
        with open("detail.json", "r") as file:
            self.data = json.load(file)

        if number == "2":
            self.view_All_Expences()

        elif number == "3":
            self.all_The_Spendings()

        else:
            print("Please Enter the Right Number")





    # If User Select the 2 Selection they can view all the expences
    def view_All_Expences(self):

        #Get the All the data in the List
        for i in self.data:
            print(i)

    # If user Select 3 Selection they can view all the Spends
    def all_The_Spendings(self):

        # Ask the User get all the spending or filter spending
        print("1.Do you want All spending")
        print("2.Filter spending")
        print("Enter the Number as your preference (1/ 2): ", end="")

        choice = input()
        if choice == "1":


            #Get the all Spends
            allAmounts = []
            # In here only get the amounts
            i = 0
            while True:
                allAmounts.append(self.data[i]["amount"])
                i = i + 1
                if i >= len(self.data):
                    break

            allSpendings = 0
            for i in allAmounts:
                allSpendings = allSpendings + float(i)

            print(f"This is the All Spending Values : {allSpendings}")

        elif choice == "2":

            print("1). By Date ")
            print("2). By Description ")
            print("Enter Your Number as your Preferences (1/ 2): ",end="")

            choice_01 = input()
            if choice_01 == "1":
                # Get the All the Spends within date that user entered

                try:
                    print("Enter the Year: ", end="")
                    dateYear = int(input())

                    print("Enter the Month : ", end="")
                    dateMonth = int(input())

                    if dateYear <= datetime.datetime.now().year:

                        if dateMonth >= 1 or dateMonth <= 12:
                            print("\n" + calendar.month(dateYear, dateMonth) + "\n")

                            for i in self.data:
                                print(i)

                            print("Enter the Date : ", end="")
                            date = int(input())

                            if calendar.monthrange(dateYear, dateMonth)[1] >= date:
                                i = 0
                                all_spending_date = 0;
                                while True:
                                    if self.data[i]["date"] == f"{dateYear}-{dateMonth:02d}-{date:02d}":
                                        all_spending_date = all_spending_date + float(self.data[i]["amount"])

                                    i += 1
                                    if i >= len(self.data):
                                        break

                                if all_spending_date == 0:
                                    print("In that month nothing Spends")
                                else:
                                    print(f"This is the Spends Value : {all_spending_date}")
                            else:
                                i = 0
                                k = 0
                                indexes = []

                                while True:
                                    value = self.data[i][3]
                                    value_01 = ""
                                    while True:
                                        if int(value_01) == dateYear:
                                            k = 0
                                            indexes.append(i)
                                            break

                                        value_01 += value[k]
                                        k += 1

                                        if len(value) <= k:
                                            k = 0
                                            break

                                    i += 1

                                all_spending_month = 0
                                i = 0
                                while True:
                                    value = self.data[indexes[i]][3][5][6]
                                    if value == str(f"{dateMonth:02d}"):
                                        all_spending_month = all_spending_month + float(self.data[i][1])
                                    i += 1

                                    if i >= len(indexes):
                                        break

                                print(f"This is the Spending in that Year : {all_spending_month}")





                        else:

                            i = 0
                            k = 0
                            indexes = []

                            while True:
                                value = self.data[i][3]
                                value_01 = ""
                                while True:
                                    if int(value_01) == dateYear:
                                        k = 0
                                        indexes.append(i)
                                        break

                                    value_01 += value[k]
                                    k += 1

                                    if len(value) <= k:
                                        k = 0
                                        break

                                i += 1

                            all_spending_year = 0
                            i = 0
                            while True:
                                all_spending_year = all_spending_year + float(self.data[indexes[i]][1])
                                i += 1

                                if len(indexes) <= i:
                                    break

                            print(f"This is the Spending in that Year : {all_spending_year}")
                except ValueError as e:
                    print(e)
                except Exception as e:
                    print(e)

            elif choice_01 == "2":
                #Get the All the Spends based on the Description
                print("Enter the Description: ",end="")
                desValue = input()

                i = 0
                spends = 0
                while True:
                    if self.data[i]["description"].lower() == desValue.lower():
                        spends = spends + float(self.data[i]["amount"])
                    i += 1

                    if i >= len(self.data):
                        break

                if spends == 0:
                    print("Nothing Spends")
                else:
                    print(f"This is the Value: {spends}")
            else:
                print("Please Enter the Right Number!")
        else:
            print("Please Enter the Right Number!")









