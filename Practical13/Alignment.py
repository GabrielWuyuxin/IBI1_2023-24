import glob
import numpy as np


# Gets all fasta files in the current directory
fasta_files = glob.glob(r'C:\Users\吴雨馨\IBI1\IBI1_2023-24\IBI1_2023-24\Practical13\*.fa')
fasta_dict = {}
#print(fasta_dict)

# Read the fasta file
for fasta_file in fasta_files:
    with open(fasta_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('>'):
                # Get sequence name
                seq_name = line.strip()
                fasta_dict[seq_name] = ''
            else:
                # Fetch sequence
                 fasta_dict[seq_name] += line.strip()

# View the results

rat_seq= fasta_dict[">sp|P31652|SC6A4_RAT Sodium-dependent serotonin transporter OS=Rattus norvegicus OX=10116 GN=Slc6a4 PE=1 SV=1"]
mouse_seq=fasta_dict[">sp|Q60857|SC6A4_MOUSE Sodium-dependent serotonin transporter OS=Mus musculus OX=10090 GN=Slc6a4 PE=1 SV=4"]
human_seq=fasta_dict[">sp|P31645|SC6A4_HUMAN Sodium-dependent serotonin transporter OS=Homo sapiens OX=9606 GN=SLC6A4 PE=1 SV=1"]

rat_name = ">sp|P31652|SC6A4_RAT Sodium-dependent serotonin transporter OS=Rattus norvegicus OX=10116 GN=Slc6a4 PE=1 SV=1"
mouse_name = ">sp|Q60857|SC6A4_MOUSE Sodium-dependent serotonin transporter OS=Mus musculus OX=10090 GN=Slc6a4 PE=1 SV=4"
human_name = ">sp|P31645|SC6A4_HUMAN Sodium-dependent serotonin transporter OS=Homo sapiens OX=9606 GN=SLC6A4 PE=1 SV=1"

#set initial distance as zero	
def calculate_distance(keyx,keyy,dict_inst):
    edit_distance=0
    x = dict_inst[keyx]
    y = dict_inst[keyy]
    for	i in range(len(human_seq)):	#compare each amino	acid	
        if x[i]!=y[i]:				
            edit_distance+=1	#add a score 1 if amino	acids are different	
    edit_percentage=edit_distance/len(human_seq)*100
    print("The edit sidtance for",keyx[4:10],"and",keyy[4:10],"is",edit_distance,"with percentage",edit_percentage,"%")
    return edit_distance


calculate_distance(rat_name,human_name,fasta_dict)
calculate_distance(mouse_name,human_name,fasta_dict)
calculate_distance(mouse_name,rat_name,fasta_dict)


