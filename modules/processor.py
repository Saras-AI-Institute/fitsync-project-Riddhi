import pandas as pd

# Function to load and process the data

def load_data():
    """
    Load the health data from a CSV file, handle missing values, 
    and convert date columns to datetime objects.
    """
    
    # Read CSV file into a DataFrame
    df = pd.read_csv('data/health_data.csv')
    
    # Fill missing 'Steps' with the median value
    steps_median = df['steps'].median()
    df['steps'].fillna(steps_median, inplace=True)
    
    # Fill missing 'Sleep_Hours' with 7.0
    df['sleep_hours'].fillna(7.0, inplace=True)
    
    # Fill missing 'Heart_Rate_bpm' with 68
    df['heart_rate_bpm'].fillna(68, inplace=True)
    
    # Fill missing values in other columns with their respective medians
    for column in df.columns:
        if column not in ['date', 'steps', 'sleep_hours', 'heart_rate_bpm']:
            median_value = df[column].median()
            df[column].fillna(median_value, inplace=True)
    
    # Convert 'Date' column to datetime objects
    df['date'] = pd.to_datetime(df['date'])
    
    return df

# Function to calculate recovery score and add it to the DataFrame

def calculate_recovery_score(df):
    """
    Calculates a 'Recovery_Score' for each day based on sleep duration,
    heart rate, and physical activity (steps). The score ranges from 0 to 100.
    """

    def calc_score(row):
        # Start with a base recovery score of 50
        score = 50

        # Sleep impacts
        sleep_hours = row['sleep_hours']
        if sleep_hours >= 7:
            score += 20  # Add points for good sleep
        elif sleep_hours < 6:
            score -= 20  # Deduct points for poor sleep

        # Heart rate impacts
        heart_rate = row['heart_rate_bpm']
        if heart_rate < 60:
            score += 15  # Add points for a lower heart rate
        elif heart_rate > 80:
            score -= 10  # Deduct points for a higher heart rate

        # Activity impacts
        steps = row['steps']
        if steps > 12000:
            score -= 5  # Reduce score slightly for very high activity due to potential strain
        elif steps < 6000:
            score -= 5  # Reduce score slightly for low activity

        # Ensure the score stays within 0 and 100
        score = max(0, min(100, score))
        return score

    # Calculate 'Recovery_Score' for each row
    df['Recovery_Score'] = df.apply(calc_score, axis=1)

    return df

# Example of how to call the function
# cleaned_data = load_data()
# print(cleaned_data.head())
# df_with_recovery = calculate_recovery_score(cleaned_data)
# print(df_with_recovery.head())

