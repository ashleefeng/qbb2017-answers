#!/bin/bash

for file in data/*.sam
do
	samtools sort -o ${file}.bam -@ 4 ${file}
	samtools index ${file}.bam > ${file}.index
done