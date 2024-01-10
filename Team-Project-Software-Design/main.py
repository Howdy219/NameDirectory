#!/usr/bin/env python3
import os
import sys
import getopt
import csv
import pandas as pd
from Alberta.Alberta import AlbertaConverter
from California.California import CaliforniaConverter
from NewBrunswick.New_Brunswick import NewBrunswickConverter
from NovaScotia.Nova_Scotia import NovaScotiaConverter


def first_Choice(NameList=[]):
  Continue = True
  specialCharacterCheck = "|`;[@_!#$%^&*" "()<>?/\|}{~:].,%+=-"
  while (Continue == True):
    errorCheck = False
    errorCheckContinue = False
    while (errorCheck == False):
      nameInput = input("Please enter a valid name to add to search: \n")
      if (nameInput.isdigit() == True):
        print("You Entered a Number not a specified name")
        errorCheck = False
      elif (nameInput == ""):
        print("Please enter a proper name.\n")
        errorCheck = False
      elif any(x in specialCharacterCheck for x in nameInput):
        print("You entered a special character, invalid name\n")
      else:
        print("Name being uploaded as parameter...\n")
        NameList.append(nameInput.title())
        errorCheck = True
        while (errorCheckContinue == False):
          continueInput = input(
            "Would you like to continue? Enter 1 for yes or 2 for no\n")
          if (continueInput.isdigit() == True):
            if (int(continueInput) == 1):
              errorCheckContinue = True
            elif (int(continueInput) == 2):
              errorCheckContinue = True
              Continue = False
            else:
              print("Please enter a valid numerical value.\n")
          else:
            print("Please enter a valid input\n")
  NameList = list(dict.fromkeys(NameList))
  return NameList


def second_Choice(yearList=[]):
  errorCheck = False
  singleYear = False
  rangeYear = False
  count = 1920
  continueCheck = False
  continueLoop = True
  counter = 0
  while (continueLoop == True):
    errorCheck = False
    singleYear = False
    rangeYear = False
    continueCheck = False
    while (errorCheck == False):
      yearInput = input(
        "Press 1 for ranks for individual year, press 2 for a range of years: \n"
      )
      if (yearInput.isdigit() == True):
        if (int(yearInput) == 1):
          errorCheck = True
          singleYear = True
        elif (int(yearInput) == 2):
          errorCheck = True
          rangeYear = True
        else:
          print("You have entered a invalid input.\n")
          errorCheck = False
      else:
        print("You have entered an invalid input.\n")

      while (singleYear == True):
        counter = 0
        count = 1920
        print("Please enter a year from 1920 - 2022: ")
        yearInput = input()
        if (yearInput.isdigit() == True):
          n = int(yearInput)
          if (n<=1919):
            print("This year is out of range, please enter a year in the valid range of years.\n")
          else:
            while (counter == 0):
              if (n == count):
                print("Year in range. Registering year now...\n")
                yearList.append(n)
                singleYear = False
                counter = 1
              elif (count == 2022):
                print(
                  "This year is out of range, please enter a year in the valid range of years.\n"
                )
                singleYear = True
                counter=1
              count = count + 1
        else:
          print("Did not enter a valid year\n")
          singleYear=True

      while (rangeYear == True):
        counter = 0
        count = 1920
        storage = 0
        repeat=0
        print(
          "Please enter a minimum year, followed by a maximum year. Current range is 1920 - 2022\n"
        )
        rangeInput1 = input("Add minimum year: \n")
        rangeInput2 = input("Add maximum year: \n")

        if (rangeInput1.isdigit() == True and rangeInput2.isdigit() == True):
          n = int(rangeInput1)
          x = int(rangeInput2)
          while (counter == 0):
            if (n == count):
              print("Year 1 in range")
              storage = storage + 1
            if (x == count):
              print("Year 2 in range")
              storage = storage + 1
            if (storage == 2):
              if (n > x):
                print(
                  "Input Error, please enter a maximum year that is greater or equal to the minimum year.\n"
                )
                counter = 1
              elif (n==2023 or x==2023):
                print("Seems like year or years are out of range.\n")
                repeat=1
              else:
                print(
                  "Valid Minimum and Maximum Years, Registering Range of Years Now...\n"
                )
                yearDifference = x - n
                for i in range(yearDifference + 1):
                  yearList.append(n)
                  n = n + 1
                rangeYear = False
                counter = 1
            if (count == 2023 and repeat!=1):
              print("Seems like year or years are out of range.\n")
              rangeYear = True
              counter = 1
            count = count + 1
        else:
          print("Did not enter a valid year or years\n")
          rangeYear=True
    while (continueCheck == False):
      continueInput = input(
        "Would you like to continue? Enter 1 for yes or 2 for no\n")
      if (continueInput.isdigit() == True):
        if (int(continueInput) == 1):
          continueCheck = True
        elif (int(continueInput) == 2):
          continueCheck = True
          continueLoop = False
        else:
            print("Please enter a valid numerical value.\n")
      else:
        print("Please enter a valid input\n")
  yearList = list(dict.fromkeys(yearList))
  return yearList


