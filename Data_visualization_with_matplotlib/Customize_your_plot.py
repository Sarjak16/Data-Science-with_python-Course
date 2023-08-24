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
