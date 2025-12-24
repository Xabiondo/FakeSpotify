
from server import descargar_mp3

def run():
    print("--- BIENVENIDO AL DESCARGADOR DE MP3 (320kbps) ---")
    url_usuario = input("Introduce la URL de YouTube: ").strip()

    if url_usuario:

        resultado = descargar_mp3(url_usuario)
        print(resultado)
    else:
        print("URL no válida.")

if __name__ == "__main__":
    run()