
# Auto api creation

a project to create a rest api with node-js and mongodb in 5 min.



## Installation

Clone the project

```bash
  git clone https://github.com/oussamabng/Auto-node-mongo-api
  cd Auto-node-mongo-api
```

install cli

```bash
  npm install -g mongoose-model-cli
```




    
## Create Model

Make your first model with
```bash
  mongoose generate model user name:string notes:mixed houseId:idt
```

Edit the uri in models/connection-string.js

```bash
 var uri = 'mongodb://localhost:27017/cli';

```

## Create Routes

edit the models array with the name of your models of the api in the file 'add_routes.py'
```bash
  models = ["User"]
```

run the script

```bash
  python3 add_routes.py
```

## Install and run

install dependecies and run the project

```bash
  npm install
  npm run dev
```
