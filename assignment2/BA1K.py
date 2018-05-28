# task: Computing a Frequency Array
sequence = "ACGCGGCTCTGAAA"
k = 2
kmer_list = []
for i in range(4**k):
    kmer_list.append(0)

def PatternToNumber(pattern): # Umformen in Decimalzahl
    decimal_number = 0
    for i in range(len(pattern)):
        if pattern[i] == "A":
            number = 0
        elif pattern[i] == "C":
            number = 1
        elif pattern[i] == "G":
            number = 2
        elif pattern[i] == "T":
            number = 3
        decimal_number += 4**(len(pattern)-i-1)*(number+1)
    return decimal_number

for i in range(len(sequence)): # erstellt Liste mit Indices der kmere
    pattern = sequence[i:i+k]
    if len(pattern) == k:
        list_index = PatternToNumber(pattern)
        for j in range(k):
            list_index -= 4**(k-j-1)
        kmer_list[list_index] += 1
for i in kmer_list:
    print(i)
# Ergebnis wird vertikal ausgegeben
