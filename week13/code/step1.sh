#!/bin/bash

for file in ~/qbb2017-answers/week13/week13_data/KRAKEN/*.kraken
do
	./step1.py ${file} 
done

for file in ~/qbb2017-answers/week13/week13_data/KRAKEN/*.krona
do
	ktImportText -o ${file}.html ${file} 
done
