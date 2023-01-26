#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
from statistics import mean


def metoda_najmniejszych_kwadratow(wartosci_x, wartosci_y, st_wielomianu):
    '''
    funkcja wyznacza macierz i wektor wynikowy formatu numpy
    wprowadzane zmienne wartosci_x i wartosci_y to listy zawierajace wartosci
    zmiennej niezaleznej i odpowiadajace im wartosci zmiennej zaleznej
    wprowadzana zmienna st_wielomianu to stopien wielomianu, ktory chcemy
    uzyskac
    '''
    if len(wartosci_x) != len(wartosci_y):
        return(-1)
    st_macierzy = st_wielomianu + 1
    macierz = np.zeros(shape=(st_macierzy, st_macierzy))
    wektor = np.zeros(shape=(st_macierzy,))
    wspolczynniki = [1 for liczba in wartosci_x]
    macierz[0, 0] = sum(wspolczynniki)
    wyniki = [liczba for liczba in wartosci_y]
    wektor[0] = sum(wyniki)
    powtorzenie = 1
    koniec = 2*st_wielomianu
    while powtorzenie <= st_wielomianu:
        wspolczynniki = [liczba_1*liczba_2 for liczba_1,
                         liczba_2 in zip(wspolczynniki, wartosci_x)]
        suma_wspolczynnikow = sum(wspolczynniki)
        krok = powtorzenie
        wiersz = 0
        while krok >= 0:
            macierz[wiersz, krok] = suma_wspolczynnikow
            wiersz += 1
            krok -= 1
        wyniki = [liczba_1*liczba_2 for liczba_1,
                  liczba_2 in zip(wyniki, wartosci_x)]
        wektor[powtorzenie] = sum(wyniki)
        powtorzenie += 1
    while powtorzenie <= koniec:
        wspolczynniki = [liczba_1*liczba_2 for liczba_1,
                         liczba_2 in zip(wspolczynniki, wartosci_x)]
        suma_wspolczynnikow = sum(wspolczynniki)
        krok = koniec - powtorzenie
        wiersz = st_wielomianu - krok
        kolumna = st_wielomianu
        while krok >= 0:
            macierz[wiersz, kolumna] = suma_wspolczynnikow
            wiersz += 1
            kolumna -= 1
            krok -= 1
        powtorzenie += 1
    return(macierz, wektor)


def metoda_eliminacji(A, B):
    '''
    funkcja wyznacza wektor X z ukladu rownan A*X=B
    macierz A pomnozona przez wektor X daje macierz B
    A i B musza byc obiektami typu array
    macierz A sprowadzana jest do macierzy trojkatnej metoda eliminacji
    w kazdym kroku eliminacji wiersz bazowy posiadal na przekatnej element
    o mozliwie najwiekszej wartosci bezwzglednej
    '''
    wiersze_a, kolumny_a = np.shape(A)
    A1 = np.copy(A)
    B1 = np.copy(B)
    wiersz = 0
    while wiersz < (wiersze_a-1):
        for liczba in range(wiersz+1, wiersze_a):
            if abs(A1[liczba][wiersz]) > abs(A1[wiersz][wiersz]):
                A1[[wiersz, liczba]] = A1[[liczba, wiersz]]
                B1[wiersz], B1[liczba] = B1[liczba], B1[wiersz]
        for wartosc_1 in range(wiersz+1, wiersze_a):
            czynnik = -(A1[wartosc_1][wiersz] / A1[wiersz][wiersz])
            for wartosc_2 in range(wiersz, kolumny_a):
                A1[wartosc_1][wartosc_2] += czynnik * A1[wiersz][wartosc_2]
            B1[wartosc_1] += czynnik * B1[wiersz]
        wiersz += 1
    X = np.zeros(shape=(kolumny_a,))
    licznik = wiersze_a - 1
    while licznik >= 0:
        suma = 0
        for wartosc_3 in range(licznik+1, kolumny_a):
            suma += A1[licznik, wartosc_3] * X[wartosc_3]
        X[licznik] = (B1[licznik] - suma) / A1[licznik, licznik]
        licznik -= 1
    return(X)


