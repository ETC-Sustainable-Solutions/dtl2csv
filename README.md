# PICCOLA UTILITY DI CONVERSIONE 

Questa app converte il formato DTL in CSV

E' limitata all'interpretazione dei valori in formato float.

---
# UTILIZZO

```
python dtl2csv.py -i [file dtl] 
```

L'output e' su Standard Output quindi per creare il CSV:

```
python dtl2csv.py -i [file dtl] > [file csv]
```

Il tool scrive la data nel formato ISO YYYY-MM-DD HH:MM:SS

Nel caso si volesse mantenere il formato UNIX TIMESTAMP utilizzare il -t

```
python dtl2csv.py -t -i [file dtl] > [file csv]
```

----
# SPECIFICHE DEL FILE DTL

## Brief description

Data log (data sampling) overhead for each record storage.

Header = 20 byte + data channel x 8byte + channel name

Entry(each) = 5bytes + sizeof( record )

## Detailed description

Content|Length(Byte)
:--|--:
Header|20
Data format of the1st channel|8
Data format of the 2nd channel|8
…|...
Text "name"|4
The name length of the 1st channel|2
The name of the 1st channel|n
The name length of the 2nd channel|2
The name of the 2nd channel|n
…|...
The time of the 1st data|4
The time to record the 1st data|1
The 1st data of the 1st channel|n
The 2nd data of the 1st channel|n

PS:

1. n : depends on the data
2. The actual recording time is [the time to save the first record]  multiples by 10.
