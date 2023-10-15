import { Request, Response } from "express";
import prismaClient from "../constants";
export const getPatients = async (req: Request, res: Response) => {
  try {
    let patients = await prismaClient.patients.findMany();
    res.status(200).send({ message: "There you go!", data: patients });
  } catch (error: any) {
    res.status(error.status).send({ message: "Failed", data: null });
  }
};
export const create = async (req: Request, res: Response) => {
  const { patient_nid, patient_frequent_sickness, patient_name } = req.body;
  try {
    let newPatient = await prismaClient.patients.create({
      data: {
        patient_name,
        patient_nid,
        patient_frequent_sickness,
      },
    });
    if (newPatient) {
      res
        .status(201)
        .send({ message: "Created patient successfully", data: newPatient });
    }
  } catch (error: any) {
    res.status(error.status).send({ message: "Failed", data: null });
  }
};
