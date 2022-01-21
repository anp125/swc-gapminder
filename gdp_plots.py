import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

filename = 'data/gapminder_gdp_oceania.csv'

# load data and transpose so that country names are
# the columns and their gdp data becomes the rows
data = pandas.read_csv('data/gapminder_gdp_oceania.csv', index_col = 'country').T

# create a plot of the transposed data
ax = data.plot(title = filename)

# set some plot attributes
ax.set_xlabel("Year")
ax.set_ylabel("GDP per Capita")
# set the x location and lebels
ax.set_xticks(range(len(data.index)))
ax.set_xtickslabels(data.index, rotation = 45)


# display the plot
plt.show()
