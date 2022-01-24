#!/bin/bash

# Usage
# Run this script at the root of individual portrait pictures such as:
# ~/Private/SFJS/2021Yearbook/Pictures/ClassScreenshots/4.srgb.png
#

set -o xtrace

python3 $(dirname "$0")/zmimg.py -a build -i "SJMH/SJM1-1/*_s??.*.png" -o classphoto.sj_7_1.png
python3 $(dirname "$0")/zmimg.py -a build -i "SJMH/SJM1-2/*_s??.*.png" -o classphoto.sj_7_2.png
python3 $(dirname "$0")/zmimg.py -a build -i "SJMH/SJM1-3/*_s??.*.png" -o classphoto.sj_7_3.png
python3 $(dirname "$0")/zmimg.py -a build -i "SJMH/SJM1-4/*_s??.*.png" -o classphoto.sj_7_4.png

python3 $(dirname "$0")/zmimg.py -a build -i "SJMH/SJM2-1/*_s??.*.png" -o classphoto.sj_8_1.png
python3 $(dirname "$0")/zmimg.py -a build -i "SJMH/SJM2-2/*_s??.*.png" -o classphoto.sj_8_2.png
python3 $(dirname "$0")/zmimg.py -a build -i "SJMH/SJM2-3/*_s??.*.png" -o classphoto.sj_8_3.png
python3 $(dirname "$0")/zmimg.py -a build -i "SJMH/SJM2-4/*_s??.*.png" -o classphoto.sj_8_4.png

python3 $(dirname "$0")/zmimg.py -a build -i "SJMH/SJM3-1/*_s??.*.png" -o classphoto.sj_9_1.png
python3 $(dirname "$0")/zmimg.py -a build -i "SJMH/SJM3-2/*_s??.*.png" -o classphoto.sj_9_2.png
python3 $(dirname "$0")/zmimg.py -a build -i "SJMH/SJM3-3/*_s??.*.png" -o classphoto.sj_9_3.png

python3 $(dirname "$0")/zmimg.py -a build -i "SJMH/SJH1-1/*_s??.*.png" -o classphoto.sj_10_1.png
python3 $(dirname "$0")/zmimg.py -a build -i "SJMH/SJH1-2/*_s??.*.png" -o classphoto.sj_10_2.png

python3 $(dirname "$0")/zmimg.py -a build -i "SJMH/SJH2-1/*_s??.*.png" -o classphoto.sj_11_1.png
python3 $(dirname "$0")/zmimg.py -a build -i "SJMH/SJH2-2/*_s??.*.png" -o classphoto.sj_11_2.png

