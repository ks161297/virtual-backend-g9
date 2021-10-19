import express, {Express, json} from "express";
import usuarioRouter from "../routes/usuario.routes";
import conexion from './sequelize';
require('dotenv').config();

export class Server{
    // private => no puede ser accedido por fuera de la clase.
    // readonly => no puede ser modificado su valor afuera del constructor.

    private readonly app: Express;
    private readonly puerto: number;
    constructor(){
        this.app = express();
        this.puerto = 8000;
        this.bodyParser();
        this.rutas();
    }
    private bodyParser(){
        this.app.use(json());
    }
    private rutas(){
        this.app.use(usuarioRouter)
    }
    public start(){
        this.app.listen(this.puerto, async() => {
            console.log(`Servidor corriendo exitosamente en el puerto ${this.puerto}`);
        
        await conexion.sync()
        console.log('Base de datos conectada con exito')
        });
    }
}
