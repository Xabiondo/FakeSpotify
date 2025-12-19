import { Component, Input } from '@angular/core';
import { CancionModel } from '../../models/cancionModel';

@Component({
  selector: 'app-cancion',
  imports: [],
  templateUrl: './cancion.component.html',
  styleUrl: './cancion.component.css',
})
export class CancionComponent {
  @Input({required : true}) data!: CancionModel;

}
