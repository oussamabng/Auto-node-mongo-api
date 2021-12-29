import express,{Request,Response} from 'express';
import { errorHandler } from '../helpers/error_handler';

const router = express.Router();

const getAll = async(model:any,req:Request,res:Response)=>{
    try {
        const collection = await model.find();
        return res.status(200).send(collection);
    } catch (error) {
        errorHandler(res,error);
    }
}

const getOne = async(model:any,req:Request,res:Response)=>{
    try {
        const collection = await model.findById(req.params.id);
        if (!collection){
            return res.status(404).send({
                message:'collection dont exists'
            }) 
        }
        return res.status(200).send(collection)
    } catch (error) {
        errorHandler(res,error);
    }
}

const createOne = async(model:any,req:Request,res:Response)=>{
    try {
        let collection = await model.create(req.body);
        await collection.save();
        return res.status(200).send(collection);
    } catch (error) {
        errorHandler(res,error);
    }
}

const updateOne = async(model:any,req:Request,res:Response)=>{
    try {
        const collection = await model.findByIdAndUpdate(req.params.id, req.body, {new: true});
        if (!collection) {
            return res.status(404).send({
                message:"collection not found"
            });
        }
        return res.status(200).send(collection);
    } catch (error) {
        errorHandler(res,error);
    }
}

const deleteOne = async(model:any,req:Request,res:Response)=>{
    try {
        await model.findByIdAndRemove(req.params.id);
        return res.status(200).send({
            message: "collection deleted"
        });
    } catch (error) {
        errorHandler(res,error);
    }
}

export { router as userRouter }
export { getAll,getOne,createOne,updateOne,deleteOne }