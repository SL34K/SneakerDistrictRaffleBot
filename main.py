#!/usr/bin/python
#.------..------..------..------..------.
#|S.--. ||L.--. ||3.--. ||4.--. ||K.--. |
#| :/\: || :/\: || :(): || :/\: || :/\: |
#| :\/: || (__) || ()() || :\/: || :\/: |
#| '--'S|| '--'L|| '--'3|| '--'4|| '--'K|
#`------'`------'`------'`------'`------'
#https://twitter.com/SL34K
#https://github.com/SL34K
#00110001 00111001
#00110000 00110011
#00110001 00111000 
#########################################
import requests, time, names, random, json, string
from random import randint, choice
sizes = ['EUR 40 | US 7','EUR 40.5 | US 7.5','EUR 41 | US 8','EUR 42 | US 8.5','EUR 42.5 | US 9','EUR 43 | US 9.5','EUR 44 | US 10','EUR 44.5 | US 10,5','EUR 45 | US 11','EUR 45.5 | US 11.5','EUR 46 | US 12','EUR 47 | US 12.5','EUR 47.5 | US 13']
def session():
    sesh = requests.session()
    sesh.headers = {
        'Origin':'https://www.sneakerdistrict.com',
        'Referer':'https://www.sneakerdistrict.com/wotherspoon/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    sesh.headers.update()
    return sesh
def proxysession(proxy):
    ip,port,username,password = proxy.split(":")
    formattedProxy = (username+':'+password+'@'+ip+':'+port)
    proxies = {'http': 'http://'+formattedProxy}
    proxies = {'https': 'https://'+formattedProxy}
    sesh = requests.Session()
    sesh.proxies = proxies
    sesh.headers = {
        'Origin':'https://www.sneakerdistrict.com',
        'Referer':'https://www.sneakerdistrict.com/wotherspoon/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    sesh.headers.update()
    return sesh
    #first,last,day,month,year,email,instaUsername,size,location
def post(sesh,url,first,last,day,month,year,email,instaUsername,size,location,delay):
    instaUsername = instaUsername.split('\n')[0]
    data = {
        'form_fields[0][name]': 'first_name',
        'form_fields[0][value]': first,
        'form_fields[1][name]': 'last_name',
        'form_fields[1][value]': last,
        'form_fields[2][name]': 'day',
        'form_fields[2][value]': day,
        'form_fields[3][name]': 'month',
        'form_fields[3][value]': month,
        'form_fields[4][name]': 'year',
        'form_fields[4][value]': year,
        'form_fields[5][name]': 'email',
        'form_fields[5][value]': email,
        'form_fields[6][name]': 'instagram_username',
        'form_fields[6][value]': instaUsername,
        'form_fields[7][name]': 'size',
        'form_fields[7][value]': size,
        'form_fields[8][name]': 'pick_up',
        'form_fields[8][value]': location,
    }
    test = sesh.post(url,data=data)
    if '{"status":"success"}'==test.text:
        print("Entered successfully:")
        signup = first,last,day,month,year,email,instaUsername,size,location
        print(signup)
        f = open('entries.txt','a')
        f.write(str(signup)+'\n')
        f.close
    time.sleep(delay)
def main(instaUsername):
    with open('config.json') as json_data_file:
        data = json.load(json_data_file)
        form = data['settings']['form']
        catchalldomain = data['settings']['catchalldomain']
        randomnames = data['settings']['randomnames']
        first = data['settings']['setfirst']
        last = data['settings']['setlast']
        signupdelay = int(data['settings']['signupdelay'])
        randomsizes = data['settings']['randomsizes']
        size = data['settings']['size']
        randomDOB = data['settings']['randomDOB']
        randomDOBupper = int(data['settings']['randomDOBupper'])
        randomDOBlower = int(data['settings']['randomDOBlower'])
        day = data['settings']['setDOBday']
        month = data['settings']['setDOBmonth']
        year = data['settings']['setDOByear']
        location = data['settings']['location']
        proxyuse = data['settings']['useproxy']
        proxy = data['settings']['proxy']
        if randomnames == 'True':
            first = names.get_first_name(gender='male')
            last = names.get_last_name()
        randomletters = "".join(choice(string.ascii_letters) for x in range(randint(1, 4)))
        username = randomletters+first+randomletters
        email = username+'@'+catchalldomain
        if randomsizes == 'True':
            size = random.choice(sizes)
        if randomDOB == 'True':
            day = random.randint(1,28)
            month = random.randint(1,12)
            year = random.randint(randomDOBlower,randomDOBupper)
        if proxyuse == 'True':
            sesh = proxysession(proxy)
        else:
            sesh = session()
        post(sesh,form,first,last,day,month,year,email,instaUsername,size,location,signupdelay)
print("@SL34K's SneakerDistrict Raffle Bot")
print("Loading usernames.txt")
with open('usernames.txt') as f:
    content = f.readlines()
for i in content:
    main(i)
