import express, {Express, json} from "express";
import imagenRouter from "../routes/imagen.routes";
import usuarioRouter from "../routes/usuario.routes";
import conexion from './sequelize';
import {v2} from "cloudinary"
import productoRouter from "../routes/producto.routes";
import compraRouter from "../routes/compra.routes";
import cors from "cors";


require('dotenv').config();

export class Server{
    // private => no puede ser accedido por fuera de la clase.
    // readonly => no puede ser modificado su valor afuera del constructor.

    private readonly app: Express;
    private readonly puerto: unknown;
    constructor(){
        this.app = express();
        this.puerto = process.env.PORT || 8000;
        this.app.use(cors());
        this.bodyParser();
        this.rutas();
        v2.config({
            cloud_name:process.env.CLOUDINARY_NAME,
            api_key:process.env.CLOUDINARY_KEY,
            api_secret:process.env.CLOUDINARY_API_SECRET,
        });
    }
    private bodyParser(){
        this.app.use(json());
    }
    private rutas(){
        this.app.use(usuarioRouter);
        this.app.use(imagenRouter);
        this.app.use(productoRouter);
        this.app.use(compraRouter);
    }
    public start(){
        this.app.listen(this.puerto, async() => {
            console.log(`Servidor corriendo exitosamente en el puerto ${this.puerto}`);
        
        await conexion.sync()
        console.log('Base de datos conectada con exito')
        });
    }
}
