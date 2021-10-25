#!/usr/bin/env bash

if [ ! -d "./monitoring" ]; then
    mkdir -p "./monitoring"
fi
FILE_LOG="./monitoring/agent.log"

while true; do
    if [ -e "tmp" ]; then
        echo "$(date +%s) $(du -s tmp | awk '{print $1}')" >>$FILE_LOG
    fi
    sleep 1
done
