#simple scatter plot
# Using the ax.scatter method, add the data to the plot: "co2" on the x-axis and "relative_temp" on the y-axis.
# Set the x-axis label to "CO2 (ppm)".
# Set the y-axis label to "Relative temperature (C)".

fig, ax = plt.subplots()

# Add data: "co2" on x-axis, "relative_temp" on y-axis
ax.scatter(climate_change["co2"], climate_change["relative_temp"])

# Set the x-axis label to "CO2 (ppm)"
ax.set_xlabel("CO2 (ppm)")

# Set the y-axis label to "Relative temperature (C)"
ax.set_ylabel("Relative temperature (C)")

plt.show()


#ENCODING TIME BY COLOUR
# Using the ax.scatter method add a scatter plot of the "co2" column (x-axis) against the "relative_temp" column.
# Use the c key-word argument to pass in the index of the DataFrame as input to color each point according to its date.
# Set the x-axis label to "CO2 (ppm)" and the y-axis label to "Relative temperature (C)".

fig, ax = plt.subplots()

# Add data: "co2", "relative_temp" as x-y, index as color
ax.scatter(climate_change["co2"], climate_change["relative_temp"], c=climate_change.index)

# Set the x-axis label to "CO2 (ppm)"
ax.set_xlabel("CO2 (ppm)")

# Set the y-axis label to "Relative temperature (C)"
ax.set_ylabel("Relative temperature (C)")

plt.show()