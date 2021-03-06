#!/bin/sh

# This script imports a MAPS database to the PyMIR3 format so you don't have to!
# Unzip a MAPS database and call this script using the data dir as parameter:
# sh import_maps.sh ../../../Downloads/MAPS_ENSTDkCl_2/ENSTDkCl/MUS/

wget http://timba.nics.unicamp.br/mir_datasets/transcription/MAPS.zip --no-check-certificate
unzip MAPS.zip

#folder=/MAPS_ENSTDkCl_2/ENSTDkCl/MUS/
#
#This is part of the old version of this script.
#if [ $# -lt 1 ]
#then
#  echo "Usage: $0 <maps directory>"
#  exit 1
#fi
#
#if [ ! -d "$1" ]
#then
#  echo "Invalid directory \"$1\"!"
#  exit 1
#fi
#
#mkdir MAPS
#mkdir MAPS/Pieces
#mkdir MAPS/Pieces/Audio
#cp "$folder"/*.wav MAPS/Pieces/Audio/
#
#mkdir MAPS/Pieces/Labels
#mkdir MAPS/Pieces/Labels/Piano
#cp "$folder"/*.txt MAPS/Pieces/Labels/Piano
#for FILE in MAPS/Pieces/Labels/Piano/*.txt
#do
#  tail -n +2 "$FILE" > /tmp/$$
#  rm "$FILE"
#  mv /tmp/$$ "$FILE"
#done
#
#mkdir MAPS/Samples
#mkdir MAPS/Samples/Audio
#mkdir MAPS/Samples/Audio/Piano
#echo "Dataset structure mounted."
#echo "Do NOT forget to add your own samples!"
