import { Router } from "express";
import { create, deleteRecord, getRecords } from "../controllers/records";

const recordsRouter = Router();

recordsRouter
.get("/", getRecords)
.post("/",create)
.delete("/:id",deleteRecord);

export default recordsRouter;
