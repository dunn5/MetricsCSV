#Author: Andrew Dunn
import urllib2
import datetime
import json

hexfile=open("hexkey.txt","r")
hexpass=hexfile.read()
hexfile.close()

urlfirst =  "https://app.mybasis.com/api/v1/chart/"+hexpass+".json?summary=true&interval=60&units=ms&start_date="
urlsecond = "&heartrate=true&steps=true&calories=true&gsr=true&skin_temp=true&air_temp=true&bodystates=true"

numdays = int(raw_input("enter number of days:").strip())
base = datetime.date.today()
dateList = [ base - datetime.timedelta(days=x) for x in range(0,numdays) ]

fp=open("output.csv","w")

for element in dateList:
    date=str(str(element.year)+"-"+str(element.month)+"-"+str(element.day))
    ipdata=urllib2.urlopen(urlfirst+date+urlsecond)
    datatowrite=ipdata.read()
    dictdata = json.loads(datatowrite)
    
    for metric in dictdata["metrics"]:
        fp.write(date+"_"+metric+", "+str(dictdata["metrics"][metric]["values"])[1:-1]+", ")
    fp.write("\n")
    
fp.close()
