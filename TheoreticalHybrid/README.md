# Advent of Code 2023
I don't use python on a regular basis but I've been using AoC as a wlay to expand my knowledge on it each year, so some of these solutions will look like a confusing mix of good and bad. Like a nice steak dinner served with kraft mac and cheese made by your nephew.

## Directory Structure
There's a directory for each day, and in each directory there's main.py and a file for each sample input and puzzle input. If the puzzle throws me for a loop I may have either multiple subdirectories for part 1/2, or separate scripts (part1.py/part2.py).

## File Structure
At the top of main.py there are 3 flags that will change how the execution behaves.
    - USE_LOGGING will turn on/off logs that are used for debugging
    - USE_DEMO will have the program use example.txt as the input when true
    - PART_ONE has the program solve the first part when true, the second part when false

## Build Requirements
[Install python3](https://www.python.org/downloads/)
(Make sure to check the box that adds it to PATH)

## How to run the damn thing
"python {pathToDirectory}\main.py"