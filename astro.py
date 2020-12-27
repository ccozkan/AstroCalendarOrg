from bs4 import BeautifulSoup
from datetime import datetime
import requests
import pytz 

year = 2021
r = requests.get('http://www.seasky.org/astronomy/astronomy-calendar-' + str(year) + '.html')
soup = BeautifulSoup(r.text,'html.parser')

tz = pytz.timezone("Europe/Istanbul")


event_date = soup.findAll('span',{'class':'date-text'})
event_title = soup.findAll('span',{'class':'title-text'})
event_title = soup.findAll('p')

events = event_title[9:-12]

def month2num(month):
    if month == 'January':
        return 1
    elif month == 'February':
        return 2
    elif month == 'March':
        return 3
    elif month == 'April':
        return 4
    elif month == 'May':
        return 5
    elif month == 'June':
        return 6
    elif month == 'July':
        return 7
    elif month == 'August':
        return 8
    elif month == 'September':
        return 9
    elif month == 'October':
        return 10
    elif month == 'November':
        return 11
    elif month == 'December':
        return 12

dicto = {}
dicto[str(year)] = {}

for event in range(0,len(events)):
    #print(event)
    dt = events[event].text.split('- ',1)[0]
    kalan = events[event].text.split('- ',1)[1]
    t = kalan.split('. ',1)[0]
    d = kalan.split('. ',1)[1]

    m = month2num(dt.split(' ',1)[0])

    day = dt.split(' ',1)[1]
    days = []

    if ', ' or ' & ' in day:
        day.replace('&',',')
        
        day = day.split(', ',1)[0]
        day = day.split(' & ',1)[0]
#    if ',' in day:
#        day = day.split(', ',1)[0]
#        for i in range(0,day.count(', ')):
#            days.append(day.split(', ',day.count(', '))[i])
#    else:
#        days.append(day)
        #print(day)



    with open("x_astrocal" + str(year)[2:] + ".org", "a") as myfile:
        myfile.write('* ' + t +'\n')


    if ' UTC' in d:
        tutc = d.split(' UTC')[0][-5:]
        #print(tutc)

        dobj = tz.localize(datetime(year, m, int(day), int(tutc[:2]), int(tutc[-2:])), is_dst=None)

        with open("x_astrocal" + str(year)[2:] + ".org", "a") as myfile:
            myfile.write('   <' + dobj.strftime('%Y-%m-%d %a %H:%M') + '>\n')
#    if ',' in day:
#        day = day.split(', ',1)[0]
#        for i in range(0,day.count(', ')):
#            days.append(day.split(', ',day.count(', '))[i])
#    else:
#        days.append(day)
        #print(day)

    else:
        #print(day)
        dobj = datetime(year,m,int(day))

        with open("x_astrocal" + str(year)[2:] + ".org", "a") as myfile:
            myfile.write('   <' + dobj.strftime('%Y-%m-%d %a') + '>\n')
       


    
   # with open("x_astrocal19.org", "a") as myfile:
    with open("x_astrocal" + str(year)[2:] + ".org", "a") as myfile:
        myfile.write(dt + '\n' + d + '\n')

        
   # with open("x_astrocal19.org", "a") as myfile:
    with open("x_astrocal" + str(year)[2:] + ".org", "a") as myfile:
        myfile.write('(copyright: seasky.org)'+ '\n')



