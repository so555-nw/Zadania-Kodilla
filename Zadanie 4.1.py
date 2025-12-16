
def slowo(slowo:str) -> bool: #deklaruję funkcję i tworzę z niej string i ustawiamy na bool
   a = slowo.lower() #zmieniam wszystkie litery na małe 
   return a == a[::-1] # używam wbudowanej funkcji w pythonie do sprawdzenia czy słowo jest palindromem (python sprawdza czy słowo ma takie same znaki od tyłu)
print(slowo("kajak"))
print(slowo("kodilla"))