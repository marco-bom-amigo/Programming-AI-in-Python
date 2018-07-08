import pandas as pd
import json
from pandas.io.json import json_normalize

data = json.load(open("exemplo.json"))
print(data)

data_frame_json = pd.read_json("exemplo.json")
print(data_frame_json)

print(json_normalize(data, "cars", ['state', 'shortname', ['info', 'owner']]))

