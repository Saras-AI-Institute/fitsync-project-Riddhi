from modules.processor import load_data, calculate_recovery_score
df = load_data()
df = calculate_recovery_score(df)
print(df[['date', 'steps', 'sleep_hours', 'heart_rate_bpm']].head(10))