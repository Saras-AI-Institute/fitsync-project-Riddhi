import pandas as pd

def load_and_analyze_data(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Print the first 5 rows
    print("First 5 rows:")
    print(df.head())
    
    # Print the number of missing values in each column
    print("\nNumber of missing values in each column:")
    print(df.isnull().sum())

if __name__ == "__main__":
    # Specify the file path
    file_path = "data/health_data.csv"
    
    # Call the function to load and analyze the data
    load_and_analyze_data(file_path)
