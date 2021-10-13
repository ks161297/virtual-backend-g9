import express, {json} from 'express';
import { tareasRouter } from '../routes/tareas.route';
import { conexion } from './sequelize';
import swagger from 'swagger-ui-express';
import documentacion from '../../swagger.json';
import cors from 'cors'
require("dotenv").config();



export class Server{
    constructor(){
        this.app = express();
        this.puerto = process.env.PORT || 8000;
        this.app.use(cors());
        this.bodyParser();
        this.rutas();
    }
    bodyParser(){
        this.app.use(json());
    }
    rutas(){
        this.app.get("/", (req, res) => {
            res.json({
                message: "Bienvenido a mi API"
            });
        });
        if (process.env.NODE_ENV === "production"){
            documentacion.host = "tareas-node.herokuapp.com";
            documentacion.schemes=["https"];
        }else{
            documentacion.host = `127.0.0.1:${this.puerto}`;
            documentacion,schemes = ["http"];
                
        }
        this.app.use('/docs', swagger.serve, swagger.setup(documentacion));
        this.app.use(tareasRouter)
    }
    start(){
        this.app.listen(this.puerto, async()=> {
            console.log(`Servidor corriendo con exito en el puerto ${this.puerto}`);
            try {
                await conexion.sync();
                console.log('Base de datos conectada exitosamente')
            }catch(error){

            }
        });
    }
}