#импорт модулей
from tkinter import *
from pytube import YouTube

# Регаем окно
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Скачивание видео с ютуба.")
Label(root, text ='Ютуб видео скачка', font ='arial 20 bold').pack()

# flone для ссылки.
def Dowloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADER', font = 'arial 15').place(x=100 , y = 210)
Button (root, text = 'Download', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2,
command = Dowloader).place(x=100, y = 150)
root.mainloop()