def third_Choice(regionList=[]):
  errorCheck = False
  continueCheck = False
  continueLoop = True
  regions = ["Alberta", "California", "New Brunswick", "Nova Scotia"]
  while (continueLoop == True):
    errorCheck = False
    continueCheck = False
    while (errorCheck == False):
      print("Enter a region (Alberta, California, New Brunswick, Nova Scotia): \n", end='')
      regionInput = input()
      if (regionInput.isdigit() == True):
        print("You entered a number please enter one of the following regions\n")
      elif (regionInput.title() in regions):
        regionList.append(regionInput.title())
        errorCheck = True
        print("Region is in current regions! Uploading to parameters...\n")
        while (continueCheck == False):
          continueInput = input(
            "Would you like to continue? Enter 1 for yes or 2 for no\n")
          if (continueInput.isdigit() == True):
            if (int(continueInput) == 1):
              continueLoop = True
              continueCheck = True
            elif (int(continueInput) == 2):
              continueCheck = True
              continueLoop = False
            else:
              print("Please enter a valid number\n")
          else:
            print("Please enter a proper value\n")
      else:
        print(
          "Your input is either invalid or we don't have data on that region\n")
  regionList = list(dict.fromkeys(regionList))
  return regionList


def fourth_Choice(gender):
  errorCheck = False
  while (errorCheck == False):
    genderInput = input(
      "Please enter a gender M for male, F for female or B for both:\n")
    if (genderInput == "M" or genderInput == "F" or genderInput == "m"
        or genderInput == "f" or genderInput == "B" or genderInput == "b"):
      gender = genderInput
      errorCheck = True
    else:
      print("You did not enter a correct input\n")
      errorCheck = False

  return gender


