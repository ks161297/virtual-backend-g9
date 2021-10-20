import {Request, Response} from "express";
import { validate } from "class-validator";
import { Usuarios} from "../config/models";
import { RegistroDto } from "../dtos/request/registro.dto";
import { plainToClass } from "class-transformer";
import { UsuarioDto } from "../dtos/response/usuario.dto";
import { LoginDto} from '../dtos/request/login.dto'
import {sign, SignOptions} from 'jsonwebtoken'
import { TipoUsuario } from "../models/usuarios.model";
import {compareSync} from "bcrypt";
import { RequestUser } from "../middlewares/validator";
import {v2} from 'cloudinary';


interface Payload {
    usuarioNombre: string
    usuarioId: string
    usuarioFoto?: string
    usuarioTipo: TipoUsuario
}
const tokenOptions: SignOptions ={
    expiresIn: '10h'
}

export const registroController = async(req: Request, res:Response)=>{
    try{
        const {body} = req;
        const data = plainToClass(RegistroDto, body);
        const validacion = await validate(data);
        console.log(validacion);
        if (validacion.length !== 0){
            const mensajes = validacion.map((error) => error.constraints);
            return res.status(400).json({
                content: mensajes,
                message: 'Error en el ingreso de valores'
            });
        }
        const usuarioEncontrado = await Usuarios.findOne({
            where: {usuarioCorreo: body.usuarioCorreo},
        });

        if (usuarioEncontrado){
            return res.status(400).json({
                content: null,
                message: "Usuario ya existe",
            });
        }




        const nuevoUsuario = await Usuarios.create(body);
        

        const payload: Payload={
            usuarioId: nuevoUsuario.getDataValue('usuarioId'),
            usuarioNombre: nuevoUsuario.getDataValue('usuarioNombre'),
            usuarioTipo: nuevoUsuario.getDataValue('usuarioTipo'),
            usuarioFoto: nuevoUsuario.getDataValue('usuarioFoto')
        }
        const jwt = sign(payload, process.env.JWT_TOKEN ?? "", tokenOptions);


        const content = plainToClass(UsuarioDto, {
            ...nuevoUsuario.toJSON(),
            usuarioJwt: jwt,
        });
        return res.status(201).json({
            content,
            message: "Usuario creado con exito",
        });
    }catch(error){
        return res.status(400).json({
            message: "Error al crear el usuario",
            content: error,
        });
    }
};


export const login = async (req: Request, res: Response)=>{
    const validador = plainToClass(LoginDto, req.body)
    try {
        const resultado = await validate(validador);

        if (resultado.length !== 0){
            return res.status(400).json({
                content: resultado.map((error) => error.constraints),
                message: "Información incorrecta"
            });
        }
        const usuarioEncontrado = await Usuarios.findOne({
            where: {usuarioCorreo: validador.correo}});
        
        if (!usuarioEncontrado){
            return res.status(400).json({
                message: "Usuario incorrecto",
                content: null,
            });
        }

        const resultado_password = compareSync(validador.password, usuarioEncontrado.getDataValue("usuarioPassword"));

        if(!resultado_password){
            return res.status(400).json({
                message: "Usuario incorrecto",
                content:null,
            });
        }
        const payload: Payload={
            usuarioId: usuarioEncontrado.getDataValue('usuarioId'),
            usuarioNombre: usuarioEncontrado.getDataValue('usuarioNombre'),
            usuarioTipo: usuarioEncontrado.getDataValue('usuarioTipo'),
            usuarioFoto: usuarioEncontrado.getDataValue('usuarioFoto')
        };
        const jwt = sign(payload, process.env.JWT_TOKEN ?? "", tokenOptions);
        return res.json({
            content: jwt,
            message: null,
        });
    }catch(error){
        if(error instanceof Error){
            return res.status(400).json({
                message: "Error al hacer login",
                content: error.message,
            });
        }
    }
};



export const perfil = (req: RequestUser, res:Response) => {
    const content = plainToClass(UsuarioDto, req.usuario);
    if (!content.usuarioFoto){
        console.log(content.usuarioNombre);
        let [nombre, apellido]=content.usuarioNombre.split(" ");
        content.usuarioFoto = `https://avatars.dicebear.com/api/initials/${nombre[0]}${apellido ?apellido[0] : ""}.svg`;
    }
    else{
        const url = v2.url(content.usuarioFoto);
        content.usuarioFoto = url;

    }
    return res.json({
        content,
    });
};

export const actualizerPerfil = (req: RequestUser, res: Response)=>{
    
}