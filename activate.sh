#!/bin/bash

export PYTHONPATH="$PYTHONPATH:$PWD/src"
export HOST="0.0.0.0"
export PORT="8080"

stop_server(){
	# test if server is running
	if test -f PID
       	then
		kill -9 $(cat PID)
		rm PID
	fi
}

run_server(){
	stop_server

	python src/server.py &
	echo $! > PID	
}


unset_alias(){
	unalias out

	# unset alias for sources
	for a in $(ls src/sources)
	do
		unalias "${a%.*}"
	done

	# unset alias for geometric functions
	for a in $(ls src/geometry)
	do
		unalias "${a%.*}"
	done
}

set_alias(){
	alias out='python src/out.py'

	# set alias for sources
	for a in $(ls src/sources)
	do
		alias "${a%.*}"='python 'src/sources/$a
	done

	# set alias for geometric functions
	for a in $(ls src/geometry)
	do
		alias "${a%.*}"='python 'src/geometry/$a
	done
}


deactivate(){
	stop_server
	unset_alias
}

run_server
set_alias

# source again to activate
unset -f run_server
unset -f set_alias
