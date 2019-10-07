#necessary imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib.patches as mpatches
import scipy.stats
from numpy.polynomial.polynomial import polyfit

#getting the file paths to the population data frames
population2012 = 'Population/ACS_12_5YR_B15003.csv'
population2013 = 'Population/ACS_13_5YR_B15003.csv'
population2014 = 'Population/ACS_14_5YR_B15003.csv'
population2015 = 'Population/ACS_15_5YR_B15003.csv'
population2016 = 'Population/ACS_16_5YR_B15003.csv'
population2017 = 'Population/ACS_17_5YR_B15003.csv'
filesPopulation = {'2012':population2012, '2013':population2013, '2014':population2014, 
                   '2015':population2015, '2016':population2016, '2017':population2017}



#dividing up the counties of North Dakota into three different regions
County_to_Regions = {
          'Adams County, North Dakota': 'West',
          'Barnes County, North Dakota': 'Central',
          'Benson County, North Dakota': 'Central',
          'Billings County, North Dakota': 'West',
          'Bottinneau County, North Dakota': 'Central',
          'Bowman County, North Dakota': 'West',
          'Burke County, North Dakota': 'West',
          'Burleigh County, North Dakota': 'Central',
          'Cass County, North Dakota': 'East',
          'Cavalier County, North Dakota': 'East',
          'Dickey County, North Dakota': 'Central',
          'Divide County, North Dakota': 'West',
          'Dunn County, North Dakota': 'West',
          'Eddy County, North Dakota': 'Central',
          'Emmons County, North Dakota': 'Central',
          'Foster County, North Dakota': 'Central',
          'Golden Valley County, North Dakota': 'West',
          'Grand Forks County, North Dakota': 'East',
          'Grant County, North Dakota': 'West',
          'Griggs County, North Dakota': 'Central',
          'Hettinger County, North Dakota': 'West',
          'Kidder County, North Dakota': 'Central',
          'LaMoure County, North Dakota': 'Central',
          'Logan County, North Dakota': 'Central',
          'McHenry County, North Dakota': 'Central',
          'McIntosh County, North Dakota': 'Central',
          'McKenzie County, North Dakota': 'West',
          'McLean County, North Dakota': 'Central',
          'Mercer County, North Dakota': 'West',
          'Morton County, North Dakota': 'West',
          'Mountrail County, North Dakota': 'West',
          'Nelson County, North Dakota': 'East',
          'Oliver County, North Dakota': 'West',
          'Pembina County, North Dakota': 'East',
          'Pierce County, North Dakota': 'Central',
          'Ramsey County, North Dakota': 'East',
          'Ransom County, North Dakota': 'Central',
          'Renville County, North Dakota': 'Central',
          'Richland County, North Dakota': 'East',
          'Rolette County, North Dakota': 'Central',
          'Sargent County, North Dakota': 'Central',
          'Sheridan County, North Dakota': 'Central',
          'Sioux County, North Dakota': 'West',
          'Slope County, North Dakota': 'West',
          'Stark County, North Dakota': 'West',
          'Steele County, North Dakota': 'East',
          'Stutsman County, North Dakota': 'Central',
          'Towner County, North Dakota': 'Central',
          'Traill County, North Dakota': 'East',
          'Walsh County, North Dakota': 'East',
          'Ward County, North Dakota': 'Central',
          'Wells County, North Dakota': 'Central',
          'Williams County, North Dakota': 'West'}

#Making this so it can be added to the data frames, to be used later
Regions = []
for key, value in County_to_Regions.items():
    Regions.append(value)

#Making dictionaries to put all the years of the population data
combined_db_Population={}
westPopulation = {}
eastPopulation = {}
centralPopulation = {}

