#!/bin/bash

for file in ./*.fastq.sam
do
	samtools sort -o "${file}.bam" ${file}
	samtools index "${file}.bam"
done