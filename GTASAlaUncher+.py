from tkinter import *
import webbrowser, os


def openMod():
    webbrowser.open('https://gta-mania.ru/category/gta-sa/')


def openVK():
    webbrowser.open('https://vk.com/itservice_berdsk')


def openGTASA():
    os.startfile('gta_sa.exe')
    quit()


def openGTASAMP():
    os.startfile('samp.exe')
    quit()


def openDELETE():
    root = Tk()
    root.title('Дополнительная информация')
    root.geometry('350x500')
    root.resizable(width=False, height=False)
    root.iconbitmap('iconlc+.ico')

    lab = Label(root, text='''Доп.информация:

Язык программирования
на котором работает лаунчер:
~~~ Python 3.7.4 32bit ~~~

Модули Python,
используемые в
работе лаунчера:
~~~ tkinter, os, webbrowser ~~~

Разработчик сборки и лаунчера:
~~~ IT сервис | Бердск ~~~

Программист(ы):
~~~ Матвей Воронцов ~~~''')
    lab.config(font=('Times', 18))
    lab.pack()

    root.mainloop()


def openINST():
    os.startfile('инструкция.txt')


window = Tk()
window.title('GTA SA LaUncher+')
window.resizable(width=False, height=False)
window.geometry('650x322')
window.iconbitmap('iconlc+.ico')

photo = PhotoImage(file="fon.png")
one = Label(window, image=photo)
one.image = photo  # just keeping a reference
one.grid()

text1 = Label(window, text='GTA SA LaUncher+', fg='red')
text1.config(font=('Times', 23))
text1.place(x=150, y=5)

text2 = Label(window, text='Сборка GTA SA', fg='red')
text2.config(font=('Times', 20))
text2.place(x=185, y=44)

dev = Button(window, text='Страница разработчика')
dev.config(width=25, height=2, bg='white smoke', fg='black', command=openVK)
dev.place(x=435, y=10)

playClassic = Button(window, text='''Играть в классическую
GTA (GTA SA)''')
playClassic.config(width=25, height=2, bg='white smoke', fg='black', command=openGTASA)
playClassic.place(x=435, y=85)

playMultiplayer = Button(window, text='''Играть в мультиплеерную
GTA (GTA SAMP 0.3.7) - по сети''')
playMultiplayer.config(width=25, height=2, bg='white smoke', fg='black', command=openGTASAMP)
playMultiplayer.place(x=435, y=127)

download = Button(window, text='''Скачать дополнительные
моды (модификации)''')
download.config(width=25, height=2, bg='white smoke', fg='black', command=openMod)
download.place(x=435, y=168)

delete = Button(window, text='''Дополнительная
информация''')
delete.config(width=25, height=2, bg='white smoke', fg='black', command=openDELETE)
delete.place(x=435, y=209)

inst = Button(window, text='Инструкция')
inst.config(width=25, height=2, bg='white smoke', fg='black', command=openINST)
inst.place(x=435, y=250)

text3 = Label(window, text='Created by: IT service Berdsk | Matvey Vorontsov', fg='black')
text3.config(font=('Times', 10))
text3.place(x=375, y=300)

window.mainloop()
