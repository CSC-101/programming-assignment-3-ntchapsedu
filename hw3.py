import data
import county_demographics
import build_data
import hw3_tests
from data import CountyDemographics

full_data = build_data.get_data()

#part1
#input is list of county demographics
#output is the total population of all the counties together
#for each object in the list find the 2014 population, then add it's value to a variable
def population_total(population: list[data.CountyDemographics])->int:
    total = 0
    for i in population:
        total += i.population['2014 Population']
    return total

#part2
#input list of county demographics and a state
#output all the counties and their demographics of that state
#for each county check if the state is the same as input state
#if same add that county to a list
def filter_by_state(demographics: list[data.CountyDemographics], state: str)->list[data.CountyDemographics]:
    counties_in_state = []
    counties = 0
    for i in demographics:
        if i.state == state:
            counties_in_state.append(i)
            counties += 1
    return counties_in_state

#part3
#input is list of county demographics and string of education/ethnicity/people below poverty line type
#output is a float number
#for each county multiply population and education/ethnicity/below poverty line and .01 to a counter (finding percentage of a population)
def population_by_education(demographics: list[data.CountyDemographics],education: str) -> float:
    total = 0
    for i in demographics:
        total += i.population['2014 Population'] * i.education[education] * 0.01
    return round(total,3)

def population_by_ethnicity(demographics: list[data.CountyDemographics],ethnicity: str)->float:
    total = 0
    for i in demographics:
        total += i.population['2014 Population'] * i.ethnicities[ethnicity] * 0.01
    return round(total,3)

def population_below_poverty(demographics: list[data.CountyDemographics])->float:
    total = 0
    for i in demographics:
        total += i.population['2014 Population'] * i.income['Persons Below Poverty Level'] * 0.01
    return round(total, 3)

#part4
#input is list of demographics and a string of education/ethnicity/below poverty level type
#out is a float representing a percentage of population
#add to a counter the function of total population of education/ethnicity/below poverty level divied by total population (gives percentage)
def percent_by_education(demographics: list[data.CountyDemographics], education: str)->float:
    total = 0
    total += population_by_education(demographics,education) / population_total(demographics) * 100
    return round(total,1)

def percent_by_ethnicity(demographics: list[data.CountyDemographics], ethnicity: str)->float:
    total = 0
    total += population_by_ethnicity(demographics,ethnicity) / population_total(demographics) * 100
    return round(total,1)

def percent_below_poverty_level(demographics: list[data.CountyDemographics])->float:
    total = 0
    total += population_below_poverty(demographics) / population_total(demographics) * 100
    return round(total,1)

#part5
#
#
#
def education_greater_than(demographics: list[data.CountyDemographics],education: str, threshold: float)->list[data.CountyDemographics]:
    counties = []
    for i in demographics:
        if i.education[education] > threshold:
            counties.append(i)
    return counties

def education_less_than(demographics: list[data.CountyDemographics],education: str, threshold: float)->list[data.CountyDemographics]:
    counties = []
    for i in demographics:
        if i.education[education] < threshold:
            counties.append(i)
    return counties
#print(education_greater_than(full_data, "Bachelor's Degree or Higher", 60))
#def education_less_than(demographics: list[data.CountyDemographics],education: str, threshold: float)->list[data.CountyDemographics]:

def ethnicity_greater_than(demographics: list[data.CountyDemographics],ethnicity: str, threshold: float)->list[data.CountyDemographics]:
    counties = []
    for i in demographics:
        if i.ethnicities[ethnicity] > threshold:
            counties.append(i)
    return counties

def ethnicity_less_than(demographics: list[data.CountyDemographics],ethnicity: str, threshold: float)->list[data.CountyDemographics]:
    counties = []
    for i in demographics:
        if i.ethnicities[ethnicity] < threshold:
            counties.append(i)
    return counties

def poverty_level_greater_than(demographics: list[data.CountyDemographics],threshold: float)->list[data.CountyDemographics]:
    counties = []
    for i in demographics:
        if i.income["Persons Below Poverty Level"] > threshold:
            counties.append(i)
    return counties

def poverty_level_less_than(demographics: list[data.CountyDemographics],threshold: float)->list[data.CountyDemographics]:
    counties = []
    for i in demographics:
        if i.income["Persons Below Poverty Level"] < threshold:
            counties.append(i)
    return counties
