
const actividades = [{
    nombre: "Ir al gimnasio",
    hora: "6:00",
    dias: ["LUN","MIE","VIE"],
},
{
    nombre: "Aprender Mongodb",
    hora: "16:00",
    dias: ["MAR","JUE"],   
}];

export const crearActividad = (req,res)=>{
    console.log(req.body);
    const {body} = req;
    actividades.push(body);


    res.status(201).json({
        message:"Actividad creada con exito",
        content: body,
    });
};

export const listarActividades = (req, res)=>{
    res.status(200).json({
        message: "Las actividades son:",
        content: actividades,
    });
};

export const devolverActividad = (req, res)=>{
    console.log(req.params);
    const {id} = req.params;
    if (actividades.length > id) {
        return res.json({
            message: null,
            content: actividades[id],
        });
    }else{
        return res.status(404).json({
            message: "Actividad no encontrada",
            content: null,
        });
    }
};

export const actualizarActividad = (req, res)=>{
    const {id} = req.params;
    if (actividades.length > id){
        actividades[id] = req.body;

        return res.json({
            message: "Actividad actualizada con exito",
            content: actividades[id],
        });
    }else{
        return res.status(404).json({
            message: "No se encontró la actividad para actualizar",
            content: null,
        });
    }
};
export const eliminarActividad = (req, res) => {
    const {id} = req.params;
    if(actividades.length>id){
        actividades.splice(id,1);
        return res.json({
            message:"Actividad eliminada con exito",
            content: actividades,
        });
    }else{
        return res.status(404).json({
            message:"No se encontró la actividad",
            content:null,
        });
    }
};