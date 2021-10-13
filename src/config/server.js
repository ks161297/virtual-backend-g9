import express, {json} from 'express';
import { tareasRouter } from '../routes/tareas.route';
import { conexion } from './sequelize';
import swagger from 'swagger-ui-express';
import documentacion from '../../swagger.json';
import cors from 'cors'



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