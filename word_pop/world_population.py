import json

from country_codes import get_country_code

# Carrega os dados em uma lista
file_name = 'word_pop/population_data.json'
with open(file_name) as f:
    pop_data = json.load(f)

# Exibe a populaçao de cada pais em 2010
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name =  pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print(f"{code}: {str(population)}")
        else:
            print(f"ERROR - {country_name}")
