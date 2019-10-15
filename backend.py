import os
import pandas, math, sqlite3 
from datetime import datetime as dt

class DateToSqlite:
    """Class with writing day, when programm was using, to the SQLite3 db."""
    
    def write():
        connection = sqlite3.connect("datesOfWork.db")
        cursor = connection.cursor()

        todayDate= str(dt.now().day)+"." + str(dt.now().month)+ "." + str(dt.now().year)
        cursor.execute("CREATE TABLE IF NOT EXISTS names(id INTEGER PRIMARY KEY, date TEXT, worked TEXT)")
        cursor.execute("INSERT INTO names (date, worked) VALUES(?,?)",(todayDate,0))

        #print(todayDate)

        connection.commit()
        connection.close()

class Datas:
    """ Class reprezent working with current file in current folder """
        
    def load_df( selected_file):
        # load selected_file into pandas
        selected_file = selected_file
        global df
        df = pandas.read_excel(selected_file)
    
    def ful_number_devide1():
        # full number devide in  selected row with name: "vystavene"
        global df, export_number
        for i in range(0, len(df.vystavene)):
            if df.vystavene[i] != 0:
                export_number = math.floor(df.vystavene[i])
                df.loc[[i],["vystavene"]] = str(export_number) 
            else:
                export_number = 0
                df.loc[[i],["vystavene"]] = export_number
                   
    def delete_line_with_null():
        global df
        df = df[df.vystavene != 0]

    def delete_line_with_null0():
        global df
        df= df[df.pouzitelne != 0] 
        
    def delete_collum(x):
        # x = column e.g. "cena"
        global df
        for i in df.columns:
            if i == x:
                df = df.drop(x, axis = 1)

    def sort(name_of_row):
        global df
        df.sort_values(by = name_of_row, inplace = True )# name = row

    def save():
        global df, file_finded
        name_new_file = file_finded[:-5] + ".csv"
        df.to_csv(name_new_file)

    def save_to_new_folder():
        global file_finded, df, file_finded
        name_new_file = file_finded[:-5] + ".csv"
        folder_new_name = "untables"
        if not folder_new_name in os.listdir():
            os.makedirs(folder_new_name)
            new_path = os.getcwd() + "\\" + folder_new_name + "\\"
            df.to_csv(new_path + name_new_file)
        else:
            new_path = os.getcwd() + "\\" + folder_new_name + "\\"
            df.to_csv(new_path+ name_new_file)



# program starter    
def file_finder(nameExpect):
    # find file with ext == .xlsx
    global df, file_finded, file, name
    DateToSqlite.write()    
    for file in os.listdir():
        name, ext = os.path.splitext(file)
        if ext == ".xlsx":
            file_finded = (name + ext)
            if nameExpect == name:
                Datas.load_df(file_finded)
                Datas.ful_number_devide1()
                Datas.delete_line_with_null0()
                Datas.delete_collum("sdfsa")
                Datas.sort("tovar")
                Datas.save_to_new_folder()
                print(name + "zhoda u tohtot")
            else:
                Datas.load_df(file_finded)
                Datas.ful_number_devide1()
                Datas.delete_line_with_null0()
                #Datas.delete_collum("sdfsa")
                Datas.sort("tovar")
                print(name)
                Datas.save_to_new_folder()
    print("exported all")





