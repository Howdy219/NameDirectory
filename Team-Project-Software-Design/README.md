
# Team Project Software Design - Team Frog

The modules needed to run this program:
pandas
os
csv
sys
getopt

**Setup**
You can run this zip file in replit or vs code. First unzip the file and make sure to have all the Region python scripts and their respective csv files are in the right region folder/directories. Output csv files (noted under sorted ending in name of csv file) should be in the output folder whereas Alberta and For example NovaScotia Folder will have include the Nova_Scotia.py Script and NovaScotia.csv file.
Output folder will include (RegionName)Sorted.csv files, where RegionName is the current region names with NO SPACES.

**Current Region Names**
Alberta
California
New Brunswick
Nova Scotia

To run the code go to main.py and run it from there. It will open a menu page in where you can input what data you want to see from the respective csv files from different areas. 

The program in main.py is a search directory that searches and prints through all the data that is present in the csv files.  This search can have its parameters edited, confining the search to only highlight information based on those parameters. 

**Default Parameters**
Parameters that are searched for when rather:
-User starts up the program for the first time.
-Resets the given parameter.

Name: Every name (no names are restricted)
Year: Every year (no years are restricted)
Frequency: Every frequency (no frequencies are restricted)
Gender: Set to Both (called B)
Regions: Every Region (every region registered in the csv file output sorted files)
Rank: Every rank (no ranks are restricted)

To change parameters, functions 1-6 allow designated variables to be changed for one's search.

**Functions**
Please Note: You can enter repeated inputs at any time, for example if you already have John as a parameter and then decide to enter John again after using names option again. The program has a system to remove duplicates, so feel free to enter answer that you may have forgotten!

Names option: Requests the user to enter any given name. No checks are made for invalid names, however invalid names will result in the search not being able to find it.  Does not take names with special characters. All special characters include: (|`;[@_!#$%^&*" "()<>?/\|}{~:].,%+=-).  Continues until user asks to quit through numerical prompt asked after.

Years option: Gives the user two options. Option 1 requests a user input for ONE year, which will be added to the requested years for the search.  Option 2 lets the user enter a range of years, where the first requested year is the minimum year of the search and the second requested year is the maximum year.  This option works when both min and max years are the same, but asks for re-input when minimum is greater than maximum.  Afterwords, all years between the minimum and maximum years (including min and max) will be added to the parameter list for years.  Continues until user asks to quit through numerical prompt asked after.  

CURRENT AVAILABLE YEARS: 1920-2022

Region Option: Gives the user the option to enter the name of a specified region (regions are listed on printing statement and under Current Province Names in ReadMe).  Then gives a prompt to continue or not (1 to continue, 2 to exit from function).  If it is one, keeps looping.

Frequency Option: Frequency refers to the total amount of people that have a registered name in that given year and region.  
The function however gives the user two options. Option 1 requests a user input for ONE specific frequency, which will be added to the requested frequencies for the search.  Option 2 lets the user enter a range of frequencies, where the first requested frequency is the minimum frequency of the search and the second requested frequency is the maximum frequency.  This option works when both min and max frequencies are the same, but asks for re-input when minimum is greater than maximum.  Afterwords, all frequencies between the minimum and maximum frequency (including min and max) will be added to the parameter list for frequency.  Continues until user asks to quit through numerical prompt asked after.

UNAVAILABLE VALUES: any value less than 0

Gender Option: Searches for data depending if user enters M(Male), F(Female) or B(Both).  Will only accept M, F, B, m, f and b for these respective definitions.

Rank Option: Searches for data depending on user inputted rank. Ranks are also associated to their specfic region as name ranks are not the same across the regions.  Follows the same format as the frequency option shown above.  Please not that ranks are listed under olympic or competetitive ranking systems, where a tie result in the same number and the next rank goes down 2 (bigger ties result in bigger descrepencies, etc.). 

UNAVAILABLE VALUES: any value less than 0

Reset a Parameter option: Opens up a new menu, which lets user enter a number between 1 and 8. Options 1-6 lets the user resets all preset names, years, regions, genders, frequencies or ranks respectively. Option 7 lets the user reset all current parameters for the search, which will give a warning that the user must answer 1 for (entering 2 leaves the warning and function entirely) the user to reset all current parameters to default.

Search Option: Prints out all data based on specified parameters.  For example, if requested John in names, 1940 to 1960 in years and Alberta and California in Regions, then it will find all the Johns between 1940 to 1960 only in Alberta and California and print them our sorted.  They are primarily sorted by Alphabetical Name, Year, Frequency of name in given year and then specified region. The two scenarios where it will not print is when:
1.All parameters are set to default, will take a very long time, memory and ram to print out every option.
2.The parameters are restrictive enough to not find any specified name, year, frequency, region, rank or gender under those restrictions.  Hence an error message will print out.

Exiting Option: Exits program.

