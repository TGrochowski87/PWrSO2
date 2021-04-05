#!/bin/bash -eu

CATALOG_MISSING=55
FILE_MISSING=66

DIR=$(realpath ${1})
FILE=$(realpath ${2})

if [[ ! -d ${DIR} ]]; then
    exit "${CATALOG_MISSING}"
fi

if [[ ! -f ${FILE} ]]; then
    exit "${FILE_MISSING}"
fi

for ITEM in $(ls ${DIR}); do
    if [[ -L ${DIR}/${ITEM} ]] && [[ ! -e ${DIR}/${ITEM} ]]; then
        echo "${ITEM} $(date --iso-8601)" >> ${FILE}
        rm ${DIR}/${ITEM}
    fi
done