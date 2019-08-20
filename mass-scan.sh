#!/usr/bin/env bash
mkdir -p /zap/wiki/scan-results

while read line; do
  ./mass-scan-wrapper.sh $line
done < /zap/wiki/target.list

./mass-score.py
