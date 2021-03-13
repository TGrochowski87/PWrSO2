#!/bin/bash

SOURCE_DIR=${1:-"lab_uno"}
RM_LIST=${2:-"lab_uno/2remove"}
TARGET_DIR=${3:-"bakap"}

if [[ ! -d ${TARGET_DIR} ]]; then
    mkdir ${TARGET_DIR}
fi

for ITEM in $(cat ${RM_LIST}); do
    if [[ -f ${SOURCE_DIR}/${ITEM} ]]; then
        rm ${SOURCE_DIR}/${ITEM}
    fi
done

for ITEM in $(ls ${SOURCE_DIR}/); do
    if [[ -f ${SOURCE_DIR}/${ITEM} ]]; then
        mv ${SOURCE_DIR}/${ITEM} ${TARGET_DIR}
    elif [[ -d ${SOURCE_DIR}/${ITEM} ]]; then
        cp -r ${SOURCE_DIR}/${ITEM} ${TARGET_DIR}
    fi
done

#mv ${TARGET_DIR}/2remove ${SOURCE_DIR}

COUNTER=$(ls ${SOURCE_DIR} | wc -w)

if [[ ${COUNTER} -gt 0 ]]; then
    echo "jeszcze cos zostalo"
else
    echo "tu byl Kononowicz"
fi

if [[ ${COUNTER} -ge 2 ]]; then
    echo "zostaly co najmniej 2 pliki"
fi

if [[ ${COUNTER} -gt 4 ]]; then
    echo "zostalo wiecej niz 4 pliki"
fi

if [[ ${COUNTER} -ge 2 ]] && [[ ${COUNTER} -le 4 ]]; then
    echo "zostaly co najmniej 2 pliki ale nie wiecej niz 4"
fi

for ITEM in $(ls ${TARGET_DIR}/); do
    if [[ -f ${TARGET_DIR}/${ITEM} ]]; then
        chmod -w ${TARGET_DIR}/${ITEM}
    fi
done

DATE=$(date "+%Y-%m-%d")

zip -r bakap_${DATE} ${TARGET_DIR}
