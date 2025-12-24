import { Component, EventEmitter, Input, Output } from '@angular/core';
import { CancionModel } from '../../models/cancionModel';

@Component({
  selector: 'app-cancion',
  imports: [],
  templateUrl: './cancion.component.html',
  styleUrl: './cancion.component.css',
})
export class CancionComponent {
  @Input({required : true}) data!: CancionModel;

  @Output() escucharCancionFlag = new EventEmitter<string>() ; 

  onClickPlay(){
    this.escucharCancionFlag.emit(this.data.url)
  }

  

}
