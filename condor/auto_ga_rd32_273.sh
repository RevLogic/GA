#!/bin/sh
for (( c=1; c<=102; c++ ))
do
   echo "------- Run number: $((c)) --------"
   python /home/lowr4210/GA/revsim/auto_ga.py /home/lowr4210/GA/revsim/tests/rd32_273.real
   echo "------- End run number: $((c)) -------"
done
