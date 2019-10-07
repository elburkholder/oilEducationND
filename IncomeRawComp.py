#import necessary packages
import pandas as pd
import matplotlib.pyplot as plt
import os

#define files
income2010 = 'EducationalAttainment/ACS_10_5YR_B20004_with_ann.csv'
income2011 = 'EducationalAttainment/ACS_11_5YR_B20004_with_ann.csv'
income2012 = 'EducationalAttainment/ACS_12_5YR_B20004_with_ann.csv'
income2013 = 'EducationalAttainment/ACS_13_5YR_B20004_with_ann.csv'
income2014 = 'EducationalAttainment/ACS_14_5YR_B20004_with_ann.csv'
#2015 has been left out due to lack of data
income2016 = 'EducationalAttainment/ACS_16_5YR_B20004_with_ann.csv'
income2017 = 'EducationalAttainment/ACS_17_5YR_B20004_with_ann.csv'

#file dictionaries to store pandas dataframes
files = {'2010':income2010, '2011':income2011, '2012':income2012, '2013':income2013, '2014':income2014, '2016':income2016, '2017':income2017}

#define counties to different regions
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

#these dictionaries will hold the pandas dataframes
combined_db={}
west = {}
east = {}
central = {}

#reading in files as pandas dataframes for each year
for key, value in files.items():
    fileData = pd.read_csv(value, skiprows = 2, na_values=(['**','-']), names = (['County', 'Median Total', 
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
    
    #appends region definitions to dataframes
    fileData['Region'] = Regions
    
    #divides counties based on region
    tempwest = fileData.loc[fileData['Region'] == 'West']
    tempeast = fileData.loc[fileData['Region'] == 'East']
    tempcentral = fileData.loc[fileData['Region'] == 'Central']
    
    #defining new column that shows difference between Bachelor and Median Income
    tempwest['Difference']= tempwest['Bachelor'] - tempwest['Median Total']
    tempeast['Difference']= tempeast['Bachelor'] - tempeast['Median Total']
    tempcentral['Difference']= tempcentral['Bachelor'] - tempcentral['Median Total']
    
    #assign dataframes to dictionaries
    combined_db.update({key:fileData.copy()})
    west.update({key:tempwest.copy()})
    east.update({key:tempeast.copy()})
    central.update({key:tempcentral.copy()})

#finding mean of each difference for each region for each year
years = ['2010', '2011', '2012', '2013', '2014', '2016', '2017']
westmeans=[]
for year in years:
    x = west[year]['Difference'].mean()
    westmeans.append(x)
eastmeans=[]
for year in years:
    x = east[year]['Difference'].mean()
    eastmeans.append(x)
centralmeans=[]
for year in years:
    x = central[year]['Difference'].mean()
    centralmeans.append(x)

#plot displays raw difference between Bachelor and Median Income over time
plt.plot(years, westmeans, color='red', label = 'West')
plt.plot(years, eastmeans, color='blue', label = 'East')
plt.plot(years, centralmeans, color='black', label = 'Central')
plt.xlabel('Year')
plt.ylabel('Difference in Money')
plt.title('The Difference in Income Between Bachelor and Median')
plt.ylim(0)
plt.legend(loc='lower right')