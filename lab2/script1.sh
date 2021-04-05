#!/bin/bash -eu

CATALOG_MISSING=55


DIR_1=$(realpath ${1})
DIR_2=$(realpath ${2})

if [[ ! -d ${DIR_1} ]] || [[ ! -d ${DIR_2} ]]; then
    exit "${CATALOG_MISSING}"
fi

for ITEM in $(ls ${DIR_1}); do
    if [[ -d ${DIR_1}/${ITEM} ]]; then
        echo "${ITEM} - it's a catalog"
        ln -s ${DIR_1}/${ITEM} ${DIR_2}/${ITEM}_ln
    elif [[ -L ${DIR_1}/${ITEM} ]]; then
        echo "${ITEM} - it's a symbolic link"
    elif [[ -f ${DIR_1}/${ITEM} ]]; then
        echo "${ITEM} - it's a regular file"
        ln -s ${DIR_1}/${ITEM} ${DIR_2}/${ITEM%.*}_ln.${ITEM##*.}
    fi
done

exit 0
