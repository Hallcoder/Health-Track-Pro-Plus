import { PrismaClient } from "@prisma/client";
import { Request, Response } from "express";
import prismaClient from "../constants";
export const getRecords = async (req: Request, res: Response) => {
  try {
    let records = await prismaClient.records.findMany();
    res.send({ data: records });
  } catch (error: any) {
    res.status(error.status).send(error.message);
  }
};

export const create = async(req:Request, res:Response) => {
        const {body_temperature,heart_rate,patient_id} = req.body;
        try {
              let newRecord = await prismaClient.records.create({
                data:{
                        body_temperature,
                        heart_rate,
                        patient_id
                }
              });
              if(newRecord){
                res.status(200).send({message:"Created record Successfully",data:newRecord});
              }  
        } catch (error:any) {
                res.status(error.status).send({data:null,message:error.message});
        }
}