def wzor_funkcji(wspolczynniki):
    '''
    funkcja wyznaczajaca wzor funkcji na podstawie wprowadzonych wspolczynnikow
    parametrem wejsciowym jest lista obliczonych wspolczynnikow rownania
    '''
    pierwszy_skladnik = f"{wspolczynniki[0]}"
    wzor = "".join(pierwszy_skladnik)
    wykladnik = 1
    for element in wspolczynniki[1:]:
        kolejny_skladnik = " "
        if element > 0:
            kolejny_skladnik += "+"
        kolejny_skladnik += f"{element}*x"
        if wykladnik > 1:
            kolejny_skladnik += f"**{wykladnik}"
        wzor += kolejny_skladnik
        wykladnik += 1
    return(wzor)


def obliczenie_wartosci(x, wspolczynniki):
    '''
    funkcja obliczajaca wartosci zmiennej zaleznej na podstawie otrzymanego
    wektora ze wspolczynnikami rownania
    parametrami wejsciowymi sa odpowiednio: lista wartosci niezaleznych oraz
    lista wyliczonych wspolczynnikow rownania
    '''
    wyniki = []
    for wartosc in x:
        wykladnik = 0
        wynik_czastkowy = 0
        for element in wspolczynniki:
            wynik_czastkowy += element*(wartosc**wykladnik)
            wykladnik += 1
        wyniki.append(wynik_czastkowy)
    return(wyniki)


def blad_sumaryczny_dopasowania(war_oczekiwane, war_rzeczywiste):
    '''
    funkcja obliczajaca sume bledow dopasowania wszystkich par obserwacji
    parametrami wejsciowymi sa odpowiednio: lista wartosci obliczonych oraz
    lista wartosci rzeczywistych zmiennej zaleznej
    '''
    bledy = [(liczba_1-liczba_2)**2 for liczba_1,
             liczba_2 in zip(war_oczekiwane, war_rzeczywiste)]
    suma_bledow = sum(bledy)
    return(suma_bledow)


def blad_sredni_na_jedna_obserwacje(suma_bledow, lista):
    '''
    funkcja obliczajaca blad sredni przypadajacy na jedna obserwacje
    parametrami wejsciowymi sa odpowiednio: blad sumaryczny dopasowania
    wszystkich obserwacji oraz lista wartosci zmiennej zaleznej lub
    niezaleznej
    '''
    blad_na_obserwacje = suma_bledow/len(lista)
    return(blad_na_obserwacje)


def blad_na_jeden_stopien_swobody(suma_bledow, lista, stopien):
    '''
    funkcja obliczajaca blad przypadajacy na jeden stopien swobody
    parametrami wejsciowymi sa odpowiednio: blad sumaryczny dopasowania
    wszystkich obserwacji, lista wartosci zmiennej zaleznej lub
    niezaleznej oraz stopien wielomianu
    '''
    blad_na_stopien = suma_bledow/(len(lista) - (stopien+1))
    return(blad_na_stopien)


def wspolczynnik_determinacji(war_rzeczywiste, war_oczekiwane):
    '''
    funkcja obliczajaca wspolczynnik determinacji dla otrzymanej funkcji
    aproksymujacej
    parametrami wejsciowymi sa odpowiednio: lista wartosci obliczonych oraz
    lista wartosci rzeczywistych zmiennej zaleznej
    '''
    srednia = mean(war_rzeczywiste)
    licznik = 0
    mianownik = 0
    for liczba_1, liczba_2 in zip(war_rzeczywiste, war_oczekiwane):
        licznik += (liczba_1 - liczba_2)**2
        mianownik += (liczba_1 - srednia)**2
    wspolczynnik = 1 - (licznik/mianownik)
    return(wspolczynnik)


