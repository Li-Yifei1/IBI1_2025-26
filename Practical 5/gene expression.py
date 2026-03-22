# Import required libraries
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Create dictionary to store 5 gene expression levels, add MYC and print the dictionary
gene_exp = {
    'TP53': 12.4,
    'EGFR': 15.1,
    'BRCA1': 8.2,
    'PTEN': 5.3,
    'ESR1': 10.7
}
# Add new gene MYC with expression level 11.6
gene_exp['MYC'] = 11.6
# Print the gene expression dictionary
print(" Gene Expression Dictionary ")
print(gene_exp)

# Step 2: Define gene of interest, check existence and print expression level
#  PSEUDOCODE: Modify gene_interest to test different genes 
gene_interest = 'EGFR'  
if gene_interest in gene_exp:
    print(" Target Gene Expression Level ")
    print("Expression level of gene", {gene_interest},":", {gene_exp[gene_interest]})
else:
    print(" Error Message ")
    print("Gene {gene_interest} not found in the dataset. Please check the gene name!")

# Step 3: Calculate and print average gene expression level
total_exp = sum(gene_exp.values()) 
gene_num = len(gene_exp)            
avg_exp = total_exp / gene_num      
print(" Average Gene Expression Level ")
print("Average expression level of all ",{gene_num}, "genes:",  {avg_exp})

# Step 4: Generate labeled bar chart
genes = list(gene_exp.keys())       
expressions = list(gene_exp.values())
plt.figure(figsize=(10, 7))          
plt.bar(genes, expressions, color='skyblue')  # Create bar plot

# Add chart labels and title
plt.title('Gene Expression Levels', fontsize=14)
plt.xlabel('Gene Name', fontsize=12)
plt.ylabel('Expression Level', fontsize=12)
plt.xticks(rotation=0)                            

# Adjust layout to prevent label overlap and display the plot
plt.tight_layout()
plt.show()
