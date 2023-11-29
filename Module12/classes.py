"""
Jennifer Larsen
11/15/2023
This program displays CSV Import to Class Object Assignment
"""

import csv


class CountyData:
    def __init__(self, name, per_capita_income, median_household_income, median_family_income, population, households):
        self.name = name
        self.per_capita_income = per_capita_income
        self.median_household_income = median_household_income
        self.median_family_income = median_family_income
        self.population = population
        self.households = households


def import_county_data(file_path):
    county_data_dict = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['County'] != 'Iowa State' and row['County'] != 'United States':
                name = row['County']
                per_capita_income = int(row['Per capita income'].replace('$', '').replace(',', ''))
                median_household_income = int(row['Median household income'].replace('$', '').replace(',', ''))
                median_family_income = int(row['Median Family Income'].replace('$', '').replace(',', ''))
                population = int(row['Population'].replace(',', ''))

                # Correct header for 'Households'
                households_header = 'Number of households'
                households = int(row[households_header].replace(',', ''))

                county = CountyData(name, per_capita_income, median_household_income, median_family_income, population,
                                    households)
                county_data_dict[name] = county
    return county_data_dict


def find_pop_household_for_county(county_data_dict, county_name):
    if county_name in county_data_dict:
        county = county_data_dict[county_name]
        return county.population / county.households
    else:
        return None


def find_total_iowa_population(county_data_dict):
    total_population = sum(county.population for county in county_data_dict.values())
    return total_population


if __name__ == "__main__":
    file_path = "Iowa 2010 Census Data Population Income.csv"
    county_data_dict = import_county_data(file_path)

    # Find and print population/household for Dallas County
    dallas_county_population_household = find_pop_household_for_county(county_data_dict, "Dallas")
    if dallas_county_population_household is not None:
        print(f"Population/Household for Dallas County: {dallas_county_population_household:.2f}")

    # Find and print total population for Iowa
    total_iowa_population = find_total_iowa_population(county_data_dict)
    print(f"Total Population for Iowa: {total_iowa_population}")
