#Aufgabe Nr. 1 mit faster frequent words
sequence = "CGGAAGCGAGATTCGCGTGGCGTGATTCCGGCGGGCGTGGAGAAGCGAGATTCATTCAAGCCGGGAGGCGTGGCGTGGCGTGGCGTGCGGATTCAAGCCGGCGGGCGTGATTCGAGCGGCGGATTCGAGATTCCGGGCGTGCGGGCGTGAAGCGCGTGGAGGAGGCGTGGCGTGCGGGAGGAGAAGCGAGAAGCCGGATTCAAGCAAGCATTCCGGCGGGAGATTCGCGTGGAGGCGTGGAGGCGTGGAGGCGTGCGGCGGGAGATTCAAGCCGGATTCGCGTGGAGAAGCGAGAAGCGCGTGCGGAAGCGAGGAGGAGAAGCATTCGCGTGATTCCGGGAGATTCAAGCATTCGCGTGCGGCGGGAGATTCAAGCGAGGAGGCGTGAAGCAAGCAAGCAAGCGCGTGGCGTGCGGCGGGAGAAGCAAGCGCGTGATTCGAGCGGGCGTGCGGAAGCGAGCGG"
k = 12
if (k > len(sequence)):
    print("Error, k > Sequence!")
print("Input: ", sequence)
print("Laenge des kmer: ", k)

# BA1M und BA1L
def PatToNum(pattern):
    dec_index = 0
    for i in range(len(pattern)):
        if pattern[i] == "A":
            factor = 0
        elif pattern[i] == "C":
            factor = 1
        elif pattern[i] == "G":
            factor = 2
        elif pattern[i] == "T":
            factor = 3
        dec_index += 4 ** (len(pattern) - 1 - i) * (factor + 1)
    return dec_index

def NumToPat(number):
    quart_text = ""
    for i in range(len((number))):
        if number[i] == "0":
            factor = "A"
        elif number[i] == "1":
            factor = "C"
        elif number[i] == "2":
            factor = "G"
        elif number[i] == "3":
            factor = "T"
        quart_text += factor
    return quart_text

def DecToQuart(dec_number):     #Umrechnung von Dezimal zu Quartaer:
    quart_number = ""  # Erstelle Zahl (im string-Format) im Quartaersystem
    while dec_number > 0:
        remainder = dec_number % 4
        dec_number = int(dec_number / 4)
        quart_number = str(remainder) + quart_number
    return quart_number

kmer_frequencies = []           # BA1K
for i in range(4**k):
    kmer_frequencies.append(0)
for i in range(len(sequence)-k+1):
    pattern = sequence[i:i+k]
    if len(pattern) == k:
        list_index = PatToNum(pattern) #gibt decimal index
        for j in range(k):
            list_index -=  4**(k-j-1)
        kmer_frequencies[list_index] +=1

def indices(list, value):           # maximum_value = max(kmer_frequencies)
    return [i for i,x in enumerate(list) if x==value] #liefert Liste

for i in indices(kmer_frequencies, max(kmer_frequencies)):
    quart_number = int(DecToQuart(i))
    for i in range(k - len(str(quart_number))):
        quart_number = "0" + str(quart_number)
    print(NumToPat(str(quart_number)))
print("mit je", max(kmer_frequencies), "mal.")
