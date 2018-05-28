# task: Implement pattern to number!
pattern = "AGT"
quarter_number = ""               # Zahl im Quartaersystem
decimal_number = 0                # Zahl im Decimalsystem

for i in range(0, len(pattern)):  # letzte Position im pattern wird nicht mitgezaehlt
    if pattern[i] == "A":
        number = 0                # type: int
    elif pattern[i] == "C":
        number = 1
    elif pattern[i] == "G":
        number = 2
    elif pattern[i] == "T":
        number = 3
    quarter_number += str(number)
    decimal_number += 4 ** (len(pattern)-i-1) * number   # multipliziert die Stellen (i) der quarter_number von links beginnend
                                                         # mit 4^(Laenge des patterns-Stelle-1), da Index bei 0 beginnt

print(pattern, "translated into quarter system:", quarter_number)
print("number in quarter system translated into decimal system:", decimal_number)
