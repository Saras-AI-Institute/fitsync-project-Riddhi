# Title of the Streamlit app
import streamlit as st
import pandas as pd
from modules.processor import process_data


st.title("FitSync - Personal Health Analytics")

# Add a sidebar filter for time range selection
st.sidebar.header("Filters")
time_range = st.sidebar.selectbox(
    "Select Time Range",
    options=["Last 7 Days", "Last 30 Days", "All time"],
    index=2
)

# Load the data
#
#
#
df = process_data()

# Filter the dataframe based on the time range selection
def filter_dataframe(df, time_range):
    if time_range == "Last 7 Days":
        return df[df['date'] >= (df['date'].max() - pd.Timedelta(days=7))]
    elif time_range == "Last 30 Days":
        return df[df['date'] >= (df['date'].max() - pd.Timedelta(days=30))]
    else:
        return df

# Apply the filter
filtered_df = filter_dataframe(df, time_range)

# Set up a 3-column layout to display metrics
col1, col2, col3 = st.columns(3)

# Display the metrics based on the filtered data
col1.metric(label="Average Steps", value=f"{filtered_df['steps'].mean():,.0f}", delta=None)
col2.metric(label="Average Sleep Hours", value=f"{filtered_df['sleep_hours'].mean():.1f}", delta=None)
col3.metric(label="Average Recovery Score", value=f"{filtered_df['Recovery_Score'].mean():.1f}", delta=None)

# Informative text
st.write("Welcome to FitSync! Analyze your personal health data to gain insights into your wellness journey.")

# Display the processed DataFrame in a clean table
st.write("### Processed Data")
st.dataframe(filtered_df)

# Sidebar navigation options (kept as is)
st.sidebar.header("Navigation")
st.sidebar.markdown("Choose an option from below:")
st.sidebar.button("Health Insights")
st.sidebar.button("Data Upload")

# Static informative text
st.info("This dashboard allows you to track and analyze your health metrics efficiently and effectively.")