import twint
import nest_asyncio
import pandas as pd

from IPython.display import display, HTML
import requests


nest_asyncio.apply()

# configure
c = twint.Config()


c.Search = 'request for startup'
c.Limit = 20
c.Pandas = True

c.Hide_output = True

#store information
c.Store_csv = True
c.Output = 'womensmarch_2016.txt'

# Run
twint.run.Search(c)

df = pd.read_csv('womensmarch_2016.txt', sep=',')

df.info()

#sort retweets, likes, and discussions and then date in descending order
df.sort_values(by= ['retweets_count', 'likes_count', 'replies_count', 'date'], ascending = False,  inplace=True)

html = df.to_html() 

#show the table in a simple web interface
text_file = open("index.html", "w")
text_file.write(html)
text_file.close()
