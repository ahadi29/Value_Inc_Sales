# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 12:56:25 2022

@author: ahadi
"""
import pandas as pd

#file_name = pd.read_csv('file.csv') || Format to read CSV files with comma(,) as the default separator. 
data = pd.read_csv('transaction.csv')

# Reassigning the data variable with new separator.
data = pd.read_csv('transaction.csv',sep=';')

#summary of dataset
data.info()

#description of dataset
data.describe

# []-list, ()-tuples, {}-set,{'a':'b'}-dictionary, range(1)-range object, var=True -Boolean

# Working with calculation
#Defining Variables

#CostPerTransaction = CostPerItem * NumberOfItemsPurchased
# variable = dataframe['column_name']

CostPerItem=data['CostPerItem']
NumberOfItemsPurchased=data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased


#Adding A new Column 
#dataframe['new_column_name']= variable_name OR dataframe['column_name'] OPERATOR dataframe['column_name']
data['CostPerTransaction'] = CostPerTransaction


#Another method to add a new column

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#SalesPerTransaction

data['SalesPerTransaction']= data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit[sales-cost]

data['ProfitPerTransaction']= data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup[(sales-cost)/cost] OR [Profit/cost]

data['Markup'] = ( data['SalesPerTransaction'] - data['CostPerTransaction'] ) / data['CostPerTransaction']

#OR

data['Markup'] = data['ProfitPerTransaction'] / data['CostPerTransaction']

#round function
#roundmarkup=round(data['Markup'],2)

#Rounding Markup
data['Markup'] = round(data['Markup'],2)

#Printing the datatype of the day column
print(data['Day'].dtype)

#Converting Day and Year to String
#Changing Column's datatype

data['Day']=data['Day'].astype(str)
data['Year']=data['Year'].astype(str)
print(data['Day'].dtype)
print(data['Year'].dtype)

#Concatenating The Day, Month, Year Values.
my_date = data['Day'] + '-' + data['Month'] + '-' + data['Year']
data['Date'] = my_date


#Using iloc to view specific columns/row
data.iloc[0]      #displays the row with index = 0
data.iloc[0:5]    #displays the first 5 rows
data.iloc[-5:]    #displays the last 5 rows

#Using head to view rows. Note both the line of code displays first five rows.
data.head(5)
data.head() 


#displays all rows and specific column
data.iloc[:,1]   # ':' represents all the rows the after comma(,) use any index value to display that particular column.


#Brings in 1st row and 0th column value.
data.iloc[1,0]

#This brings up first 3 rows and columns value.
data.iloc[0:3,0:3]  

#Using Split to split the Client Keyword's Field.
#new_variable = column.str.split('sep',expand =True)

split_col = data['ClientKeywords'].str.split(',',expand=True)

#creating the new columns to store the split column values
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#Using the replace function to replace function to replace '[' and ']' with '' in the column values of new split column values.
data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']' , '')

#Using the lower function to lowercase the ItemDescription
data['ItemDescription'] = data['ItemDescription'].str.lower()


#Using the capiltalize function to capiltalize the first letter of every sentence in the ItemDescription.
data['ItemDescription'] = data['ItemDescription'].str.capitalize()

#How to Merge Files

#Bringing In the new dataset.
seasons_data=pd.read_csv('value_inc_seasons.csv',sep=';')

#Merging files: merge_df = pd.merge(df_old, df_new, on='key')
data=pd.merge(data,seasons_data, on='Month') #Python is going to look at the months in data table then look at the months in seasons_data table and see where they match andn bring in the seasons based on that.Note: It wont bring the month from season file instead it will use the month in data file only and then use the month in both the table to get the value of seasons.


#Dropping the columns that we don't need.
#df=df.drop('columnname' , axix = 1) Note: axix = 1 is for columns and axis = 0 is for row.

data = data.drop('ClientKeywords', axis = 1)
data = data.drop(['Year','Month','Day'], axis = 1)  # If you want to drop multiple column you can do it this way.


#Export into CSV file.
data.to_csv('ValueInc_Cleaned_File.csv', index = False) # If you want to include the Index column from your df to your csv use 'Index=True' otherwise use 'Index=False'
