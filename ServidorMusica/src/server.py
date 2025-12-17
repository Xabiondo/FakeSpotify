from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import yt_dlp
from ytmusicapi import YTMusic

app = FastAPI()

# Inicializamos (location a veces ayuda, pero la búsqueda es universal)
ytmusic = YTMusic(language='es', location='ES')


# --- MODELOS ---
class VideoRequest(BaseModel):
    url: str


# --- ENDPOINT 1: DESCARGAR ---
@app.post("/descargar")
async def descargar_mp3(request: VideoRequest):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'descargas/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }

    try:
        print(f"Descargando: {request.url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([request.url])
        return {"status": "success", "mensaje": "Descarga completada"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# --- ENDPOINT 2: VIRALES (Modo Búsqueda) ---
@app.get("/virales")
async def obtener_virales():
    try:
        print("Buscando éxitos en España...")

        # ESTRATEGIA SEGURA: Usar el buscador en lugar de los charts
        # Buscamos "Top España" y filtramos solo por "songs" (canciones)
        # limit=20 para tener margen por si alguna falla
        resultados = ytmusic.search("Top España", filter="songs", limit=20)

        lista_limpia = []

        # Procesamos los 10 primeros resultados válidos
        contador = 1
        for track in resultados:
            if contador > 10:
                break

            # Solo procesamos si tiene videoId (es reproducible)
            if 'videoId' in track:

                # Gestión segura de imagen
                imagen = ""
                if 'thumbnails' in track and track['thumbnails']:
                    imagen = track['thumbnails'][-1]['url']

                # Gestión segura de artista
                artista = "Desconocido"
                if 'artists' in track and track['artists']:
                    artista = track['artists'][0]['name']

                item = {
                    "posicion": contador,
                    "titulo": track.get('title'),
                    "artista": artista,
                    "video_id": track.get('videoId'),
                    "url_youtube": f"https://www.youtube.com/watch?v={track.get('videoId')}",
                    "imagen": imagen
                }

                lista_limpia.append(item)
                contador += 1

        return {"top_10": lista_limpia}

    except Exception as e:
        print(f"Error búsqueda: {e}")
        raise HTTPException(status_code=500, detail=f"Error buscando canciones: {str(e)}")