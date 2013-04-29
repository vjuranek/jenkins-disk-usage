#!/bin/bash 

export PYTHONPATH="../lib/python:/home/vjuranek/tmp/tmp/jenkinsapi"

./tex_generate.py
cd ../tex
make
evince report.pdf &
