# task: Implement number to pattern!
decimal_number = int(45)
print("Input: decimal number:", decimal_number)
lenght = int(4)
quarter_number = ""

while decimal_number > 0:
    remainder = decimal_number % 4                  # ermittelt den Rest aus der Teilung durch 4
    decimal_number = int(decimal_number / 4)        # teilt die Decimalzahl durch 4 bis eine 0 entsteht
    quarter_number = str(remainder) + quarter_number    # bildet die Zahl im Quartaersystem
for i in range(lenght-len(quarter_number)):         # falls die Zahl im Quartaersystem kuerzer ist als die gegebene
    quarter_number = "0" + quarter_number           # Laenge, wird 0 vorgesetzt

def NumberToPattern(pattern):                       # wandelt jede Stelle der Quartaerzahl in zugehoerige Base um
    dna_sequence = ""
    for i in range(len(pattern)):
        if pattern[i] == "0":
            letter = "A"
        elif pattern[i] == "1":
            letter = "C"
        elif pattern[i] == "2":
            letter = "G"
        elif pattern[i] == "3":
            letter = "T"
        dna_sequence += letter
    return dna_sequence

print("Input: length of DNA-sequence:", lenght)
print("number in quarter system:", quarter_number)
print("corresponding DNA-sequence:", NumberToPattern(quarter_number))
