# Importamos el nombre correcto de la función
from server import descargar_audio

def run():
    print("--- BIENVENIDO AL DESCARGADOR DE MP3 (320kbps) ---")
    url_usuario = input("Introduce la URL de YouTube: ").strip()

    if url_usuario:
        # Usamos la función correcta
        resultado = descargar_audio(url_usuario)
        print(resultado)
    else:
        print("URL no válida.")

if __name__ == "__main__":
    run()