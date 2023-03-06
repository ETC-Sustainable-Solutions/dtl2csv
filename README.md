# SMALL CONVERSION UTILITY 

This app converts DTL format to CSV format.

It is limited to interpreting values in float format.

---
# USE.

```
python dtl2csv.py -i [dtl file] 
```

The output is on Standard Output so to create the CSV:

```
python dtl2csv.py -i [dtl file] > [csv file]
```

The tool writes the date in the ISO format YYYY-MM-DD HH:MM:SS

In case you want to keep the UNIX TIMESTAMP format use the -t

```
python dtl2csv.py -t -i [dtl file] > [csv file]
```

----
# DTL FILE SPECIFICATIONS

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
2. the actual recording time is [the time to save the first record]  multiples by 10.
