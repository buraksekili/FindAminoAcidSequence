
# file = open("codons.txt", "r")
# all_lines = file.readlines()
# empty_list = []
# for i in range(2, len(all_lines)):
#     strip_lines = all_lines[i].strip()
#     empty_list.append(strip_lines)
# res_list = []
# for i in range(len(empty_list)):
#     res_list.append(empty_list[i].split("\t"))
# fin_dict = {}

# for i in res_list:
#     if i[0] not in fin_dict.keys():
#         fin_dict[i[0]] = i[1]
#     elif i[0] in fin_dict.keys():
#         fin_dict[i[0]] += i[1]
# print(fin_dict) 

# aminoacid_dict = {'ACA': 'Thr', 'GCA': 'Ala', 'ATT': 'Ile', 'AAA': 'Lys', 'AGG': 'Arg', 'CGC': 'Arg', 'AAG': 'Lys', 'TTA': 'Leu', 'TAT': 'Tyr', 'TGC': 'Cys', 'TTC': 'Phe', 'CAC': 'His', 'GGT': 'Gly', 'GTG': 'Val', 'TTT': 'Phe', 'CAA': 'Gln', 'ACT': 'Thr', 'ATA': 'Ile', 'GAC': 'Asp', 'CGA': 'Arg', 'TCC': 'Ser', 'CAT': 'His', 'TCG': 'Ser', 'GAA': 'Glu', 'ATC': 'Ile', 'CAG': 'Gln', 'CGG': 'Arg', 'AGA': 'Arg', 'TCT': 'Ser', 'AGT': 'Ser', 'CTG': 'Leu', 'AAC': 'Asn', 'GTC': 'Val', 'CCT': 'Pro', 'TGT': 'Cys', 'GTA': 'Val', 'ATG': 'Met', 'TGG': 'Trp', 'CCA': 'Pro', 'ACC': 'Thr', 'ACG': 'Thr', 'GAT': 'Asp', 'AAT': 'Asn', 'TCA': 'Ser', 'GAG': 'Glu', 'GCC': 'Ala', 'GCT': 'Ala', 'AGC': 'Ser', 'GCG': 'Ala', 'CCG': 'Pro', 'TAG': 'Stp', 'CTC': 'Leu', 'GGG': 'Gly', 'GGA': 'Gly', 'CCC': 'Pro', 'CTT': 'Leu', 'GTT': 'Val', 'CGT': 'Arg', 'TAA': 'Stp', 'TTG': 'Leu', 'GGC': 'Gly', 'TGA': 'Stp', 'CTA': 'Leu', 'TAC': 'Tyr'}

# print(aminoacid_dict.keys())

# keys = ['CTG', 'ATT', 'TCT', 'GGT', 'CAG', 'ATC', 'CAC', 'AAG', 'ATG', 'GTG', 'CAA', 'TCC', 'CTC', 'GAA', 'GAC', 'GGA', 'TTC', 'TAG', 'AGA', 'GTT', 'GTA', 'AGG', 'CAT', 'AAC', 'TGA', 'TGC', 'CCG', 'CGC', 'AAA', 'CGA', 'TTG', 'CGT', 'CCT', 'TGT', 'TCG', 'TTT', 'GGC', 'ATA', 'GTC', 'TAC', 'CCA', 'GCC', 'ACT', 'AGC', 'AAT', 'CCC', 'TCA', 'TTA', 'CTT', 'TAA', 'GAT', 'GCG', 'ACG', 'TAT', 'CTA', 'ACC', 'GCT', 'TGG', 'GGG', 'GCA', 'AGT', 'ACA', 'CGG', 'GAG']

# for k, v in aminoacid_dict.items():

a = "bir"
d = a[:2]
print(d)