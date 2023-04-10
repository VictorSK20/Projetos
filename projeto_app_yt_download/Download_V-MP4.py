# Criando um programa de download de videos do Youtube

from tkinter import *
from pytube import YouTube
from tkinter import filedialog, Entry
from pytube.exceptions import RegexMatchError
import time

janela = Tk()
janela.title('Download MP4 - Youtube')


def download(link_):
    if link_:
        try:
            pasta = filedialog.askdirectory()
            YouTube(link_).streams.get_highest_resolution().download(pasta)
            time.sleep(15)
            aviso()
        except RegexMatchError:
            aviso_error()
    else:
        aviso_error()


def aviso():
    janela_msg = Toplevel()
    janela_msg.title('Aviso')
    janela_msg.geometry('300x300')

    Label(janela_msg, text='Download concluído !', font='arial 20', pady=30).pack()

    Button(janela_msg, text='OK', command=janela_msg.destroy).pack()


def aviso_error():
    janela_msg = Toplevel()
    janela_msg.title('Aviso')
    janela_msg.geometry('300x300')

    Label(janela_msg, text='Insira um link valio', font='arial 20', pady=30).pack()

    Button(janela_msg, text='OK', command=janela_msg.destroy).pack()


quadro = Frame(janela)
quadro.pack()

Label(quadro, text='Insira o link: ', font='arial 12 bold').pack(side='left')
link = Entry(quadro, font='arial 20', width=50)
link.pack(side='left')

Button(quadro, bg='green', text='>>>', bd=1, fg='white', width=4, height=2, command=lambda: download(link.get())).pack()

janela.mainloop()

