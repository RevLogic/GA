#!/bin/sh
for (( c=1; c<=2; c++ ))
do
   echo "------- Run number: $((c)) --------"
   python /home/lowr4210/GA/revsim/auto_ga.py /home/lowr4210/GA/revsim/tests/hwb9_121.real
   echo "------- End run number: $((c)) -------"
done
