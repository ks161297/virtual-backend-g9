import {Request, Response} from "express";
import { Usuarios} from "../config/models";

export const registroController = async(req: Request, res:Response)=>{
    try{
        const {body} = req;
        const nuevoUsuario = await Usuarios.create(body);

        return res.status(201).json({
            content: nuevoUsuario,
            message: "Usuario creado con exito",
        });
    }catch(error){
        return res.status(400).json({
            message: "Error al crear el usuario",
            content: error,
        });
    }
};