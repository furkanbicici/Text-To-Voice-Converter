from gtts import gTTS
import tkinter
import os

window = tkinter.Tk()
window.title("Text To Voice")
window.config(padx=30, pady=30)

def text_voice():
    input_text = my_entry.get()
    language = "tr"
    speech = gTTS(text=input_text, lang=language, slow=False)
    speech.save("media.mp4")
    os.system("start media.mp4")

#ui

my_label = tkinter.Label(text="Lütfen Metni Giriniz ")
my_label.pack()

my_entry = tkinter.Entry(width=20)
my_entry.pack()

my_button = tkinter.Button(text="Dönüştür", command=text_voice)
my_button.pack()

window.mainloop()


