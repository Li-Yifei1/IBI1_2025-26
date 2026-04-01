seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
start_codon = 'AUG'
stop_codon = {'UAA', 'UAG', 'UGA'}
longest_orf = ''
max_length = 0
for i in range(len(seq) - 2):
    if seq[i:i+3] == start_codon:
        for j in range(i + 3, len(seq) - 2, 3):
            current_codon = seq[j:j+3]
            if current_codon in stop_codon:
                current_orf = seq[i:j+3]
                current_length = len(current_orf)
                if current_length > max_length:
                    max_length = current_length
                    longest_orf = current_orf
                break

print(longest_orf)
print(max_length)