from databuilder.ehrql import Dataset
from databuilder.tables.beta.smoketest import patients

index_year = 2022
min_age = 18
max_age = 80
# a whole bunch of edits here




year_of_birth = patients.date_of_birth.year
age = index_year - year_of_birth

