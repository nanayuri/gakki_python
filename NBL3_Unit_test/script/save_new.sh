#!/bin/bash
source ~/.profile
echo 'start save new event list'
scsolsshow -NAlmServer -lEventList -r > new_event.txt
echo 'end save new event list'
