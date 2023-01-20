#!/bin/bash

for a in $(ls src/sources)
do
	alias "${a%.*}"='python 'src/sources/$a
done
