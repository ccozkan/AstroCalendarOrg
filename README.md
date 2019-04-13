# AstroCalendarOrg
converts astronomic events calendar from seasky.org to org mode file and possibly to icalendar (ics) file


This project is inspired from kroeliebuschie/AstroCalendar. There was some bug when I was trying to convert ics to org file. I couldn't fix it, so I wrote this one. 
## usage

Make sure you have python3 and requests, bs4, datetime, pytz packages are installed.
Alse modify the timezone in line 9, if you want it to be accurate.

 
Following command creates the org file

```bash
python3 astro.py
```

## ics file

Emacs has an icalendar file export.

## future work

i may implement multiple year and multiple event day support, i may not.

## be aware

the content on seaksy.org is copyrighted.

>Information contained within this site may be used for any personal, educational, and most non-commercial purposes as long as Sea and Sky is credited as the source.
