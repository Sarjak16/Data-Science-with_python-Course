# Customizing data appearence.....................................................................................................................
# Call ax.plot to plot "MLY-PRCP-NORMAL" against "MONTHS" in both DataFrames.
# Pass the color key-word arguments to these commands to set the color of the Seattle data to blue ('b') and the Austin data to red ('r').
# Pass the marker key-word arguments to these commands to set the Seattle data to circle markers ('o') and the Austin markers to triangles pointing downwards ('v').
# Pass the linestyle key-word argument to use dashed lines for the data from both cities ('--').

# Plot Seattle data, setting data appearance
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color="b", marker="o", linestyle="--")

# Plot Austin data, setting data appearance
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color="r", marker="v", linestyle="--")

# Call show to display the resulting plot
plt.show()

#Customizing axis labels and adding titles........................................................................................................
# Use the set_xlabel method to add the label: "Time (months)".
# Use the set_ylabel method to add the label: "Precipitation (inches)".
# Use the set_title method to add the title: "Weather patterns in Austin and Seattle".

ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# Customize the x-axis label
ax.set_xlabel ("Time (months)")

# Customize the y-axis label
ax.set_ylabel ("Precipitation (inches)")

# Add the title
ax.set_title("Weather patterns in Austin and Seattle")

# Display the figure
plt.show()
