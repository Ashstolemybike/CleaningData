import csv
import pandas as pd

'''Read in the following file in python, transform it, and save it to a new file. The transformations should remove
any rows with missing values, and any rows where the student was absent for all assessments. The columns Zscore,
 gender, and syllabus should also be removed. Take the three date columns and concatenate them into one (birth_day, 
 birth_month, birth_year -> birthdate).
 - remove rows where assessments are all absent
 - remove rows with missing values
 - remove zscore, gender and syllabus
 - merge the dates to bday/bmonth/byear under birthdate
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

while True:
    df = read_csv("data.csv")
    #raw_data = pd.read_csv("data.csv")
    df = remove_zscore(df)
    df = remove_gender(df)
    df = remove_syllabus(df)

    df.to_csv('clean_data.csv')
    break
