import csv
import datetime

import pandas as pd

'''Read in the following file in python, transform it, and save it to a new file. The transformations should remove
any rows with missing values, and any rows where the student was absent for all assessments. The columns Zscore,
 gender, and syllabus should also be removed. Take the three date columns and concatenate them into one (birth_day, 
 birth_month, birth_year -> birthdate).
 - remove rows where assessments are all absent
 - remove rows with missing values
 - remove zscore, gender and syllabus DONE!!!!!
 - merge the dates to bday/bmonth/byear under birthdate DONE!!!
 '''


def read_csv(filename):
    '''Read the file in'''
    data = pd.read_csv(filename)
    #with open(filename, newline='') as csvfile:
    #    csvreader = pd.read_csv(csvfile, delimiter=',')
    #df = pd.DataFrame(csvreader)
    return data

def write_csv(filename, df1):
    df1.to_csv(filename, sep='\t')


def remove_zscore(data):
    '''Drop ZScore from the table'''
    data = data.drop("Zscore", axis=1)
    return data

def remove_gender(data):
    data = data.drop("gender", axis=1)
    return data

def remove_syllabus(data):
    data = data.drop("syllabus", axis=1)
    return data

def birth_date(data):
    '''combines the 3 columns under 1 column'''
    month = {'January' : 1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, \
             'September': 9, 'October':10,'November':11,'December':12}
    data.birth_month = data.birth_month.map(month)
    data = data.assign(birthdate = data.birth_day.astype(str) + '/' + \
                       data.birth_month.astype(str) + '/' + \
                       data.birth_year.astype(str) )
    data = data.drop("birth_day", axis=1)
    data = data.drop("birth_month", axis=1)
    data = data.drop("birth_year", axis=1)

    return data

def remove_birth_day(data):
    data = data[data.birth_day != 'Invalid error']
    data = data[data.birth_day != ' ']
    ##data = data[data.birth_day > 31] #To remove days over 31
    return data

def remove_rows(data):
    data = data[data.index != '-']
    data = data[data.stream != '-']
    data = data[data.sub1 != '-']
    data = data[data.sub2 != '-']
    data = data[data.sub3 != '-']
    data = data[data.island_rank != '-']
    data = data[data.district_rank != '-']
    return data

def remove_absent(data):

    data = data.drop(data[(data['sub1_r'] == 'Absent') & (data['sub2_r'] == 'Absent') & (data['sub3_r'] == 'Absent') & (data['cgt_r'] == 'Absent') & (data['general_english_r'] == 'Absent')])
    return data
    #if data[data.sub1_r != 'Absent'] and data[data.sub2_r != 'Absent'] and data[data.sub3_r != 'Absent'] and data[data.cgt_r != 'Absent'] and data[data.general_english_r != 'Absent']:


def check_valid_date(data):
    if data.birth_month == "February" and data.birth_year%4 == 0:
        data = data.drop(data[(data['birth_day'] > 29)])
    else:
        pass
    return data

while True:
    df = read_csv("data.csv")
    df = remove_zscore(df)
    df = remove_gender(df)
    df = remove_syllabus(df)
    df = check_valid_date(df)
    df = remove_birth_day(df)
    df = birth_date(df)
    df = remove_rows(df)
    df = remove_absent(df)

    df.to_csv('clean_data.csv')
    break
