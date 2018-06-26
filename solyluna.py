import ephem
import datetime
from math import radians as rad,degrees as deg

#defining position
lat = '39.2155693'
long = '-2.3110731'
eleva = 735

obs = ephem.Observer()

sun = ephem.Sun(obs)
moon = ephem.Moon(obs)

obs.long = ephem.degrees(long)
obs.lat = ephem.degrees(lat)
#obs.date = '1997/3/10 05:16:30'
obs.date = ephem.now()    # + ephem.hour * 2
obs.elevation = eleva

print ("\n")
print (obs)
print ("\n")

r1 = obs.next_rising(sun)
s1 = obs.next_setting(sun)
#noon = obs.solarnoon(sun)
sun.compute(obs)

#print ("Salida Sol (UTC time): ", r1)
#print ("Puesta Sol (UTC time): ", s1)
print("Salida Sol: (Hora Local)  {:%H:%M}".format(ephem.localtime(r1)))
print("Puesta Sol: (Hora Local)  {:%H:%M}".format(ephem.localtime(s1)))
print("Posición del Sol: ", round(deg(sun.alt),2) , round(deg(sun.az),2) )
print ("")

r1 = obs.next_rising(moon)
s1 = obs.next_setting(moon)
moon.compute(obs)

#print ("Salida Luna (UTC time): ", r1)
#print ("Salida Luna (UTC time): ", s1)
print("Salida Luna: (Hora Local)  {:%H:%M}".format(ephem.localtime(r1)))
print("Puesta Luna: (Hora Local)  {:%H:%M}".format(ephem.localtime(s1)))
print("Posición de la Luna: ", round(deg(moon.alt),2) , round(deg(moon.az),2) )
print ("")
print (ephem.next_new_moon(obs.date))

nnm = ephem.next_new_moon(obs.date)
pnm = ephem.previous_new_moon(obs.date)
lunation=(obs.date-pnm)/(nnm-pnm)
symbol=lunation*26

print(round(lunation,2))


if symbol < 0.2 or symbol > 25.8 :
    symbol = '1'  # new moon
else:
    symbol = chr(ord('A')+int(symbol+0.5)-1)

print(symbol)




