#!/bin/bash
cd "$(dirname "$0")"          # ensure we’re in /content/tabsyn
export PYTHONPATH="$PWD"      # add repo root to module path
python3 -m tabsyn.vae.main    \
  --dataname tm_1804           \
  --method vae                 \
  --mode train