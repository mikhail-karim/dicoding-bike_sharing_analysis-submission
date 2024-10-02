import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

def weather_effect_on_shares(df):
    daily_weather_df = df.groupby('date').agg({
        'total': 'sum', 
        'normal_temp': 'mean',
        'normal_humidity': 'mean'
    }).reset_index()
    
    return daily_weather_df


def shares_on_unsuitable_weather(df):
    unsuitable_weather_df = main_hour_df.groupby('weather_type').agg({
        'total': 'sum'
    }).reset_index()
    
    unsuitable_weather_df = unsuitable_weather_df[~unsuitable_weather_df['weather_type'].isin(['Clear/Cloudy'])]
    
    return unsuitable_weather_df


def shares_on_different_day_types(df):
    day_type_df = df.groupby('day_type').agg({
        'total': 'sum'
    }).reset_index()
    
    day_type_df['day_type'] = day_type_df['day_type'].replace({
        0 : 'Weekend',
        1 : 'Working Day'
    })
    
    return day_type_df


def shares_by_the_hours(df):
    hourly_rentals_df = df.groupby('hour').agg({
        'total': 'sum'
    }).reset_index()
    
    hourly_rentals_df['average'] = hourly_rentals_df['total'] / df['total'].sum()
    
    return hourly_rentals_df

# Load cleaned data
main_day_df = pd.read_csv("https://raw.githubusercontent.com/mikhail-karim/dicoding-bike_sharing_analysis-submission/refs/heads/main/dashboard/main_day.csv")
main_hour_df = pd.read_csv("https://raw.githubusercontent.com/mikhail-karim/dicoding-bike_sharing_analysis-submission/refs/heads/main/dashboard/main_hour.csv")

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("./dashboard/Bicycle.png")
    st.markdown("""
    Name: Mikhail Shams Afzal Karim\n
    Email: mikhailsakarim@gmail.com\n
    ID Dicoding: mikhailkarim2004\n
    """)

# Convert date column to datetime
main_day_df['date'] = pd.to_datetime(main_day_df['date'])

# Prepare dataframes for charts
daily_weather_df = weather_effect_on_shares(main_day_df)
unsuitable_weather_df = shares_on_unsuitable_weather(main_day_df)
day_type_df = shares_on_different_day_types(main_day_df)
hourly_rentals_df = shares_by_the_hours(main_hour_df)

# Dashboard header
st.header(':sparkles: Bike Sharing Data Analysis :sparkles:')

col1, col2, col3 = st.columns(3)
with col1:
    total_users = main_day_df['total'].sum()
    st.metric("Total Users", value=total_users)

with col2:
    total_registered = main_day_df['registered'].sum()
    st.metric("Registered Users", value=total_registered)

with col3:
    total_casual = main_day_df['casual'].sum()
    st.metric("Casual Users", value=total_casual)

# 1. Total Bike Share Usage Over Time
st.subheader('Total Bike Share Usage Over Time')
fig1, ax1 = plt.subplots(figsize=(12, 6))
ax1.plot(daily_weather_df['date'], daily_weather_df['total'], label='Total Bike Rentals', color='blue')
ax1.set_xlabel('Date')
ax1.set_ylabel('Total Rentals')
ax1.set_title('Daily Bike Sharing')
ax1.legend()
ax1.grid(True)
st.pyplot(fig1)

# 2. Average Temperature Over Time
st.subheader('Average Temperature Over Time')
fig2, ax2 = plt.subplots(figsize=(12, 6))
ax2.plot(daily_weather_df['date'], daily_weather_df['normal_temp'], label='Average Temperature (°C)', color='orange')
ax2.set_xlabel('Date')
ax2.set_ylabel('Temperature (°C)')
ax2.set_title('Average Daily Temperature')
ax2.legend()
ax2.grid(True)
st.pyplot(fig2)

# 3. Average Humidity Over Time
st.subheader('Average Humidity Over Time')
fig3, ax3 = plt.subplots(figsize=(12, 6))
ax3.plot(daily_weather_df['date'], daily_weather_df['normal_humidity'], label='Average Humidity (%)', color='green')
ax3.set_xlabel('Date')
ax3.set_ylabel('Humidity (%)')
ax3.set_title('Average Daily Humidity')
ax3.legend()
ax3.grid(True)
st.pyplot(fig3)

st.markdown(f"""
    These charts shows that the changes in weather conditions such as temperature and humidity does NOT have any significant impact, if any, on the bike sharing usage.
    """, unsafe_allow_html=True)

# 4. Bike Rentals Under Unsuitable Weather Conditions
st.subheader('Bike Sharing Under Unsuitable Weather Conditions')
fig4, ax4 = plt.subplots(figsize=(12, 6))

# Ensure you are plotting total rentals per weather condition
sns.barplot(data=unsuitable_weather_df, x='weather_type', y='total', ax=ax4)

# Set labels and title
ax4.set_xlabel('Weather Condition')
ax4.set_ylabel('Total Rentals')
ax4.set_title('Total Rentals During Unsuitable Weather Conditions')
ax4.set_ylim(1000, 800000)

# Show the plot
st.pyplot(fig4)

st.markdown(f"""
    This charts shows that under unsuitable weather condition, bike sharing usage still sees relatively high rates as long as it's a non-stormy weather condition.
    """, unsafe_allow_html=True)

# 5. Bike Sharing Usage by Day Type
st.subheader('Bike Sharing Usage by Day Type')
fig5, ax5 = plt.subplots(figsize=(6, 6))
ax5.pie(day_type_df['total'], labels=day_type_df['day_type'], autopct='%1.1f%%', startangle=90)
ax5.axis('equal')  # Equal aspect ratio ensures pie chart is circular.
ax5.set_title('Total Bike Rentals by Day Type (Working Day vs Weekend)')
st.pyplot(fig5)

st.markdown(f"""
    This charts shows that bike sharing are most often during weekends.
    """, unsafe_allow_html=True)

# 6. Bike Rentals by Hour of the Day
st.subheader('Bike Rentals by Hour of the Day')
fig6, ax6 = plt.subplots(figsize=(16, 6))
fig7, ax7 = plt.subplots(figsize=(16, 6))


# Total Rentals by Hour
sns.barplot(x='hour', y='total', data=hourly_rentals_df, ax=ax6, color='blue')
ax6.set_xlabel('Hour of the Day')
ax6.set_ylabel('Total Rentals')
ax6.set_title('Total Bike Rentals by Hour of the Day')

st.pyplot(fig6)

# Average Rentals by Hour
sns.barplot(x='hour', y='average', data=hourly_rentals_df, ax=ax7, color='orange')
ax7.set_xlabel('Hour of the Day')
ax7.set_ylabel('Average Rentals')
ax7.set_title('Average Bike Rentals by Hour of the Day')

st.pyplot(fig7)

st.markdown(f"""
    This charts shows that evening hours saw the highest rate in bike sharing, whereas early morning hours before 7AM saw the lowest rate in bike sharing.
    """, unsafe_allow_html=True)
