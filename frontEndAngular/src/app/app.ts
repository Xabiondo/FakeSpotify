import { Component, inject, OnInit, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CancionComponent } from './components/cancion/cancion.component';
import { CancionModel } from './models/cancionModel';
import { SpotifyService } from './services/spotify.service';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, CancionComponent],
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
