-- CreateTable
CREATE TABLE "records" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "heart_rate" REAL NOT NULL,
    "body_temperature" REAL NOT NULL,
    "patient_id" INTEGER NOT NULL,
    CONSTRAINT "records_patient_id_fkey" FOREIGN KEY ("patient_id") REFERENCES "patients" ("patient_id") ON DELETE RESTRICT ON UPDATE CASCADE
);

-- CreateTable
CREATE TABLE "patients" (
    "patient_id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "patient_name" TEXT NOT NULL,
    "patient_nid" TEXT NOT NULL,
    "patient_frequent_sickness" TEXT NOT NULL
);
