from cgitb import text
from tkinter import*
from tkinter import ttk
from pytube import YouTube
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO

root = Tk()
root.title("Descargardor de Videos YT")
frame = Frame(root)
frame.config(width=800, height=500)
frame.pack()


link_video = StringVar()
texto_etiqueta = "Inserta el link del video:"
etiqueta_link = Label(frame, text= texto_etiqueta, font=("Arial bold", 20)).place(x=270, y=30)
entrada_link = Entry(frame, width=80, textvariable = link_video).place(x=100, y=90)
boton_descargar = Button(frame, width=20, text = "Descargar", command=lambda:descargar())

def buscar(link_video):
    try:
        buscar_video(link_video)
    except:
        error_label= Label(frame, text= "Ha ocurrido un error", font=("Arial bold", 20)).place(x=350, y=200)

boton_buscar = Button(frame, text="Buscar", width=10, font=("Arial bold", 15), command=lambda:buscar(link_video)).place(x=600, y=80)


def buscar_video(link_video):
    url = YouTube(str(link_video.get()))
    titulo = url.title
    url_min = url.thumbnail_url
    u = urlopen(url_min)
    raw_data = u.read()
    u.close()
    im = Image.open(BytesIO(raw_data))
    im = im.resize((210,118), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(im)
    label_miniatura = Label(frame, image = img)
    label_miniatura.image = img
    label_titulo = Label(frame, text=titulo, font=("Arial bold", 10))
    #boton_descargar = Button(frame, width=20, text = "Descargar", command=lambda:descargar)
    label_titulo.place(x=350, y=140)
    label_miniatura.place_configure(width=210, height=118, x= 100, y=140)
    boton_descargar.place(x=350, y=210)
    
    
def descargar():
    b_progreso = ttk.Progressbar(frame, orient="horizontal", length=400)
    b_progreso.place(x=200, y=300)
    progreso(b_progreso)

def progreso(bp):
    bp.step(20)











root.mainloop()
