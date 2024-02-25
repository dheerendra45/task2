#!/bin/bash

printdate() {
    date
}

for i in "modified"/*; do
    if [ -f "$i" ]; then
        echo "$(printdate)" >> "$i"
	printdate
        echo " '$i'."
    fi
done
~#it will first show current date and time than file name which found in modified directory 
