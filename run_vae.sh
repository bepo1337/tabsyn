#!/bin/bash
cd "$(dirname "$0")"          # /content/tabsyn
export PYTHONPATH="$PWD"

python3 main.py \
  --dataname tm_1804 \
  --method vae \
  --mode train \
  --gpu 0