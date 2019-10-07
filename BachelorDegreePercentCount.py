#import necessary packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

#defining educational population data for each year
population2012 = 'Population/ACS_12_5YR_B15003.csv'
population2013 = 'Population/ACS_13_5YR_B15003.csv'
population2014 = 'Population/ACS_14_5YR_B15003.csv'
population2015 = 'Population/ACS_15_5YR_B15003.csv'
population2016 = 'Population/ACS_16_5YR_B15003.csv'
population2017 = 'Population/ACS_17_5YR_B15003.csv'
files = {'2012':population2012, '2013':population2013, '2014':population2014, '2015':population2015, '2016':population2016, '2017':population2017}

#defines counties as different regions
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
Regions = []
for key, value in County_to_Regions.items():
    Regions.append(value)

#reads in data as pandas dataframes into regional dictionaries
combined_db={}
west = {}
east = {}
central = {}
for key, value in files.items():
    fileData = pd.read_csv(value, skiprows=1, na_values = '', usecols = [2, 3, 4, 35, 36, 37, 38, 39, 40, 41, 42, 
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

    fileData['Region'] = Regions
    
    #divides counties into regions
    tempwest = fileData.loc[fileData['Region'] == 'West']
    tempeast = fileData.loc[fileData['Region'] == 'East']
    tempcentral = fileData.loc[fileData['Region'] == 'Central']
    
    #assigns dataframes to dictionaries
    combined_db.update({key:fileData.copy()})
    west.update({key:tempwest.copy()})
    east.update({key:tempeast.copy()})
    central.update({key:tempcentral.copy()})

#lists in order to find sums
years = ['2012', '2013', '2014', '2015', '2016', '2017']
west_Bachelor = []
east_Bachelor = []
central_Bachelor = []
west_Total =[]
east_Total = []
central_Total = []

#sums total and bachelor populations for different dataframes for different regions
for year in years:
    x = west[year]['Bachelor'].sum()
    west_Bachelor.append(x)
    a = west[year]['Total Population'].sum()
    west_Total.append(a)
    y = east[year]['Bachelor'].sum()
    east_Bachelor.append(y)
    b = east[year]['Total Population'].sum()
    east_Total.append(b)
    z = central[year]['Bachelor'].sum()
    central_Bachelor.append(z)
    c = central[year]['Total Population'].sum()
    central_Total.append(c)
    
#makes lists into arrays in order to do computations
west_Bachelor_array = np.asarray(west_Bachelor)
west_Total_array = np.asarray(west_Total)
east_Bachelor_array = np.asarray(east_Bachelor)
east_Total_array = np.asarray(east_Total)
central_Bachelor_array = np.asarray(central_Bachelor)
central_Total_array = np.asarray(central_Total)

#calculates percentages
west_Percent = (west_Bachelor_array / west_Total_array)*100
east_Percent = (east_Bachelor_array / east_Total_array)*100
central_Percent = (central_Bachelor_array / central_Total_array)*100

#makes graph for Bachelor percentage
plt.figure(0)
plt.plot(years, west_Percent, color='red', label = 'West')
plt.plot(years, east_Percent, color='blue', label = 'East')
plt.plot(years, central_Percent, color='black', label = 'Central')
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.title('Percentage of Bachelor Degrees of the Total Population')
plt.ylim(16,24)
plt.legend(loc='center left')

#makes graph for raw Bachelor numbers
plt.figure(1)
plt.plot(years, west_Bachelor_array, color='red', label='West')
plt.plot(years, east_Bachelor_array, color='blue', label='East')
plt.plot(years, central_Bachelor_array, color='black', label='Central')
plt.xlabel('Year')
plt.title('Number of people with a Bachelor Degree in Different Regions of ND over time')
plt.ylabel('Number of People')
plt.legend(loc='center right')