class CountyDemographics:
    """CountyDemographics class for assignemnt"""

    def __init__(self, rank, county, per_capita_income, median_household_income, median_family_income, population, number_of_households):
        self.rank = rank
        self.county = county
        self.per_capita_income = per_capita_income
        self.median_household_income = median_household_income
        self.median_family_income = median_family_income
        self.population = population
        self.number_of_households = number_of_households

    def get_pop_and_house(self):
        return f"County: {self.county}\nPopulation: {self.population}\nNumber of Households: {self.number_of_households}\n"

import csv
from class_definitions import CountyDemographics as CountyDemo

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
        county[str(row[1])] = CountyDemo(row[0], row[1], row[2], row[3], row[4], row[5], row[6])


#Remove bad data
county.pop("United States")
county.pop("Iowa State")

#Variables
countyDallas = CountyDemo(county["Dallas"].rank, county["Dallas"].county, county["Dallas"].per_capita_income, county["Dallas"].median_household_income, county["Dallas"].median_family_income, county["Dallas"].population, county["Dallas"].number_of_households)

#Print Dallas Information
print(countyDallas.get_pop_and_house())

#Total Iowa Population
pop_sum = 0
for key in county:
    pop_sum += int(county[key].population.replace(',',''))
print("Total Population of Iowa: " + str(pop_sum))
