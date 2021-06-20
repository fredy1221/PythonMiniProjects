import pywhatkit as whatsapp
import pyautogui as pg
import time
import os
import openpyxl
import pandas as pd

APP_PATH= 'C:\\Users\\User\\Desktop\\freelance\\covid_tool\\results.xlsx' #path to the spreadsheet where the contacts are stored
message1 = "The COVID-19 test result for the client "
message2 = " came back "
message3 = ", thank you!"

names=[]
numbers=[]
results=[]

wb_obj = openpyxl.load_workbook(APP_PATH)
sheet = wb_obj.active

list_iterator = iter(sheet.iter_rows())
next(list_iterator)

for row in list_iterator:
    names.append(row[0].value)
    numbers.append(row[1].value)
    results.append(row[2].value)
print(names,numbers,results)

for i in  range(len(numbers)):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    hour = int(current_time[0] + current_time[1])
    minute = int(current_time[3] + current_time[4])+1

    whatsapp.sendwhatmsg("+"+str(int(numbers[i])),message1+names[i]+message2+results[i]+message3,hour,minute)
    pg.press("enter")
