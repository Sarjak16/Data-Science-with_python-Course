#Sharing_Visualizations

# The data you will use is the same weather data we used in the first lesson: you will have available to you the DataFrame seattle_weather and the DataFrame austin_weather, both with records of the average temperature in every month.

# Select the 'ggplot' style, create a new Figure called fig, and a new Axes object called ax with plt.subplots.

# Select the 'Solarize_Light2' style, create a new Figure called fig, and a new Axes object called ax with plt.subplots.

# Use the "ggplot" style and create new Figure/Axes
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
plt.show()

# Use the "Solarize_Light2" style and create new Figure/Axes
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()

#Save figures with different sizes....
# Figure object’s set_size_inches method. This method takes a sequence of two values. The first sets the width and the second sets the height of the figure.

# Here, you will again have a Figure object called fig already provided (you can run plt.show if you want to see its contents). Use the Figure methods set_size_inches and savefig to change its size and save two different versions of this figure.

# Set the figure size as width of 3 inches and height of 5 inches and save it as 'figure_3_5.png' with default resolution.

# Set the figure size to width of 5 inches and height of 3 inches and save it as 'figure_5_3.png' with default settings.Figure object’s set_size_inches method. This method takes a sequence of two values. The first sets the width and the second sets the height of the figure.

# Here, you will again have a Figure object called fig already provided (you can run plt.show if you want to see its contents). Use the Figure methods set_size_inches and savefig to change its size and save two different versions of this figure.

# Set the figure size as width of 3 inches and height of 5 inches and save it as 'figure_3_5.png' with default resolution.

# Set the figure size to width of 5 inches and height of 3 inches and save it as 'figure_5_3.png' with default settings.


# Set figure dimensions and save as a PNG
fig.set_size_inches([3, 5])
fig.savefig('figure_3_5.png')

# Set figure dimensions and save as a PNG
fig.set_size_inches([5, 3])
fig.savefig('figure_5_3.png')


# Saving file sevral times
#Examine the figure by calling the plt.show() function.
 
 plt.show()
#Save the figure into the file my_figure.png, using the default resolution.
# Save as a PNG file
fig.savefig('my_figure.png')


#Save the figure into the file my_figure_300dpi.png and set the resolution to 300 dpi.
# Save as a PNG file with 300 dpi
fig.savefig('my_figure_300dpi.png', dpi=300)
