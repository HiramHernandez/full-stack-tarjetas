import { Component, OnDestroy, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators} from "@angular/forms";
import { ToastrService } from 'ngx-toastr';
import { Subscription } from 'rxjs';
import { TarjetaCredito } from 'src/app/models/tarjetaCredito';
import { TarjetaService } from 'src/app/services/tarjeta.service';


@Component({
  selector: 'app-tarjeta-credito',
  templateUrl: './tarjeta-credito.component.html',
  styleUrls: ['./tarjeta-credito.component.css']
})
export class TarjetaCreditoComponent implements OnInit, OnDestroy {
  form: FormGroup;
  subscription: Subscription;
  tarjeta!: TarjetaCredito;
  idTarjeta: number = 0;

  constructor(private formBuilder: FormBuilder,
    private tarjetaService: TarjetaService,
    private toastR: ToastrService
    )
  {
    this.form = this.formBuilder.group({
      id: 0,
      titular: ['', [Validators.required]],
      numero_tarjeta: ['', [Validators.required, Validators.maxLength(16), Validators.minLength(16)]],
      fecha_expiracion: ['', [Validators.required, Validators.maxLength(5), Validators.minLength(5)]], 
      cvv: ['', [Validators.required, Validators.maxLength(3), Validators.minLength(3)]]
    });
  }

  ngOnInit(): void {
    this.subscription = this.tarjetaService.obtenerTarjeta$().subscribe(data =>{
      console.log(data);
      this.tarjeta = data;
      this.form.patchValue({
        titular: this.tarjeta.titular,
        numero_tarjeta: this.tarjeta.numero_tarjeta,
        fecha_expiracion: this.tarjeta.fecha_expiracion,
        cvv: this.tarjeta.cvv
      });
      this.idTarjeta = this.tarjeta.id;
    });
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }

  guardarTarjeta(){
    if(this.idTarjeta === 0){
      this.agregar();
    } else {
      this.editar();
    }
   
  }

  agregar(){
    const tarjeta: TarjetaCredito = {
      titular: this.form.get('titular').value,
      numero_tarjeta: this.form.get('numero_tarjeta').value,
      fecha_expiracion: this.form.get('fecha_expiracion').value,
      cvv: this.form.get('cvv').value,
    }

    this.tarjetaService.guardarTarjeta(tarjeta).subscribe(data => {
      this.toastR.success("Registro exitoso", "La tarjeta fue agregada");
      this.tarjetaService.obtenerTarjeta();
      this.form.reset();
    })
  }

  editar(){
    const tarjeta: TarjetaCredito = {
      id: this.tarjeta.id,
      titular: this.form.get('titular').value,
      numero_tarjeta: this.form.get('numero_tarjeta').value,
      fecha_expiracion: this.form.get('fecha_expiracion').value,
      cvv: this.form.get('cvv').value,
    };
    this.tarjetaService.actualizarTarjeta(this.idTarjeta, tarjeta).subscribe(data => {
      this.toastR.success("Registro actualizado", "La tarjeta fue actualizada");
      this.tarjetaService.obtenerTarjeta();
      this.form.reset();
      this.idTarjeta = 0;
    });
  }






}
