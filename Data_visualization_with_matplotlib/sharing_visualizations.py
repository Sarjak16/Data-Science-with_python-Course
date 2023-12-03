#switching between styles:
#Select the 'ggplot' style, create a new Figure called fig, and a new Axes object called ax with plt.subplots.
# Use the "ggplot" style and create new Figure/Axes
plt.style.use("ggplot")
fig,ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
plt.show()