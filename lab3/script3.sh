#!/bin/bash -ue

DIR=$(realpath ${1})

# We wszystkich plikach w katalogu ‘groovies’ zamień $HEADER$ na /temat/
for ITEM in $(ls ${DIR}); do
    echo "$(sed -r 's|\$HEADER\$|/temat/|g' ${DIR}/${ITEM})" > ${DIR}/${ITEM}
done

# We wszystkich plikach w katalogu ‘groovies’ po każdej linijce z 'class' dodać '  String marker = '/!@$%/''
for ITEM in $(ls ${DIR}); do
   echo "$(cat ${DIR}/${ITEM} | sed  '/class/ a String marker = \x27/!@$%/\x27')" > ${DIR}/${ITEM}
done

# We wszystkich plikach w katalogu ‘groovies’ usuń linijki zawierające frazę 'Help docs:'"
for ITEM in $(ls ${DIR}); do
    echo "$(sed '/.*Help docs:.*/d' ${DIR}/${ITEM})" > ${DIR}/${ITEM}
done