import express, {json, urlencoded, raw} from "express";
import morgan from "morgan";
import {actividades_router} from "../routes/actividades"

export class Server {
    constructor(){
        this.app = express();
        this.puerto = 8000;
        this.cors();
        this.bodyParser();
        this.rutas();
    }

    bodyParser(){
        this.app.use(json());
        this.app.use(raw());
    }
    rutas(){
        this.app.use(morgan("dev"));
        this.app.use(actividades_router);
        this.app.get("/", (req, res)=>{res.status(200).send("Bienvenido a mi API");});
    }
    cors(){
        this.app.use((req, res, next) => {
            res.header("Access-Control-Allow-Origin","*");
            res.header("Access-Control-Allow-Headers","Content-Type, Authorization");
            res.header("Access-Control-Allow-Methods","GET, POST, PUT, DELETE");
            next();

        })
    }
    start(){
        this.app.listen(this.puerto, ()=>{
            console.log(`Servidor corriendo en el puerto ${this.puerto}`)
        })
    }
}