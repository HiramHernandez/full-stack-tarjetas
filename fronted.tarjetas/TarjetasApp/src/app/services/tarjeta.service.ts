import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { TarjetaCredito } from '../models/tarjetaCredito';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TarjetaService {
  myAppUrl: string = "http://localhost:8000/";
  myApiUrl: string = "api/tarjeta";
  list: TarjetaCredito[] = [];
  private actualizarFormulario = new BehaviorSubject<TarjetaCredito>({} as any);

  constructor(private http: HttpClient) { }

  guardarTarjeta(tarjeta: TarjetaCredito): Observable<TarjetaCredito>{
    return this.http.post<TarjetaCredito>(this.myAppUrl + this.myApiUrl, tarjeta);
  }

  obtenerTarjeta(){
    this.http.get(this.myAppUrl + this.myApiUrl).toPromise()
      .then(data => {
        this.list = data as TarjetaCredito[];
      });
  }

  eliminarTarjeta(id: number): Observable<TarjetaCredito>{
    return this.http.delete<TarjetaCredito>(this.myAppUrl + this.myApiUrl + "/" + id);
  }

  actualizar(tarjeta){
    this.actualizarFormulario.next(tarjeta);
  }

  actualizarTarjeta(id: number, tarjeta: TarjetaCredito): Observable<TarjetaCredito>{
    const url: string = `${this.myAppUrl}${this.myApiUrl}\\${id}`;
    return this.http.put<TarjetaCredito>(url, tarjeta);
  }

  obtenerTarjeta$(): Observable<TarjetaCredito>{
    return this.actualizarFormulario.asObservable();
  }

}