def fifth_Choice(freqList=[]):
  errorCheck = False
  singleFreq = False
  rangeFreq = False
  continueLoop = True
  continueCheck = False
  while (continueLoop == True):
    continueCheck = False
    singleFreq = False
    rangeFreq = False
    errorCheck = False
    while (errorCheck == False):
      freqInput = input(
        "Press 1 for requesting an individual frequency, press 2 for a range of frequency: \n"
      )
      if (freqInput.isdigit() == True):
        if (int(freqInput) == 1):
          errorCheck = True
          singleFreq = True
        elif (int(freqInput) == 2):
          errorCheck = True
          rangeFreq = True
        else:
          print("You have entered a invalid input.\n")
          errorCheck = False
          continueCheck=True
      else:
        print("You have entered an invalid input.\n")
        continueCheck=True
        errorCheck=False

      while (singleFreq == True):
        freqInput = input(
          "Please enter a frequency you would like to search for: \n")
        if (freqInput.isdigit() == True):
          n = int(freqInput)
          if (int(freqInput) <= 0):
            print("Please enter a value higher than 0\n")
            singleFreq = True
          else:
            print("Valid Frequency Acquired! Uploading to parameters...\n")
            freqList.append(int(freqInput))
            continueCheck=False
            singleFreq = False
        else:
          print("Did not enter a valid frequency\n")
          singleFreq = True

      while (rangeFreq == True):
        rangeInput1 = input("Add minimum frequency: \n")
        rangeInput2 = input("Add max frequency: \n")
        storage = 0
        if (rangeInput1.isdigit() == True and rangeInput2.isdigit() == True):
          n = int(rangeInput1)
          x = int(rangeInput2)
          if (n > x):
            print(
              "Please enter a max frequency that is higher than the minimum frequency\n"
            )
          else:
            if (n > 0):
              storage = storage + 1
            if (x > 0):
              storage = storage + 1
            if (x==0 or n==0):
              print("Please enter a value higher than 0.\n")
            elif (storage == 2):
              frequencyDifference = x - n
              print("Range of frequencies is valid. Uploading to parameters...\n")
              for i in range(frequencyDifference+1):
                freqList.append(n)
                n=n+1
              rangeFreq = False
              continueCheck=False
            else:
              print("Did not enter a valid numerical value\n")
        else:
          print("Did not enter a valid number\n")
          rangeFreq = True
      while (continueCheck == False):
        continueInput = input(
          "Would you like to continue? Enter 1 for yes or 2 for no\n")
        if (continueInput.isdigit() == True):
          if (int(continueInput) == 1):
            continueCheck = True
          elif (int(continueInput) == 2):
            continueCheck = True
            continueLoop = False
          else:
            print("Please enter a valid numerical value.\n")
        else:
          print("Please enter a valid input\n")
  freqList = list(dict.fromkeys(freqList))
  return freqList


def sixth_Choice(rankList=[]):
  errorCheck = False
  singleRank = False
  rangeRank = False
  continueLoop = True
  continueCheck = False
  while (continueLoop == True):
    continueCheck = False
    singleRank = False
    rangeRank = False
    errorCheck = False
    while (errorCheck == False):
      rankInput = input(
        "Press 1 for ranks for an individual rank, press 2 for a range of ranks: \n"
      )
      if (rankInput.isdigit() == True):
        if (int(rankInput) == 1):
          errorCheck = True
          singleRank = True
        elif (int(rankInput) == 2):
          errorCheck = True
          rangeRank = True
        else:
          print("You have entered a invalid numerical input.\n")
          errorCheck = False
          continueCheck=True
      else:
        print("You have entered an invalid input.\n")
        continueCheck=True
        errorCheck=False

      while (singleRank == True):
        rankInput = input(
          "Please enter a rank you would like to search for: \n")
        if (rankInput.isdigit() == True):
          n = int(rankInput)
          if (int(rankInput) <= 0):
            print("Please enter a value higher than 0\n")
            singleRank = True
          else:
            print("Rank is in range! Uploading to parameters...\n")
            rankList.append(int(rankInput))
            singleRank = False
            continueCheck=False
        else:
          print("Did not enter a valid rank\n")
          singleRank = True

      while (rangeRank == True):
        rangeInput1 = input("Add minimum rank: \n")
        rangeInput2 = input("Add max rank: \n")
        storage = 0
        if (rangeInput1.isdigit() == True and rangeInput2.isdigit() == True):
          n = int(rangeInput1)
          x = int(rangeInput2)
          if (n > x):
            print(
              "Please enter a max rank that is higher than the minimum rank\n")
          else:
            if (n > 0):
              storage = storage + 1
            if (x > 0):
              storage = storage + 1
            if (n<=0 or x<=0):
              print("Please enter a value higher than 0\n")
            elif (storage == 2):
              rankDifference = x - n
              print("Ranks are in range! Uploading to parameters...\n")
              for i in range(rankDifference+1):
                rankList.append(n)
                n = n + 1
              rangeRank = False
              continueCheck=False
            else:
              print("Please enter a valid input\n")
        else:
          print("Did not enter a valid number\n")
          rangeRank = True
      while (continueCheck == False):
        continueInput = input(
          "Would you like to continue? Enter 1 for yes or 2 for no\n")
        if (continueInput.isdigit() == True):
          if (int(continueInput) == 1):
            continueCheck = True
          elif (int(continueInput) == 2):
            continueCheck = True
            continueLoop = False
          else:
            print("Please enter a valid number\n")
        else:
          print("Please enter a valid input\n")
  rankList = list(dict.fromkeys(rankList))
  return rankList