#importing all the population data dataframes
for key, value in filesPopulation.items():
    fileDataPopulation = pd.read_csv(value, skiprows=1, na_values = '', usecols = [2, 3, 4, 35, 36, 37, 38, 39, 40, 41, 42, 
                                                   43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                       names = (['County', 'Total Population', 'Total MOE', 'High School', 'High School MOE', 'GED', 
                                 'GED MOE', 'Small College', 'Small College MOE', 'Big College', 'Big College MOE', 
                                 'Associate', 'Associate MOE', 'Bachelor', 'Bachelor MOE', 'Master', 'Master MOE', 
                                 'Professional', 'Professional MOE', 'Doctorate', 'Doctorate MOE']), dtype = {'County':'str', 
                                 'Total Population':'int', 'Total MOE':'float', 'High School':'int', 'High School MOE':'int', 
                                 'GED':'int', 'GED MOE':'int', 'Small College':'int', 'Small College MOE':'int', 
                                 'Big College':'int', 'Big College MOE':'int', 'Associate':'int', 'Associate MOE':'int', 
                                 'Bachelor':'int', 'Bachelor MOE':'int', 'Master':'int', 'Master MOE':'int', 
                                 'Professional':'int', 'Professional MOE':'int', 'Doctorate':'int', 'Doctorate MOE':'int'})
    
    #Using the region separation above and applying it to the data frames
    fileDataPopulation['Region'] = Regions
    
    #making three new dataframes by separating the counties by Region 
    tempwest = fileDataPopulation.loc[fileDataPopulation['Region'] == 'West']
    tempeast = fileDataPopulation.loc[fileDataPopulation['Region'] == 'East']
    tempcentral = fileDataPopulation.loc[fileDataPopulation['Region'] == 'Central']

    #putting the new dataframes into their respective Dictionary
    combined_db_Population.update({key:fileDataPopulation.copy()})
    westPopulation.update({key:tempwest.copy()})
    eastPopulation.update({key:tempeast.copy()})
    centralPopulation.update({key:tempcentral.copy()})
    
#############################################

#file paths for income data
income2010 = 'EducationalAttainment/ACS_10_5YR_B20004_with_ann.csv'
income2011 = 'EducationalAttainment/ACS_11_5YR_B20004_with_ann.csv'
income2012 = 'EducationalAttainment/ACS_12_5YR_B20004_with_ann.csv'
income2013 = 'EducationalAttainment/ACS_13_5YR_B20004_with_ann.csv'
income2014 = 'EducationalAttainment/ACS_14_5YR_B20004_with_ann.csv'
#2015 has been left out due to lack of data
income2016 = 'EducationalAttainment/ACS_16_5YR_B20004_with_ann.csv'
income2017 = 'EducationalAttainment/ACS_17_5YR_B20004_with_ann.csv'
filesIncome = {'2010':income2010, '2011':income2011, '2012':income2012, '2013':income2013, '2014':income2014, '2016':income2016, '2017':income2017}

#Making dictionaries to put all the years of the income data
combined_db_Income={}
westIncome = {}
eastIncome = {}
centralIncome = {}


#importing all the population data dataframes
for key, value in filesIncome.items():
    fileDataIncome = pd.read_csv(value, skiprows = 2, na_values=(['**','-']), names = (['County', 'Median Total', 
                    'MOE Median Total', 'Less Than High School Median','MOE Less Than High School', 
                    'High School Median', 'MOE High School', 'Some College/Associate Median', 
                    'MOE Some College/Associate', 'Bachelor', 'MOE Bachelor', 'Graduate', 
                    'MOE Graduate']), 
                    usecols = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], dtype = {'County':'str', 
                    'Median Total':'int', 'MOE Median Total':'int', 
                    'Less Than High School Median':'float', 'MOE Less Than High School':'float', 
                    'High School Median':'int', 'MOE High School':'int', 
                    'Some College/Associate Median':'int','MOE Some College/Associate':'int', 
                    'Bachelor':'int', 'MOE Bachelor':'int', 'Graduate':'float', 'MOE Graduate':'float'})
    
    #Using the region separation above and applying it to the data frames
    fileDataIncome['Region'] = Regions
    
    #making three new dataframes by separating the counties by Region 
    tempwest = fileDataIncome.loc[fileDataIncome['Region'] == 'West']
    tempeast = fileDataIncome.loc[fileDataIncome['Region'] == 'East']
    tempcentral = fileDataIncome.loc[fileDataIncome['Region'] == 'Central']
    
    tempwest['Percentage']= tempwest['Median Total'] / tempwest['Bachelor']
    tempeast['Percentage']= tempeast['Median Total']/ tempeast['Bachelor']
    tempcentral['Percentage']= tempcentral['Median Total'] / tempcentral['Bachelor']
    
    #putting the new dataframes into their respective Dictionary
    combined_db_Income.update({key:fileDataIncome.copy()})
    westIncome.update({key:tempwest.copy()})
    eastIncome.update({key:tempeast.copy()})
    centralIncome.update({key:tempcentral.copy()})

#########################################################

#denotating years to be used for loops
yearsIncome = ['2012', '2013', '2014', '2015', '2016', '2017']

#empty lists for the amount of bachelors by region
west_Bachelor = []
east_Bachelor = []
central_Bachelor = []

#empty lists for the total population by region
west_Total =[]
east_Total = []
central_Total = []


#putting the data by year into the arrays above
for year in yearsIncome:
    x = westPopulation[year]['Bachelor'].sum()
    west_Bachelor.append(x)
    a = westPopulation[year]['Total Population'].sum()
    west_Total.append(a)
    y = eastPopulation[year]['Bachelor'].sum()
    east_Bachelor.append(y)
    b = eastPopulation[year]['Total Population'].sum()
    east_Total.append(b)
    z = centralPopulation[year]['Bachelor'].sum()
    central_Bachelor.append(z)
    c = centralPopulation[year]['Total Population'].sum()
    central_Total.append(c)

#turning the lists into arrays
west_Bachelor_array = np.asarray(west_Bachelor)
west_Total_array = np.asarray(west_Total)
east_Bachelor_array = np.asarray(east_Bachelor)
east_Total_array = np.asarray(east_Total)
central_Bachelor_array = np.asarray(central_Bachelor)
central_Total_array = np.asarray(central_Total)

