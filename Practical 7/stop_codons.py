START_CODON_DNA = 'ATG'
STOP_CODONS_DNA = "(TAA|TAG|TGA)"

INPUT_FILE = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
OUTPUT_FILE = 'stop_genes.fa'

current_header = ''
current_seq = ''

with open(INPUT_FILE, 'r') as infile, open(OUTPUT_FILE, 'w') as outfile:
    outfile.write("# This file is created automatically\n")

    for line in infile:
        line = line.strip()
        if not line:
            continue
        if line.startswith('>'):
            if current_header and current_seq:
                start_index = current_seq.find(START_CODON_DNA)
                found_stop_codons = set()
                if start_index != -1:
                    for j in range(start_index + 3, len(current_seq) - 2, 3):
                        codon = current_seq[j:j+3]
                        if codon in STOP_CODONS_DNA:
                            found_stop_codons.add(codon)
                if found_stop_codons:
                    gene_name = ''
                    for part in current_header.split():
                        if part.startswith('gene:'):
                            gene_name = part.split(':')[1]
                            break
                    new_header = f'>{gene_name} {" ".join(sorted(found_stop_codons))}'
                    outfile.write(new_header + '\n')
                    outfile.write(current_seq + '\n')

            current_header = line
            current_seq = ''
        else:
            current_seq += line

    if current_header and current_seq:
        start_index = current_seq.find(START_CODON_DNA)
        found_stop_codons = set()
        if start_index != -1:
            for j in range(start_index + 3, len(current_seq)-2, 3):
                codon = current_seq[j:j+3]
                if codon in STOP_CODONS_DNA:
                    found_stop_codons.add(codon)
        if found_stop_codons:
            gene_name = ''
            for part in current_header.split():
                if part.startswith('gene:'):
                    gene_name = part.split(':')[1]
                    break
            new_header = f'>{gene_name} {" ".join(sorted(found_stop_codons))}'
            outfile.write(new_header + '\n')
            outfile.write(current_seq + '\n')

print("Done! The output file is definitely created in your folder.")
