import { Component, inject, OnInit, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CancionComponent } from './components/cancion/cancion.component';
import { CancionModel } from './models/cancionModel';
import { SpotifyService } from './services/spotify.service';
import { BarraSuperior } from './layout/barraSuperior/barraSuperior.component';

@Component({
  selector: 'app-root',
  standalone: true ,
  imports: [RouterOutlet, CancionComponent , BarraSuperior],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App implements OnInit{

  private spotifyService = inject(SpotifyService) ; 
canciones = signal<CancionModel[]>([]);

  async ngOnInit() {
     const datos = await  this.spotifyService.getCancionesVirales();
     this.canciones.set(datos)
     
    
  }

}
