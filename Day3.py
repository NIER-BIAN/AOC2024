#=========================================================
# Pt1

import re

with open('input.txt', 'r') as file:
    puzzleInput = file.read()

# capture everything between "mul(" and the next ")".
# r""
# mul
# \(
# \d+: Matches one or more digits
# note the caputring groups created around both \d+
# ,
# \)
pattern = r"mul\((\d+),(\d+)\)"

matches = re.findall(pattern, puzzleInput)

print(sum([int(pair[0])*int(pair[1]) for pair in matches]))

#=========================================================
# Pt2

import re

with open('input.txt', 'r') as file:
    puzzleInput = file.read()

# remove everything between "don't()"s and the next "do()" or the end of str
def remove_substring(input_string):

    while True:
        start_index = input_string.find("don't()")

        # if no don't() in str, return str
        if start_index == -1:
            break

        end_index = input_string.find("do()", start_index + len("don't()"))

        # if no do() in remaining str, remove to the end of str
        if end_index == -1:
            end_index = len(input_string)
            
        input_string = input_string[:start_index] + input_string[end_index:]
        
    return input_string

cleanPuzzleInput = remove_substring(puzzleInput)

pattern = r"mul\((\d+),(\d+)\)"

matches = re.findall(pattern, cleanPuzzleInput)

print(sum([int(pair[0])*int(pair[1]) for pair in matches]))
