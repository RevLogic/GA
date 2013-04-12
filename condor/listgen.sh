#!/bin/sh
FILES=`ls ./files/`
rm -f ./exec/*.cir.sh
rm -f ./exec/*.job

for i in $FILES
    do

`cat > ./exec/$i.cir.sh <<EOF
#!/bin/bash
./auto_run.sh ../files/$i
EOF`

chmod u+x ./exec/*.cir.sh

CURRPATH=`pwd`
LOGPATH=$CURRPATH/logs/runs/$i
#echo $LOGPATH
mkdir -p $LOGPATH/o
mkdir -p $LOGPATH/e

CLUSTERPROC="\$(Cluster).\$(Process)"


`cat > ./exec/submit_$i.job << EOF

Universe   = vanilla
Executable = $i.cir.sh
Log        = $LOGPATH/e/$i.log
Output     = $LOGPATH/o/$i.o.$CLUSTERPROC
Error      = $LOGPATH/e/$i.e.$CLUSTERPROC
Notification = Never
Queue 10

EOF`

done



