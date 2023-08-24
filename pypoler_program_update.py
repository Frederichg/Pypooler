from PyQt5.QtWidgets import *
from PyQt5 import uic
import pandas as pd
import os


def update(selected_text,selected_text1,folder_path): #In this part selected_text corresponds to the criterim chosen in the comboBox by the user
        selected_text = selected_text
        selected_text1 =selected_text1
        #self.lineEdit.setText(selected_text)
        
        # Load the Excel file into a DataFrame
        
        folder_path = folder_path #put the good path
        #df = pd.read_excel(folder_path)
        
        # List all files in the folder with .xlsx extension
        files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

        # Sort files based on their creation time
        files.sort(key=lambda x: os.path.getctime(os.path.join(folder_path, x)), reverse=True)

        # Get the most recent file
        most_recent_file = files[0]

        # Open the most recent file using pandas
        df = pd.read_excel(os.path.join(folder_path, most_recent_file), engine='openpyxl')
   
        # Load the Excel file into a DataFrame

        
        # Initialize common_row_numbers as all row numbers
        common_row_numbers = set(range(len(df)))

        i=0
        val = [selected_text,selected_text1,"default"]  # Change this to the column indices you want to check
        #val = [self.comboBoox.currentText(),self.comboBoox_2.currentText(),"default"] normaly with all the values it would be : val = [self.comboBoox.currentText(),self.comboBoox_2.currentText(),self.comboBoox_3.currentText(),self.comboBoox_4.currentText() etc]
        #         # Get the row numbers where selected_text is found in column 1
        # matching_row_numbers_column1 = df[df.iloc[:, 1] == 2].index
        
#         # Get the row numbers where the value in column 2 is equal to 0
       # matching_row_numbers_column2 = df[df.iloc[:, 2] == "CV_Youmna.docx"].index 
        
        for i in range(3):
            # Find the row numbers where the value in column i is equal to selected_text
            
            if val[i].isdigit():
               val[i] = int(val[i])
            else:
                val[i]= val[i]
                     
            if val[i]!="default" :#if the user doesn't choose a criterim, default will be the current value of the comboBoox 
                matching_row_numbers = set(df[df.iloc[:, i+1] == val[i]].index)
                common_row_numbers &= matching_row_numbers
            
            
            # Perform AND operation with the current matching_row_numbers
            
        #common_row_numbers = list(set(matching_row_numbers_column1) & set(matching_row_numbers_column2))

        row_numbers_list = list(common_row_numbers)
        
        if len(row_numbers_list) > 0:
            print(f"In the columns {val}, the rows that are equal to '{selected_text}' and '{selected_text1}' are {row_numbers_list}.")
        else:
            print(f"No rows found with the given conditions.")
        i = 0
        while i < len(row_numbers_list):
            row_number = row_numbers_list[i]
            value = df.iloc[row_number, 0]  # Assuming you want to retrieve from Column 1 (index 0)... # Row 2 (index 1), Column 2 (index 1)
            print(value)
            print(i)
            
            i=i+1

