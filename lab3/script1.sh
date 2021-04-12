#!/bin/bash -ue

FILE=$(realpath ${1})

# Znajdź w pliku access_log zapytania, które mają frazę ""denied"" w linku
cat ${FILE} | grep "/denied"

# Znajdź w pliku access_log zapytania typu POST
cat ${FILE} | grep "\"POST"

# Znajdź w pliku access_log zapytania wysłane z IP: 64.242.88.10
cat ${FILE} | grep "^64\.242\.88\.10 "

# Znajdź w pliku access_log wszystkie zapytania NIEWYSŁANE z adresu IP tylko z FQDN
cat ${FILE} | grep "^[a-zA-Z]"

# Znajdź w pliku access_log unikalne zapytania typu DELETE
cat ${FILE} | grep "\"DELETE" | sort -u

# Znajdź unikalnych 10 adresów IP w access_log"
cat ${FILE} | grep -o "[0-9]*\.[0-9]*\.[0-9]*\.[0-9]* " | sort -u | head -n 10