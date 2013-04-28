#!/bin/bash 

./tex_generate.py
cd ../tex
make
evince report.pdf &
