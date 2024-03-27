# Objective: implement a more efficient version than the "matching sequence" algorithm to determine which sequences occur the most
# 1. find all frequent k-mers if we determine the maximum value in the table
# 2. identify the keys of the frequency table achieving this value
# 3. append each one that we find to a growing list—return this list 

def main():
    lines = []
    with open('/Users/lizzyjoo/bioinformatics_coding/exercises/frequency_table/debugging_files/inputs/real_dataset.txt', 'r') as file:
        for line in file:
            line = line.strip()
            lines.append(line)
    text = lines [0]
    integer = int(lines[1])

    # output result(to match recommended output)
    result = frequent_words(text,integer)
    print(*result)


# create a dictionary which contains items of 3 k-mers that can be generated in a given Text (key)
# counts the number of occurrences of every 3-mer in Text (value)
# i.e. Input: a string Text and an integer k; Output: their frequency table as a map of string keys to integer values.
def frequency_table(text, k):
    # dictionary
    dict = {}
    n = len(text)
    for i in range(n-k):
        pattern = text[i:i+k]
        if pattern not in dict.keys():
            dict[pattern] = 1
        else:
            dict[pattern] += 1
    return dict

# return the maximum value in a given dictionary
def max_map(dict):
    # list of all the values
    x = dict.values()
    # return the maximum value from the list
    return max(x)


def frequent_words(text, k):
    frequent_patterns = []
    freq_map = frequency_table(text,k)
    max = max_map(freq_map)
    for pattern in freq_map:
        if freq_map[pattern] == max:
            frequent_patterns.append(pattern)
    return sorted(frequent_patterns)


main()