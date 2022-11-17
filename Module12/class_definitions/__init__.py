class CountyDemos:
    """CountyDemos class"""

    def __init__(self, population, num_households):
        self.population = population
        self.num_households = num_households


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