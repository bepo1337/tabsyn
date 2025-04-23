#!/bin/bash
cd "$(dirname "$0")"          # /content/tabsyn
export PYTHONPATH="$PWD"

python3 main.py \
  --dataname tm_1804 \
  --method tabsyn \
  --mode sample \
  --save_path=tm_2304_samples.json \
  --gpu 0

