from tkinter import*
from tkinter import ttk
from pytube import YouTube
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
import threading

root = Tk()
root.title("Descargardor de Videos YT")
frame = Frame(root)
frame.config(width=800, height=500)
frame.pack()


link_video = StringVar()
texto_etiqueta = "Inserta el link del video:"
etiqueta_link = Label(frame, text= texto_etiqueta, font=("Arial bold", 20)).place(x=270, y=30)
entrada_link = Entry(frame, width=80, textvariable = link_video).place(x=100, y=90)
#global label_titulo
#global titulo
#titulo = ""
label_titulo = Label(frame, text="", font=("Arial bold", 10))
#label_miniatura = Label(frame, image = None)


def buscar(link_video):
    try:
        hilo1 = threading.Thread(target=buscar_video(link_video),args=link_video)
        #buscar_video(link_video)
        hilo1.start()
    except:
        error_label= Label(frame, text= "Ha ocurrido un error", font=("Arial bold", 20)).place(x=350, y=200)

boton_buscar = Button(frame, text="Buscar", width=10, font=("Arial bold", 15), fg="white", bg="#c4302b", command=lambda:buscar(link_video)).place(x=600, y=80)


def buscar_video(link_video):
 
    global url 
    url = YouTube(str(link_video.get()), on_progress_callback=progreso)
    video = url.streams.get_highest_resolution()
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
    label_titulo['text']=titulo
    #label_titulo = Label(frame, text=titulo, font=("Arial bold", 10))
    global b_progreso
    b_progreso = ttk.Progressbar(frame, orient="horizontal", length=400)
    boton_descargar = Button(frame, width=20, text = "Descargar", fg="white", bg="#8DB600", command=lambda:descargar(video))
    label_titulo.place(x=350, y=140)
    label_miniatura.place_configure(width=210, height=118, x= 100, y=140)
    
    boton_descargar.place(x=350, y=210)
    
    
def descargar(video):
    #b_progreso.place(x=200, y=300)
    hilo = threading.Thread(target=descargar_video(video), args=video)
    hilo.start()

def descargar_video(video):
    video.download()
 

def progreso(stream=None, chunk=None, file_handle=None, bytes_remaining=None):
    pass
    #b_progreso.step(int(100 - (100*(bytes_remaining))))




root.mainloop()
