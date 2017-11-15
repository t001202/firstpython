import json

filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)
	# print(pop_data)
#打印每个国家的人数
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = pop_dict['Value']
		print(country_name + " : " + population)
