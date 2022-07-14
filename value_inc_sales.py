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

