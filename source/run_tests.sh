#!/usr/bin/env bash

# File: run_tests.sh
# Written By: Luis Moraguez
# Description: Automatically will run all unit tests located in the tests/ directory
# Usage: ./run_tests.sh

$PWD/python3-virtualenv/bin/python -m unittest discover -v tests/
