import matplotlib.pyplot as plt

START_CODON_DNA = 'ATG'
ALL_STOP_CODONS = {'TAA', 'TAG', 'TGA'}

INPUT_FILE = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
OUTPUT_IMAGE = 'codon_frequency_pie.png'

codon_count = {}

# 1. Ask the user to input a stop codon
while True:
    target = input("Enter stop codon to analyze (TAA/TAG/TGA): ").strip().upper()
    if target in ALL_STOP_CODONS:
        break
    print("Invalid input. Please enter TAA, TAG, or TGA.")

def process_sequence(seq, target_codon, counts_dict):
    """Helper function to find longest ORF and count upstream codons."""
    start_idx = seq.find(START_CODON_DNA)
    if start_idx != -1:
        # Extract the sequence from ATG to the end
        orf_seq = seq[start_idx:]
        target_positions = []
        
        # Find all in-frame positions of the target stop codon
        for j in range(0, len(orf_seq) - 2, 3):
            if orf_seq[j:j+3] == target_codon:
                target_positions.append(j)
                
        # If there are multiple instances, consider the one giving the longest ORF
        if target_positions:
            last_j = max(target_positions)
            
            # Count all codons strictly upstream of this specific stop codon
            for k in range(0, last_j, 3):
                c = orf_seq[k:k+3]
                counts_dict[c] = counts_dict.get(c, 0) + 1


current_seq = ''
with open(INPUT_FILE, 'r') as infile:
    for line in infile:
        line = line.rstrip() 
        if not line:
            continue
        
        if line.startswith('>'):
            if current_seq:
                process_sequence(current_seq, target, codon_count)
            current_seq = ''
        else:
            current_seq += line
            
    if current_seq:
        process_sequence(current_seq, target, codon_count)

# Print out the results
print(f"\nCodon counts upstream of {target}:")
for codon, cnt in sorted(codon_count.items()):
    print(f"{codon}: {cnt}")

# Generate and save pie chart
if codon_count:
    sorted_counts = dict(sorted(codon_count.items(), key=lambda item: item[1], reverse=True))
    
    labels = list(sorted_counts.keys())
    values = list(sorted_counts.values())
    
    plt.figure(figsize=(14, 10))
    
    colors = [plt.cm.hsv(i / len(labels)) for i in range(len(labels))]
    
   
    patches, texts, autotexts = plt.pie(
        values, 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=colors,
        textprops={'fontsize': 4.5, 'weight': 'bold'}
    )
    
    plt.title(f'Codon Frequency Upstream of {target}\n(All {len(labels)} Codons, Sorted by Frequency Descending)')
    plt.axis('equal')
    
    plt.legend(
        patches, labels,
        title=f"Codon (Total: {len(labels)})",
        loc="lower left",
        bbox_to_anchor=(1.05, 0.1), 
        fontsize=6,
        ncol=4
    )
    
    plt.savefig(OUTPUT_IMAGE, bbox_inches='tight', dpi=300)
    plt.close()
    
    print(f"\nSuccess! Highly detailed pie chart saved as '{OUTPUT_IMAGE}'")
else:
    print(f"\nNo valid sequences found ending with '{target}'.")