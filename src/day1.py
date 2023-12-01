import os
import re

def partOne(lines):
    count = 0
    for line in lines:
        nums = re.sub(r"\D", "", line)
        first = nums[:1]
        last = nums[-1:]
        rowNum = int(first + last)
        count += rowNum
    return count

def partTwo(lines):
    switch = {
        "one": "o1e",
        "two": "t2o",
        "three": "th3ee",
        "four": "fo4ur",
        "five": "fi5ve",
        "six": "s6x",
        "seven": "se7en",
        "eight": "ei8ht",
        "nine": "ni9ne"
    }
    replacedLines = []
    for l in lines:
        tmpLine = l
        for k in switch:
            tmpLine = re.sub(k, switch.get(k), tmpLine)
        replacedLines.append(tmpLine)
    return partOne(replacedLines)


filePath = os.path.abspath(os.path.dirname(__file__))
input = open(os.path.join(filePath, 'day1Input'), 'r')
lines = input.readlines()

print("Advent of Code 2023 - Day 1!")
print(f"Sum part 1: {partOne(lines)}")
print(f"Sum part 2: {partTwo(lines)}")

input.close()
