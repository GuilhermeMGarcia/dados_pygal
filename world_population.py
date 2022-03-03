import json

# Carrega os dados em uma lista
file_name = 'population_data.json'
with open(file_name) as f:
    pop_data = json.load(f)

# Exibe a populaçao de cada pais em 2010
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name =  pop_dict['Country Name']
        population = pop_dict['Value']
        print(f"{country_name} : {population}")
