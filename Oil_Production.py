#import necessary packages
import pandas as pd
import matplotlib.pyplot as plt

#define csv and read in as pandas dataframe
f = 'Oil/ND_Oil.csv'
df = pd.read_csv(f, skiprows = 17, nrows=96, header = None)
df.columns = ['Month', 'Oil Produced']

#flips dataframe to show 2010 data first
df = df.reindex(index=df.index[::-1])

#resets index adn deletes index column
df = df.reset_index()
df = df.drop(columns='index')

#divide data into separate years
oilProduction2010= df.loc[0:13,:]
oilProduction2011= df.loc[13:25,:]
oilProduction2012= df.loc[25:37,:]
oilProduction2013= df.loc[37:49,:]
oilProduction2014= df.loc[49:61,:]
oilProduction2015= df.loc[61:73,:]
oilProduction2016= df.loc[73:85,:]
oilProduction2017= df.loc[85:97,:]

#define lists to find sum for each year
dfs = [oilProduction2010, oilProduction2011, oilProduction2012, oilProduction2013, oilProduction2014, oilProduction2015, oilProduction2016, oilProduction2017]
Sums = []
Years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]

#sums oil for each year
for x in dfs:
    Total_oil = x['Oil Produced'].sum()
    Sums.append(Total_oil)

#plot to show oil production for each year
plt.plot(Years, Sums)
plt.title('North Dakota Oil Production')
plt.ylabel('Thousands of Barrels')
plt.xlabel('Years')
plt.ylim(0)