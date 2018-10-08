#!/usr/bin/python3
import datetime
import csv
# import os
# from time import sleep
# # os.system("fswebcam -D 1 -S 3 /home/osmc/public_html/outside.jpg")
# # sleep(5)
# print("Content-Type: text/html\n")
# print("<!DOCTYPE html>")
# print("<html>")
# print("<head>")
# print("""<meta charset="UTF-8">""")
# print("<title>Weather Reports</title>")
# print("""<LINK rel="stylesheet" href="/css/main.css" type="text/css">""")
# print("</head>")
# print("""<table class="table" border="0" cellspacing="0" summary="outline"><body><tr><td id="main_body">""")
# print("""<a href = "/~osmc/">Home</a>""")
# print("</br>")
# print("""<img src="/~osmc/outside.jpg"></br>""")
with open("/home/pi/weather.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        tem = float(row[0])
        pre = float(row[1])
        hum = float(row[2])
        ts = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M')
print("temperature:{0:.1f}&deg;C</br>pressure:{1:.1f}hPa</br>humidity:{2:.1f}%</br>{3:%Y/%m/%d %H:%M}".format(tem,pre,hum,ts))

# print("</td></tr></table></body>")
# print("</html>")