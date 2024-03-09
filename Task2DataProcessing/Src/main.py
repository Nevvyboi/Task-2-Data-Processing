import pandas as pd
import os
import matplotlib.pyplot as plt

def cleanData(file):
    data = pd.read_csv(file,
                        sep = ";",
                        header = 0
    )
    return data

def calculateTotals4ColumnsAndStatistics(data, file):
    totals = data.sum(numeric_only = True)
    
    summary_stats = data.describe().transpose()
    
    totals_df = pd.DataFrame([totals], index = ['Total'])
    df_with_totals = pd.concat([data, totals_df, summary_stats])
    df_with_totals.to_csv(createNameofFile2Save(file, "csv"), index = False)

def createNameofFile2Save(f, ext):
    current_working_directory = os.getcwd()
    fileName = os.path.splitext(os.path.basename(os.path.basename(f)))[0]
    fileName = f"{current_working_directory}\{fileName}CleansedData.{ext}"
    return fileName
    
def plotGraph(data, f):
    column_totals = data.sum(numeric_only = True)

    plt.figure(figsize=(10, 6))
    column_totals.plot(kind='bar', color='skyblue')
    plt.title('Total Values of Each Column')
    plt.xlabel('Columns')
    plt.ylabel('Total Value')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(createNameofFile2Save(f, "png")) 

def main():

    file = input("Enter the full path of the csv file:\n")
    file = file.replace('"', "")
    
    cleansedData = cleanData(file)
    
    calculateTotals4ColumnsAndStatistics(cleansedData, file)
    
    plotGraph(cleansedData, file)

    while True:
        checkIfColumnExist = [e.capitalize() for e in cleansedData.columns]
        listOfColumns = "\n".join([e.capitalize() for e in cleansedData.columns])
        chosenColumn = input(f"Enter the column name you wish to filter:\n{listOfColumns}\n(Enter 'EXIT' to exit)\n")
        try:
            if chosenColumn == "EXIT":
                break
            else:
                if str(chosenColumn) in checkIfColumnExist:
                    try:
                        sortedData = cleansedData.sort_values(by = chosenColumn.lower())
                    except Exception as e:
                        print(e)
                    print(sortedData)
                else:
                    print("Column selected does not exist!")
        except Exception as e:
            pass
    
    
if __name__ == "__main__":
    main()