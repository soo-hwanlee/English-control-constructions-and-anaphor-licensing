#!/bin/bash


for f in ../stimuli/*.txt
do
out_f="../output/$(basename $f .txt)"
python compute_perplexity.py $f $out_f.csv
done
