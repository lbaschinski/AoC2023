import os
import re

RED = 12
GREEN = 13
BLUE = 14

def num(str):
    return int(re.sub(r"\D", "", str))

def partOne(lines):
    sum = 0
    for line in lines:
        gameList = line.split(": ")
        gameNumber = num(gameList[0])
        games = gameList[1].split("; ")
        isGamePossible = True
        for game in games:
            colors = game.split(", ")
            isDrawPossible = True
            for color in colors:
                if "red" in color:
                    if num(color) > RED:
                        isDrawPossible = False
                        break
                if "green" in color:
                    if num(color) > GREEN:
                        isDrawPossible = False
                        break
                if "blue" in color:
                    if num(color) > BLUE:
                        isDrawPossible = False
                        break
            if not isDrawPossible:
                isGamePossible = False
                break
        if isGamePossible:
            sum += gameNumber
    return sum
    
def partTwo(lines):
    sum = 0
    for line in lines:
        gameList = line.split(": ")
        games = gameList[1].split("; ")
        minRed = 0
        minGreen = 0
        minBlue = 0
        for game in games:
            colors = game.split(", ")
            for color in colors:
                if "red" in color:
                    redNum = num(color)
                    if redNum > minRed:
                        minRed = redNum
                if "green" in color:
                    greenNum = num(color)
                    if greenNum > minGreen:
                        minGreen = greenNum
                if "blue" in color:
                    blueNum = num(color)
                    if blueNum > minBlue:
                        minBlue = blueNum
        sum += minRed * minGreen * minBlue
    return sum

filePath = os.path.abspath(os.path.dirname(__file__))
input = open(os.path.join(filePath, 'day2Input'), 'r')
lines = input.readlines()

print("Advent of Code 2023 - Day 2!")
print(f"Sum part 1: {partOne(lines)}")
print(f"Sum part 2: {partTwo(lines)}")

input.close()
