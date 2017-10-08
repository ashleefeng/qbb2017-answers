#!/bin/bash

for file in ./gwas/*.qassoc
do
	./02-manhattan.py ${file} ${file}.png
done