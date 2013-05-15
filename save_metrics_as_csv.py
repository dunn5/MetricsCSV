#Author: Andrew Dunn
#andrewedunn.net
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

headers = ["skin_temp","heart_rate","air_temp","calories","gsr","steps"]

fp.write("date ,")
for header in headers:
    for j in range(0,1440):
        zero1= "0" if ((j-(j%60))/60)<10 else ""
        zero2= "0" if (j%60)<10 else ""
        fp.write(header+"_"+zero1+str((j-(j%60))/60)+zero2+str(j%60)+", ")

fp.write("\n")

for element in dateList:
    date=str(str(element.year)+"-"+str(element.month)+"-"+str(element.day))
    ipdata=urllib2.urlopen(urlfirst+date+urlsecond)
    datatowrite=ipdata.read()
    dictdata = json.loads(datatowrite)

    fp.write(date+", ")
    for metric in dictdata["metrics"]:
        fp.write(str(dictdata["metrics"][metric]["values"])[1:-1]+", ")
    fp.write("\n")
    
fp.close()
