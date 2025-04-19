#!/bin/bash
cd "$(dirname "$0")"          # /content/tabsyn
# 2) expose your repo on PYTHONPATH
export PYTHONPATH="$PWD"

# 3) run the root entry‑point with the right flags
python3 main.py \
  --dataname tm_1804 \
  --method vae \
  --mode train \
  --gpu 0