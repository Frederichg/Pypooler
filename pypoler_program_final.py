# import os

# def rename_file(directory, old_name, new_name):
#     try:
#         old_path = os.path.join(directory, old_name)
#         new_path = os.path.join(directory, new_name)

#         # Check if the old file exists in the directory
#         if os.path.exists(old_path):
#             os.rename(old_path, new_path)
#             print(f"File renamed from '{old_name}' to '{new_name}' successfully.")
#         else:
#             print(f"Error: The file '{old_name}' does not exist in the directory.")
#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     s="2"
#     directory_path = "C:\\Users\\tutag\\OneDrive\\Documents\\fichier excel"  # Replace this with the path of the directory containing the file
#     old_file_name = "new_files.pst"  # Replace this with the current name of the file
#     new_file_name = "new_file"+s+".pst"  # Replace this with the new name you want for the file
#     rename_file(directory_path, old_file_name, new_file_name)

""" import os
import shutil
import datetime

def copy_files_and_append_by_date(source_directory, destination_directory):
    try:
        # Create the destination directory if it doesn't exist
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        # Get a list of files in the source directory
        files = os.listdir(source_directory)

        # Loop through the files and sort them by date modified
        sorted_files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(source_directory, x)))

        # Loop through the sorted files
        for file in sorted_files:
            source_path = os.path.join(source_directory, file)
            destination_path = os.path.join(destination_directory, file)

            # Get the last modified timestamp of the file
            timestamp = os.path.getmtime(source_path)
            modified_date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d_%H-%M-%S')

            # Rename the file based on the modified date
            file_name, file_extension = os.path.splitext(file)
            new_file_name = f"{file_name}_{modified_date}{file_extension}"
            destination_path = os.path.join(destination_directory, new_file_name)

            # Copy the file to the destination directory
            shutil.copy(source_path, destination_path)
            print(f"File '{file}' copied successfully to '{destination_path}'.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    source_file ="C:\\Users\\tutag\\OneDrive\\Documents\\fichier excel"  # Replace this with the path of the source file
    destination_directory = "C:\\Users\\tutag\\OneDrive\\Documents\\final_file"  # Replace this with the path of the destination directory
    copy_files_and_append_by_date(source_file, destination_directory)

 """

""" import os

directory = "C:\\Users\\tutag\\OneDrive\\Documents\\fichier excel"  # Replace with the path to your directory

file_names = os.listdir(directory)

for index, file_name in enumerate(file_names):
    print(f"Index: {index}, File Name: {file_name}")
    
    if index == 2:
        # Perform the action you want for the file at index 2
        print(f"Performing action for file at index 2: {file_name}") """


# import shutil
# import os

# source_directory = "C:\Users\tutag\OneDrive\Documents\pymark_bon"  # Replace with the source directory path
# destination_directory = "C:\\Users\\tutag\\OneDrive\\Documents\\final_file"  # Replace with the destination directory path

# # Get a list of all files in the source directory
# file_list = os.listdir(source_directory)

# for filename in file_list:
#     source_path = os.path.join(source_directory, filename)
#     destination_path = os.path.join(destination_directory, filename)

#     # Copy the file from source to destination
#     shutil.copy(source_path, destination_path)
#     print(f"File {filename} copied to {destination_directory}")


# from PyQt5.QtWidgets import *
# from PyQt5 import uic


# class MyGUI(QMainWindow):
#     def __init__(self):
#         super(MyGUI, self).__init__()
#         super(MyGUI,self).__init__ ()
#         uic.loadUi("mygui.ui",self)
#         self.show()

#         self.pushButton_2.clicked.connect(self.update)
        
#         combo_box = self.comboBoox  
#         combo_box.addItem("Item 1")
#         combo_box.addItem("Item 2")
#         combo_box.addItem("Item 3")

#         mylis = ["test1","test2","test3","test4","test5"]
#         combo_box.addItems(mylis)

#     def update(self) : 
#         self.lineEdit.setText(self.comboBoox.currentText())
            

# def main() :
#     app = QApplication([])
#     window = MyGUI()
#     app.exec_()
#excel_file = "C:\\Users\\tutag\\OneDrive\\Documents\\final_file\\output_.xlsx"  # Replace with the actual file path
         
# main()

# from PyQt5.QtWidgets import *
# from PyQt5 import uic
# import pandas as pd

# class MyGUI(QMainWindow):
#     def __init__(self):
#         super(MyGUI, self).__init__()
#         uic.loadUi("mygui.ui", self)
#         self.show()

#         self.pushButton_2.clicked.connect(self.update)
        
#         self.comboBoox.addItem("Tutassa.docx")
#         self.comboBoox.addItem("Item 2")
#         self.comboBoox.addItem("Item 3")
        
#         self.comboBoox_2.addItem("2023_07_20__09_57_06_296.csv")
#         self.comboBoox_2.addItem("Item 2")
#         self.comboBoox_2.addItem("Item 3")

#         my_list = ["test1", "test2", "test3", "test4", "test5"]
#         self.comboBoox.addItems(my_list)

#     def update(self): 
#         selected_text = self.comboBoox.currentText()
#         selected_text1 = self.comboBoox_2.currentText()
        
        
#         # Load the Excel file into a DataFrame
#         excel_file = "C:\\Users\\tutag\\OneDrive\\Documents\\final_file\\index3.xlsx"
#         df = pd.read_excel(excel_file)
        
#         # Get the row numbers where selected_text is found in column 1
#         matching_row_numbers_column1 = df[df.iloc[:, 1] == 1].index
        
#         # Get the row numbers where the value in column 2 is equal to 0
#         matching_row_numbers_column2 = df[df.iloc[:, 2] == 0].index
#         matching_row_numbers_column3 = 0
#         val=4
#         tab = [matching_row_numbers_column1,matching_row_numbers_column2,matching_row_numbers_column3]
        
#         # Find the common row numbers from both conditions
#         for i in val : 
#            common_row_numbers &= list(set(tab[i]) 
        
#         common_row_numbers = list(set(matching_row_numbers_column1) & set(matching_row_numbers_column2))
        
#         if len(common_row_numbers) > 0:
#             row_numbers_list = common_row_numbers
#             print(f"In the column 1, the rows that are equal to '{selected_text}' and in column 2 the rows that are equal to 0 are {row_numbers_list}.")
#         else:
#             print(f"No rows found with both conditions.")
        
#         i=0   
#         while i< len(row_numbers_list) : 
#             value = df.iloc[i, 0]  # Row 2 (index 1), Column 2 (index 1)
#             print(value)
#             i=i+1
        
        
        
            
        

# def main():
#     app = QApplication([])
#     window = MyGUI()
#     app.exec_()

# if __name__ == "__main__":
#     main()


from PyQt5.QtWidgets import *
from PyQt5 import uic
import pandas as pd
from pypoler_program_update import update
import os

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("mygui.ui", self)
        self.show()

        self.pushButton_2.clicked.connect(self.update)
        
        self.comboBoox.addItem("default")
        self.comboBoox.addItem("31")
        self.comboBoox.addItem("1")
        
        self.comboBoox_2.addItem("default")
        self.comboBoox_2.addItem("0")
        self.comboBoox_2.addItem("666")
        self.comboBoox_2.addItem("16")

        my_list = ["test1", "test2", "test3", "test4", "test5"]
        self.comboBoox.addItems(my_list)

    def update(self): 
        update(self.comboBoox.currentText(),self.comboBoox_2.currentText(),"C:\\Users\\tutag\\OneDrive\\Documents\\final_file")

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == "__main__":
    main()



