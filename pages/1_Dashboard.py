import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os


# Add the modules directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.processor import process_data

# Title of the Streamlit app with emoji
st.title("FitSync - Personal Health Analytics 🚀")

# Add a sidebar filter for time range selection with emoji
st.sidebar.header("Filters 🔍")
time_range = st.sidebar.selectbox(
    "Select Time Range",
    options=["Last 7 Days 📅", "Last 30 Days 📆", "All time 🌐"],
    index=2
)

# Load the data with caching
@st.cache_data
def load_data():
    return process_data()

# Use cached data retrieval
df = load_data()

# Filter the dataframe based on the time range selection
def filter_dataframe(df, time_range):
    if time_range == "Last 7 Days 📅":
        return df[df['date'] >= (df['date'].max() - pd.Timedelta(days=7))]
    elif time_range == "Last 30 Days 📆":
        return df[df['date'] >= (df['date'].max() - pd.Timedelta(days=30))]
    else:
        return df

# Apply the filter
filtered_df = filter_dataframe(df, time_range)

# Set up a 3-column layout to display metrics
col1, col2, col3 = st.columns(3)

# Display the metrics with emojis
col1.metric(label="Avg Steps 🚶‍♂️", value=f"{filtered_df['steps'].mean():,.0f}")
col2.metric(label="Avg Sleep 💤", value=f"{filtered_df['sleep_hours'].mean():.1f}")
col3.metric(label="Avg Recovery Score 💪", value=f"{filtered_df['Recovery_Score'].mean():.1f}")

# Informative text with emoji
st.write("Welcome to FitSync! Analyze your personal health data to gain insights into your wellness journey. 🔍")

# Create two columns for the first set of charts
left_col1, right_col1 = st.columns(2)

# Dual Line Chart: Recovery Score and Sleep Hours trend over time
left_col1.write("### Recovery Score Sleep Trend 🛌")
fig1 = px.line(filtered_df, x='date', y=['Recovery_Score', 'sleep_hours'], title="Recovery Score Sleep Trend")
left_col1.plotly_chart(fig1, use_container_width=True)

# Scatter Plot: Recovery Score vs Steps, colored by Sleep_Hours
right_col1.write("### Recovery Score vs Daily Steps 🚶")
fig2 = px.scatter(filtered_df, x='steps', y='Recovery_Score', color='sleep_hours', title="Recovery Score vs Daily Steps")
right_col1.plotly_chart(fig2, use_container_width=True)

# Create another two columns for the second set of charts
left_col2, right_col2 = st.columns(2)

# Scatter Plot: Recovery Score vs heart_rate_bpm
left_col2.write("### Recovery Score vs Resting Heart Rate ❤️")
fig3 = px.scatter(filtered_df, x='heart_rate_bpm', y='Recovery_Score', title="Recovery Score vs Resting Heart Rate")
left_col2.plotly_chart(fig3, use_container_width=True)

# Line Chart: Calories_Burned trend over time
right_col2.write("### Daily Calories Burned Trend 🔥")
fig4 = px.line(filtered_df, x='date', y='calories_burned', title="Daily Calories Burned Trend")
right_col2.plotly_chart(fig4, use_container_width=True)

# Static informative text
st.info("This dashboard allows you to track and analyze your health metrics efficiently and effectively. 📊")

