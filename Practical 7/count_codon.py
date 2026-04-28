import re
import matplotlib.pyplot as plt

# Requirement: Ask user to input (Lecture 7.2 stdout/stdin)
user_stop = input("Enter a stop codon (TAA, TAG, or TGA): ").upper()

# Ensure we use Regex for the user's input
input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
codon_usage = {}

with open(input_file, "r") as f:
    full_seq = ""
    for line in f:
        line = line.rstrip()
        if line.startswith(">"):
            if full_seq.startswith("ATG"):
                # Split into codons
                codons = [full_seq[i:i+3] for i in range(0, len(full_seq)-2, 3)]
                # Lecture logic: check if user_stop exists via regex
                if re.search(user_stop, full_seq):
                    # Process codons upstream of the first instance
                    for c in codons:
                        if re.search(user_stop, c): break
                        codon_usage[c] = codon_usage.get(c, 0) + 1
            full_seq = ""
        else:
            full_seq += line

# Requirement: Pie chart and file output
if codon_usage:
    top_10 = dict(sorted(codon_usage.items(), key=lambda x: x[1], reverse=True)[:10])
    plt.pie(top_10.values(), labels=top_10.keys(), autopct='%1.1f%%')
    plt.title(f"Codon usage before {user_stop}")
    plt.savefig("codon_usage.png") # Save to file as per guidance
    plt.show()
