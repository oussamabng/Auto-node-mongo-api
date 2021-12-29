import os

# Models to create routes
models = ["User"]


# Folder Path
path = "./routes";
  
# Change the directory
os.chdir(path)

 # File to read
file_path = "route.ts"

for model in models:
    if not os.path.exists("{}.ts".format(model.lower())):
        # create the route
        f = open("{}.ts".format(model.lower()),"w")

        f.write("import express,{Request,Response} from 'express';\n")

        begin = "import {"
        end = "} from"
        imp = " ".join([begin,model,end])

        
        f.write("const User = require('../models/{}');\n".format(model))

        f.write("import { getAll, getOne,createOne,updateOne,deleteOne } from './route';\n\n")


        f.write("const router = express.Router();\n\n")

        # /GET
        f.write("// get all {}\n".format(model))
        begin = "{getAll("
        end = ",req,res);});"
        imp = " ".join([begin,model,end])
        f.write("router.get('/api/{}',[],(req:Request,res:Response)=>{}\n\n".format(model.lower(),imp))

        # /GET/ID
        f.write("// get a {}\n".format(model))
        begin = "{getOne("
        end = ",req,res);});"
        imp = " ".join([begin,model,end])
        f.write("router.get('/api/{}/:id',[],(req:Request,res:Response)=>{}\n\n".format(model.lower(),imp))

        # /POST
        f.write("// create {}\n".format(model))
        begin = "{createOne("
        end = ",req,res);});"
        imp = " ".join([begin,model,end])
        f.write("router.post('/api/{}',[],(req:Request,res:Response)=>{}\n\n".format(model.lower(),imp))

        # /PATCH 
        f.write("// update {}\n".format(model))
        begin = "{updateOne("
        end = ",req,res);});"
        imp = " ".join([begin,model,end])
        f.write("router.patch('/api/{}/:id',[],(req:Request,res:Response)=>{}\n\n".format(model.lower(),imp))
            

        # /DELETE 
        f.write("// delete {}\n".format(model))
        begin = "{deleteOne("
        end = ",req,res);});"
        imp = " ".join([begin,model,end])
        f.write("router.delete('/api/{}/:id',[],(req:Request,res:Response)=>{}\n\n".format(model.lower(),imp))

        # Export
        begin = "{ router as"
        middle = "{}Router".format(model.lower())
        end = "}"
        imp = " ".join([begin,middle,end])
        f.write("export  {} ".format(imp))



        # with is like your try .. finally block in this case
        with open('../server.ts', 'r') as file:    
            # read a list of lines into data
            data = file.readlines()
            begin = "import {"
            middle = "{}Router".format(model.lower())
            end = "} from"
            imp = " ".join([begin,middle,end])
            data[5] = "{} './routes/{}';\n".format(imp,model.lower())
            data[12] = "router.use({}Router);\n\n".format(model.lower())
            with open('../server.ts', 'w') as file:
                file.writelines(data)