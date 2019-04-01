tekst = "Anna, paweł, JuliA"

lista = tekst.split(", ")
print(tekst)
print(type(lista))
print(lista)
imie1 = lista[0]
print(imie1)
imieDuze = imie1.upper()
print(imieDuze) #wyswoetla duzymy literami
imieMale = imie1.lower()
print(imieMale)
#sprawdzenie zawartosci
print("\nPodaj swoje nazwisko: ", end="")
nazwisko = input()
zawartosc = nazwisko.isalpha() #czy jest zawartość?
print(zawartosc) #True vs False
nazwisko = ""
print(nazwisko.isalpha())
text1 = "\nJulia"
text2 = "\nNowak"
text1 = text1.rstrip()
print(text1 + " " + text2)
#wyświetalnie ciągu znaków
#wszytskie wersje pythona
text ="%s, Java i %s" % ("PHP", "Python")
print(text)
#nowsze wersje
text = "{1}, Java i {0}".format("PHP", "Python")
print(text)

#help(text.replace)

new = text.replace("PHP", "C#")
print(new)
#wpisywanie danych
rok = 2019
miesiac = "kwiecień"
dzien = 1
print("\nData: ", end="")
print(dzien, miesiac, rok, sep="-")
