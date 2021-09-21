# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5
import requests
import json

BASE_URL = "https://pokeapi.co/api/v2/pokemon"
request = requests.get(BASE_URL)
data = request.json()

for k, v in data.items():
    if k == 'results':
        for key, val in v[0].items():
            if key == 'url':
                new_url = val

new_url = new_url[0:-2]

for num in range(0, 152):
    new = new_url + f'{num}'
    response = requests.get(new)
    # new_data = response.json()
    # for k, v in new_data.items():
    #     if k == 'forms':
    #         for kay, vee in v[0]:
    #             if kay['name'] == 'bulbasaur':
    #                 print(kay, vee)
