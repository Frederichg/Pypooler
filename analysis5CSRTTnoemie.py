import pandas as pd

def count_dependent_variables(csv_file):
    # Define the column names
    column_names = ['line_number', 'seconde', 'milliseconde', 'inout', 'stateNO', 'statename']
    
    # Define the independent variables
    independent_vars = ['sec2', 'sec5', 'sec3', 'sec4']

    # Define the dependent variables
    dependent_vars = ['Premature', 'Omission', 'IncorrectResp', 'CorrectResp']

    # Load the CSV file, skip the first 11 rows, and define the column names
    data = pd.read_csv(csv_file, skiprows=range(1, 12), names=column_names, usecols=range(6))

    # Define a condition for the start of a trial
    start_of_trial = (data['statename'] == 'ComptNbessai') & (data['stateNO'] == 2)

    # Get the indices where a new trial starts
    start_indices = data[start_of_trial].index

    # Add the index of the last row to the list of indices
    # This will serve as the end index for the last trial
    end_indices = start_indices[1:].append(pd.Index([len(data)]))

    # Initialize a dictionary to hold the counts
    counts = {var: {dep_var: 0 for dep_var in dependent_vars} for var in independent_vars}

    # Iterate through each trial
    for start, end in zip(start_indices, end_indices):
        # Get the data for this trial
        trial_data = data.iloc[start:end]
        
        # Find which independent variable this trial corresponds to
        for var in independent_vars:
            if var in trial_data['statename'].values:
                # Count the occurrences of each dependent variable
                for dep_var in dependent_vars:
                    if dep_var in trial_data['statename'].values:
                        counts[var][dep_var] += 1

    return counts

# Usage:
# counts = count_dependent_variables("/path/to/your/file.csv")
# print(counts)
