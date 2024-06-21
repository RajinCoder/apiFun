import requests
import pandas as pd
import sqlalchemy as db

url = 'https://api.sportmonks.com/v3/football/fixtures'
header = {'Authorization': '8VXrDStCmKp2kNnZHwoaYv3mMYCA3oAwJcRqxzg5f5k4k8Ek3bNv7J5AhWqd'}

response = requests.get(url, headers=header)
engine = db.create_engine('sqlite:///soccer_matches.db')


huge_dict_matches = response.json()['data']


dictionary = {
  'name': [],
  'result_info': [],
  'starting_at': []
  }
print(huge_dict_matches)
def append_dict(dictionary, huge_dict_matches):
  for index in range(len(huge_dict_matches)):
    row = huge_dict_matches[index]

    dictionary['name'].append(row.get('name'))
    dictionary['result_info'].append(row.get('result_info'))
    dictionary['starting_at'].append(row.get('starting_at'))


pdFrame = pd.DataFrame.from_dict(dictionary)

pdFrame.to_sql('soccer_matches', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM soccer_matches LIMIT 3;")).fetchall()
   print(pd.DataFrame(query_result))