def search(NameList, YearList, RegionList, Sex, FreqList, RankList):
  csvNameList = []
  csvYearList = []
  csvRegionList = []
  csvRegionNameList = []
  csvFreqList = []
  csvSexList = []
  csvRankList = []
  allRegionsFile = [
    "Output/AlbertaSorted.csv", "Output/CaliforniaSorted.csv",
    "Output/NewBrunswickSorted.csv", "Output/NovaScotiaSorted.csv"
  ]
  allRegions = ["Alberta", "California", "New Brunswick", "Nova Scotia"]
  selectedRegions = []
  regionCount = 0
  print("\n\nHere is the output:")
  searchCheck = False
  if (len(NameList) == 0 and len(YearList) == 0 and len(RegionList) == 0
      and len(FreqList) == 0 and (Sex == 'B' or Sex == 'b') and len(RankList)==0):
    print("You didn't add any parameters. Please enter parameters.")
    return
  else:
    searchCheck = True
  while (searchCheck == True):
    #For loop, followed by with open (csvNameList[i]) as csvDataFile, followed by row in csvReader, followed then by if statements.
    #Year list should grab new data from csv file, but then other factors like name, sex and frequency should edit from the list that year has collected.
    if (len(RegionList) != 0):
      for i in RegionList:
        if (i == "New Brunswick"):
          tempName = "Output/NewBrunswickSorted.csv"
          csvRegionNameList.append(tempName)
          selectedRegions.append(i)
        elif (i == "Nova Scotia"):
          tempName = "Output/NovaScotiaSorted.csv"
          csvRegionNameList.append(tempName)
          selectedRegions.append(i)
        else:
          tempName = "Output/" + str(i) + "Sorted.csv"
          csvRegionNameList.append(tempName)
          selectedRegions.append(i)
        #Open up all csv files necessary
    else:
      csvRegionNameList = allRegionsFile
      selectedRegions = allRegions
    for specifiedRegionCSV in csvRegionNameList:
      with open(specifiedRegionCSV, encoding='utf8') as csvDataFile:
        next(csvDataFile)
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
          if (len(YearList) != 0):
            #Shrink data list down to just specific year
            for year in YearList:
              if (year == int(row[2])):
                csvNameList.append(row[0].strip())
                csvFreqList.append(int(row[1]))
                csvYearList.append(int(row[2]))
                csvSexList.append(str(row[3]))
                csvRankList.append(int(float(row[4])))
                csvRegionList.append(str(selectedRegions[regionCount]))
          else:
            #Else statement if years are not requested
            csvNameList.append(row[0].strip())
            csvFreqList.append(int(row[1]))
            csvYearList.append(int(row[2]))
            csvSexList.append(str(row[3]))
            csvRankList.append(int(float(row[4])))
            csvRegionList.append(str(selectedRegions[regionCount]))
          #Sorting of names, does so by comparing NameList (list of names as parameters) and all names that were collected through the year list.  If there is not a corresponding name
          if (len(NameList) != 0):
            indexName = 0
            for CurrentNames in csvNameList[:]:
              foundName = 0
              for Name in NameList:
                if (CurrentNames.upper() == Name.upper()):
                  foundName = 1
              if (foundName != 1):
                del csvNameList[indexName]
                del csvFreqList[indexName]
                del csvYearList[indexName]
                del csvSexList[indexName]
                del csvRankList[indexName]
                del csvRegionList[indexName]
              else:
                indexName = indexName + 1
          if (len(FreqList) != 0):
            #Shrink data list down to just specific frequencies
            for CurrentFreq in csvFreqList[:]:
              foundFreq = 0
              indexFreq = 0
              for Frequency in FreqList:
                if (Frequency == CurrentFreq):
                  foundFreq = 1
              if (foundFreq != 1):
                del csvNameList[indexFreq]
                del csvFreqList[indexFreq]
                del csvYearList[indexFreq]
                del csvSexList[indexFreq]
                del csvRankList[indexFreq]
                del csvRegionList[indexFreq]
              else:
                indexFreq = indexFreq + 1
              foundFreq = 0
          #Shrink data list down to just specific genders
          if (Sex != 'B' and Sex != 'b'):
            indexSex = 0
            for CurrentSex in csvSexList[:]:
              if (CurrentSex != Sex):
                del csvNameList[indexSex]
                del csvFreqList[indexSex]
                del csvYearList[indexSex]
                del csvSexList[indexSex]
                del csvRankList[indexSex]
                del csvRegionList[indexSex]
              else:
                indexSex = indexSex + 1

          if (len(RankList) != 0):
            #Shrink data list down to just specific ranks
            for CurrentRank in csvRankList[:]:
              foundRank = 0
              indexRank = 0
              for Rank in FreqList:
                if (Rank == CurrentRank):
                  foundRank = 1
              if (foundRank != 1):
                del csvNameList[indexRank]
                del csvFreqList[indexRank]
                del csvYearList[indexRank]
                del csvSexList[indexRank]
                del csvRankList[indexRank]
                del csvRegionList[indexRank]
              else:
                indexRank = indexRank + 1
              foundRank = 0
      regionCount = regionCount + 1
    searchCheck = False
  #Runs resultingData to print out data results.
  finishCheck = resultingData(csvNameList, csvFreqList, csvYearList,
                              csvSexList, csvRegionList, csvRankList)
  if (finishCheck == 0):
    print(
      "There are no names registered under those specified parameters. Please change parameters and try again for results.\n\n\n"
    )
  elif (finishCheck == 1):
    print("Success! Current data is shown above.\n\n\n")
  else:
    print(
      "An error has occured with processing the data, please try again with different parameters.\n\n\n"
    )


