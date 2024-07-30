#!/bin/bash

if [ "$EUID" -ne 0 ]
    then echo "You seem to be running as a non-root user. Please run as root."
    exit
fi

mv sodium/ ../sodiumui
rm -r ../sodium
cd ..