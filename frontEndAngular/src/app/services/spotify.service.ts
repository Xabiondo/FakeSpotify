import { Injectable } from '@angular/core';
import { CancionModel } from '../models/cancionModel';

@Injectable({
  providedIn: 'root',
})
export class SpotifyService {


  getCancionesVirales(): Promise<CancionModel[]>{

    return fetch('http://localhost:8000/api/virales')
    .then(res => res.json())
    .then(res =>{
       console.log(res)
      return res as CancionModel[]
    })

  }

  
}
