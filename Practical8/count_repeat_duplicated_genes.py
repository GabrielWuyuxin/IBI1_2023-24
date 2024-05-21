# Function to count overlapping occurrences of a substring in a string
def count_overlapping(seq, sub):
    count = start = 0
    # Loop to find all overlapping instances of the substring
    while True:
        start = seq.find(sub, start) + 1
        if start > 0:
            count += 1
        else:
            return count

# Function to process the input FASTA file and output genes with specified repeats
def process_duplicates(input_file, repeat, output_file):
    # Open the input and output files
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        write_flag = False
        seq_data = ''
        gene_name = ''
        
        for line in infile:
            # Check if the line is a header line
            if line.startswith('>'):
                # If previously read sequence has the repeat, write it to the output file
                if write_flag and repeat in seq_data:
                    count = count_overlapping(seq_data, repeat)
                    outfile.write(f'>{gene_name}_{count}\n{seq_data}\n')
                
                # Check if the current gene is a duplication
                write_flag = 'duplication' in line
                gene_name = line.split(' ')[0][1:]
                seq_data = ''
            elif write_flag:
                # Concatenate sequence lines
                seq_data += line.strip()
        
        # Check the last read sequence if it needs to be written
        if write_flag and repeat in seq_data:
            count = count_overlapping(seq_data, repeat)
            outfile.write(f'>{gene_name}_{count}\n{seq_data}\n')

if __name__ == "__main__":
    # Prompt the user to enter the repeat sequence
    repeat = input("Enter the repeat sequence (GTGTGT or GTCTGT): ")
    
    # Define the input and output file paths
    input_file = r'C:\Users\吴雨馨\Downloads\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
    output_file = f'{repeat}_duplicate_genes.fa'
    
    # Call the function to process the duplicates
    process_duplicates(input_file, repeat, output_file)

