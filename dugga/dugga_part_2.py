# dugga part 2
# this file takes a CSV file and makes a histogram of the provided column in that CSV
# while using this file, make sure you have the csv in the same directory or provide the full path to it
# example command to run the script: python dugga_part_2.py data.csv column_name number_of_bins "Title" "X-axis label" "Y-axis label"

# import necessary libraries and modules
import sys
# import csv ##not needed as we use pandas to import the csv file into a dataframe
import pandas as pd
import matplotlib.pyplot as plt

# read the parameters from command line argument
csv_file = sys.argv[1]
column_on_xaxis = sys.argv[2]
number_bins = int(sys.argv[3])
title = sys.argv[4]
xlabel = sys.argv[5]
ylabel = sys.argv[6]

# load the csv file into a pandas dataframe with comma as separator
df = pd.read_csv(csv_file, sep=',')

# basic error messages for common mistakes in command line arguments has to be after reading the csv file into a dataframe so we can check if the column name exists in the dataframe
if not csv_file.endswith('.csv'):
    raise ValueError("The provided file is not a CSV file")
if column_on_xaxis not in df.columns:
    raise ValueError(f"Column '{column_on_xaxis}' not found in the CSV file")
if number_bins <= 0:
    raise ValueError("Number of bins must be a positive integer")

# function to create and save histogram plot with given parameters in command line arguments
def histplot_csv(column_on_xaxis, number_bins, title, xlabel, ylabel):
    # plotting the histogram using matplotlib, data isnt a variable because dataframe is the provided data in the csv file
    # other parameters such as bins and edgecolor are added for better visualization
    plt.hist(df[column_on_xaxis], bins=number_bins, edgecolor="black")
    # adding title and labels to the plot
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # graphs x axis began at -.5 and it looked ugly so i adjusted the limit to make it more beautiful
    plt.xlim(0)
    plt.show()
    return plt.savefig(f"{column_on_xaxis}_distribution.png", dpi=300)    # other more general solution: (f'histplot_{xlabel}_vs_{ylabel}.png', dpi=300)

histplot_csv(column_on_xaxis, number_bins, title, xlabel, ylabel)







