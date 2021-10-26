#!/usr/bin/env bash

# Create a directory ./monitoring if it does not exist
if [ ! -d "./monitoring" ]; then
    mkdir ./monitoring
fi
FILE_LOG="./monitoring/agent.log"

while true; do
    if [ -e "tmp" ]; then
        echo "$(date +%s) $(du -s tmp | awk '{print $1}')" >>$FILE_LOG
    fi
    sleep 1
done
