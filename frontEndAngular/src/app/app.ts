import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Cancion } from './components/cancion/cancion';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet , Cancion ],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
 city:string = 'Barcelona'
}
