import { Component, OnInit } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { TarjetaService } from 'src/app/services/tarjeta.service';

@Component({
  selector: 'app-list-tarjeta-credito',
  templateUrl: './list-tarjeta-credito.component.html',
  styleUrls: ['./list-tarjeta-credito.component.css']
})
export class ListTarjetaCreditoComponent implements OnInit {

  constructor(public tarjetaService: TarjetaService, private toastR: ToastrService) { }

  ngOnInit(): void {
    this.tarjetaService.obtenerTarjeta();
  }

  eliminarTarjeta(id: number){
    if(confirm("Esta seguro que desea eliminar el registro")){
      this.tarjetaService.eliminarTarjeta(id).subscribe(data => {
        this.toastR.warning("Registro eliminada", "La tarjeta fue eliminada")
        this.tarjetaService.obtenerTarjeta();
      })
    }
  }

  editar(tarjeta){
    this.tarjetaService.actualizar(tarjeta);
  }




}
