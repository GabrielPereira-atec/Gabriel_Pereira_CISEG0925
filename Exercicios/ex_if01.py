seg = 0
hr=0
mins=0

seg = int(input("Defina os segundos: \n"))

hr = seg//3600
mins = seg//60

if seg>=3600 :
    print (seg, "segundos é igual a",hr, "Horas")
elif seg>=60 :
    print (seg, "segundos é igual a",mins, "Minutos")
else :
    print (seg, "segundos é equivalente a:",seg ,"segundos")

#print ("\n\nO valor inserido é igual a ", hr, "horas,", mins,"minutos e", seg,"segundos")