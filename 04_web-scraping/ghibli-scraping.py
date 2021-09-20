import requests
import pprint
import json


with open('ghibli_data.json', 'r') as fin:
    data = json.load(fin)

films = []

for x in data:
    films_dict = {}
    films_dict['title'] = x['title']
    films_dict['rt_score'] = x['rt_score']
    films_dict['year'] = x['release_date']
    films.append(films_dict)

with open('ghibli_scores.json', 'r') as fin:
    data = json.load(fin)

pprint.pprint(data)
# with open('ghibli_scores.json', 'w') as fout:
#     json.dump(films, fout)

# pprint.pprint(data_2)

# films = {}
# for x in data:
#     films[x['title']] = int(x['rt_score'])

# with open ('ghibli_scores.json', 'w') as fout:
#     json.dump(films, fout)

# response = requests.get('https://ghibliapi.herokuapp.com/films')
# data = response.json()
# # Print all titles
# for x in response.json():
#     #print(x['title'] + x['running_time'])

# # Get longest film running time
# new_dict = {}

# for x in response.json():
#     new_dict[x['title']] = int((x['running_time']))

# # print(max(new_dict.values()))
# for k, v in new_dict.items():
#     if v == 137:
#         #print(k)

# for x in response.json():
#     if x['running_time'] == '137':
#         pprint.pprint(x)

# with open('ghibli_data.json', 'w') as fout:
#     json.dump(data, fout)