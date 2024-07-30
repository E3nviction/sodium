#!/bin/bash

if [ "$EUID" -ne 0 ]
    then echo "You seem to be running as a non-root user. Please run as root."
    exit
fi

rm README.md
rm LICENSE
rm changelog.md
rm TODO.md
mv sodium/* .
rm sodium/ -d
rm install.sh