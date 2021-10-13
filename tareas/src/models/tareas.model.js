import { DataTypes } from "sequelize"
import {conexion} from '../config/sequelize'

export const tareaModel = () => 
    conexion.define("tarea",{
        tareaId: {
            primaryKey: true,
            unique: true,
            autoIncrement: true,
            allowNull: false,
            field: 'id',
            type: DataTypes.INTEGER,
        },
        tareaNombre: {
            type: DataTypes.STRING(50),
            field: 'nombre',
            allowNull: false
        },
        tareaHora:{
            type: DataTypes.TIME,
            field: 'hora',
            allowNull: true
        },
        tareaDias:{
            type: DataTypes.ARRAY(DataTypes.ENUM(["LUN", "MAR" , "MIE" , "JUE" , "VIE" , "SAB" , "DOM"])),
            field:'dias',
            allowNull: true,
        },
    },{
        tableName:"tareas",
        timestamps: true,
        updatedAt: "fecha_de_actualizacion",
    }
  );