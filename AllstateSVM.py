from __future__ import division
import scipy
from sklearn import svm
import numpy as np
import csv
import sys

import pandas as pd

########################################### Added by Rakesh Adhikesavan ##############################
def readFile(path):
    df = pd.read_csv(path) #returns a dataFrame, this can later be converted to a numpy array which is useful for sklearn's algorithms. 
    return df

        
train = readFile("train.csv")
test = readFile("test.csv")

print train.head(10) #prints first 10 rows of the dataFrame

########################################################################################################

# First job is to read in the data from the training data that Kaggle provides. This
# training data is in the form of a csv file. This CSV file should be in the same
# directory as this program. 

# We want to skip the first row in the csv file because it just 
# contains column header
skip = True
train_file = open('train.csv')
csv_file = csv.reader(train_file)

for row in csv_file:
	if (skip == True):
		skip = False
		continue

# Repeating same process for test file (except we don't know Ytest)
skip = True
test_file = open('test.csv')
csv_file2 = csv.reader(test_file)

for row in csv_file2:
	if (skip == True):
		skip = False
		continue