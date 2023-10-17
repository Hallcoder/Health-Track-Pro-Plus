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
export const createPatient = async (req: Request, res: Response) => {
  console.log('creating patient...');
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

export const deletePatient = async (req:Request, res:Response) => {
  try {
    let id = req.params.id;
    if (!id) throw new Error("Invalid id");
     
    await prismaClient.patients.delete({
      where:{
      patient_id:Number(id),
      }
    })
    res
        .status(200)
        .send({ message: "deleted patient successfully", data: null });
  } catch (error:any) {
    res.status(error.status).send({ data: null, message: error.message });
  }
}
