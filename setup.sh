#!/bin/bash

# Checking for python3 install
check_python3() {
    #using dpkg to check if python is installed
    local python3Status=$(dpkg-query -W python3 | grep "install ok installed" &> /dev/null; echo $?)
}

    if $python3Status == 0
        then
            echo "Python3 is installed!"
        else
            echo "Python3 is not installed!"

echo "Setup for doorknob"
check_python3