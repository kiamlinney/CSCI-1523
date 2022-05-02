'''
Program: Programming Project #3, file: PP03Csci1523Spr2022.txt
Author: Liam Kinney
Date: 04/11/2022
Purpose: Continuation of Programming Project 2, analyze the contents of auhtlog.txt
Steps:
1. Prepare a GUI front end that will allow a user to enter a beginning date into a input box and an ending 
date into an input box.
2. Using the two dates entered write a Python script that opens the file and retrieves all the logon attempts 
within the date range provided.
3. Extract the following from each line: date, time, IP address and username. 
3. Place data into a scroll box so that the user can scroll forward and back to review the data.

Extra credit: Be able to click on each row of data and have additional information output.
'''

import re
from breezypythongui import EasyFrame
from tkinter import ANCHOR

with open ("authlog.txt", "r") as file:
    read_lines = file.readlines()

class ipParser(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, width = 700, height = 500, title = "Programming Project 3 - Liam Kinney")
        self.addLabel(font = ("Avenir", 20, "bold"), text = "CSCI 1523 - Search authlog.txt file", row = 0, column = 0, columnspan = 5, sticky = "NSEW", foreground = "black")

        self.addLabel(font = ("Avenir", 18, "italic"), text = "Start Date:", row = 2, column = 0, columnspan = 2, sticky = "NEW")
        startTextField = self.startDate = self.addTextField(text = "", row = 2, column = 3, sticky = "NEW")
        startTextField["foreground"] = "black"
        startTextField["background"] = "powderblue"
        startTextField["insertbackground"] = "black"

        self.addLabel(text = "Format: M/D", font = ("Avenir", 12), row = 2, column = 3, sticky = "EW", foreground = "lightgray")

        self.addLabel(font = ("Avenir", 18, "italic"), text = "End Date:", row = 2, column = 0, columnspan = 2, sticky = "SEW")
        endTextField = self.endDate = self.addTextField(text = "", row = 2, column = 3, sticky = "SEW")
        endTextField["foreground"] = "black"
        endTextField["background"] = "powderblue"
        endTextField["insertbackground"] = "black"

        searchButton = self.addButton(text = "Search", row = 2, column = 4, command = self.search)
        searchButton["foreground"] = "black"
        searchButton["font"] = "Avenir", 15, "bold"

        self.addLabel(font = ("Avenir", 18), text = "Login Attempts", row = 3, column = 0, columnspan = 5, sticky = "EW")
        listBox = self.loginAttempts = self.addListbox(row = 4, column = 3)
        listBox["foreground"] = "black"
        listBox["background"] = "powderblue"    

        global ports
        ports = []
        def moreInformation():
            lineNumber = int(listBox.get(ANCHOR).split(")")[0])
            line = listBox.get(ANCHOR).split(" ")
            self.addLabel(font = ("Avenir", 14), text = (f"More from {line[1]} {line[3]} {line[4]}:\nPort: {ports[lineNumber-1]}"), row = 5, column = 3, sticky = "NEW")

        moreInfoButton = self.addButton(text = "More Info", row = 5, column = 0, command = moreInformation)
        moreInfoButton["foreground"] = "black"
        moreInfoButton["font"] = "Avenir", 14, "bold"

    def search(self):
        def dateConvert(date):
            def getMonth(date):
                if date == 1: return "Jan"
                elif date == 2: return "Feb"
                elif date == 3: return "Mar"
                elif date == 4: return "Apr"
                elif date == 5: return "May"
                elif date == 6: return "Jun"
                elif date == 7: return "Jul"
                elif date == 8: return "Aug"
                elif date == 9: return "Sep"
                elif date == 10: return "Oct"
                elif date == 11: return "Nov"
                elif date == 12: return "Dec"

            pdate = date.partition("/")
            if int(pdate[2]) < 10:
                return getMonth(int(pdate[0])) + "  " + pdate[2]
            elif int(pdate[2]) >= 10:
                return getMonth(int(pdate[0])) + " " + pdate[2]

        start_date = dateConvert(self.startDate.getText())
        end_date = dateConvert(self.endDate.getText())

        ip_list = []
        times = []
        for i in reversed(read_lines):
            pattern = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", i)
            port_pattern = re.search(r"port\s(\d{1,5})", i)
            if start_date in i:
                if pattern:
                    ip_list.append(pattern.group(1))
                    times.append(self.startDate.getText() + " " + (i[6:15]))
                    if port_pattern:
                        ports.append(port_pattern.group(1))
                    else:
                        ports.append("No port found")
            if end_date in i:
                if pattern:
                    ip_list.append(pattern.group(1))
                    times.append(self.endDate.getText() + " " + (i[6:15]))
                    if port_pattern:
                        ports.append(port_pattern.group(1))
                    else:
                        ports.append("No port found")
        
        data = {}
        for value, key in enumerate(times):
            data[key] = ip_list[value]
    
        self.loginAttempts.clear()
        final_data = [str(key) + " " + str(value) + " root" for key, value in data.items()]
        for x, key in enumerate(data):
            self.loginAttempts.insert(x, (f"{x+1}) " + final_data[x]))
        
def main():
    ipParser().mainloop()
if __name__ == "__main__":
    main()