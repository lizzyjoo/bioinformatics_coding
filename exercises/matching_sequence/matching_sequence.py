# will implement pattern_count function 
# Input: Strings Text and Pattern. The data set contains two lines.
# Output: Count(Text, Pattern).
# two strategies

def main():
    lines = []
    # open file 
    with open('/Users/lizzyjoo/bioinformatics_coding/exercises/matching_sequence/debugging_files/inputs/real_dataset.txt', 'r') as file:
        for line in file:
            line = line.strip()
            lines.append(line)
    text = lines [0]
    pattern = lines[1]

    #output
    print(pattern_count_loop(text, pattern))

# Strategy 1: use .count() method in Python
def pattern_count(text, pattern):
    
    count = text.count(pattern)

    return count

# Strategy 2: use a for loop
# logic: iterate through the text, check x number of characters to see if 
# if those characters match 'pattern,' x being # of chars in 'pattern'
def pattern_count_loop(text, pattern):
    # occurence counter
    n = 0
    pattern_length = len(pattern)
    for i in range(len(text)):
        if text[i: i + pattern_length] == pattern:
            n += 1

    return n


main()