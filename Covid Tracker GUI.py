from covid import Covid
import tkinter as tk

covid=Covid()

#https://pypi.org/project/covid/
HEIGHT = 500
WIDTH = 600

def get_info(country):
    infos=covid.get_status_by_country_name(country)
    print (infos)
    final_str = 'Country: %s \nConfirmed: %s \nActive: %s \nDeath: %s \nRecovered: %s' % (infos["country"], infos["confirmed"], infos["active"],infos["deaths"],infos["recovered"])
    labelResults['text']=final_str


def list_countries():
    countries = covid.list_countries()
    print(countries)
    final_str=""
    i=0
    for c in countries:
        i=i+1
        final_str += ' %s  '%(c['name'])
        if i==9:
            final_str +='\n'
            i=0
    labelResults['text']=final_str




root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


upper_frame = tk.Frame(root, bg='#A63821', bd=5)
upper_frame.place(relx=0.5, rely=0.1, relwidth=0.85, relheight=0.1, anchor='n')

countryNameEntry = tk.Entry(upper_frame, font=40)
countryNameEntry.place(relwidth=0.5, relheight=1)

butnGetInfo = tk.Button(upper_frame, text="Get INFO", font=40, command=lambda: get_info(countryNameEntry.get()))
butnGetInfo.place(relx=0.8, relheight=1, relwidth=0.2)

butnGetList = tk.Button(upper_frame, text="List", font=40, command=lambda: list_countries())
butnGetList.place(relx=0.55, relheight=1, relwidth=0.2)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.85, relheight=0.7, anchor='n')

labelResults = tk.Label(lower_frame, font=40)
labelResults.place(relwidth=1, relheight=1)

root.mainloop()
