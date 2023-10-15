import express,{ Application } from "express";
import  recordsRouter  from "./routers/records";
const port = process.env.PORT || 3000;
const app: Application = express();
app.use('/records',recordsRouter);
app.listen(port, () =>{
    console.log('Listening on port '+port);
});

