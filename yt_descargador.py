from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from pytube import YouTube
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
import threading
import datetime

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
label_duracion = Label(frame, text="", font=("Arial bold", 10))
#label_descripcion = Label(frame, text="", font=("Arial bold", 10), width=100)
#label_miniatura = Label(frame, image = None)
error_label= Label(frame, text= "", font=("Arial bold", 20))

def buscar(link_video):
    try:
        error_label['text'] = ""
        hilo1 = threading.Thread(target=buscar_video(link_video),args=link_video)
        #buscar_video(link_video)
        hilo1.start()
    except:
        error_label['text'] = "Ha ocurrido un error"
        error_label.place(x=350, y=180)
        #error_img = PhotoImage(file="images/error_img.png")
        #label_miniatura_err = Label(frame, image = error_img)
        #label_miniatura_err.place(x= 100, y=140)
        err_img = Image.open("images/error_img.png")
        err_img = err_img.resize((210,118), Image.ANTIALIAS)
        photo_err = ImageTk.PhotoImage(image=err_img)
        label_miniatura_err = Label(frame, image = photo_err)
        label_miniatura_err.image = photo_err
        label_miniatura_err.place_configure(width=210, height=118, x= 100, y=140)
        

boton_buscar = Button(frame, text="Buscar", width=10, font=("Arial bold", 15), fg="white", bg="#c4302b", command=lambda:buscar(link_video)).place(x=600, y=80)


def buscar_video(link_video):
 
    global url 
    url = YouTube(str(link_video.get()), on_progress_callback=progreso)
    video = url.streams.get_highest_resolution()
    titulo = url.title
    duracion = str(datetime.timedelta(seconds=url.length))
    #descripcion = url.description
    url_min = url.thumbnail_url
    u = urlopen(url_min)
    raw_data = u.read()
    u.close()
    im = Image.open(BytesIO(raw_data))
    im = im.resize((210,118), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(im)
    label_miniatura = Label(frame, image = img)
    label_miniatura.image = img
    label_titulo['text'] = titulo
    label_duracion['text'] = "Duraci??n: " + duracion
    #label_descripcion['text'] = descripcion
    #label_titulo = Label(frame, text=titulo, font=("Arial bold", 10))
    global b_progreso
    b_progreso = ttk.Progressbar(frame, orient="horizontal", length=400)
    boton_descargar = Button(frame, width=20, text = "Descargar", fg="white", bg="#8DB600", command=lambda:descargar(video))
    label_titulo.place(x=350, y=140)
    label_duracion.place(x=350, y=160)
    #label_descripcion.place(x=350, y=180)
    label_miniatura.place_configure(width=210, height=118, x= 100, y=140)
    
    boton_descargar.place(x=350, y=210)
    
    
def descargar(video):
    #b_progreso.place(x=200, y=300)
    hilo = threading.Thread(target=descargar_video(video), args=video)
    hilo.start()

def descargar_video(video):
    video.download()
    messagebox.showinfo("Descarga completa", "??Descarga completada con ??xito!")
 

def progreso(stream=None, chunk=None, file_handle=None, bytes_remaining=None):
    pass
    #b_progreso.step(int(100 - (100*(bytes_remaining))))




root.mainloop()
