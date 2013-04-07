#!/bin/sh
#for (( c=1; c<=102; c++ ))
for (( c=1; c<=102; c++ ))
do
   echo "------- Run number: $((c)) --------"
   python /home/lowr4210/GA/revsim/gsym6.py
   echo "------- End run number: $((c)) -------"
done
