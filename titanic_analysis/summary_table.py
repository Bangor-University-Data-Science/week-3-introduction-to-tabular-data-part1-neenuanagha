import pandas as pd

# Mock a DataFrame
mock_df = pd.DataFrame(data={
    'Age': [22, 38, 26, 35, None],
    'Sex': ['male', 'female', 'female', 'male', 'male'],
    'Survived': [0, 1, 1, 0, 1]
})

# Function to create summary table
def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, 
    and if it has missing values.
    
    Args:
        df (pd.DataFrame): The dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    summary_data = {
        'Feature Name': df.columns,
        'Data Type': df.dtypes.values,
        'Has Missing Values?': df.isnull().any().values,
        'Number of Unique Values': df.nunique().values
    }
    summary_df = pd.DataFrame(summary_data)
    return summary_df

# Create the summary DataFrame
summary_df = create_summary_table(mock_df)

# Debug: Print the columns to verify their names
print("Columns in summary_df:", summary_df.columns)

# Assertions to verify the summary table structure
assert 'Feature Name' in summary_df.columns, f"Summary should include 'Feature Name'. Found columns: {summary_df.columns.tolist()}"
assert 'Data Type' in summary_df.columns, f"Summary should include 'Data Type'. Found columns: {summary_df.columns.tolist()}"
assert 'Has Missing Values?' in summary_df.columns, f"Summary should include 'Has Missing Values?'. Found columns: {summary_df.columns.tolist()}"
assert 'Number of Unique Values' in summary_df.columns, f"Summary should include 'Number of Unique Values'. Found columns: {summary_df.columns.tolist()}"

# Print the summary DataFrame to visually verify
print(summary_df)
