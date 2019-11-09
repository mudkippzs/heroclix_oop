#!/bin/bash
while True;do
	sleep $1
	echo "Deciminute Test Runner @ $(date +%H:%M:%S/%m-%d-%y)"
	for python_file in *_tests.py;do
		echo "======================"
		echo "TESTING: $python_file"
		echo "----------------------"		
		coverage run $python_file && coverage report -m
		echo "======================"
	done
done