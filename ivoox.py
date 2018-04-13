import subprocess
import time,os,re,requests,json
from urllib.request import urlopen
from urllib.parse import urlencode

TOKEN = ',,,,,:AAH-1mZ3C-,,,,,,,,,,,,,,,,,,'
BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'

def reply(msg):
    result = urlopen(BASE_URL + 'sendMessage', urlencode({
    'chat_id': ',,,,,,,',
    'text': msg
    }).encode('utf-8'))

    return

def urlify(s):

     # Remove all non-word characters (everything except numbers and letters)
     s = re.sub(r"[^\w\s]", '', s)
     # Replace all runs of whitespace with a single dash
     s = re.sub(r"\s+", '_', s)
     return s


agent = '"iVoox/2.17(135) (Linux; Android 5.0; Scale/1.0)"'
url1  = "http://api.ivoox.com/1-1/"
url2  = "?function=getSuscriptionAudios&format=json&session=00000000000000"

headers = {
    'User-Agent': agent,
    'Accept-Encoding': 'gzip',
    'accept-language': 'es-ES',
    'Connection': 'Keep-Alive',
}

i = 0

while True:
    r = requests.get(url1+url2, headers=headers)
    if r.status_code == 200 or i > 9:
        break
    i += 1
    time.sleep(3+i)
    print("Error en la descarga.")

i = 0

for row in r.json():
    i += 1
    podcasttitle = urlify(row['podcasttitle'])
    file = str(row['file'])
    filename = os.path.basename(file)
    print ("<<<   ",row['datetext'], podcasttitle)
    if not os.path.exists('/home/pythoner/.temp/' + podcasttitle):
        #break
        os.makedirs('/home/pythoner/.temp/' + podcasttitle)
    savefile = '/home/pythoner/.temp/' + podcasttitle +"/" +filename.split("_")[0] + '.mp3'
    #webfile = 'https://192.168.2.1/' + podcasttitle +"/" +filename.split("_")[0] + '.mp3'
    if (row['datetext'] == 'hace 2 días' ):
        if os.path.isfile(savefile):
            os.remove(savefile)

    if (row['datetext'] == 'Hoy' or row['datetext'][0:7] == 'hace 1 ' ):
        if not os.path.exists(savefile):
            reply(podcasttitle)
            reply(file)
        #os.system('wget --user-agent='+ agent +' -c ' + file + ' -O ' + savefile )
        os.system('touch ' + savefile )
        print (podcasttitle, savefile)
        print ("-----------------------------------------------------------------------------------")





--------------------------------- crontab -e -------------------------------------------------------------------------



SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin


0,15,30,45  * * * * /usr/bin/python3 /home/pythoner/ivoox.py

0 7 * * * /usr/bin/python3 /home/pythoner/br.py
