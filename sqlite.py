from tkinter import ttk
from tkinter import * #imports everything for the window, like buttons
import sqlite3

class Student: 

    db_name = 'database.db'

    def __init__(self, window): 
        self.wind = window
        self.wind.title('Attendance Application')

        #creating a frame container. Here we insert elements like buttons
        frame = LabelFrame(self.wind, text = 'Register Your Attendance') #Frame inside main window
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        #Name Input
        Label(frame, text = 'Name: ').grid(row=1, column = 0, )
        self.name = Entry(frame)
        self.name.focus
        self.name.grid(row = 1, column = 1)

        #Assistance Input
        Label(frame, text = 'Assistance: 1 if present, 0 if absent: ').grid(row = 2, column = 0)
        self.assistance = Entry(frame)
        self.assistance.grid(row = 2, column = 1)

        #Button Add Student
        ttk.Button(frame, text = 'Add Student', command = self.add_student).grid(row = 3, columnspan = 2, sticky = W + E)
                   
        #Table
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Name', anchor = CENTER)
        self.tree.heading('#1', text = 'Assistance', anchor = CENTER)

        self.get_assistance

    def run_query(self, query, parameters = ()): #run query
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit
        return result
    
    def get_assistance(self):
         #cleaning table
         records = self.tree.get_children #gets all the data in the table
         for element in records:
            self.tree.delete(element)
         #quering data    
         query = 'SELECT * FROM students'
         db_rows = self.run_query(query)
         for row in db_rows:
            self.tree.insert('', 0, text = row[1], values = row[2])

    #Validation
    def validation(self):
        return len(self.name.get()) != 0 and len(self.assistance.get()) != 0
   
    def add_student(self):
        if self.validation():
            print(self.name.get())
            print(self.assistance.get())
        else:
            print('Name and Assistance are required')


if __name__ == '__main__':
    window = Tk()
    application = Student(window)
    window.mainloop()

