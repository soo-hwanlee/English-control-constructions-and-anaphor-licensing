#!/bin/bash

python analyze_results.py --baseline ../output/obj_baseline.csv --distractor ../output/obj_distractor.csv --ungrammatical ../output/obj_ungrammatical.csv > ../results/object_control.csv
python analyze_results.py --baseline ../output/subj_baseline.csv --distractor ../output/subj_distractor.csv --ungrammatical ../output/subj_ungrammatical.csv > ../results/subject_control.csv

python analyze_results.py --baseline ../output/subj_intrans_grammatical.csv --distractor ../output/subj_intrans_grammatical.csv --ungrammatical ../output/subj_intrans_ungrammatical.csv > ../results/subject_intransitive.csv


python analyze_results.py --baseline ../output/obj_baseline.gpt2-xl.csv --distractor ../output/obj_distractor.gpt2-xl.csv --ungrammatical ../output/obj_ungrammatical.gpt2-xl.csv > ../results/object_control.gpt2-xl.csv
python analyze_results.py --baseline ../output/subj_baseline.gpt2-xl.csv --distractor ../output/subj_distractor.gpt2-xl.csv --ungrammatical ../output/subj_ungrammatical.gpt2-xl.csv > ../results/subject_control.gpt2-xl.csv
python analyze_results.py --baseline ../output/subj_intrans_grammatical.gpt2-xl.csv --distractor ../output/subj_intrans_grammatical.gpt2-xl.csv --ungrammatical ../output/subj_intrans_ungrammatical.gpt2-xl.csv > ../results/subject_intransitive.gpt2-xl.csv
