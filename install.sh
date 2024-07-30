#!/bin/bash

if [ "$EUID" -ne 0 ]
    then echo "You seem to be running as a non-root user. Please run as root."
    exit
fi

echo "installing sodium..."
rm README.md > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Error occurred while removing README.md"
fi
rm LICENSE > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Error occurred while removing LICENSE"
fi
rm changelog.md > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Error occurred while removing changelog.md"
fi
rm TODO.md > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Error occurred while removing TODO.md"
fi
mv sodium/* . > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Error occurred while moving files"
fi
rm -r sodium > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Error occurred while removing sodium folder"
fi
echo "successfully installed sodium"
rm install.sh > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Error occurred while removing install.sh"
fi