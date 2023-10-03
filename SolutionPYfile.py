# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TuZVsUg6BkCG892mijHVowoyYJIPkTeo

# By- Shreyansh Agrawal

## Assignment submission to **Bluejay Delivery**

for Software Development internship position.
"""

#Importing libraries
import pandas as pd

# Reading the CSV file
file_path = 'Assignment_Timecard.csv'
df = pd.read_csv(file_path)
df

# Convert 'Time' and 'Time Out' columns to datetime
df['Time'] = pd.to_datetime(df['Time'])
df['Time Out'] = pd.to_datetime(df['Time Out'])

df

# Sort the dataframe by 'Employee Name' and 'Time'
df.sort_values(by=['Employee Name', 'Time'], inplace=True)

df

# Initialize variables to track consecutive days and time between shifts
consecutive_days = 0
previous_employee = None
previous_shift_end = None

# Creating a text file to write the output
output_file = open('output.txt', 'w')

# Iterate over the dataframe
for index, row in df.iterrows():
    current_employee = row['Employee Name']
    current_time = row['Time']

    # Check if it's a new employee
    if current_employee != previous_employee:
        consecutive_days = 0

    # Check if it's a consecutive day
    elif (current_time - previous_shift_end).total_seconds() <= 3600:
        consecutive_days += 1
    else:
        consecutive_days = 0

    # Task 1: Print employees who have worked for 7 consecutive days
    if consecutive_days >= 7:
        print(f"{current_employee} has worked for 7 consecutive days.", file=output_file)

    # Task 2a: Print employees who have less than 10 hours between shifts but more than 1 hour
    if previous_shift_end is not None and (current_time - previous_shift_end).total_seconds() < 36000 and (current_time - previous_shift_end).total_seconds() > 3600:
        print(f"{current_employee} has less than 10 hours between shifts.", file=output_file)

    # Task 2b: Print employees who have worked for more than 14 hours in a single shift
    if (row['Time Out'] - row['Time']).total_seconds() > 50400:
        print(f"{current_employee} has worked for more than 14 hours in a single shift.", file=output_file)

    previous_employee = current_employee
    previous_shift_end = row['Time Out']

# Closing the output file
output_file.close()