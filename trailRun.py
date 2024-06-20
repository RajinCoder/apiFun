import requests

url = 'https://api.sportmonks.com/v3/football/fixtures'
header = {'Authorization': '8VXrDStCmKp2kNnZHwoaYv3mMYCA3oAwJcRqxzg5f5k4k8Ek3bNv7J5AhWqd'}

response = requests.get(url, headers=header)

print(response.status_code)
huge_dict_matches = response.json()['data']
for index in range(len(huge_dict_matches)):
  dictionary = huge_dict_matches[index]
  print(f"The fixture was {dictionary.get('name')} and {dictionary.get('result_info')} This happened {dictionary.get('starting_at')}")
