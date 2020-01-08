#!/bin/bash

sudo ifconfig wlan1 down
sudo iwconfig wlan1 mode Monitor
sudo ifconfig wlan1 up

