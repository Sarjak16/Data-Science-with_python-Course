
# Read data with time index..............................................................
# Import the pandas library as pd.
# Read in the data from a CSV file called 'climate_change.csv' using pd.read_csv.
# Use the parse_dates key-word argument to parse the "date" column as dates.
# Use the index_col key-word argument to set the "date" column as the index.

# Import pandas as pd
import pandas as pd

# Read the data from file using read_csv
climate_change = pd.read_csv('climate_change.csv',parse_dates=["date"],index_col="date")

#Plot time-series data
# Add the data from climate_change to the plot: use the DataFrame index for the x value and the "relative_temp" column for the y values.
# Set the x-axis label to 'Time'.
# Set the y-axis label to 'Relative temperature (Celsius)'.
# Show the figure.

import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Add the time-series for "relative_temp" to the plot
ax.plot(climate_change.index, climate_change['relative_temp'])

# Set the x-axis label
ax.set_xlabel('Time')

# Set the y-axis label
ax.set_ylabel('Relative temperature (Celsius)')

# Show the figure
plt.show()



# Using a time index to zoom in...........................................................................
# Use plt.subplots to create a Figure with one Axes called fig and ax, respectively.
# Create a variable called seventies that includes all the data between "1970-01-01" and "1979-12-31".
# Add the data from seventies to the plot: use the DataFrame index for the x value and the "co2" column for the y values.

import matplotlib.pyplot as plt

# Use plt.subplots to create fig and ax
fig, ax= plt.subplots()

# Create variable seventies with data from "1970-01-01" to "1979-12-31"
seventies = climate_change["1970-01-01" : "1979-12-31"]

# Add the time-series for "co2" data from seventies to the plot
ax.plot(seventies.index, seventies["co2"])

# Show the figure
plt.show()





# PLOTTING TIMESERIES WITH DIFFERENT VARIABLES............................................................................................
# 1.Plotting two variables................................
# Use plt.subplots to create a Figure and Axes objects called fig and ax, respectively.
# Plot the carbon dioxide variable in blue using the Axes plot method.
# Use the Axes twinx method to create a twin Axes that shares the x-axis.
# Plot the relative temperature variable in red on the twin Axes using its plot method.

import matplotlib.pyplot as plt

# Initalize a Figure and Axes
fig,ax=plt.subplots()

# Plot the CO2 variable in blue
ax.plot(climate_change.index, climate_change["co2"], color='blue')

# Create a twin Axes that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature in red
ax2.plot(climate_change.index, climate_change["relative_temp"], color='red')

plt.show()
