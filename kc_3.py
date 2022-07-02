import os
import pandas as pd

#Filepath and filename
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'assets', 'file_example_CSV_5000.csv')
file = open(filename, 'r')

#User input for search string. Examples to search: France, Gaston, Male 
search_string = input ("What do you want to search for in the file: ")

def num_of_strings (file, search_string):
    ''' Search number of string occurrences in the file
    input: file and string to search
    output: number of string occurrences found'''
    num_of_str = 0
    for line in file:
        if search_string in line:
            num_of_str += 1
    return num_of_str


print(
    f"The number of times {search_string} appear in file is {num_of_strings(file, search_string)}")
file.close()

#User input on category/column to be used to calculate average age
age_by = input(
    "How do you want to search for average age (Country, Gender, Last Name, First Name): ")

def ave_age(filename, age_by):
    '''Find average age by category
    input: filename with and category
    output: average age in the given category'''

    df = pd.read_csv(filename)
    average_age = df.groupby(age_by)['Age'].mean()
    return average_age

print(f"Averege age by {ave_age(filename, age_by)}")



