import requests
import json

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

# print(post_codes_req.status_code)
# print(post_codes_req.headers)
# print(post_codes_req.content)
# print(type(post_codes_req.content))
# print(post_codes_req.json())
# print(type(post_codes_req.json())) # .json() method in requests lib, converts to dict

# pokemon_req = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
# pokemon_json = json.dumps(pokemon_req.json(), indent=2)
# print(pokemon_json)

# json_body = json.dumps({"postcodes": ["OX49 5NU", "M32 0JG", "NE30 1DP"]})
# headers = {"Content-Type": "application/json"}
# post_multi_req = requests.post("https://api.postcodes.io/postcodes/", headers=headers, data=json_body)

# print(json.dumps(post_multi_req.json(), indent=2))