def resultingData(NameList, FrequencyList, YearList, SexList, RegionList,
                  RankList):
  finalNameList = []
  finalYearList = []
  finalFrequencyList = []
  finalSexList = []
  finalRegionList = []
  finalRankList = []
  if ((len(NameList) == 0 or len(FrequencyList) == 0 or len(YearList) == 0
       or len(RegionList) == 0) or len(SexList) == 0):
    return 0
  else:
    print("Names\t\t Year\t Frequency\t Gender\t Rank\t\t Region")
    requestedPeople = {
      'Name': NameList,
      'Frequency': FrequencyList,
      'Year': YearList,
      'Sex': SexList,
      'Region': RegionList,
      'Rank': RankList
    }
    people_df = pd.DataFrame(requestedPeople)
    people_df.sort_values(["Name", "Year", "Frequency", "Rank", "Region"],
                          axis=0,
                          ascending=[True, True, True, False, True],
                          inplace=True)
    finalNameList = people_df["Name"].tolist()
    finalYearList = people_df["Year"].tolist()
    finalFrequencyList = people_df["Frequency"].tolist()
    finalSexList = people_df["Sex"].tolist()
    finalRegionList = people_df["Region"].tolist()
    finalRankList = people_df["Rank"].tolist()
    for Position in range(len(NameList)):
      if (len(finalNameList[Position]) >= 7):
        print(finalNameList[Position],
              '\t',
              finalYearList[Position],
              '\t',
              finalFrequencyList[Position],
              end='')
      else:
        print(finalNameList[Position],
              '\t\t',
              finalYearList[Position],
              '\t',
              finalFrequencyList[Position],
              end='')
      if (finalFrequencyList[Position] >= 100):
        print('\t\t', finalSexList[Position], end='')
      else:
        print('\t\t\t', finalSexList[Position], end='')
      print('\t\t', finalRankList[Position], end='')
      if (finalRankList[Position] < 100):
        print('\t\t\t', finalRegionList[Position])
      else:
        print('\t\t', finalRegionList[Position])

    return 1
  return -1


def printFunction(List):
  if (len(List) == 0):
    print("Set to All", end='')
  else:
    for i in range(len(List)):
      if (i + 1 == len(List)):
        print(List[i], end='')
      else:
        print(List[i], ", ", end='', sep='')
  print('\n')


