import re

seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

start_pattern = "AUG"
stop_pattern = "(UAA|UAG|UGA)" 

max_len = 0
longest_orf = ""

for match in re.finditer(start_pattern, seq):
    orf_start = match.start() # This is the .start() shown in your photo
    
    for i in range(orf_start, len(seq) - 2, 3):
        index = i
        codon = seq[index:index+3]
      
        if re.search(stop_pattern, codon):
            orf_end = i + 3
            current_orf = seq[orf_start:orf_end]
     
            if len(current_orf) > max_len:
                max_len = len(current_orf)
                longest_orf = current_orf
            break # Once a stop is found, this ORF ends

# Output results
print("The longest ORF is:", longest_orf)
print("Its length in nucleotides is:", max_len)
