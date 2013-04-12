#!/bin/sh
for (( c=1; c<=102; c++ ))
do
   echo "------- Run number: $((c)) --------"
   python /home/lowr4210/GA/revsim/auto_ga.py /home/lowr4210/GA/revsim/tests/decod24-v3_45.real
   echo "------- End run number: $((c)) -------"
done
