#!/bin/bash

while true  
do  
    for channel in {1..14}
    do
        iwconfig wlan1 channel $channel
        sleep 0.1s
    done
done  
