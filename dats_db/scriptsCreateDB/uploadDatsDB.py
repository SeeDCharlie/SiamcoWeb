import pandas as pd

def xlsx_to_csv(pathXlsx, pathCsv):
    read_file = pd.read_excel (r'../SIAMCO_ACTIVITIES.xlsx')
    read_file.to_csv (r'Path to store the CSV file\File name.csv', index = None, header=True)

def uploadActivities():
