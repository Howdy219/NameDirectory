#!/usr/bin/env python3
import os
import sys
import getopt
import csv
import pandas as pd


def NovaScotiaConverter():
  inputFileName = "NovaScotia/NovaScotia.csv"

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
      if (row[2].strip() != " " and row[2].strip() != "NONAME"):
        ranks.append(int(linePlacement))
        years.append(int(row[0]))
        tempName = row[2].strip()
        names.append(tempName)
        frequency.append(int(row[3]))
        gender.append(row[1].strip())
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
    people_df.to_csv("./Output/NovaScotiaSorted.csv",
                     sep=',',
                     index=False,
                     encoding='utf-8')
