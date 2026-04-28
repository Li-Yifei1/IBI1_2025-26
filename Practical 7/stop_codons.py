import re

input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "stop_genes.fa"
stop_pattern = "(TAA|TAG|TGA)"

with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
    gene_name = ""
    gene_seq = ""

    for line in f_in:
        line = line.rstrip()
        if line.startswith(">"):
            # Process the previous gene using Lecture logic
            if gene_seq.startswith("ATG"):
                # Use regex to find all in-frame stop codons
                found_stops = []
                for i in range(0, len(gene_seq)-2, 3):
                    codon = gene_seq[i:i+3]
                    match = re.search(stop_pattern, codon)
                    if match:
                        found_stops.append(match.group())
                
                if found_stops:
                    unique_stops = ",".join(set(found_stops))
                    f_out.write(f">{gene_name};{unique_stops}\n{gene_seq}\n")
            
            name_match = re.search(r'^>(\S+)', line)
            gene_name = name_match.group(1) if name_match else "Unknown"
            gene_seq = ""
        else:
            gene_seq += line

# Final gene processing logic (same as inside the loop)
