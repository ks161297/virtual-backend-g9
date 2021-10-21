declare global{
    namespace NodeJS{
        interface ProcessEnv{
            DATABASE_URL: string;
            NODE_ENV: "development" | "production";
            JWT_TOKEN: string;
            CLOUDINARY_NAME:string;
            CLOUDINARY_KEY:string;
            CLOUDINARY_API_SECRET:string;
            PORT: number;
        }
    }
}
export{};