import re

# working with a sequence
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

start_codon = "AUG"
stop_codon = "(UAA|UAG|UGA)"

longest_orf = ""
max_length = 0

# We need to check all possible positions to find the *longest* ORF
for pos in range(len(seq) - 2):
    # Check if a start codon exists at the current position
    # using re.search as shown in the lecture example
    if re.search(pattern=start_codon, string=seq[pos:pos+3]):
        orf_start = pos
                
        for i in range(orf_start, len(seq) - 2, 3):
            index = i
            codon = seq[index:index+3]
            
            # Check if it is a stop codon 
            if re.search(pattern=stop_codon, string=codon):
                orf_end = i + 3
                current_orf = seq[orf_start:orf_end]
                current_length = len(current_orf)
                
                # Compare and store the longest ORF
                if current_length > max_length:
                    max_length = current_length
                    longest_orf = current_orf
                
                # Stop extending this specific ORF once a stop codon is found
                break

print("Longest ORF:", longest_orf)
print("Length:", max_length)