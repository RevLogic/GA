#!/bin/sh
FILE=$1

for (( d=1; d<=10; d++ ))
#for (( d=1; d<=1; d++ ))
do
  echo " |*******^*^*^******************---******---******************^*^*^*******| "
  echo " |**************** File=<$FILE> Set #$((d)) *******************| "
  echo " |*******^*^*^******************---******---******************^*^*^*******| "

  IPOP=`shuf -i 50-1000 -n 1`
  IMUT=`shuf -i 5-10 -n 1`
  SMUT=`shuf -i 2-5 -n 1`
  CIMG=`shuf -i 10-25 -n 1`
  MRPM=`shuf -i 1-10 -n 1`

  echo " |->>>>>> --- Set #$((d)) variables: --- <<<<<<| "
  echo " | init_population_size =            $IPOP  "
  echo " | initial_population_mutations =    $IMUT  "
  echo " | subsequent_population_mutations = $SMUT  "
  echo " | cost_improvement_goal =           $CIMG  "
  echo " | max_removals_per_mutation =       $MRPM  "
  echo

  #for (( c=1; c<=102; c++ ))
  for (( c=1; c<=50; c++ ))
  do
     echo " |------- <$FILE> Set #$((d))  Run #$((c)) --------| "
     #python /home/lowr4210/GA/revsim/auto_ga.py /home/lowr4210/GA/revsim/tests/rd32_273.real $IPOP $IMUT $SMUT $CIMG $MRPM
     #python ../revsim/auto_ga.py ../revsim/tests/rd32_273.real $IPOP $IMUT $SMUT $CIMG $MRPM
     python ../../revsim/auto_ga.py $FILE $IPOP $IMUT $SMUT $CIMG $MRPM
   
     echo " |------- End run number: $((c)) -------|"
  done
done
