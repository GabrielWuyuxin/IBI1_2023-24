import re

input_file_path = r"C:\Users\吴雨馨\Downloads\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file_path = "duplicated_genes.fa"

def find_duplicated_genes(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as handle, open(output_file_path, 'w', encoding='utf-8') as output_file:
        found_duplication = False
        for line in handle:
            line = line.rstrip()
            if line.startswith('>'):
                if 'duplication' in line:
                    found_duplication = True
                    gene_name = line.split()[0]  # get gene name
                    output_file.write(gene_name + "\n")
                else:
                    found_duplication = False
            elif found_duplication:
                output_file.write(line + "\n")

# Call the function to filter and save the result
find_duplicated_genes(input_file_path, output_file_path)

# Displays some of the content written to the file to confirm correctness
with open(output_file_path, 'r', encoding='utf-8') as output_file:
    dup_genes = output_file.read(2000)
    print(dup_genes)