import { Injectable } from '@angular/core';
import { CancionModel } from '../models/cancionModel';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})


export class SpotifyService {

  constructor(private http: HttpClient){}

  //He hecho una mezcla incómoda de JS nativo, y Angular, pero bueno, es funcional . 

  descargarCancion(urlCancion:string){

    return fetch('http://localhost:8000/api/descargar/?')

  }

escucharCancion(videoId: string) : Observable<any> {
  
  return this.http.get<any>('http://localhost:8000/api/play?videoId=' + videoId)

}
  getCancionesBusquedaPersonalizada( busqueda:string ) : Promise<CancionModel[]>{

    const busquedaLimpia = encodeURIComponent(busqueda)
    //Esto es para que en caso de que la busqueda tenga espacios, se cambie con formato de navegador
    //Ejemplo : pasa de "Bad bunny" a "Bad%20Bunny"

    return fetch('http://localhost:8000/api/busqueda/?busqueda='+busquedaLimpia)
    .then(res => res.json())
    .then(res =>{
      console.log(res)
      return res as CancionModel[]
    })

  }

  getCancionesVirales(): Promise<CancionModel[]>{

    return fetch('http://localhost:8000/api/virales')
    .then(res => res.json())
    .then(res =>{
       console.log(res)
      return res as CancionModel[]
    })

  }

  
}
