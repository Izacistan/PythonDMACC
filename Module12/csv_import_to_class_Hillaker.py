import csv

class CountyDemos:
    def __int__(self, rank, county, per_capita_income, median_household_income, median_family_income, population, number_of_households):
        self._rank = rank
        self._county = county
        self._per_capita_income = per_capita_income
        self._median_household_income = median_household_income
        self._median_family_income = median_family_income
        self._population = population
        self._number_of_households = number_of_households

with open('Iowa 2010 Census Data Population Income.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # initialize empty dictionary
    county = {}
    for row in csv_reader:
        # skip the first line in the file because it is the header
        if line_count == 0:
            line_count += 1
            continue
        # create an item in dictionary county with a key of the county name and a value of the object
        county[str(row[0])] = CountyDemos(row[1],row[2])

print (county['Polk'].population)