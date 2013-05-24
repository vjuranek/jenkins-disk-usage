#!/bin/bash

find $1  -name "*log" -type f -ctime +2 -print0 | xargs -0 gzip
