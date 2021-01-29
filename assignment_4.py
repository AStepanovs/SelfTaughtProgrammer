import csv
filmlist = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open ("C:/Users/AndrisStepanovs/Desktop/tstp/films.csv", "w", newline="") as f:
    write = csv.writer(f, delimiter = ";")
    i=0
    while i< len(filmlist):
        write.writerow(filmlist[i])
        i += 1
