import customtkinter as ctk
from server import descargar_audio

def iniciar_descarga():
    url = entry_url.get()
    if url:
        label_estado.configure(text="Descargando... por favor espera", text_color="orange")
        app.update() # Refresca la UI
        resultado = descargar_audio(url)
        label_estado.configure(text=resultado, text_color="green")
    else:
        label_estado.configure(text="¡Pega una URL primero!", text_color="red")

# Configuración de la ventana
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("YouTube to MP3 Downloader")
app.geometry("500x300")

# Elementos de la interfaz
label_titulo = ctk.CTkLabel(app, text="MP3 Downloader (320kbps)", font=("Arial", 20, "bold"))
label_titulo.pack(pady=20)

entry_url = ctk.CTkEntry(app, placeholder_text="Pega el enlace de YouTube aquí", width=400)
entry_url.pack(pady=10)

btn_descargar = ctk.CTkButton(app, text="Descargar MP3", command=iniciar_descarga, fg_color="#cc0000", hover_color="#ff0000")
btn_descargar.pack(pady=20)

label_estado = ctk.CTkLabel(app, text="")
label_estado.pack(pady=10)

app.mainloop()