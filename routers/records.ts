import { Router } from "express";
import { create, getRecords } from "../controllers/records";

const recordsRouter = Router();

recordsRouter
.get("/", getRecords)
.post("/",create);

export default recordsRouter;
