#!/usr/bin/bash
cp deg2rad.exe tests/
python -m unittest -v tests/test_deg2rad.py
rm tests/deg2rad.exe