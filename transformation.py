# transformations.py
 
import pandas as pd
 
def replace_null_firstname(dataframe):
    dataframe['Firstname'].fillna('FNU', inplace=True)
    return dataframe
 
def replace_null_lastname(dataframe):
    dataframe['Lastname'].fillna('LNU', inplace=True)
    return dataframe
 
def concatenate_name(dataframe):
    dataframe['Name'] = dataframe['Firstname'] + ' ' + dataframe['Lastname']
    return dataframe
 
def replace_null_score(dataframe):
    dataframe['ScoreValue'].fillna(0, inplace=True)
    return dataframe
 
def remove_duplicates(dataframe):
    # Remove duplicates from the DataFrame
    dataframe = dataframe.drop_duplicates()
    return dataframe
