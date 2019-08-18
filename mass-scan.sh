#!/usr/bin/env bash
while read line; do
  ./mass-scan-wrapper.sh $line
done < /zap/wiki/target.list

./mass-score.py
