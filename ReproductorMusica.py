from pygame import mixer
from tkinter import *

#Funciones

reproduccion = True

def resume():
    print(btn.cget('text'))
    if (btn.cget('text') == '|>'):
       mixer.music.pause()
       btn.configure(text = "||")
    else:
        mixer.music.unpause()
        btn.configure(text = "|>")
        

#Configuracion interfaz
window = Tk()
window.title("Reproductor de musica")
window.geometry("300x200")

# Botones
btn = Button(window, text="|>", command=resume, bg="red", width = 2, height= 2, font=("Courier", 44))
btn.grid(column=2, row=0)


#---------------------------



mixer.init()

mixer.music.load("C:\\Users\\Dell\\Downloads\\Love Never Felt So Good.mp3")
mixer.music.set_volume(3)
mixer.music.play()



while True:
    print("Presiona 'p' para pausar y 'r' para reanudar.")
    print("Presiona 'e' para salir del programa.")
    print("Presiona 's' para cambiar el volumen")
    query = input(">>> ")
    if query == 'p':
        mixer.music.pause()
    elif query == 'r':
        mixer.music.unpause()
    elif query == 's':
        new_volume = float(input("Ingrese el numero de volumen"))
        mixer.music.set_volume(new_volume)
    elif query == "e":
        mixer.music.stop()
        break
     