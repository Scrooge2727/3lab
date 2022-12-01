from this import d
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import redis


client = redis.Redis(
    host="apn1-pro-raccoon-34089.upstash.io",
    port="34089",
    password="66fff6635b254c1082e4c956bd376004",
)
# client.set('user1', 'Arial 12 normal blue')
# client.set('user2','')
# client.set('user3', 'Arial 12 normal blue')


# print(client.get('user1'))

root = tk.Tk()

root.title("lab1 Redisneww")
root.geometry("1200x600")

text = tk.StringVar()
label_wwod2 = tk.Label(textvariable=text, font="Arial")
label_wwod2.grid(row=5, column=3)
label_wwod = tk.Label(text="", font="Arial")
label_wwod.grid(row=5, column=2)
entry_wwod = tk.Entry(font="Arial", foreground="black", textvariable=text)
entry_wwod.grid(row=5, column=1)
warning_label = tk.Label(text="")
warning_label.grid(row=5, column=4)


def connection():
    warning_label.config(text="")
    shrift = entry_shrift.get()
    size = entry_size.get()
    nachert = entry_nachert.get()
    color = entry_color.get()
    if size.isdigit() == False or size == "":
        warning_label.config(text="Ошибка")
        return
    if (
        any(map(str.isdigit, shrift)) == True
        or shrift == ""
        or nachert == ""
        or color == ""
        or any(map(str.isdigit, nachert)) == True
        or any(map(str.isdigit, color)) == True
    ):
        warning_label.config(text="Ошибка")
        return

    rez = (
        entry_shrift.get()
        + " "
        + entry_size.get()
        + " "
        + entry_nachert.get()
        + " "
        + entry_color.get()
    )
    client.set(comboBox.get(), rez)
    strin = str(rez)
    i = len(strin) - 1
    while i > 0:
        if strin[i] == " ":
            break
        i = i - 1
    str1 = ""
    str2 = ""
    j = 0
    while j < i:
        str1 = str1 + strin[j]
        j = j + 1
    i = i + 1
    while i < len(strin):
        str2 = str2 + strin[i]
        i = i + 1
    entry_shrift.delete(0, tk.END)
    entry_shrift.insert(0, shrift)
    entry_size.delete(0, tk.END)
    entry_size.insert(0, size)
    entry_nachert.delete(0, tk.END)
    entry_nachert.insert(0, nachert)
    entry_color.delete(0, tk.END)
    entry_color.insert(0, str2)
    label_wwod2.config(font=(shrift, size, nachert), foreground=str2)


def callbackFunc(event):

    qq = client.get(comboBox.get())
    strin = str(qq)
    i = len(strin) - 1
    while i > 0:
        if strin[i] == " ":
            break
        i = i - 1
    str1 = ""
    str2 = ""
    j = 0
    while j < i:
        str1 = str1 + strin[j]
        j = j + 1
    i = i + 1
    while i < len(strin) - 1:
        str2 = str2 + strin[i]
        i = i + 1

    i = len(str1) - 1
    while i > 0:
        if str1[i] == " ":
            break
        i = i - 1
    str3 = ""
    nachert = ""
    j = 0
    while j < i:
        str3 = str3 + str1[j]
        j = j + 1

    i = i + 1
    while i < len(str1):
        nachert = nachert + str1[i]
        i = i + 1

    i = len(str3) - 1
    while i > 0:
        if str3[i] == " ":
            break
        i = i - 1
    shrift = ""
    size = ""
    j = 0
    while j < i:
        shrift = shrift + str3[j]
        j = j + 1

    i = i + 1
    while i < len(str3):
        size = size + str3[i]
        i = i + 1
    rrr = shrift.replace("b", "", 1)
    rrr = rrr.replace("'", "", 1)
    entry_shrift.delete(0, tk.END)

    entry_shrift.insert(0, rrr)
    entry_size.delete(0, tk.END)
    entry_size.insert(0, size)
    entry_nachert.delete(0, tk.END)
    entry_nachert.insert(0, nachert)
    entry_color.delete(0, tk.END)
    entry_color.insert(0, str2)
    label_wwod2.config(font=(shrift, size, nachert), foreground=str2)


mas = ["user1", "user2", "user3"]

label_comboBox = tk.Label(
    text="Пользователь: ",
    font="Arial",
)
label_comboBox.grid(row=4, column=0)
comboBox = ttk.Combobox(values=mas)
comboBox.grid(row=4, column=1)


shrift = tk.Label(
    text="Название шрифта: ",
    font="Arial",
)
shrift.grid(row=0, column=0)
size = tk.Label(
    text="Размер шрифта: ",
    font="Arial",
)
size.grid(row=1, column=0)
nachert = tk.Label(
    text="Начертание: ",
    font="Arial",
)  # italic - naklon
nachert.grid(row=2, column=0)
label_color = tk.Label(
    text="Цвет: ",
    font="Arial",
)
label_color.grid(row=3, column=0)

comboBox.bind("<<ComboboxSelected>>", callbackFunc)

entry_shrift = tk.Entry(
    font="Arial",
)
entry_shrift.grid(row=0, column=1)
entry_size = tk.Entry(
    font="Arial",
)
entry_size.grid(row=1, column=1)
entry_nachert = tk.Entry(
    font="Arial",
)
entry_nachert.grid(row=2, column=1)
entry_color = tk.Entry(
    font="Arial",
)
entry_color.grid(row=3, column=1)


do_it = tk.Button(text="Enter text", command=connection)
do_it.grid(row=6, column=1)


root.mainloop()
