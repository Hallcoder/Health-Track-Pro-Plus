import { application } from "express";
const port = process.env.PORT || 3000;
application.listen(port,() =>{
    console.log('Listening on port '+port);
});
application.use('/records',)