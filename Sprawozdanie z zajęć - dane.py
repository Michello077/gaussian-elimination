#!/usr/bin/env python
# coding: utf-8

import numpy as np
from time import perf_counter
from statistics import mean


def metoda_eliminacji(A, B):
    '''
    funkcja wyznacza wektor X z ukladu rownan A*X=B
    macierz A pomnozona przez wektor X daje macierz B
    A i B musza byc obiektami typu array
    macierz A sprowadzana jest do macierzy trojkatnej metoda eliminacji
    '''
    wiersze_a, kolumny_a = np.shape(A)
    wiersze_b = np.shape(B)[0]
    if kolumny_a != wiersze_b:
        return(-1, None)
    kroki = 0
    wiersz = 0
    while wiersz < (wiersze_a-1):
        if A[wiersz][wiersz] == 0:
            return(-2, None)
        for wartosc_1 in range(wiersz+1, wiersze_a):
            czynnik = -(A[wartosc_1][wiersz] / A[wiersz][wiersz])
            kroki += 2
            for wartosc_2 in range(wiersz, kolumny_a):
                A[wartosc_1][wartosc_2] += czynnik * A[wiersz][wartosc_2]
                kroki += 2
            B[wartosc_1] += czynnik * B[wiersz]
            kroki += 2
        wiersz += 1
    X = np.zeros(shape=(kolumny_a,))
    licznik = wiersze_a - 1
    while licznik >= 0:
        suma = 0
        for wartosc_3 in range(licznik+1, kolumny_a):
            suma += A[licznik, wartosc_3] * X[wartosc_3]
            kroki += 2
        if A[licznik, licznik] == 0:
            return(-3, None)
        X[licznik] = (B[licznik] - suma) / A[licznik, licznik]
        kroki += 2
        licznik -= 1
    return(X, kroki)


def norma_euklidesowa(wektor):
    '''
    funkcja oblicza norme euklidesowa z otrzymanego wektora
    '''
    suma = 0.0
    for element in wektor:
        suma = suma + element**2
    return(suma**0.5)


