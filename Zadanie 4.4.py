import sys
import logging
logging.basicConfig(level=logging.DEBUG)

a =input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ") 

if a == '1':
    logging.info("Wybrałeś dodawanie")
    b=  float(input ("podaj pierszą cyfrę "))
    c=  float(input ("podaj drugą cyfrę "))
    print("Oto wynik dodawania: ", round(c + b, 2)) # zaokrąglam 
elif a == '2':
    logging.info("Wybrałeś odejmowanie")
    d=  float(input ("podaj pierszą cyfrę "))
    e=  float(input ("podaj drugą cyfrę "))
    print("Oto wynik odejmowania: ", round(d - e, 2))
elif a == '3':
    logging.info("Wybrałeś mnożenie")
    f=  float(input ("podaj pierszą cyfrę "))
    g=  float(input ("podaj drugą cyfrę "))
    print("Oto wynik mnożenia: ", round(f * g, 2))
elif a == '4':
    logging.info("Wybrałeś dzielenie")
    h=  float(input ("podaj pierszą cyfrę "))
    i=  float(input ("podaj drugą cyfrę "))
    print("Oto wynik dzielenia: ", round(h / i, 2))
else:
    print("wpisz cyfrę od 1 do 4")
    exit(1)