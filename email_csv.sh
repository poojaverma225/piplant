#!/bin/bash

the_csv="/home/piplant/piplant_data.csv"

echo "the data 4 tdy yay" | mutt -a "$the_csv" -s  "the goods have arrived" -- asappooja@gmail.com
