# ex csv
import csv
with open('zaragoza_2010_10.csv') as fin:
    reader = csv.reader(fin, delimiter=";")
    for fila in reader:
        print fila

with open('codigo_ascii.txt', 'w') as fout:
    writer = csv.writer(fout)
    ascii_a = ord('a')
    for n in range(26):
        writer.writerow((chr(ascii_a+n),
                         ascii_a + n))

with open('codigo_ascii.txt') as f:
    print f.read()
                         
