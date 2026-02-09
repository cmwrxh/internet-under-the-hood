#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: ./latency_bench.sh domain"
  exit 1
fi

echo "Running latency test for $1"

ping -c 10 $1 | tee latency_output.txt

avg=$(grep 'avg' latency_output.txt | awk -F '/' '{print $5}')
echo "Average RTT: $avg ms"
