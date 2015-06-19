#!/bin/bash
set -o errexit

# Gets features from a directory of midi files.

database=${1%/}

if [ ! -d "$database" -o -z "$database" ]
then
  echo "'$database' isn't a directory"
  exit
fi

for name in `find "$database" -name '*.mid'`
do
    #echo ./pymir3-cl.py tool midi2score $name /tmp/$$.score
    ./pymir3-cl.py tool midi2score 0 $name /tmp/$$.score


    feats=''
    for feature in density intervals pitchclass range relativerange rhythm
    do
    thisfeat=`./pymir3-cl.py symbolic $feature /tmp/$$.score`
    feats=`echo $feats $thisfeat`
    done

echo $name $feats
done


