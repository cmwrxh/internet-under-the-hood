#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: ./latency_bench.sh domain"
  exit 1
fi

ping -n 5 $1
