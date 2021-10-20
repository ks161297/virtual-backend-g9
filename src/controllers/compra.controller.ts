import { plainToClass } from "class-transformer";
import { Request, Response } from "express";
import { validate } from "class-validator";
import {Compras, Detalles, Productos} from '../config/models';
import { CompraDto, DetalleCompraDto } from "../dtos/request/compra.dto";
import conexion from "../config/sequelize";
import { RequestUser } from "../middlewares/validator";
import {configure, preferences, payment, merchant_orders } from "mercadopago";

import {CreatePreferencePayload} from 'mercadopago/models/preferences/create-payload.model';



export const crearCompra = async (req: RequestUser, res:Response) => {
    const validador = plainToClass(CompraDto, req.body);
    const errores = await validate(validador);
    if(errores.length !==0){
        const mensaje_error = errores.map((error) => error.children);
        const mensaje_error_final = mensaje_error.map((error) =>
            error?.map((error_hijo) => {
                console.log(error_hijo);

                return error_hijo.children 
                    ? error_hijo.children.map(
                        (error_hijo_hijo) => error_hijo_hijo.constraints
                      )
                    : null;
            })
        );
        console.log(mensaje_error);

        return res.status(400).json({
            content: mensaje_error_final,
            message: "Campos inválidos"
        });
    }

    const transaccion = await conexion.transaction();
    try {
        let total = 0.0;
        const nuevaCompra = await Compras.create(
            {
                compraFecha: new Date(),
                compraTotal: total,
                usuarioId: req.usuario?.getDataValue("usuarioId"),
            },
            {transaction: transaccion}
        );
        console.log(nuevaCompra.toJSON());
        //Sin promise all así sería
        for (const key in validador.detalle){}

        

        await Promise.all(
            validador.detalle.map(async(detalle_compra) => {
                const producto = await Productos.findByPk(detalle_compra.producto, {
                    attributes: ["productoCantidad", "productoPrecio"], 
            });
            if(!producto){
                throw new Error(`Producto ${detalle_compra.producto} no existe`);
            }
            if(detalle_compra.cantidad > producto.getDataValue("productoCantidad")){
                throw new Error(
                    `Producto ${detalle_compra.producto} no hay suficientes cantidades`
                );
            }

            await Detalles.create(
                {
                    productoId: detalle_compra.producto,
                    compraId: nuevaCompra.getDataValue("compraId"),
                    detalleCantidad: detalle_compra.cantidad,
                    detalleTotal: 
                        detalle_compra.cantidad * producto.getDataValue("productoPrecio"),
                },
                {transaction: transaccion}
            );
                
            await Productos.update(
                {
                    productoCantidad: 
                        producto.getDataValue("productoCantidad") - detalle_compra.cantidad,
                },
                {
                    where:{
                        productoId: detalle_compra.producto,
                    },
                    transaction: transaccion,
                }
            );
        
           
            total +=
                detalle_compra.cantidad * producto.getDataValue("productoPrecio");
                       
            await Compras.update(
                {
                    compraTotal: total,
                },
                {
                    where:{
                        compraId: nuevaCompra.getDataValue("compraId"),
                    },
                    transaction: transaccion,
                }
                );
            })
        );
                
        await transaccion.commit()
        return res.status(201).json({
            message: "Compra realizada exitosamente",
            content: nuevaCompra,
        });
   

    } catch(error: unknown){
        await transaccion.rollback();
        return res.status(500).json({
            message: "Error al crear la compra",
            content: error instanceof Error ? error.message : "",
        });
    }
}


export const crearPreferencia = async(req: Request, res:Response) => {
    configure({ 
        access_token:"APP_USR-8208253118659647-112521-dd670f3fd6aa9147df51117701a2082e-677408439",
        integrator_id:"dev_24c65fb163bf11ea96500242ac130004",
    });
    const payload: CreatePreferencePayload = {
        back_urls:{
            success: "google.com",
            failure: "youtube.com",
            pending: "gmail.com"
        },
        auto_return: "approved",
        payer:{
            name: "Lalo",
            surname: "Landa",
            // address: {
            //     street_name: "Falsa",
            //     street_number: "123",
            //     zip_code: "1111",
            // },
            email:'test_user_46542185@testuser.com',
            // phone: {
            //     area_code: "11",
            //     number: "22223333",
            // },
            identification:{
                number:"22334445",
                type:"DNI",
            }
        },
        items: [{
            id: "12",
            title: "Yogurt Griego de 1lt.",
            description: "Sabroso yogurt de tierras griegas",
            picture_url: "https:// ...",
            category_id: "001",
            quantity: 2,
            unit_price: 12.5,
            currency_id: "PEN"
        },],
        payment_methods: {
            excluded_payment_methods: [{id: "master"}, {id: "debmaster" }],

            //excluded_payment_types: [{id : "atm"}],

            installments: 6
        },
        notification_url: "https://bodega-mp-marigrace.herokuapp.com/mp-notificaciones"
    };
        try{
            const rptaMP = await preferences.create(payload);
            console.log(rptaMP);
            return res.json({
                message: "Preferencia creada exitosamente",
                content: rptaMP
            })
        }catch(e){
            console.log(e);

            return res.json({
                message: "Error al crear la preferencia",
            });
        }
        
    };

export const mpNotificaciones = (req: Request, res: Response)=>{
    console.log('------- BODY ----------');
    console.log(req.body);
    console.log("----------- QUERY PARAMS -----------");
    console.log(req.query);

    return res.status(200).send("ok");
};