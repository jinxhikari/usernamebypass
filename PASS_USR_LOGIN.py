import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import os
import sys
import string
import time
import webbrowser
import pprint as pprint

def get_forms(ses, url):
    ses = HTMLSession()
    res = ses.get(url)
    soup = bs(res.html.html,"html.parser")
    return soup.find_all("form")



def get_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for in_tag in form.find_all("input"):
        in_type = in_tag.attrs.get("type", "text")
        in_name = in_tag.attrs.get("name")
        in_val = in_tag.attrs.get("value", "")
        inputs.append({"type" : in_type, "name" : in_name, "value" : in_val})

    for select in form.find_all("select"):
        sel_name = select.attrs.get("name")
        sel_type = "select"
        sel_options = []
        sel_val = ""
        for sel_opt in select.find_all("options"):
            option_val = sel_opt.attrs.get("value")
            if option_val:
                sel_options.append(option_val)
                if sel_opt.attrs.get("selected"):
                    sel_default_val = option_val
        if not sel_default_val and sel_opt:
            sel_default_val = sel_options[0]

        inputs.append({"type" : sel_type, "name" : sel_name, "values" : sel_options, "value" : sel_default_val})

    for text in form.find_all("textarea"):
        text_name = text.attrs.get("name")
        text_type = "textarea"
        text_val = text.attrs.get("value", "")
        inputs.append({"type" : text_type, "name" : text_name, "value" : text_val})


    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details



if __name__ == "__main__":
    url = 'https://login.webzen.com/'
    
    digits = list(range(1000, 9999,1))
    username = "king"
    password = "password"
    #add digits later once we confirmed posts work
    payload = {
        'username' : username,
        'current-password': password
    }

    form = {}
    user_index = 1
    pass_index = 2

    data = {}

    #sent = requests.post(url, allow_redirects=False, data=payload)
    #print(sent.text)

    session = HTMLSession()
    forms = get_forms(session, url)
    for i, form in enumerate(forms, start=1):
        form_details = get_details(form)
        print("="*50, f"form #{i}", "="*50)
        print(form_details)
        print('\n')

    form_details = get_details(forms[0])
    #FIXME this dict isn't formatted correctly
    for input_tag in form_details["inputs"]:
        if input_tag["type"] == "hidden":
            data[input_tag["name"]] = input_tag["value"]
        elif input_tag["type"] == "checkbox":
            data[input_tag["name"]] = input_tag["value"]
        
        print(input_tag)

    print(data)

'''
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
'''
