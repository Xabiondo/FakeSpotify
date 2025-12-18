from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import yt_dlp
from ytmusicapi import YTMusic

app = FastAPI()


ytmusic = YTMusic(language='es', location='ES')

#aqui los dto, para
class VideoRequest(BaseModel):
    url: str

class CancionDepurada(BaseModel):
    title:str
    duration:str
    artists:List[str]
    views:str
    url:str
    photoRoute:str
    album:Optional[str]


@app.post("/api/descargar")
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

@app.get("/api/busqueda")
async def busqueda(busqueda: str):
    try:
        print("buscando " , busqueda)
        resultado = ytmusic.search(busqueda , filter="songs", limit=20)
        resultadoFiltrado = []
        for cancion in resultado:
            #esta comprobación se hace, para ver si el Json que devuelve tiene en el diccionario
            #videoId, asegurando así que es una canción , y no otra cosa.
            if 'videoId' in cancion:
                imagen = ""
                if 'thumbnails' in cancion and cancion['thumbnails']:
                    imagen = cancion['thumbnails'][-1]['url']
                titulo = cancion.get('title')
                duracion = cancion.get('duration')
                artistas = []
                if 'artists' in cancion and cancion['artists']:
                    for artista in cancion['artists']:
                        artistas.append(artista['name'])
                urlDescarga = cancion['videoId']
                urlDescarga = f"https://www.youtube.com/watch?v={urlDescarga}"
                visualizaciones = cancion.get('views')
                album = cancion.get('album' , {}).get('name')

                objeto = CancionDepurada(
                    title = titulo ,
                    duration=duracion ,
                    artists=artistas,
                    views=visualizaciones ,
                    url = urlDescarga,
                    photoRoute = imagen,
                    album = album



                )
                resultadoFiltrado.append(objeto)
        return resultadoFiltrado




    except Exception as e:
        print(f"Error buscando canciones: {str(e)}")


@app.get("/api/virales")
async def obtener_virales():
    try:
        print("Buscando éxitos en España...")
        resultados = ytmusic.search("Top España", filter="songs", limit=20)
        lista_limpia = []
        contador = 1
        for track in resultados:
            if contador > 10:
                break
            if 'videoId' in track:

                imagen = ""
                if 'thumbnails' in track and track['thumbnails']:
                    imagen = track['thumbnails'][-1]['url']

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