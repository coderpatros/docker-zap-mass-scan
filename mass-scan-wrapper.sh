#!/usr/bin/env bash

date=`date +%F`
mkdir -p "wiki/scan-results/$1"
results_filename="wiki/scan-results/$1/$date"

cmd="./zap-full-scan.py -j -l PASS -t https://$1/ -d"

echo $cmd
$cmd > $results_filename

if [ ! -s $results_filename ]
then
  echo "Results file is empty :( $results_filename"
  # Delete it otherwise it will look like everything passed:/
  rm $results_filename
fi

# Ensure ZAP has completely shut down, otherwise it can corrupt the db of the next run
sleep 5 