import requests
from collections import Counter
import matplotlib.pyplot as plt


app_token = ''
secret_token = ''
url = 'https://data.delaware.gov/resource/y8fa-dqxh.json?$limit=100000'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
kent = 0
ncc = 0
sussex = 0
for item in data:
    if item['county_of_residence'] == 'Sussex':
        sussex += 1
    elif item['county_of_residence'] == 'New Castle':
        ncc += 1
    else:
        kent += 1
print(sussex, kent, ncc)
# from 2009 to 2014 there were 72,456 births in delaware
# 13475 in sussex county, 19154 in kent county, and 39827 in new castle county
twenty_to_thirtyfour = 0
thirty_five_plus = 0
under_twenty = 0
under_twenty_list = []
for item in data:
    if item['mom_s_age'] == '20-34':
        twenty_to_thirtyfour += 1
    elif item['mom_s_age'] == '35+':
        thirty_five_plus += 1
    else:
        under_twenty += 1
        under_twenty_list.append(item)
print(under_twenty, twenty_to_thirtyfour, thirty_five_plus)
labels = 'Under Twenty', 'Twenty to Thirty Four', 'Thirty-five plus'
sizes = [5271, 56402, 10738]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
ax1.axis('equal')
plt.show()