def wyrazenie_funkcji(wzor):
    '''
    funkcja przeksztalca wzor funkcji podany jako string do wyrazenia
    matematycznego
    parametrem wejsciowym jest wzor zapisany jako string
    '''
    funkcja = eval(wzor)
    return(funkcja)


# wielkosci macierzy
x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 50]

# czasy obliczen
y1 = [1.391959199999998e-05, 2.721842642642595e-05, 4.5849125125124354e-05, 7.002124500000017e-05, 0.00010223666966966769, 0.00014269197300000069, 0.00019229621199999647, 0.0002512722442442443, 0.0003219795650000017, 0.0017776352862862875, 0.021273412208625872]
# liczby krokow
y2 = [14, 40, 84, 150, 242, 364, 520, 714, 950, 6500, 90750]
# wartosci bledu
y3 = [4.526846524873364e-15, 1.9802719475849116e-14, 9.081630043134478e-14, 3.2075746905062784e-13, 2.173280548724011e-13, 4.177102178919595e-13, 1.6176279954795788e-12, 6.736749867969288e-13, 1.664543966120848e-12, 1.0408019150338877e-11, 2.5069010654414576e-10]


'''
# zaleznosc czasu obliczen od wielkosci macierzy
print("Analiza czasu")
print("==========")

czas_wspolczynniki = []
czas_wzor_funkcji = []
czas_blad_sumaryczny_dopasowania = []
czas_blad_sredni_na_jedna_obserwacje = []
czas_blad_na_jeden_stopien_swobody = []
czas_wspolczynnik_determinacji = []


for stopien in range(1, 10):
    macierz_1, wektor_1 = metoda_najmniejszych_kwadratow(x, y1, stopien)

    wektor_wspolczynnikow_1 = metoda_eliminacji(macierz_1, wektor_1)
    czas_wspolczynniki.append(wektor_wspolczynnikow_1)

    wzor_funkcji_1 = wzor_funkcji(wektor_wspolczynnikow_1)
    czas_wzor_funkcji.append(wzor_funkcji_1)

    lista_wynikow_1 = obliczenie_wartosci(x, wektor_wspolczynnikow_1)

    blad_sumaryczny_dopasowania_1 = blad_sumaryczny_dopasowania(
        lista_wynikow_1, y1)
    czas_blad_sumaryczny_dopasowania.append(blad_sumaryczny_dopasowania_1)

    blad_sredni_na_jedna_obserwacje_1 = blad_sredni_na_jedna_obserwacje(
        blad_sumaryczny_dopasowania_1, x)
    czas_blad_sredni_na_jedna_obserwacje.append(
        blad_sredni_na_jedna_obserwacje_1)

    blad_na_jeden_stopien_swobody_1 = blad_na_jeden_stopien_swobody(
        blad_sumaryczny_dopasowania_1, x, stopien)
    czas_blad_na_jeden_stopien_swobody.append(blad_na_jeden_stopien_swobody_1)

    wspolczynnik_determinacji_1 = wspolczynnik_determinacji(
        y1, lista_wynikow_1)
    czas_wspolczynnik_determinacji.append(wspolczynnik_determinacji_1)


# print(czas_wspolczynniki)
# print(czas_wzor_funkcji)
# print(czas_blad_sumaryczny_dopasowania)
# print(czas_blad_sredni_na_jedna_obserwacje)
# print(czas_blad_na_jeden_stopien_swobody)
# print(czas_wspolczynnik_determinacji)


for element in range(0, 9):
    print("Stopien wielomianu:", element+1)
    print("Wspolczynniki:", czas_wspolczynniki[element])
    print("Wzor:", czas_wzor_funkcji[element])
    print("Blad sumaryczny dopasowania:",
          czas_blad_sumaryczny_dopasowania[element])
    print("Blad sredni na jedna obserwacje:",
          czas_blad_sredni_na_jedna_obserwacje[element])
    print("Blad na jeden stopien swobody:",
          czas_blad_na_jeden_stopien_swobody[element])
    print("Wspolczynnik determinacji:",
          czas_wspolczynnik_determinacji[element])
    print("==========")


x = np.linspace(0, 10, 1000000)
stopien_funkcji = 1
for element in czas_wzor_funkcji:
    plt.plot(x, wyrazenie_funkcji(element),
             label=f"stopien wielomianu: {stopien_funkcji}")
    stopien_funkcji += 1
plt.xlim([0, 10])
plt.xlabel("Stopien macierzy")
plt.ylim([-0.00001, 0.0001])
plt.ylabel("Ilosc czasu")
plt.title("Analiza czasu")
plt.legend()
plt.show()
'''


