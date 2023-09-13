# Bar charts.................................................................
# Call the ax.bar method to plot the "Gold" column as a function of the country.
# Use the ax.set_xticklabels to set the x-axis tick labels to be the country names.
# In the call to ax.set_xticklabels rotate the x-axis tick labels by 90 degrees by using the rotation key-word argument.
# Set the y-axis label to "Number of medals".

fig, ax = plt.subplots()

# Plot a bar-chart of gold medals as a function of country
ax.bar(medals.index, medals["Gold"])

# Set the x-axis tick labels to the country names
ax.set_xticklabels(medals.index, rotation= 90)

# Set the y-axis label
ax.set_ylabel("Number of medals")

# plt.show()


#Stacked BarChart

# Call the ax.bar method to add the "Gold" medals. Call it with the label set to "Gold".
# Call the ax.bar method to stack "Silver" bars on top of that, using the bottom key-word argument so the bottom of the bars will be on top of the gold medal bars, and label to add the label "Silver".
# Use ax.bar to add "Bronze" bars on top of that, using the bottom key-word and label it as "Bronze".
# Add bars for "Gold" with the label "Gold"
ax.bar(medals.index, medals["Gold"], label="Gold")

# Stack bars for "Silver" on top with label "Silver"
ax.bar(medals.index, medals["Silver"], bottom=medals["Gold"], label="Silver")

# Stack bars for "Bronze" on top of that with label "Bronze"
ax.bar(medals.index, medals["Bronze"], bottom=medals["Gold"] + medals["Silver"], label="Bronze")

# Display the legend
ax.legend()

plt.show()

#Quantitative comparisons: histograms

