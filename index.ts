import express, { Application } from "express";
import recordsRouter from "./routers/records";
import patientsRouter from "./routers/patients";
const port = process.env.PORT || 3000;
const app: Application = express();
app.use(express.json());
app.use("/records", recordsRouter);
app.use("/patients", patientsRouter);
app.listen(port, () => {
  console.log("Listening on port " + port);
});
