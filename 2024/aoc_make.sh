#!/bin/bash

# Check if the correct number of parameters is provided
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <day_number>"
  exit 1
fi

DAY_NUMBER=$1
DIRECTORY="./day$DAY_NUMBER"

# Create the directory
mkdir -p "$DIRECTORY"

# Create the files
touch "$DIRECTORY/README.md"
touch "$DIRECTORY/day${DAY_NUMBER}part1.py"
touch "$DIRECTORY/day${DAY_NUMBER}part2.py"
touch "$DIRECTORY/input${DAY_NUMBER}.txt"

echo "Directory and files created successfully in $DIRECTORY"
