#!/bin/bash

d=day$1
mkdir -p $d && cd $d && touch $d.py input.txt input2.txt answers
echo "with open('day$1/input.txt', 'r') as f:" > $d.py 
echo "  data = f.read()" >> $d.py
exit 0