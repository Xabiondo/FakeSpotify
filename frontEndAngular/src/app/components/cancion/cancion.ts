import { Component } from '@angular/core';

@Component({
  selector: 'app-cancion',
  imports: [],
  templateUrl: './cancion.html',
  styleUrl: './cancion.css',
})
export class Cancion {
  cancion:string = "resentia" ;
  autor:string = "pablo chill e" ;
  estaSuscrito:boolean = true ; 

}
