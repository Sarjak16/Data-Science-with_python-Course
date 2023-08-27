
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
