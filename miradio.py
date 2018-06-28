def hashcode(s):  # http://garage.pimentech.net/libcommonPython_src_python_libcommon_javastringhashcode/
    h = 0
    for c in s:
        h = (31 * h + ord(c)) & 0xFFFFFFFF
    return ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000

# Sistema de codificacion que usa la app MiRadio para Android, codifica la url del streaming de las emisoras.
# La funcion hashcode no llega a necesitarse, solo la añado porque en el original en java, la usa.
# https://storage.googleapis.com/miradio/public/spain/stations/spain_destacadas.xml
# https://storage.googleapis.com/miradio/public/spain/stations/spain_locales.xml
import requests
import xmltodict

def miradio(input):

    output =""

    line = ""
    S1 = ""
    S2 = ""

    for i in range(0,len(input)-1,2):
        if (i == len(input)-1):
            S1 = S1 + input[:len(input)-1]
        else:

            S1 = S1 + input[i+1:i+2]
            S2 = input[i:i+1] + S2


    line = S1 + S2

    b = "9876543210/:.zyxwvutsrqponmlkjihgfedcba"
    a = "0123456789abcdefghijklmnopqrstuvwxyz.:/"

    for i in range(0,len(line)):

        for j in range(0,39):

            if line[i] == a[j]:
                output = output + b[j]
                break
            else:
                if j == 38: output = output + line[i]


    return (output)

URL = "https://storage.googleapis.com/miradio/public/spain/stations/spain_destacadas.xml"
headers = {'Content-Type': 'text/xml',
           'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12F69',
           'Accept': 'gzip'}

response = requests.get(URL, headers=headers)
#with open('spain_destacadas.xml', 'wb') as file:
#    file.write(response.content)

with open('./spain_destacadas.xml') as fd:
    doc = xmltodict.parse(fd.read())

codes = [] # https://stackoverflow.com/questions/40154727/how-to-use-xmltodict-to-get-items-out-of-an-xml-file

for emisora in doc['Contenido']['Emisora']:
    #codes.append(emisora['Nombre'])
    print (emisora['Nombre'])
    #print (emisora['NewUrlStream'])
    print (miradio(emisora['NewUrlStream']))
    print ("\n")



