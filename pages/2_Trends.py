import streamlit as st
import pandas as pd
import plotly.express as px
from modules.processor import process_data


# Title of the page
st.title("Trends & Insights")

# Sidebar filter copied from the dashboard page
st.sidebar.header("Filters")
time_range = st.sidebar.selectbox(
    "Select Time Range",
    options=["Last 7 Days", "Last 30 Days", "All time"],
    index=2
)

def filter_dataframe(df, time_range):
    if time_range == "Last 7 Days":
        return df[df['date'] >= (df['date'].max() - pd.Timedelta(days=7))]
    elif time_range == "Last 30 Days":
        return df[df['date'] >= (df['date'].max() - pd.Timedelta(days=30))]
    else:
        return df

# Load and filter data
df = process_data()

# Check for 'calories_burned' column presence
if 'calories_burned' not in df.columns:
    st.error("'calories_burned' column is not present in the data.")
else:
    # Filter data based on selected time range
    filtered_df = filter_dataframe(df, time_range)

    # Display summary statistics
    st.subheader("Summary Statistics")
    summary_cols = ['Recovery_Score', 'sleep_hours', 'steps', 'calories_burned']
    st.write(filtered_df[summary_cols].agg(['mean', 'min', 'max']))

    # Line chart for Recovery Score month-wise
    st.subheader("Average Recovery Score per Month")
    filtered_df['month'] = filtered_df['date'].dt.to_period('M').astype(str)  # Convert Period to string
    monthly_avg_recovery = filtered_df.groupby('month')['Recovery_Score'].mean().reset_index()
    fig_line = px.line(monthly_avg_recovery, x='month', y='Recovery_Score', title='Monthly Average Recovery Score')
    st.plotly_chart(fig_line, use_container_width=True)

    # Histograms distribution
    st.subheader("Distribution Histograms")
    col1, col2 = st.columns(2)

    # Histogram for Steps
    fig_steps = px.histogram(filtered_df, x='steps', nbins=50, title='Steps Distribution')
    col1.plotly_chart(fig_steps, use_container_width=True)

    # Histogram for Calories Burned
    fig_calories = px.histogram(filtered_df, x='calories_burned', nbins=50, title='Calories Burned Distribution')
    col2.plotly_chart(fig_calories, use_container_width=True)

    # Columns for further histograms
    col3, col4 = st.columns(2)

    # Histogram for Recovery Score
    fig_recovery = px.histogram(filtered_df, x='Recovery_Score', nbins=50, title='Recovery Score Distribution')
    col3.plotly_chart(fig_recovery, use_container_width=True)

    # Histogram for Sleep Hours
    fig_sleep = px.histogram(filtered_df, x='sleep_hours', nbins=50, title='Sleep Hours Distribution')
    col4.plotly_chart(fig_sleep, use_container_width=True)
