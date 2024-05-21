seq = "ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA"
count = 0
for i in range(len(seq) - 5):
    if seq[i:i+6] == "GTGTGT" or seq[i:i+6] == "GTCTGT":
        count += 1
print(count)