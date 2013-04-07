#!/bin/sh
for (( c=1; c<=102; c++ ))
do
   echo "------- Run number: $((c)) --------"
   python /home/lowr4210/GA/revsim/auto_ga.py /home/lowr4210/GA/revsim/tests/urf4_187.real
   echo "------- End run number: $((c)) -------"
done
