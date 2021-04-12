#!/bin/bash -ue

FILE=$(realpath ${1})

# Z pliku yolo.csv wypisz wszystkich, których id jest liczbą nieparzystą. Wyniki zapisz na standardowe wyjście błędów.
cat ${FILE} | sed 1d | grep "^[0-9]*[1,3,5,7,9]," 1>&2

# Z pliku yolo.csv wypisz każdego, kto jest wart dokładnie $2.99 lub $5.99 lub $9.99. Nie wazne czy milionów, czy miliardów (tylko nazwisko i wartość). 
# Wyniki zapisz na standardowe wyjście błędów
cat ${FILE} | sed 1d | grep ".*\$[2,5,9]\.99[B,M]$" | cut -d',' -f3,7 1>&2

# Z pliku yolo.csv wypisz każdy numer IP, który w pierwszym i drugim oktecie ma po jednej cyfrze. Wyniki zapisz na standardowe wyjście błędów"
cat ${FILE} | sed 1d | grep -o "[0-9]\.[0-9]\.[0-9]*\.[0-9]*" > 1>&2