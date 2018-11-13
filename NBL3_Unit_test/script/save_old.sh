#!/bin/bash
source ~/.profile
echo 'start save old event list'
scsolsshow -NAlmServer -lEventList -r > old_event.txt
echo 'end save old event list'
