# a321_temps_analysis.py
# This program uses the pandas module to load a 2-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot a graph and a bar chart
import matplotlib.pyplot as plt
import pandas as pd

# Load in the data with read_csv()
# TODO #1: change the file name to your data file name
co2_data = pd.read_csv("co2_data.csv", header=0)   # identify the header row
co2_data['Average'] = co2_data['Average'].replace(-99.99, math.nan)
co2_data.dropna(subset=['Average'], inplace=True)
# TODO #2: Use matplotlib to make a line graph
plt.plot(co2_data["decimal_year"], co2_data['Average'], color='gray')
plt.ylabel('CO2 PPM')
plt.xlabel('Years')
plt.title('Change in Temperatures')
plt.show()

# TODO #3: Plot LOWESS in a line graph

# TODO #4: Use matplotlib to make a bar chart


# TODO #5: Calculate min, max, and avg anomaly and the corresponding min/max years
