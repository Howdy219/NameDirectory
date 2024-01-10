#!/usr/bin/env python3
import os
import sys
import getopt
import csv
import pandas as pd


def CaliforniaConverter():
  
  inputFileName = "California/CaliforniaNames.csv"

  ranks = []
  names = []
  frequency = []
  years = []
  gender = []
  linePlacement = 1

  with open(inputFileName) as csvDataFile:
    next(csvDataFile)
    csvReader = csv.reader(csvDataFile, delimiter=',')
    for row in csvReader:
      if (row[1].strip() != " " and str(row[1].strip()) != "NONAME"
          and str(row[3].strip()) != "M"):
        ranks.append(int(linePlacement))
        years.append(int(row[0]))
        tempName = row[3].strip()
        names.append(tempName)
        frequency.append(int(row[4]))
        if (row[1].strip() == "Male"):
          gender.append("M")
        elif (row[1].strip() == "Female"):
          gender.append("F")
        else:
          gender.append("N/A")
        linePlacement = linePlacement + 1

    people = {
      'Names': names,
      'Frequency': frequency,
      'Years': years,
      'Gender': gender
    }
    people_df = pd.DataFrame(people)
    people_df.sort_values(["Frequency", "Names"],
                          axis=0,
                          ascending=[False, True],
                          inplace=True)
    people_df['Rank'] = people_df['Frequency'].rank(method='min',
                                                    ascending=False)
    people_df.to_csv("Output/CaliforniaSorted.csv",
                     sep=',',
                     index=False,
                     encoding='utf-8')
