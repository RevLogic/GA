#!/bin/sh
DIRS=`ls initial_runs/`
echo $DIRS
for i in $DIRS; do
	echo $i
	grep 'Improvement:' initial_runs/$i/o/* > ./data/out.$i.cir.improvements.csv
done

DIRS=`ls runs/`
echo $DIRS
for i in $DIRS; do
	echo $i
	grep 'Improvement:' runs/$i/o/* > ./data/out.$i.cir.improvements.csv
done
