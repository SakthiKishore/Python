import pandas as pd

# update path of json file

df = pd.read_json (r'C:\Users\SakthiKishore\Desktop\data.json')

#pd.read_csv for csv file

# print (df)
# df.to_csv - for write to csv file

df.to_excel("json_output.xlsx")  