'''
# zaleznosc ilosci obliczen od wielkosci macierzy
print("Analiza ilosci obliczen")
print("==========")

kroki_wspolczynniki = []
kroki_wzor_funkcji = []
kroki_blad_sumaryczny_dopasowania = []
kroki_blad_sredni_na_jedna_obserwacje = []
kroki_blad_na_jeden_stopien_swobody = []
kroki_wspolczynnik_determinacji = []


for stopien in range(1, 10):
    macierz_2, wektor_2 = metoda_najmniejszych_kwadratow(x, y2, stopien)

    wektor_wspolczynnikow_2 = metoda_eliminacji(macierz_2, wektor_2)
    kroki_wspolczynniki.append(wektor_wspolczynnikow_2)

    wzor_funkcji_2 = wzor_funkcji(wektor_wspolczynnikow_2)
    kroki_wzor_funkcji.append(wzor_funkcji_2)

    lista_wynikow_2 = obliczenie_wartosci(x, wektor_wspolczynnikow_2)

    blad_sumaryczny_dopasowania_2 = blad_sumaryczny_dopasowania(
        lista_wynikow_2, y2)
    kroki_blad_sumaryczny_dopasowania.append(blad_sumaryczny_dopasowania_2)

    blad_sredni_na_jedna_obserwacje_2 = blad_sredni_na_jedna_obserwacje(
        blad_sumaryczny_dopasowania_2, x)
    kroki_blad_sredni_na_jedna_obserwacje.append(
        blad_sredni_na_jedna_obserwacje_2)

    blad_na_jeden_stopien_swobody_2 = blad_na_jeden_stopien_swobody(
        blad_sumaryczny_dopasowania_2, x, stopien)
    kroki_blad_na_jeden_stopien_swobody.append(blad_na_jeden_stopien_swobody_2)

    wspolczynnik_determinacji_2 = wspolczynnik_determinacji(
        y2, lista_wynikow_2)
    kroki_wspolczynnik_determinacji.append(wspolczynnik_determinacji_2)


# print(kroki_wspolczynniki)
# print(kroki_wzor_funkcji)
# print(kroki_blad_sumaryczny_dopasowania)
# print(kroki_blad_sredni_na_jedna_obserwacje)
# print(kroki_blad_na_jeden_stopien_swobody)
# print(kroki_wspolczynnik_determinacji)


for element in range(0, 9):
    print("Stopien wielomianu:", element+1)
    print("Wspolczynniki:", kroki_wspolczynniki[element])
    print("Wzor:", kroki_wzor_funkcji[element])
    print("Blad sumaryczny dopasowania:",
          kroki_blad_sumaryczny_dopasowania[element])
    print("Blad sredni na jedna obserwacje:",
          kroki_blad_sredni_na_jedna_obserwacje[element])
    print("Blad na jeden stopien swobody:",
          kroki_blad_na_jeden_stopien_swobody[element])
    print("Wspolczynnik determinacji:",
          kroki_wspolczynnik_determinacji[element])
    print("==========")


x = np.linspace(0, 100000, 1000000)
stopien_funkcji = 1
for element in kroki_wzor_funkcji:
    plt.plot(x, wyrazenie_funkcji(element),
             label=f"stopien wielomianu: {stopien_funkcji}")
    stopien_funkcji += 1
plt.xlim([0, 60])
plt.xlabel("Stopien macierzy")
plt.ylim([0, 100000])
plt.ylabel("Liczba krokow")
plt.title("Analiza ilosci obliczen")
plt.legend()
plt.show()
'''


