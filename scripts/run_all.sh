#!/bin/bash
set -e
cd "$(dirname "$0")/.."
python3 src/verify_claims.py
python3 src/market_benchmark.py
python3 src/hidden_patterns.py
echo "ALL BENCHMARKS DONE - see benchmarks/"
