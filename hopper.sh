#!/bin/bash

while true  
do  
    for channel in {1..13}
    do
        sudo iwconfig wlan1 channel $channel
        sleep 0.1s
    done
done  
