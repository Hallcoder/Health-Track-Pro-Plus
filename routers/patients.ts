import { Router } from "express";
import { createPatient, deletePatient, getPatients } from "../controllers/patients";

const patientsRouter = Router();

patientsRouter
.get("/", getPatients)
.post("/",createPatient)
.delete("/:id",deletePatient)
export default patientsRouter;
