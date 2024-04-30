def main():
    lines = []
    with open('/Users/lizzyjoo/bioinformatics_coding/exercises/reverse_complement/dataset_30273_2 (2).txt', 'r') as file:
        for line in file:
            line = line.strip()
            lines.append(line)
    text = lines[0]
    print(reverse_complement(text))


def reverse_complement(dna_string):
    
    nucleotides = {"A":"T", "C":"G", "G":"C", "T":"A"}

    complement = ""
    for char in dna_string:
        complement += nucleotides.get(char)
    return complement[::-1]

def get_complementary_strand(filename):
    """Reads a DNA sequence from a text file and returns its complementary strand (5' to 3').

    Args:
        filename: The name of the text file containing the DNA sequence.

    Returns:
        The complementary DNA strand.
    """

    with open(filename, 'r') as file:
        dna_sequence = file.read().strip()

    complement = ''
    dna_complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

    for base in dna_sequence:
        complement += dna_complement.get(base, 'N') 

    return complement[::-1]  

# Example usage
filename = "/Users/lizzyjoo/bioinformatics_coding/exercises/reverse_complement/dna_sequence.txt"
result = get_complementary_strand(filename)
print("The complementary strand is:", result)