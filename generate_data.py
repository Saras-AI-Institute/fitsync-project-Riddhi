import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(0)

# Generate date range for 365 days starting from 2025-01-01
dates = [datetime(2025, 1, 1) + timedelta(days=i) for i in range(365)]
# Generate data for each column
steps = np.random.normal(8500, 2000, 365).clip(3000, 18000)
sleep_hours = np.random.normal(7.2, 1, 365).clip(4.5, 9.5)
heart_rate_bpm = np.random.normal(68, 10, 365).clip(48, 110)
calories_burned = np.random.uniform(1800, 4200, 365)
active_minutes = np.random.uniform(20, 180, 365)

# Create DataFrame
data = pd.DataFrame({
    'date': dates,
    'steps': steps,
    'sleep_hours': sleep_hours,
    'heart_rate_bpm': heart_rate_bpm,
    'calories_burned': calories_burned,
    'active_minutes': active_minutes
})

# Introduce 5% missing values in each column
for column in ['steps', 'sleep_hours', 'heart_rate_bpm', 'calories_burned', 'active_minutes']:
    data[column].loc[data.sample(frac=0.05).index] = np.nan

# Save to CSV
data.to_csv('data/health_data.csv', index=False)