import numpy as np
cero = "0"
siglo1 = "19"
siglo2 = "19"

con31 = [1,3,5,7,8,10,12 ]
con30 = [2,4,6,9,11 ]

while (1):
    
    dia1 = str(np.random.randint(1,31))     
    if dia1 == 31 : 
        mes1 = str(np.random.choice(con31))
    else :
        mes1 = str(np.random.choice(con30))
    ano1 = str(np.random.randint(48,64))
    
    

    dia2 = str(np.random.randint(1,31))     
    if dia2 == 31 : 
        mes2 = str(np.random.choice(con31))
    else :
        mes2 = str(np.random.choice(con30))
    ano2 = str(np.random.randint(48,64))
    
    
    
        dia3 = str(np.random.randint(1,31))     
    if dia3 == 31 : 
        mes3 = str(np.random.choice(con31))
    else :
        mes3 = str(np.random.choice(con30))
    ano3 = str(np.random.randint(48,64))
    
    
    
        dia4 = str(np.random.randint(1,31))     
    if dia4 == 31 : 
        mes4 = str(np.random.choice(con31))
    else :
        mes4 = str(np.random.choice(con30))
    ano4 = str(np.random.randint(48,64))
    
    
    
	if len(dia1) < 2  : dia1 = cero + dia1
	if int(mes1) < 10 : mes1 = cero + mes1
	if int(dia2) < 10 : dia2 = cero + dia2
	if int(mes2) < 10 : mes2 = cero + mes2

	if len(dia3) < 2  : dia3 = cero + dia3
	if int(mes3) < 10 : mes3 = cero + mes3
	if int(dia4) < 10 : dia4 = cero + dia4
	if int(mes4) < 10 : mes4 = cero + mes4


	# password = dia1+mes1+siglo1+ano1+dia2+mes2+siglo2+ano2
	password = dia1+mes1+dia2+mes2+dia3+mes3+dia4+mes4

	if len(password) > 8 :
			print (password)


# python2 generador_avenida.py | aircrack-ng -e wIFI_ESSI wpa.cap -w -


