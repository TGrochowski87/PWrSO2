#!/bin/bash -eu

CATALOG_MISSING=55

DIR=$(realpath ${1})

if [[ ! -d ${DIR} ]]; then
    exit "${CATALOG_MISSING}"
fi

for ITEM in $(ls ${DIR}); do
    if [[ -f ${DIR}/${ITEM} ]] && [[ ${ITEM##*.} == "bak" ]]; then
        chmod uo-w ${DIR}/${ITEM}
    fi

    if [[ -d ${DIR}/${ITEM} ]] && [[ ${ITEM##*.} == "bak" ]]; then
        chmod ug-r ${DIR}/${ITEM}
    fi

    if [[ -d ${DIR}/${ITEM} ]] && [[ ${ITEM##*.} == "tmp" ]]; then
        chmod -R ugo-w ${DIR}/${ITEM}
    fi

    if [[ -d ${DIR}/${ITEM} ]] && [[ ${ITEM##*.} == "txt" ]]; then
        chmod ugo-rwx ${DIR}/${ITEM}
        chmod u+r ${DIR}/${ITEM}
        chmod g+w ${DIR}/${ITEM}
        chmod o+x ${DIR}/${ITEM}
    fi

    if [[ -d ${DIR}/${ITEM} ]] && [[ ${ITEM##*.} == "exe" ]]; then
        chmod ugo+x ${DIR}/${ITEM}
        chmod u+s ${DIR}/${ITEM}
    fi
done