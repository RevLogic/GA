#!/bin/sh
FILES=`ls ./files/`
for i in $FILES
    do
        echo "#!/bin/bash" >> ./exec/$i.cir.sh
        echo "./auto_run.sh ../files/$i" >> ./exec/$i.cir.sh
done

