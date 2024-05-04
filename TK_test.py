# 开发者：ByShook
# 开发时间：2024/5/4 上午1:52
from tkinter import *
from tkinter import messagebox

root = Tk()

brn01 = Button(root)
brn01["text"] = "点我就送花"

brn01.pack()


def songhua(e):
    messagebox.showinfo("Message", "songhua")
    print("songhua")


brn01.bind("<Button-1>", songhua)

root.mainloop()
