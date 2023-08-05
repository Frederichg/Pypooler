'''This part will record the output and name it according to NOW()'''
'''remain to make it work as a function that Main can call'''

from datetime import datetime

# Create a DataFrame from the returned values
df_output = pd.DataFrame(values, columns=['Output'])

# Add a column for the line numbers
df_output['Line'] = range(1, len(df_output) + 1)

# Add a column for the file name
df_output['File Name'] = file_name

# Reorder the columns
df_output = df_output[['Line', 'File Name', 'Output']]

# Create a timestamp for the output file name
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_file_name = f'/data/output_{timestamp}.xlsx'

# Write the DataFrame to an Excel file
df_output.to_excel(output_file_name, index=False)

print(f'Output written to {output_file_name}')