'''
# przygotowanie zbioru danych
czasy = []
obliczenia = []
bledy = []


# macierz 2x2
czasy_2 = []
obliczenia_2 = []
bledy_2 = []

for i in range(1000):
    A = np.random.randint(1, 100, size=(2, 2)).astype("float")
    B = np.random.randint(1, 100, size=(2, 1)).astype("float")

    A_copy = A
    B_copy = B

    start = perf_counter()
    X, kroki = metoda_eliminacji(A, B)
    end = perf_counter()

    if kroki is not None:
        czas = end-start
        czasy_2.append(czas)
        obliczenia_2.append(kroki)

        B2 = np.dot(A_copy, X)

        wektor = (B_copy.flatten() - B2)
        blad = norma_euklidesowa(wektor)
        bledy_2.append(blad)

czasy.append(mean(czasy_2))
obliczenia.append(mean(obliczenia_2))
bledy.append(mean(bledy_2))


# macierz 3x3
czasy_3 = []
obliczenia_3 = []
bledy_3 = []

for i in range(1000):
    A = np.random.randint(1, 100, size=(3, 3)).astype("float")
    B = np.random.randint(1, 100, size=(3, 1)).astype("float")

    A_copy = A
    B_copy = B

    start = perf_counter()
    X, kroki = metoda_eliminacji(A, B)
    end = perf_counter()

    if kroki is not None:
        czas = end-start
        czasy_3.append(czas)
        obliczenia_3.append(kroki)

        B3 = np.dot(A_copy, X)

        wektor = (B_copy.flatten() - B3)
        blad = norma_euklidesowa(wektor)
        bledy_3.append(blad)

czasy.append(mean(czasy_3))
obliczenia.append(mean(obliczenia_3))
bledy.append(mean(bledy_3))


# macierz 4x4
czasy_4 = []
obliczenia_4 = []
bledy_4 = []

for i in range(1000):
    A = np.random.randint(1, 100, size=(4, 4)).astype("float")
    B = np.random.randint(1, 100, size=(4, 1)).astype("float")

    A_copy = A
    B_copy = B

    start = perf_counter()
    X, kroki = metoda_eliminacji(A, B)
    end = perf_counter()

    if kroki is not None:
        czas = end-start
        czasy_4.append(czas)
        obliczenia_4.append(kroki)

        B4 = np.dot(A_copy, X)

        wektor = (B_copy.flatten() - B4)
        blad = norma_euklidesowa(wektor)
        bledy_4.append(blad)

czasy.append(mean(czasy_4))
obliczenia.append(mean(obliczenia_4))
bledy.append(mean(bledy_4))


# macierz 5x5
czasy_5 = []
obliczenia_5 = []
bledy_5 = []

for i in range(1000):
    A = np.random.randint(1, 100, size=(5, 5)).astype("float")
    B = np.random.randint(1, 100, size=(5, 1)).astype("float")

    A_copy = A
    B_copy = B

    start = perf_counter()
    X, kroki = metoda_eliminacji(A, B)
    end = perf_counter()

    if kroki is not None:
        czas = end-start
        czasy_5.append(czas)
        obliczenia_5.append(kroki)

        B5 = np.dot(A_copy, X)

        wektor = (B_copy.flatten() - B5)
        blad = norma_euklidesowa(wektor)
        bledy_5.append(blad)

czasy.append(mean(czasy_5))
obliczenia.append(mean(obliczenia_5))
bledy.append(mean(bledy_5))


# macierz 6x6
czasy_6 = []
obliczenia_6 = []
bledy_6 = []

for i in range(1000):
    A = np.random.randint(1, 100, size=(6, 6)).astype("float")
    B = np.random.randint(1, 100, size=(6, 1)).astype("float")

    A_copy = A
    B_copy = B

    start = perf_counter()
    X, kroki = metoda_eliminacji(A, B)
    end = perf_counter()

    if kroki is not None:
        czas = end-start
        czasy_6.append(czas)
        obliczenia_6.append(kroki)

        B6 = np.dot(A_copy, X)

        wektor = (B_copy.flatten() - B6)
        blad = norma_euklidesowa(wektor)
        bledy_6.append(blad)

czasy.append(mean(czasy_6))
obliczenia.append(mean(obliczenia_6))
bledy.append(mean(bledy_6))


# macierz 7x7
czasy_7 = []
obliczenia_7 = []
bledy_7 = []

for i in range(1000):
    A = np.random.randint(1, 100, size=(7, 7)).astype("float")
    B = np.random.randint(1, 100, size=(7, 1)).astype("float")

    A_copy = A
    B_copy = B

    start = perf_counter()
    X, kroki = metoda_eliminacji(A, B)
    end = perf_counter()

    if kroki is not None:
        czas = end-start
        czasy_7.append(czas)
        obliczenia_7.append(kroki)

        B7 = np.dot(A_copy, X)

        wektor = (B_copy.flatten() - B7)
        blad = norma_euklidesowa(wektor)
        bledy_7.append(blad)

czasy.append(mean(czasy_7))
obliczenia.append(mean(obliczenia_7))
bledy.append(mean(bledy_7))


# macierz 8x8
czasy_8 = []
obliczenia_8 = []
bledy_8 = []

for i in range(1000):
    A = np.random.randint(1, 100, size=(8, 8)).astype("float")
    B = np.random.randint(1, 100, size=(8, 1)).astype("float")

    A_copy = A
    B_copy = B

    start = perf_counter()
    X, kroki = metoda_eliminacji(A, B)
    end = perf_counter()

    if kroki is not None:
        czas = end-start
        czasy_8.append(czas)
        obliczenia_8.append(kroki)

        B8 = np.dot(A_copy, X)

        wektor = (B_copy.flatten() - B8)
        blad = norma_euklidesowa(wektor)
        bledy_8.append(blad)

czasy.append(mean(czasy_8))
obliczenia.append(mean(obliczenia_8))
bledy.append(mean(bledy_8))


# macierz 9x9
czasy_9 = []
obliczenia_9 = []
bledy_9 = []

for i in range(1000):
    A = np.random.randint(1, 100, size=(9, 9)).astype("float")
    B = np.random.randint(1, 100, size=(9, 1)).astype("float")

    A_copy = A
    B_copy = B

    start = perf_counter()
    X, kroki = metoda_eliminacji(A, B)
    end = perf_counter()

    if kroki is not None:
        czas = end-start
        czasy_9.append(czas)
        obliczenia_9.append(kroki)

        B9 = np.dot(A_copy, X)

        wektor = (B_copy.flatten() - B9)
        blad = norma_euklidesowa(wektor)
        bledy_9.append(blad)

czasy.append(mean(czasy_9))
obliczenia.append(mean(obliczenia_9))
bledy.append(mean(bledy_9))


# macierz 10x10
czasy_10 = []
obliczenia_10 = []
bledy_10 = []

for i in range(1000):
    A = np.random.randint(1, 100, size=(10, 10)).astype("float")
    B = np.random.randint(1, 100, size=(10, 1)).astype("float")

    A_copy = A
    B_copy = B

    start = perf_counter()
    X, kroki = metoda_eliminacji(A, B)
    end = perf_counter()

    if kroki is not None:
        czas = end-start
        czasy_10.append(czas)
        obliczenia_10.append(kroki)

        B10 = np.dot(A_copy, X)

        wektor = (B_copy.flatten() - B10)
        blad = norma_euklidesowa(wektor)
        bledy_10.append(blad)

czasy.append(mean(czasy_10))
obliczenia.append(mean(obliczenia_10))
bledy.append(mean(bledy_10))


# macierz 20x20
czasy_20 = []
obliczenia_20 = []
bledy_20 = []

for i in range(1000):
    A = np.random.randint(1, 100, size=(20, 20)).astype("float")
    B = np.random.randint(1, 100, size=(20, 1)).astype("float")

    A_copy = A
    B_copy = B

    start = perf_counter()
    X, kroki = metoda_eliminacji(A, B)
    end = perf_counter()

    if kroki is not None:
        czas = end-start
        czasy_20.append(czas)
        obliczenia_20.append(kroki)

        B20 = np.dot(A_copy, X)

        wektor = (B_copy.flatten() - B20)
        blad = norma_euklidesowa(wektor)
        bledy_20.append(blad)

czasy.append(mean(czasy_20))
obliczenia.append(mean(obliczenia_20))
bledy.append(mean(bledy_20))


# macierz 50x50
czasy_50 = []
obliczenia_50 = []
bledy_50 = []

for i in range(1000):
    A = np.random.randint(1, 100, size=(50, 50)).astype("float")
    B = np.random.randint(1, 100, size=(50, 1)).astype("float")

    A_copy = A
    B_copy = B

    start = perf_counter()
    X, kroki = metoda_eliminacji(A, B)
    end = perf_counter()

    if kroki is not None:
        czas = end-start
        czasy_50.append(czas)
        obliczenia_50.append(kroki)

        B50 = np.dot(A_copy, X)

        wektor = (B_copy.flatten() - B50)
        blad = norma_euklidesowa(wektor)
        bledy_50.append(blad)

czasy.append(mean(czasy_50))
obliczenia.append(mean(obliczenia_50))
bledy.append(mean(bledy_50))


# zbior danych
print(czasy)
print(obliczenia)
print(bledy)
'''