#using the arrays above to get the percent of bachelor degrees
west_Percent = (west_Bachelor_array / west_Total_array)*100
east_Percent = (east_Bachelor_array / east_Total_array)*100
central_Percent = (central_Bachelor_array / central_Total_array)*100



#redoing the years array to fit the Population data
yearsPopulation = ['2012', '2013', '2014', '2016', '2017']


#empty arrays to put the amount of bachelors per county and region
westBachelorSeperate = []
eastBachelorSeperate = []
centralBachelorSeperate = []


#getting the population bachelor amount again
for year in yearsPopulation:
    x = westPopulation[year]['Bachelor']/westPopulation[year]['Total Population']
    y = eastPopulation[year]['Bachelor']/eastPopulation[year]['Total Population']
    z = centralPopulation[year]['Bachelor']/centralPopulation[year]['Total Population']
    
    westBachelorSeperate.append(x)
    eastBachelorSeperate.append(y)
    centralBachelorSeperate.append(z)



#getting the median income for each county
westMedian=[]
eastMedian=[]
centralMedian=[]
for year in yearsPopulation:
    x = westIncome[year]['Median Total']
    y = eastIncome[year]['Median Total']
    z = centralIncome[year]['Median Total']
    
    westMedian.append(x)
    eastMedian.append(y)
    centralMedian.append(z)

#empty arrays for the R values for each year
r_values_west=[]
r_values_east=[]
r_values_central=[]
r_values_total=[]

#this does three things 
for x in range(5):
    #making scatter plots showing each county's bachelor degree compared to income level
    plt.scatter(westMedian[x],westBachelorSeperate[x], c= 'red',alpha = 0.6)
    plt.scatter(eastMedian[x],eastBachelorSeperate[x], c = 'blue',alpha = 0.6)
    plt.scatter(centralMedian[x],centralBachelorSeperate[x], c = 'black',alpha = 0.6)
    
    #This obtains the best fit line for each region and displays it
    b_west, m_west = polyfit(westMedian[x], westBachelorSeperate[x], 1)
    b_east, m_east = polyfit(eastMedian[x], eastBachelorSeperate[x], 1)
    b_central, m_central = polyfit(centralMedian[x], centralBachelorSeperate[x], 1)
    plt.plot(westMedian[x], b_west + westMedian[x]*m_west, c='red', alpha = 0.6)
    plt.plot(eastMedian[x], b_east + eastMedian[x]*m_east, c='blue', alpha = 0.6)
    plt.plot(centralMedian[x], b_central + centralMedian[x]*m_central, c='black', alpha = 0.6)
    
    #scatterplot development
    plt.title(yearsPopulation[x])
    plt.xlabel("County Median Income")
    plt.ylabel("Percentage of Bachelor Degrees")
    red_west = mpatches.Patch(color='red', label='West Counties')
    blue_east = mpatches.Patch(color='blue', label='East Counties')
    black_central = mpatches.Patch(color='black', label='Central Counties')
    plt.legend(handles=[red_west, blue_east, black_central])
    plt.show()
    plt.clf()
    
    #This gets the R values for the Bachelor degrees compared to income
    slope, intercept, r_value_west, p_value, std_err = scipy.stats.linregress(westMedian[x], westBachelorSeperate[x])
    r_values_west.append(r_value_west)
    slope, intercept, r_value_east, p_value, std_err = scipy.stats.linregress(eastMedian[x], eastBachelorSeperate[x])
    r_values_east.append(r_value_east)
    slope, intercept, r_value_central, p_value, std_err = scipy.stats.linregress(centralMedian[x], centralBachelorSeperate[x])
    r_values_central.append(r_value_central)
    westMedian_List = westMedian[x].tolist()
    eastMedian_List = eastMedian[x].tolist()
    centralMedian_List = centralMedian[x].tolist()
    westBachelor_List = westBachelorSeperate[x].tolist()
    eastBachelor_List = eastBachelorSeperate[x].tolist()
    centralBachelor_List = centralBachelorSeperate[x].tolist()
    all_points_Income = westMedian_List + eastMedian_List + centralMedian_List
    all_points_Bachelor = westBachelor_List + eastBachelor_List + centralBachelor_List
    slope, intercept, r_value_total, p_value, std_err = scipy.stats.linregress(all_points_Income, all_points_Bachelor)
    r_values_total.append(r_value_total)


#This plots the R values for each year based on county position
plt.plot(yearsPopulation, r_values_west, color = 'red', label='West')
plt.plot(yearsPopulation, r_values_east, color = 'blue', label='East')
plt.plot(yearsPopulation, r_values_central, color = 'black', label='Central')
plt.plot(yearsPopulation, r_values_total, color = 'yellow', label = 'Total State')
plt.title('Correlation Coefficient between Bachelor Percentage and Median Income')
plt.xlabel('Year')
plt.ylabel('Correlation Coefficient')
plt.legend(loc='center left')