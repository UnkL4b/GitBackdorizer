#!/bin/bash

echo "Commit into repo..."
printf "Username for 'https://github.com': "
read EMAIL
stty -echo
printf "Password for 'https://$EMAIL@github.com':"
read PASSWORD
stty echo
printf "\n"
echo $EMAIL $PASSWORD
