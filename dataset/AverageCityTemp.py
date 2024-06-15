import os
import pandas as pd
from sklearn.linear_model import LinearRegression

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Get the current working directory
current_directory = os.getcwd()

# Construct the full path to your CSV file
file_name = 'averaged_data.csv'
file_path = os.path.join(current_directory, "dataset", "historicalTemps", file_name)

# Step 1: Load data into a pandas DataFrame
df = pd.read_csv(file_path)

def getCityTemp(country_name, city_name):

  # Example Args
  #country_name = 'Algeria'
  #city_name = 'Algiers'

  filtered_df = df[(df['Country'] == country_name) & (df['City'] == city_name)]
  fahrenheit_temp = filtered_df['AvgTemperature'].iloc[0]
  
  celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
  
  return celsius_temp

