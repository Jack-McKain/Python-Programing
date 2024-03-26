import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
sh_raw = pd.read_csv('movies.csv', 
   header = None, 
   names = ['Year','Title','Comic','IMDB','RT','','OpeningWeekendBoxOffice','AvgTicketPriceThatYear','EstdOpeningAttendance','USPopThatYear'])

sh = sh_raw[np.isfinite(sh_raw.OpeningWeekendBoxOffice)]
#print(sh.head(5))

'''
# Normalize and scatterplot the scores
imdb_normalized = sh.IMDB / 10         
sh.insert(10,'IMDBNormalized',imdb_normalized)
rt_normalized = sh.RT/100        
sh.insert(11, 'RTNormalized', rt_normalized)
sh.plot.scatter(x ='RTNormalized', y ='IMDBNormalized')
plt.show()

print(sh[['RTNormalized','IMDBNormalized']].corr())
print(sh[['RTNormalized','IMDBNormalized']].describe())
'''

#Only DC movies
dc_movies = sh[sh['Comic'] == 'DC']
print(dc_movies)
print("\n\n\n")

#First 2 columns
print(dc_movies.head(2))
print("\n\n\n")

#First 2 Marvel movies
marvel_movies = sh[sh['Comic'] == 'Marvel']
print(marvel_movies.head(2))
print("\n\n\n")

#Scatterplot ticketprice vs. Year
plt.scatter(sh['Year'], sh['AvgTicketPriceThatYear'], c="red")
plt.title('Average Ticket Price by Year')
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.show()

#Correlation
print(sh[['Year','AvgTicketPriceThatYear']].corr())
print("\n\n\n")

#Summary
print(sh['OpeningWeekendBoxOffice'].describe())