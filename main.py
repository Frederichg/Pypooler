'''This is the main part of the Pooler, it open the Index than pass it to a function'''
import pandas as pd


# Open the Index2.xlsx file
df_index = pd.read_excel('/data/Index2.xlsx')

# This is an example like : Get the value at line 5, column 1
# In the real program this will be the SQL like
file_name = df_index.iloc[4, 0]  # Note: pandas uses 0-based indexing

# Add .csv extension if not present
if not file_name.endswith('.csv'):
    file_name += '.csv'

# Call the function
# The will need a way to select the specific function according to Column 2 of the Index
values = testfunction5csrtt(file_name)

print(values)

#There needs a creation of the Output .xlsx file with the values in it
#Each line will be a different files
#The first column can be the name of the file and the second column the line number from the Index
