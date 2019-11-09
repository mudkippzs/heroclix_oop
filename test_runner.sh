#!/bin/bash
while True;do
	sleep $1
	coverage erase
	echo "Deciminute Test Runner @ $(date +%H:%M:%S/%m-%d-%y)"
	echo "======================"
	for python_file in *_tests.py;do
		echo "TESTING: $python_file"		
		coverage run $python_file && mv .coverage .coverage.$python_file
	done
	echo "======================"
	coverage combine .coverage*
	coverage report -m
done