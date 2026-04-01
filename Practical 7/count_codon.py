import matplotlib.pyplot as plt

START_CODON_DNA = 'ATG'
ALL_STOP_CODONS = {'TAA', 'TAG', 'TGA'}
INPUT_FILE = r'C:\Users\thinkpad\Downloads\Practical 7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
OUTPUT_IMAGE = r'C:\Users\thinkpad\Downloads\Practical 7\codon_frequency_pie.png'

codon_count = {}
current_header = ''
current_seq = ''

while True:
    target = input("Enter stop codon to analyze (TAA/TAG/TGA): ").strip().upper()
    if target in ALL_STOP_CODONS:
        break
    print("Invalid input. Please try again.")

with open(INPUT_FILE, 'r') as infile:
    for line in infile:
        line = line.strip()
        if not line:
            continue
        if line.startswith('>'):
            if current_header and current_seq:
                start_idx = current_seq.find(START_CODON_DNA)
                if start_idx != -1:
                    positions = []
                    for j in range(start_idx + 3, len(current_seq)-2, 3):
                        if current_seq[j:j+3] == target:
                            positions.append(j)
                    if positions:
                        last_j = max(positions)
                        for k in range(start_idx, last_j, 3):
                            c = current_seq[k:k+3]
                            codon_count[c] = codon_count.get(c, 0) + 1
            current_header = line
            current_seq = ''
        else:
            current_seq += line

    if current_header and current_seq:
        start_idx = current_seq.find(START_CODON_DNA)
        if start_idx != -1:
            positions = []
            for j in range(start_idx + 3, len(current_seq)-2, 3):
                if current_seq[j:j+3] == target:
                    positions.append(j)
            if positions:
                last_j = max(positions)
                for k in range(start_idx, last_j, 3):
                    c = current_seq[k:k+3]
                    codon_count[c] = codon_count.get(c, 0) + 1

print("\nCodon counts upstream of", target)
for codon, cnt in sorted(codon_count.items()):
    print(codon, cnt)

if codon_count:
    plt.figure(figsize=(10,6))
    plt.pie(codon_count.values(), labels=codon_count.keys(), autopct='%1.1f%%', startangle=90)
    plt.title(f'Codon Frequency for {target}')
    plt.savefig(OUTPUT_IMAGE, bbox_inches='tight')
    plt.close()
    print("\nPie chart saved as", OUTPUT_IMAGE)