#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 19:41:39 2018

@author: Luis Gustavo Grubert Valensuela
*******************************************************************************
Name: Luis Gustavo Grubert Valensuela Z#:23351882 lvalensuela2015@fau.edu
Course: Python Programming COP 4045-001 Spring 2018
Professor: Dr. Ionut Cardei
Due Date:02/18/2018             Due Time: 11:30PM
Assignment Homework 3
Last Changed: 02/18/2018
Description:
In this assignment two functions will be created:
    a) a function called get_csv_data() that takes these parameters:
    f: an open file object in CSV format (similar to our lb-james.csv file), 
    where the first line has only column headings, followed by lines with 
    comma-separated data items,
    string_pos_lst: a list with index positions (starting from 0) for columns 
    that have a string format. For the lb-james.csv file, this list should be 
    [0, 2, 3, 4]. All other columns are assumed to have a float format. 
    Assume that this list is not sorted in any way.
    sep: a string representing the column separator with default value “,”
    b)a function get_columns() that returns selected columns as lists using 
    as input argument a list returned by function get_csv_data().
    Function get_columns() takes as paramers:
    data_lst: a list previously returned from a call to function get_csv_data()
    cols_lst: a list with the headings of columns to be returned
    
    The two above functions will be used to generate lists that will be used
    to construct a graph based on the data presente at the .csv file
*******************************************************************************
"""
import string
import pylab
def get_csv_data(f, string_pos_lst, sep = ","):
    """ Function that that takes these parameters:
    f: an open file object in CSV format (similar to our lb-james.csv file), 
    where the first line has only column headings, followed by lines with 
    comma-separated data items,
    string_pos_lst: a list with index positions (starting from 0) for columns 
    that have a string format. For the lb-james.csv file, this list should be 
    [0, 2, 3, 4]. All other columns are assumed to have a float format. 
    Assume that this list is not sorted in any way.
    sep: a string representing the column separator with default value “,” """
    
    badCharacter = string.whitespace + "\\\n"
    data_lst = [lineStr for lineStr in f]
    myList = [data_lst[lines].split(sep) for lines in range(len(data_lst))]
    #myFilteredList = [[myList[lines][fields] for fields in range(len(myList[lines])) if fields in string_pos_lst]for lines in range(len(myList))]
    #myList = [[float(myList[lines][fields].replace("\\\n", "")) for fields in range(len(myList[lines])) if fields not in string_pos_lst]for lines in range(len(myList)) if lines != 0]
    for lines in range(len(myList)):
        for fields in range(len(myList[lines])):
            if fields not in string_pos_lst:
                for char in myList[lines][fields]:
                    if char in badCharacter:
                        myList[lines][fields] = myList[lines][fields].replace(char,'')
                try:
                    if lines != 0:
                        myList[lines][fields] = float(myList[lines][fields])
                except:
                    continue
    return myList


def get_columns(data_lst, cols_lst):
    """Function that returns selected columns as lists using 
    as input argument a list returned by function get_csv_data().
    Function get_columns() takes as paramers:
    data_lst: a list previously returned from a call to function get_csv_data()
    cols_lst: a list with the headings of columns to be returned"""
    
    listColumms = []
    for fields in range(len(data_lst[0])):
        if data_lst[0][fields] in cols_lst:
            listColumms.append(fields)

    individual_cols = []
    selected_cols = []
    for ncolumms in range(len(listColumms)):
        if len(individual_cols) > 0:
            selected_cols.append(individual_cols)
        individual_cols = []
        for lines in range(len(data_lst)):
            for fields in range(len(data_lst[lines])):
                if fields == listColumms[ncolumms] and lines != 0:
                    individual_cols.append(data_lst[lines][fields])
    #adding the last list to the selected_cols
    selected_cols.append(individual_cols)
    return selected_cols


bb_file = open("lb-james.csv", "r")
james_lst = get_csv_data(bb_file, [0, 2, 3, 4], ",")
selected_cols_lst = get_columns(james_lst, ["Season", "3P%"])
selected_cols_3pointPercentage = get_columns(james_lst, ["Season", "3P%"])
selected_cols_2pointPercentage = get_columns(james_lst, ["Season", "2P%"])
selected_cols_FTpointPercentage = get_columns(james_lst, ["Season", "FT%"])

selected_cols_MPpoint = get_columns(james_lst, ["Season", "MP"])
selected_cols_PTSpoint = get_columns(james_lst, ["Season", "PTS"])

xs = selected_cols_3pointPercentage[0]
ys = selected_cols_3pointPercentage[1]

xt = selected_cols_2pointPercentage[0]
yt = selected_cols_2pointPercentage[1]

xu = selected_cols_FTpointPercentage[0]
yu = selected_cols_FTpointPercentage[1]


# prepare the domain for the function we graph

pylab.title("Lebron James' Shooting %")
# pylab.axes.plot

pylab.plot(xs, ys, "go-", label='3P%')
pylab.plot(xt, yt, "ro-", label='2P%')
pylab.plot(xu, yu, "bo-", label='FT%')
pylab.xticks(rotation = 45)
pylab.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
pylab.grid()

pylab.show
pylab.pause(1)



xs = selected_cols_MPpoint[0]
ys = selected_cols_MPpoint[1]

xt = selected_cols_PTSpoint[0]
yt = selected_cols_PTSpoint[1]


# prepare the domain for the function we graph

pylab.title("Minutes and point totals per game")



pylab.plot(xs, ys, "go-", label = 'MP')
pylab.plot(xt, yt, "ro-", label = 'PTS')
pylab.xticks(rotation = 45)
pylab.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
pylab.grid()

pylab.show
pylab.pause(1)

print("end")
