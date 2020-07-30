import pandas as pd
from motorDBaux import motor_pg



def xlsx_to_csv(pathXlsx, pathCsv):
    read_file = pd.read_excel (r'../SIAMCO_ACTIVITIES.xlsx')
    read_file.to_csv (r'Path to store the CSV file\File name.csv', index = None, header=True)

def uploadActivities():
    motDB = motor_pg()
    fActivities =  open("dats_db/dats/SIAMCO_ACTIVITIES.csv")

    for line in fActivities.readlines():
        dats = line.split("|")
        unidadM = motDB.getStatement("select id_unid from measurement_units where code_dian = %s", (dats[3],) ).fetchone()[0]
        dInsert = (dats[1], dats[2], str(unidadM), dats[4])
        print("datos a insertar : ", dInsert)
        motDB.executeStatement("insert into activities(cod, description, unit, valueunit) values(%s, %s, %s, %s)", dInsert)
    
    motDB.commit()
    motDB.closeDB()
    fActivities.close()

#uploadActivities()