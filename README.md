This page contains visualizations of available open datasets with information from Delaware.

# Births in Delaware from 2009 to 2014
Using the following [dataset](https://dev.socrata.com/foundry/data.delaware.gov/y8fa-dqxh) we can analyze the births in Delaware from 2009 to 2014. I will be using the requests library to do so.

    import requests
    url = 'https://data.delaware.gov/resource/y8fa-dqxh.json?$limit=100000'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

We can now use our response object to analyze the data. Delaware is a small state, let's find out how many births, of the total 72456, were in each county. Delaware has three counties: New Castle, Kent, Sussex.

    kent, sussex, ncc = 0, 0, 0
    for item in data:
        if item['county_of_residence'] == 'Sussex':
            sussex += 1
        elif item['county_of_residence'] == 'New Castle':
            ncc += 1
        else:
            kent += 1
    print(ncc, kent, sussex)

We can plot that data to show the following:


    labels = 'NCC', 'Kent', 'Sussex'
    sizes = [ncc, kent, sussex]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
    ax1.axis('equal')
    plt.show()
    
![chart1](http://i.imgur.com/5qki6p6.png)
