import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'barra-superior',
  standalone: true , 
  imports: [],
  templateUrl: './barraSuperior.component.html',
  styleUrl: './barraSuperior.component.css',
})
export class BarraSuperior {

  @Output() llamarFuncionBusqueda = new EventEmitter<string>(); 

  mandarBusqueda(texto : string){
    this.llamarFuncionBusqueda.emit(texto)
  }

}
