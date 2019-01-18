def main():
    take_input = True
    while take_input:
        print("""
        What would you like to convert?
        1) DNA (Coding Strand 5'-3') to mRna(5'-3')
        2) DNA (Template strand 3'-5') to mRNA(5'-3')
        3) Quit
        """, end="")
        decision = input("")

        if decision.isdigit() == True:
            int_decision = int(decision)
            if int_decision == 1:
                coding_strand = input("Enter the coding strand: ")
                upper_coding_strand = coding_strand.upper()
                cs = codingDNA(coding_strand)
                if cs == False:
                    return False
                final_aa = findAA(upper_coding_strand)
                print("Amino acid sequence is\n", final_aa)
            elif int_decision == 2:
                template_strand = input("Enter the template strand: ")
                td = templateDNA(template_strand)
                if td == False:
                    return False
                upper_td = td.upper()
                print(td)
                td_aa = findAA(upper_td)
                print(td_aa.strip(" - "))
            elif int_decision == 3:
                take_input = False
            else:
                print("Invalid choice")
        else:
            print("Invalid choice")


def findAA(result):
    aminoacid_dict = {'ACA': 'Thr', 'GCA': 'Ala', 'ATT': 'Ile', 'AAA': 'Lys', 'AGG': 'Arg', 'CGC': 'Arg', 'AAG': 'Lys', 'TTA': 'Leu', 'TAT': 'Tyr', 'TGC': 'Cys', 'TTC': 'Phe', 'CAC': 'His', 'GGT': 'Gly', 'GTG': 'Val', 'TTT': 'Phe', 'CAA': 'Gln', 'ACT': 'Thr', 'ATA': 'Ile', 'GAC': 'Asp', 'CGA': 'Arg', 'TCC': 'Ser', 'CAT': 'His', 'TCG': 'Ser', 'GAA': 'Glu', 'ATC': 'Ile', 'CAG': 'Gln', 'CGG': 'Arg', 'AGA': 'Arg', 'TCT': 'Ser', 'AGT': 'Ser', 'CTG': 'Leu', 'AAC': 'Asn', 'GTC': 'Val', 'CCT': 'Pro', 'TGT': 'Cys', 'GTA': 'Val', 'ATG': 'Met', 'TGG': 'Trp', 'CCA': 'Pro', 'ACC': 'Thr', 'ACG': 'Thr', 'GAT': 'Asp', 'AAT': 'Asn', 'TCA': 'Ser', 'GAG': 'Glu', 'GCC': 'Ala', 'GCT': 'Ala', 'AGC': 'Ser', 'GCG': 'Ala', 'CCG': 'Pro', 'TAG': 'Stp', 'CTC': 'Leu', 'GGG': 'Gly', 'GGA': 'Gly', 'CCC': 'Pro', 'CTT': 'Leu', 'GTT': 'Val', 'CGT': 'Arg', 'TAA': 'Stp', 'TTG': 'Leu', 'GGC': 'Gly', 'TGA': 'Stp', 'CTA': 'Leu', 'TAC': 'Tyr'}
    aminoacids = ""

    for i in range(0, len(result), 3):
        codon = result[i:i+3]
        if codon == "ATG" or codon == "AUG":
            aminoacids += "Met(Start) - "
        elif codon == "TAA" or codon == "TGA" or codon == "TAG" or codon == "UAG" or codon == "UGA" or codon == "UAA"    :
            aminoacids += "STOP - "
        else:
            aminoacids += aminoacid_dict[codon] + " - "
    return aminoacids.strip(" - ")

def codingDNA(dna):
    valid_genes = ["a", "c", "t", "g", "A", "C", "T", "G"]
    res_coding_strand = ""
    for gene in dna:
        if gene not in valid_genes:
            print("Invalid DNA sequence")
            return False
        else:
            if gene == "t":
                res_coding_strand += "u"
            elif gene == "T":
                res_coding_strand += "U"
            else:
                res_coding_strand += gene
    return "mRNA sequence is 5' " + res_coding_strand + " 3'"

def templateDNA(dna):
    check_validity = True
    valid_genes = ["a", "c", "t", "g", "A", "C", "T", "G"]
    res_coding_strand = ""
    for gene in dna:
        if gene not in valid_genes:
            print("Invalid DNA sequence")
            check_validity = False
            return check_validity
        else:
            if gene == "a":
                res_coding_strand += "u"
            elif gene == "c":
                res_coding_strand += "g"
            elif gene == "t":
                res_coding_strand += "a"
            elif gene == "g":
                res_coding_strand += "c"
            elif gene == "A":
                res_coding_strand += "U"
            elif gene == "C":
                res_coding_strand += "G"
            elif gene == "T":
                res_coding_strand += "A"
            elif gene == "G":
                res_coding_strand += "C"
    if check_validity:
        return  res_coding_strand

if __name__ == '__main__':
    main()