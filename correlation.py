import csv
import plotly.express as px
import numpy as np


def getDataSource(data_path):
    Days_Present=[]
    Marks_in_Percentage=[]
    with open(data_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            Marks_in_Percentage.append(float(row["Marks In Percentage"]))
            Days_Present.append(float(row["Days Present"]))

    return {"x":Days_Present,"y":Marks_in_Percentage}    
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("The correlation between the Marks in Percentage and the Days present is :",correlation[0,1])
def setup():
    data_path = "C:\\Users\\TRUSTANA MARKETING\\OneDrive\\Desktop\\Whitehat jr\\Python_Class\\Student Marks vs Days Present.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    with open(data_path) as f:
        reader = csv.DictReader(f)
        fig = px.scatter(reader, x = "Days Present", y = "Marks In Percentage")
        fig.show()
setup()

