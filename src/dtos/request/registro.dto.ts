import { IsEmail, IsEnum, IsNotEmpty, IsOptional, IsString, Length, Matches } from "class-validator"
import { TipoUsuario } from "../../models/usuarios.model"

export class RegistroDto{
    @IsString()
    @IsNotEmpty()    
    usuarioNombre: string

    @IsEmail()
    @IsNotEmpty()
    usuarioCorreo: string

    @IsString()
    @Matches(
        /(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#&?])[A-Za-z\d@$!%*#&?]{6,}/,
        {
            message:
            "Password inválida, está debe contener al menos una mayúscula, una minúscula, un número y un carácter especial. Logitud mínima 6."
        }
    )
    @IsNotEmpty()
    usuarioPassword: string

    @IsEnum(TipoUsuario)
    @IsOptional()
    usuarioTipo?:string

    @IsOptional()
    @IsString()
    usuarioFoto?:string;
}