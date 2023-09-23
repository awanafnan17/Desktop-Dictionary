import json
from tkinter import *
from PIL import Image, ImageTk
from difflib import get_close_matches

windows = Tk()
data = json.load(open("data.json"))
    
def display_text():
   global entry
   string= entry.get()
   label.configure(text=string)

def diction(word):
    if word.casefold() in data:
        output.delete(1.0, END)
        output.config(fg="#fff")
        output.insert(END, data[word])
    elif len(get_close_matches(word, data.keys())) > 0:
        output.config(fg='red')
        output.delete(1.0, END)
        output.insert(END, "Did you mean {} to mean: {}".format(get_close_matches(word, data.keys())[0], data[get_close_matches(word, data.keys())[0]]))
        out = get_close_matches(word, data.keys())
        

# height = 650
# width = 358

windows.title("Afnan's Dictionary")
# windows.geometry("812x812")
image = Image.open('backc.png')
photo_Image = ImageTk.PhotoImage(image)

# windows.attributes("-fullscreen", True)
label = Label(windows, image=photo_Image)
label.pack(pady=0)

entryVariable = StringVar()
entry= Entry(windows, textvariable=entryVariable, bg="#FFFD38", fg="black", justify=CENTER, font=("Arial", 28))
entry.place(relx=.185, rely=.70, relwidth=.63, relheight=.082)

butt1 = Button(windows, text= "Search", bg="green", fg="white", justify=CENTER, font=("Courier", 30, "bold"), command= lambda : diction(entryVariable.get()))
butt1.place(relx=.40, rely=.85, relwidth=.2, relheight=.052)

output = Text(windows, fg='#fff', relief=FLAT, bg="#444444", font=("Courier", 20, "bold"))
output.place(relx=.185, rely=.09, relwidth=.63, relheight=.20)


windows.mainloop()