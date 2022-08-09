import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from xml.etree import ElementTree
import csv


# create the root window
root = tk.Tk()
root.title('XML to Azure CSV Converter')
root.resizable(False, False)
root.geometry('300x150')


def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('xml files', '*.xml*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )
    parse_xml(filename)

# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)

def parse_xml(filePath):
    # PARSE XML
    xml = ElementTree.parse(filePath)

    # CREATE CSV FILE
    csvfile = open("food_data.csv",'w',encoding='utf-8')
    csvfile_writer = csv.writer(csvfile)

    # ADD THE HEADER TO CSV FILE
    csvfile_writer.writerow(["name","price","description", "calories"])

    # FOR EACH FOOD
    for food in xml.findall("food"):
        
        if(food):
            # EXTRACT FOOD DETAILS  
            name = food.find("name")
            price = food.find("price")
            description = food.find("description")
            calories = food.find("calories")
            csv_line = [name.text, price.text, description.text, calories.text]

        # ADD A NEW ROW TO CSV FILE
        csvfile_writer.writerow(csv_line)
    csvfile.close()  


# run the application
root.mainloop()