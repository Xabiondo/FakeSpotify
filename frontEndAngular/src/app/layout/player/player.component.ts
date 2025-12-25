import { Component, Input } from '@angular/core';
import { CancionModel } from '../../models/cancionModel';

@Component({
  selector: 'app-player',
  imports: [],
  templateUrl: './player.component.html',
  styleUrl: './player.component.css',
})
export class Player {

  @Input({required : true}) cancion!: CancionModel ; 

  @Input() urlAudio : string = "";

}
