# In here Im going to Add Expences to JSON File
#First We need to Import the Packages that Can help to Use it
import calendar
import datetime
import json
import os.path
from sys import intern


class Expences:

    #First take the Input From the User

    def __init__(self,id,amount,description,date):
        self.id = id
        self.amount =  amount
        self.description = description
        self.date = date


    # In this Method Add All details to the File
    def add_Expences(self):
        # Write to the JSON File
        expences_details = {"id" : self.id, "amount": self.amount,"description":self.description,"date":self.date}

        if os.path.exists("detail.json"):


            with open("detail.json", "r") as file:
                data = json.load(file)

            data.append(expences_details)

            with open("detail.json","w")as file:
                json.dump(data,file,indent=4)
        else:
            with open("detail.json","w")as file:
                json.dump(expences_details,file)




        print("Successfully Added")


    # In this Method Delete the Details
    def delete_Expences(self):
        print("1. ID")
        print("2. Date")
        print("Delete by (1/ 2): ",end="")
        selection = input()

        if selection == "1":
            with open("detail.json","r") as file:
                data  = json.load(file)

            for i in data:
                print(i)
            print("What do you want to Delete : ",end="")
            delete_details = int(input())

            i = 0
            holdIndex = []

            k = 0
            while True:
                if data[i]["id"] == delete_details:
                    holdIndex.append(i)
                    k += 1

                i += 1
                if i >= len(data):
                    break


            if len(holdIndex) <= 0:
                print("Not Found!")
            else:

                i = 0
                while i < len(holdIndex):
                    with open("detail.json", "r") as file:
                        dt = json.load(file)
                    dt.remove(dt[holdIndex[i]])

                    with open("detail.json", "w") as file:
                        json.dump(dt, file, indent=4)

                    i += 1
                print("Successfully Deleted")

        elif selection == "2":
            print("Enter the Year : ",end="")
            year = input()

            if int(year)  <= datetime.datetime.now().year:

                print("Enter the Month: ",end="")
                month = input()

                if 0 < int(month) <= 12:
                    print("\n"+calendar.month(int(year),int(month))+"\n")

                    with open("detail.json", "r") as file:
                        data = json.load(file)

                    for i in data:
                        print(i)


                    print("Enter the Date: ",end="")
                    date = input()

                    if calendar.monthrange(int(year), int(month))[1] >= int(date):


                        holdIndex = []
                        i = 0

                        reMonth  = ""
                        reDate = ""
                        if int(month) < 10:
                            reMonth = "0"+month

                            if int(date) < 10:
                                reDate = "0"+date
                            else:
                                reDate = date
                        else:
                            if int(date) < 10:
                                reDate = "0"+date
                            else:

                                reDate = date

                        userDate = year+"-"+reMonth+"-"+reDate
                        while True:
                            if data[i]["date"] == userDate:
                                holdIndex.append(i)

                            i += 1
                            if i >= len(data):
                                break


                        i = 0
                        if len(holdIndex) == 0:
                            print("Not Found!")
                        else:
                            while i < len(holdIndex):
                                data.remove(data[holdIndex[i]])

                                with open("detail.json", "w") as file:
                                    json.dump(data, file, indent=4)
                                i += 1
                            print("Successfully Deleted")



                else:
                    print("Please Enter the Right Month")

            else:
                print("Please Enter the Right Year!")



        else:
            print("Please Enter the Right Number!")






