#!/bin/bash

sudo ifdown wlan1
sudo iwconfig wlan1 mode Monitor
sudo ifup wlan1