def main(argv):
  NovaScotiaConverter()
  AlbertaConverter()
  NewBrunswickConverter()
  CaliforniaConverter()
  choice = 0
  NameList = []
  YearList = []
  RegionList = []
  Sex = 'B'
  FreqRange = []
  RankList = []
  while (int(choice) != 9):
    errorCheck = False
    while (errorCheck == False):
      print("Parameter Options\n")
      print("1. Specified Name(s)")
      print("2. Specified Year(s)")
      print("3. Specified Region(s)")
      print("4. Specified Sex")
      print("5. Specified Frequency Range")
      print("6. Specified Rank Range")
      print("7. Reset a Parameter")
      print("8. Start Search!")
      print("9. Exit Program")
      print("\nCurrent Parameters\n")
      print("Names: ", end='')
      printFunction(NameList)
      print("Years: ", end='')
      printFunction(YearList)
      print("Regions: ", end='')
      printFunction(RegionList)
      print("Gender: ", Sex.upper())
      print("\nFrequencies: ", end='')
      printFunction(FreqRange)
      print("Ranks: ", end='')
      printFunction(RankList)
      choice = input("Please select an option: ")
      if (choice.isdigit() == True):
        if (int(choice) == 1):
          NameList=first_Choice(NameList)
          errorCheck = True
        elif (int(choice) == 2):
          YearList=second_Choice(YearList)
          YearList.sort()
          errorCheck = True
        elif (int(choice) == 3):
          RegionList=third_Choice(RegionList)
          errorCheck = True
        elif (int(choice) == 4):
          errorCheck = True
          Sex=fourth_Choice(Sex)
        elif (int(choice) == 5):
          FreqRange=fifth_Choice(FreqRange)
          FreqRange.sort()
          FreqRange.sort()
          errorCheck = True
        elif (int(choice) == 6):
          RankList=sixth_Choice(RankList)
          RankList.sort()
          errorCheck = True
        elif (int(choice) == 7):
          errorCheck = True
          answerNum = 0
          while (answerNum != 8):
            print(
              "Please enter the associated number to remove the specified parameter: "
            )
            print("1. All Specified Names")
            print("2. All Specified Years")
            print("3. All Specified Regions")
            print("4. All Specified Genders")
            print("5. All Specified Frequencies")
            print("6. All Specified Ranks")
            print("7. Reset ALL PARAMETERS")
            print("8. Go Back To Main Menu")
            answerNum = input("Enter associated option: ")
            if (int(answerNum) == 1):
              NameList.clear()
              break
            elif (int(answerNum) == 2):
              YearList.clear()
              break
            elif (int(answerNum) == 3):
              RegionList.clear()
              break
            elif (int(answerNum) == 4):
              Sex = 'B'
              break
            elif (int(answerNum) == 5):
              FreqRange.clear()
              break
            elif (int(answerNum) == 6):
              RankList.clear()
              break
            elif (int(answerNum) == 7):
              finalCheck = True
              #Should we just comment this part out cause it is causing some weird errors and code works fine without bottom piece of code:
              while (finalCheck == True):
                finalAnswer=0
                finalAnswer = input("Enter 1 to confirm or 2 to cancel: ")
                if (finalAnswer.isdigit() == True):
                  if (int(finalAnswer)==1):
                    NameList.clear()
                    YearList.clear()
                    RegionList.clear()
                    Sex = 'B'
                    FreqRange.clear()
                    RankList.clear()
                    finalCheck = False
                    answerNum = 8
                  elif (int(finalAnswer)==2):
                    print("Returning to main menu...")
                    finalCheck = False
                    answerNum = 8
                  else:
                    print("Please enter a valid number\n")
                else:
                  print("Not a valid input. Try again.")
            elif (int(answerNum) == 8):
              print("Returning to main menu...")
            else:
              print("Please enter a valid number from the options listed.")
        elif (int(choice) == 8):
          search(NameList, YearList, RegionList, Sex, FreqRange, RankList)
          errorCheck = True
        elif (int(choice) == 9):
          errorCheck = True
        else:
          print("\nEnter a proper input number\n")
      elif (choice.isdigit() == False):
        print("\n\n\n\n\nPlease enter proper input\n")


if __name__ == "__main__":
  main(sys.argv[1:])
