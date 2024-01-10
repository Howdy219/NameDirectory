#!/usr/bin/env python3
import os
import sys
import getopt
import csv
import pandas as pd


def AlbertaConverter():

  inputFileName = "Alberta/Alberta.csv"

  ranks = []
  names = []
  frequency = []
  gender = []
  years = []
  i = 0
  #print("test")
  with open(inputFileName) as csvDataFile:
    next(csvDataFile)
    csvReader = csv.reader(csvDataFile, delimiter=',')
    for row in csvReader:
      if i < 4:
        i = i + 1
      else:

        if (row[1].strip() != " " and str(row[1].strip()) != "NONAME"):
          ranks.append(int(row[0]))
          nameUpper = row[1].upper()
          names.append(nameUpper)
          frequency.append(int(row[2]))
          if (row[3].strip() == "Boy"):
            gender.append("M")
          elif (row[3].strip() == "Girl"):
            gender.append("F")
          else:
            gender.append("No Gender")
          years.append(int(row[4]))

        i = i + 1

    peopleAlberta = {
      'Names': names,
      'Frequency': frequency,
      'Years': years,
      'Gender': gender
    }
    people_df = pd.DataFrame(peopleAlberta)
    people_df.sort_values(["Frequency", "Names"],
                          axis=0,
                          ascending=[False, True],
                          inplace=True)
    people_df['Rank'] = people_df['Frequency'].rank(method='min',
                                                    ascending=False)
    people_df.to_csv("Output/AlbertaSorted.csv",
                     sep=',',
                     index=False,
                     encoding='utf-8')
