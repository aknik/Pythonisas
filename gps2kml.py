#!/usr/bin/python3

# Copyright (C) 2007 by Jaroslaw Zachwieja
# Published under the terms of GNU General Public License v2 or later.
# License text available at http://www.gnu.org/licenses/licenses.html#GPL

# sudo apt install python3-pip
# sudo apt-get --reinstall install python3-pyasn1 python3-pyasn1-modules
# sudo pip3 install pyserial oauth2client gspread
# sudo pip3 install --upgrade google-auth-oauthlib

import serial
import string
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import datetime
from time import sleep
from threading import Thread
import os
import subprocess

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
gc = gspread.authorize(credentials)
sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/11s1tjjTWLUl29IPJzg8o07aqZwOgXuxQL9qqV4ZLBfg')
worksheet = sheet.get_worksheet(0)


gps = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
file = '/home/usuario/nmea.kml'

print ("Serving data")

latitude = 0
longitude = 0
speed = 0
heading = 0
altitude = 0
range = 1000
tilt = 30
cuenta = 0
linea = ""

showGpsData = True
showUpdateMessage = True
secondOld = 0

def setDateTimeUTC2(seconds_epoch):
    command_wait('date -u -s "@' + str(seconds_epoch) + '"')


def setDateTimeUTC(year, month, day, hour, minute, second):
    
    global seconds_epoch
    strUTCyear2set = str(year)
    strUTCmonth2set = str(month)
    strUTCday2set = str(day)
    strUTChour2set = str(hour)
    strUTCminute2set = str(minute)
    strUTCsecond2set = str(second)

    if(len(strUTCyear2set) < 4):
        strUTCyear2set = str(year + 2000)

    if(len(strUTCmonth2set) < 2):
        strUTCmonth2set = '0' + strUTCmonth2set

    if(len(strUTCday2set) < 2):
        strUTCday2set = '0' + strUTCday2set

    if(len(strUTChour2set) < 2):
        strUTChour2set = '0' + strUTChour2set

    if(len(strUTCminute2set) < 2):
        strUTCminute2set = '0' + strUTCminute2set

    if(len(strUTCsecond2set) < 2):
        strUTCsecond2set = '0' + strUTCsecond2set

    command_wait('date -u +%Y%m%d -s "' + strUTCyear2set +
                                          strUTCmonth2set +
                                          strUTCday2set + '"')

    command_wait('date -u +%T -s "' + strUTChour2set + ':' +
                                      strUTCminute2set + ':' +
                                      strUTCsecond2set + '"')

    seconds_epoch = time.mktime(datetime.datetime.now().timetuple())
    seconds_epoch += 3
    setDateTimeUTC2(seconds_epoch)


def command_wait(command):
    ## command = "sudo mount /dev/sda1 /mnt/usb"
    process = subprocess.Popen(command,
                               shell=True,
                               stdout=subprocess.PIPE)
    process.wait()
    if(process.returncode != 0):
        print ('command wait - error: ')
        print (process.returncode)


def command_nowait(command):
    ## command = "sudo mount /dev/sda1 /mnt/usb"
    #process = subprocess.Popen(command,
    #                            shell=True,
    #                            stdout=subprocess.PIPE)
    subprocess.Popen(command,
                     shell=True,
                     stdout=subprocess.PIPE)
    ## process.wait()
    ## print process.returncode



while 1:

    line = (gps.readline()).decode('cp437')
    line = str(line)

    #print (line)
    line.replace(",,", ",0,")
    #line.replace("'", "")
    datablock = line.split(',')


    if line[0:6] == '$GPRMC':
        if line[7:13] == linea[7:13]:
            continue

        linea = line
        print (line)
        
        #$GPRMC,115033.00,A,3916.26184,N,00219.23143,W,0.167,,270418,,,A*66
        hourGPS = int(datablock[1][:2])
        minuteGPS = int(datablock[1][2:4])
        secondGPS = int(datablock[1][4:6])
        dayGPS = int(datablock[9][:2])
        monthGPS = int(datablock[9][2:4])
        yearGPS = int(datablock[9][4:6])

        minuteNow = time.strftime("%M")
        minuteOld = minuteNow
             
        secondNow = time.strftime("%S")
        if secondOld != secondNow:
            secondOld = secondNow
            print ('UTC: ' + str(datetime.datetime.utcnow()))
            print ('Local: ' + str(datetime.datetime.now()))
            print           
 

        if datablock[3] == "":
            datablock[3] = "0";
        latitude_in = float(datablock[3].replace(" ", ""))
        if datablock[5] == "":
            datablock[5] = "0";
        longitude_in = float(datablock[5].replace(" ", ""))
        if datablock[8] == "":
            datablock[8] = "0";
        altitude = float(datablock[8].replace(" ", ""))
        if datablock[7] == "":
            datablock[7] = "0";
        speed_in = float(datablock[7].replace(" ", ""))
        heading = float(datablock[8].replace(" ", ""))

        if datablock[4] == 'S':
            latitude_in = -latitude_in

        if datablock[6] == 'W':
            longitude_in = -longitude_in

            latitude_degrees = int(latitude_in/100)
            latitude_minutes = latitude_in - latitude_degrees*100

            longitude_degrees = int(longitude_in/100)
            longitude_minutes = longitude_in - longitude_degrees*100

            latitude = latitude_degrees + (latitude_minutes/60)
            longitude = longitude_degrees + (longitude_minutes/60)


        cuenta = cuenta + 1

        if cuenta > 60:

            setDateTimeUTC(yearGPS,
                       monthGPS,
                       dayGPS,
                       hourGPS,
                       minuteGPS,
                       secondGPS)
                       
            worksheet.update_acell('A2', latitude)
            worksheet.update_acell('B2', longitude)
            worksheet.update_acell('C2', seconds_epoch)
            cuenta = 0
            print (latitude)
            print (longitude)

        speed = int(speed_in * 1.852)
        range = ( ( speed / 100  ) * 350 ) + 650
        tilt = ( ( speed / 120 ) * 43 ) + 30

        if speed < 10:
            range = 200
            tilt = 30
            heading = 0

        output = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.0">
    <Placemark>
        <name>%s km/h</name>
        <description>^</description>
        <LookAt>
            <longitude>%s</longitude>
            <latitude>%s</latitude>
            <range>%s</range>
            <tilt>%s</tilt>
            <heading>%s</heading>
        </LookAt>
        <Point>
            <coordinates>%s,%s,%s</coordinates>
        </Point>
    </Placemark>
</kml>""" % (speed,longitude,latitude,range,tilt,heading,longitude,latitude,altitude)

        f=open(file, 'w')
        f.write(output)
        f.close()


