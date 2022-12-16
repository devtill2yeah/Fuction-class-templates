

#we need to import a few things to make it work first
from lxml.html import fromstring
from itertools import cycle
import requests

#This sets a list of proxies. You can get this from many different sites.
PROXY_LIST = ['1.10.240.135:8080',
'101.109.142.5:8080',
'177.124.16.178:45817',
'101.109.110.221:8080']

#creates a 'pool' of proxies which is based on the list so it isn't one after another. This helps if you have many sequential proxies.
proxy_pool = cycle(PROXY_LIST)
#sets an empty list of working proxies which we will populate later
working_proxies = []
#sets the url you want to visit - this one just returns an IP address
url = 'https://www.canihazip.com/s'

#goes through each proxy in the PROXY_LIST - you could set the second part (where len(PROXY_LIST) is) to a big number if you wanted to keep testing.
for i in range(0,len(PROXY_LIST)):
 #Get the next proxy from the pool
 proxy = next(proxy_pool)
 print("Request #%d"%i)
 try:
     #print response from website
     response = requests.get(url, proxies={"http": proxy, "https": proxy})
     print("working proxy at:"+str(response.content))
     working_proxies.append(proxy)
 except:
     #if it doesnt work throw a connect error
     print("Connnection error")

#lists all working proxies, it converts the list to a set so it only shows unique values.
print("The working proxies are:"+ str(set(working_proxies)))

