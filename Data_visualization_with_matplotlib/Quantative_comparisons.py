# # Bar charts.................................................................
# # Call the ax.bar method to plot the "Gold" column as a function of the country.
# # Use the ax.set_xticklabels to set the x-axis tick labels to be the country names.
# # In the call to ax.set_xticklabels rotate the x-axis tick labels by 90 degrees by using the rotation key-word argument.
# # Set the y-axis label to "Number of medals".

# fig, ax = plt.subplots()

# # Plot a bar-chart of gold medals as a function of country
# ax.bar(medals.index, medals["Gold"])

# # Set the x-axis tick labels to the country names
# ax.set_xticklabels(medals.index, rotation= 90)

# # Set the y-axis label
# ax.set_ylabel("Number of medals")

# # plt.show()