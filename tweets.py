import twint
import nest_asyncio
import pandas as pd

from IPython.display import display, HTML
import requests


nest_asyncio.apply()

# Configure
c = twint.Config()


c.Search = 'request for startup'
c.Limit = 20
c.Pandas = True

c.Hide_output = True

c.Store_csv = True
c.Output = 'womensmarch_2016.txt'

# Run
twint.run.Search(c)

df = pd.read_csv('womensmarch_2016.txt', sep=',')

df.info()

df.to_html("Table.htm") 
# assign it to a  
# variable (string) 
html_file = df.to_html()
display(HTML(html_file))

#def show_tweet(link):
 #   '''Display the contents of a tweet. '''
 #   url = 'https://publish.twitter.com/oembed?url=%s' % link
 #   response = requests.get(url)
 #   html = response.json()["html"]
 #   display(HTML(html))
    
    
    
#sample_tweet_link = df.sample(20)['link'].values[0]
#display(sample_tweet_link)
#show_tweet(sample_tweet_link)

