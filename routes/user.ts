import express,{Request,Response} from 'express';
const User = require('../models/User');
import { getAll, getOne,createOne,updateOne,deleteOne } from './route';

const router = express.Router();

// get all User
router.get('/api/user',[],(req:Request,res:Response)=>{getAll( User ,req,res);});

// get a User
router.get('/api/user/:id',[],(req:Request,res:Response)=>{getOne( User ,req,res);});

// create User
router.post('/api/user',[],(req:Request,res:Response)=>{createOne( User ,req,res);});

// update User
router.patch('/api/user/:id',[],(req:Request,res:Response)=>{updateOne( User ,req,res);});

// delete User
router.delete('/api/user/:id',[],(req:Request,res:Response)=>{deleteOne( User ,req,res);});

export  { router as userRouter } 