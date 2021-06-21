import google
import re
import tkinter as tk
import os
import shutil
import glob

import xlwt
from xlwt import Workbook

wb = Workbook()

HEIGHT = 600
WIDTH = 800



def get_results(num_page,search_string,excel_file):
    ws = wb.add_sheet(excel_file)
    label_log['text']="getting emails"

    try:
        num_page = int(num_page)
    except:
        label_log['text']="make sure the number of pages is a number, 4 is assigned"
        num_page=4


    emails=[]
    emails_Sorted=[]


    search_results = google.search(search_string, num_page)
    print (search_results)
    for res in search_results:
        emails.append(  re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', res.description)   )



    for i in range (len(emails)):
        try:
            emails_Sorted.append (emails[i][0])
        except:
            continue
    print(emails_Sorted)


    if emails_Sorted == []:
        label_log['text']="too many requests sent, try again later"
    else:
        for i in range (len(emails_Sorted)):
            ws.write(i,0,emails_Sorted[i])
        try:
            wb.save(excel_file)
            label_log['text']="excel file saved"
        except:
            label_log['text']="make sure the excel file is closed and try again"



root = tk.Tk()
root.title('My Title')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH ,bg='grey',)
canvas.pack()

intro_frame = tk.Frame(root, bg='#80c1ff', bd=5)
intro_frame.place(relx=0.5, rely=0.1, relwidth=0.95, relheight=0.2, anchor='n')

label = tk.Label(intro_frame,text="Get emails app", font= ('Helvetica', 20, 'bold'))
label.place(relx=0.5, relwidth=1, relheight=1, anchor='n')

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.45, relwidth=0.95, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)
entry.insert(0,"“Realtor” Location: UK “@hotmail”")

button = tk.Button(frame, text="SEARCH", font=40, command=lambda: get_results(num_pages_source.get(),entry.get(),excel_file_name.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

second_frame = tk.Frame(root, bg='#80c1ff', bd=5)
second_frame.place(relx=0.5, rely=0.65, relwidth=0.95, relheight=0.2, anchor='n')

num_pages_source = tk.Entry(second_frame, font=40)
num_pages_source.insert(0,'4')
num_pages_source.place(relx=0.18,rely=0.05,relwidth=0.5, relheight=0.4)

label_pages = tk.Label(second_frame,text="# pages")
label_pages.place(relx=0,rely=0.05,relwidth=0.15, relheight=0.4)

label_excel = tk.Label(second_frame,text="excel file name")
label_excel.place(relx=0,rely=0.5,relwidth=0.15, relheight=0.4)

excel_file_name = tk.Entry(second_frame, font=40)
excel_file_name.place(relx=0.18,rely=0.5,relwidth=0.5, relheight=0.4)
excel_file_name.insert(0,'mailing_list.xls')

log_frame = tk.Frame(root, bg='#80c1ff', bd=5)
log_frame.place(relx=0.5, rely=0.87, relwidth=0.95, relheight=0.1, anchor='n')

label_log = tk.Label(log_frame)
label_log.place(relx=0.5, relwidth=1, relheight=1, anchor='n')

root.mainloop()


"""
Support:
https://stackoverflow.com/questions/17681670/extract-email-sub-strings-from-large-document

dependencies:
pip3 install xlwt

"""
