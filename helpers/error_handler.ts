import {Response} from 'express';

const errorHandler = (res:Response,e:any)=>{
    const result = (e as Error).message;
        return res.status(404).send({
            message:result
        })
}

export { errorHandler }