'''
# zaleznosc wartosci bledu wektora wynikowego od wielkosci macierzy
print("Analiza bledu")
print("==========")

blad_wspolczynniki = []
blad_wzor_funkcji = []
blad_blad_sumaryczny_dopasowania = []
blad_blad_sredni_na_jedna_obserwacje = []
blad_blad_na_jeden_stopien_swobody = []
blad_wspolczynnik_determinacji = []


for stopien in range(1, 10):
    macierz_3, wektor_3 = metoda_najmniejszych_kwadratow(x, y3, stopien)

    wektor_wspolczynnikow_3 = metoda_eliminacji(macierz_3, wektor_3)
    blad_wspolczynniki.append(wektor_wspolczynnikow_3)

    wzor_funkcji_3 = wzor_funkcji(wektor_wspolczynnikow_3)
    blad_wzor_funkcji.append(wzor_funkcji_3)

    lista_wynikow_3 = obliczenie_wartosci(x, wektor_wspolczynnikow_3)

    blad_sumaryczny_dopasowania_3 = blad_sumaryczny_dopasowania(
        lista_wynikow_3, y3)
    blad_blad_sumaryczny_dopasowania.append(blad_sumaryczny_dopasowania_3)

    blad_sredni_na_jedna_obserwacje_3 = blad_sredni_na_jedna_obserwacje(
        blad_sumaryczny_dopasowania_3, x)
    blad_blad_sredni_na_jedna_obserwacje.append(
        blad_sredni_na_jedna_obserwacje_3)

    blad_na_jeden_stopien_swobody_3 = blad_na_jeden_stopien_swobody(
        blad_sumaryczny_dopasowania_3, x, stopien)
    blad_blad_na_jeden_stopien_swobody.append(blad_na_jeden_stopien_swobody_3)

    wspolczynnik_determinacji_3 = wspolczynnik_determinacji(
        y3, lista_wynikow_3)
    blad_wspolczynnik_determinacji.append(wspolczynnik_determinacji_3)


# print(blad_wspolczynniki)
# print(blad_wzor_funkcji)
# print(blad_blad_sumaryczny_dopasowania)
# print(blad_blad_sredni_na_jedna_obserwacje)
# print(blad_blad_na_jeden_stopien_swobody)
# print(blad_wspolczynnik_determinacji)


for element in range(0, 9):
    print("Stopien wielomianu:", element+1)
    print("Wspolczynniki:", blad_wspolczynniki[element])
    print("Wzor:", blad_wzor_funkcji[element])
    print("Blad sumaryczny dopasowania:",
          blad_blad_sumaryczny_dopasowania[element])
    print("Blad sredni na jedna obserwacje:",
          blad_blad_sredni_na_jedna_obserwacje[element])
    print("Blad na jeden stopien swobody:",
          blad_blad_na_jeden_stopien_swobody[element])
    print("Wspolczynnik determinacji:",
          blad_wspolczynnik_determinacji[element])
    print("==========")


x = np.linspace(0, 10, 1000000)
stopien_funkcji = 1
for element in blad_wzor_funkcji:
    plt.plot(x, wyrazenie_funkcji(element),
             label=f"stopien wielomianu: {stopien_funkcji}")
    stopien_funkcji += 1
plt.xlim([0, 10])
plt.xlabel("Stopien macierzy")
plt.ylim([-5e-11, 1e-11])
plt.ylabel("Wartosc bledu wektora wynikowego")
plt.title("Analiza wartosci bledu")
plt.legend()
plt.show()
'''
