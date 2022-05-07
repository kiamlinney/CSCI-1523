'''
Program: Programming Project #4
Author: Liam Kinney
Date: 5/2/2022
Purpose: Continuation of project 2 and 3. Search files in the /var/log directory on a Linux machine. 
1. Using the /var/log/auth.log file, prepare a program that will display the date of the first record, the last record, 
and the total number of lines in the file. Also, prepare a GUI that will allow the user to scroll through all records in which 
the vim editor was used to access the /etc/apt/sources.list file.
2. Using the /var/log/message file, prepare a program that will display the date of the first record, the last record, 
and the total number of lines in the file. Also, prepare a GUI that will allow the user to scroll through all of the lines within
the file that contain the string ”notepad-plus-plus".
3. Using the /var/log/syslog file, prepare a program that will display the date of the first record, the last record, 
and the total number of lines in the file. Also, prepare a GUI that will allow the user to scroll through all of the lines that
contain the string ”rtkit".
'''

from breezypythongui import EasyFrame
from tkinter import END

with open ("/var/log/auth.log", "r") as authlog:
    read_auth_lines = authlog.readlines()
with open("/var/log/message", "r") as message:
    read_msg_lines = message.readlines()
with open("/var/log/syslog", "r") as syslog:
    read_sys_lines = syslog.readlines()

class FileSearch(EasyFrame):
    def __init__(self):
        bg = "powderblue"
        EasyFrame.__init__(self, width = 700, height = 500, title = "CSCI 1523, Assignment #4 - Liam Kinney", background = bg)
        self.addLabel(font = ("Avenir", 18, "bold"), text = "CSCI 1523 - Assignment #4", row = 0, column = 0, columnspan = 5, sticky = "NSEW", foreground = "black", background = bg)

        self.addLabel(font = ("Avenir", 16, "italic"), text = "Log file:", row = 2, column = 0, sticky = "NEW", background = bg)
        logFile = self.logFile = self.addTextField(text = "", row = 2, column = 3, sticky = "NEW", state = "readonly")
        logFile["foreground"] = "black"

        self.addLabel(font = ("Avenir", 16, "italic"), text = "Date of First Record:", row = 2, column = 0, sticky = "EW", background = bg)
        firstRecord = self.firstDate = self.addTextField(text = "", row = 2, column = 3, sticky = "EW", state = "readonly")
        firstRecord["foreground"] = "black"

        self.addLabel(font = ("Avenir", 16, "italic"), text = "Date of Last Record:", row = 2, column = 0, columnspan = 2, sticky = "SEW", background = bg)
        lastRecord = self.lastDate = self.addTextField(text = "", row = 2, column = 3, sticky = "SEW", state = "readonly")
        lastRecord["foreground"] = "black"

        self.addLabel(font = ("Avenir", 16, "italic"), text = "Number of Records:", row = 3, column = 0, columnspan = 2, sticky = "NEW", background = bg)
        numRecords = self.numRecords = self.addTextField(text = "", row = 3, column = 3, sticky = "NEW", state = "readonly")
        numRecords["foreground"] = "black"

        self.addLabel(font = ("Avenir", 16), text = "Relavent Records", row = 3, column = 0, columnspan = 5, sticky = "SEW", background = bg)
        listBox = self.loginAttempts = self.addListbox(row = 4, column = 3)
        listBox["foreground"] = "white"
        listBox["background"] = "black"    

        menuBar = self.addMenuBar(row = 4, column = 4)
        fileMenu = menuBar.addMenu("          Select the file          ")
        fileMenu["foreground"] = "black"
        fileMenu["font"] = "Avenir", 15
        fileMenu.addMenuItem("auth.log", command = self.authlog)
        fileMenu.addMenuItem("message", command = self.message)
        fileMenu.addMenuItem("syslog", command = self.syslog)
    
    def authlog(self):
        first_auth_line = read_auth_lines[0]
        last_auth_line = read_auth_lines[-1]
        total_lines = 0

        self.loginAttempts.clear()
        for i in (read_auth_lines):
            total_lines += 1
            first_date = first_auth_line[:15]
            last_date = last_auth_line[:15]
            self.firstDate.setText(first_date)
            self.lastDate.setText(last_date)
            self.numRecords.setText(total_lines)
            self.logFile.setText("/var/log/auth.log")
    
            if "vim" and "sources.list" in i:
                self.loginAttempts.insert(END, i)

    def message(self):
        first_msg_line = read_msg_lines[0]
        last_msg_line = read_msg_lines[-1]
        total_lines = 0

        self.loginAttempts.clear()
        for i in (read_msg_lines):
            total_lines += 1
            first_date = first_msg_line[:15]
            last_date = last_msg_line[:15]
            self.firstDate.setText(first_date)
            self.lastDate.setText(last_date)
            self.numRecords.setText(total_lines)
            self.logFile.setText("/var/log/message")
            
            if "notepad-plus-plus" in i:
                self.loginAttempts.insert(END, i)

    def syslog(self):
        first_sys_line = read_sys_lines[0]
        last_sys_line = read_sys_lines[-1]
        total_lines = 0

        self.loginAttempts.clear()
        for i in (read_sys_lines):
            total_lines += 1
            first_date = first_sys_line[:15]
            last_date = last_sys_line[:15]
            self.firstDate.setText(first_date)
            self.lastDate.setText(last_date)
            self.numRecords.setText(total_lines)
            self.logFile.setText("/var/log/syslog")
            
            if "rtkit" in i:
                self.loginAttempts.insert(END, i)
            
def main():
    FileSearch().mainloop()
if __name__ == "__main__":
    main()
