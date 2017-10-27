#!/bin/bash

for file in data/*.fastq
do
	bowtie2 -x data/chr19_idx -U ${file} -S ${file}.sam
done