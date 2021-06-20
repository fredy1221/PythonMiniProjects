import tkinter as tk
import os
import shutil
import glob

HEIGHT = 600
WIDTH = 800


def rename_files(path):
    counter=0
    if os.path.isdir(path):
        for filename in os.listdir(path):
            filename_without_ext = filename.split(".")[0]
            extension = filename.split(".")[1]
            if extension=="jpg" or extension=="jpeg" or extension=="png":
                counter+=1
                new_file_name = "photo_"+str(counter)
                new_file_name_with_ext = new_file_name+"."+extension
                print(new_file_name_with_ext)
                os.rename(os.path.join(path,filename),os.path.join(path,new_file_name_with_ext))
        label_log['text']= "Files renamed"
    else:
        label_log['text']="Enter valid path for rename files"

def move_files(srcDir, dstDir):
    # Check if both the are directories
    if os.path.isdir(srcDir):
        if os.path.isdir(dstDir) == False:
            try:
                os.mkdir(dstDir)
                label_log['text']="destination directory created"
            except:
                label_log['text']="Enter valid destination path to move files"
        else:
            for filename in os.listdir(srcDir):
                try:
                    name = filename.split(".")[0]
                    extension = filename.split(".")[1]
                except:
                    name = filename
                    extension = 'folders'
                destination = dstDir + "\\" + extension
                if not os.path.exists(destination):
                    os.mkdir(destination)
                    print("Directory " , destination ,  " Created ")
                else:
                    print("Directory " , destination ,  " already exists")

                shutil.move(srcDir+"//"+filename, destination)
            label_log['text']= "Files moved"
    elif os.path.isdir(srcDir) == False:
        label_log['text']="Enter valid source path to move files"



root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH ,bg='grey',)
canvas.pack()

# background_image = tk.PhotoImage(file='landscape.png')
# background_label = tk.Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)

intro_frame = tk.Frame(root, bg='#80c1ff', bd=5)
intro_frame.place(relx=0.5, rely=0.1, relwidth=0.95, relheight=0.2, anchor='n')

label = tk.Label(intro_frame,text="MOVE OR RENAME APP", font= ('Helvetica', 20, 'bold'))
label.place(relx=0.5, relwidth=1, relheight=1, anchor='n')


frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.45, relwidth=0.95, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Rename Files", font=40, command=lambda: rename_files(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)



second_frame = tk.Frame(root, bg='#80c1ff', bd=5)
second_frame.place(relx=0.5, rely=0.65, relwidth=0.95, relheight=0.2, anchor='n')

move_entry_source = tk.Entry(second_frame, font=40)
move_entry_source.place(relx=0.18,rely=0.05,relwidth=0.5, relheight=0.4)

label_src = tk.Label(second_frame,text="Source")
label_src.place(relx=0,rely=0.05,relwidth=0.15, relheight=0.4)

label_src = tk.Label(second_frame,text="Destination")
label_src.place(relx=0,rely=0.5,relwidth=0.15, relheight=0.4)

move_entry_dest = tk.Entry(second_frame, font=40)
move_entry_dest.place(relx=0.18,rely=0.5,relwidth=0.5, relheight=0.4)

move_button = tk.Button(second_frame, text="Move Files", font=40, command=lambda: move_files(move_entry_source.get(),move_entry_dest.get()))
move_button.place(relx=0.7, relheight=1, relwidth=0.3)


log_frame = tk.Frame(root, bg='#80c1ff', bd=5)
log_frame.place(relx=0.5, rely=0.87, relwidth=0.95, relheight=0.1, anchor='n')

label_log = tk.Label(log_frame)
label_log.place(relx=0.5, relwidth=1, relheight=1, anchor='n')


# lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
# lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')



root.mainloop()
