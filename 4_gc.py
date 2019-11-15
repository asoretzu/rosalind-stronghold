# ID = "GC"
# PROJECT = "Computing GC Content"

# The GC-content of a DNA string is given by the percentage of symbols in the
# string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is
# 37.5%. Note that the reverse complement of any DNA string has the same
# GC-content.

# DNA strings must be labeled when they are consolidated into a database.
# A commonly used method of string labeling is called FASTA format. In this
# format, the string is introduced by a line that begins with '>', followed by
# some labeling information. Subsequent lines contain the string itself; the
# first line to begin with '>' indicates the label of the next string.

# In Rosalind's implementation, a string in FASTA format will be labeled by the
# ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and
# 9999.

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

# Return: The ID of the string having the highest GC-content, followed by the
# GC-content of that string. Rosalind allows for a default error of 0.001 in all
# decimal answers unless otherwise stated; please see the note on absolute error
# below.

# Sample Dataset

# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT

# Sample Output

# Rosalind_0808
# 60.919540


file_name = "TXT/gc.txt"


def GC():
    fasta_ids = []
    fasta_codes = []
    pair_count = []
    gc_content = []

    with open(file_name, mode="r") as f:
        for line in f:
            if line[0] == ">":
                line = line[1:-1]
                fasta_ids.append(line)

    with open(file_name, mode="r") as f:
        for line in f:
            string = ""
            print(line[0])
            # while line[0] != ">" and line:
            #     string = string + line[0:-1]
            # fasta_codes.append(string)

        # print(len(fasta_codes))
        # print(fasta_codes)
        #
        # for codes in fasta_codes:
        #     count = 0
        #     for i in range(0, len(codes)):
        #             code = codes[i]
        #             if code == "G" or code == "C":
        #                 count = count + 1
        #     pair_count.append(count)
        #
        # for i in range(0, len(fasta_ids)):
        #     porcent = ((100 / len(fasta_codes[i])) * pair_count[i])
        #     gc_content.append(porcent)
        #
        # for i in range(0, len(fasta_ids)):
        #     print("{}\n{}".format(fasta_ids[i], round(gc_content[i], 6)))


if __name__ == "__main__":
    GC()
