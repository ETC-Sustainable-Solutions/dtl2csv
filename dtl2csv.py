#!/usr/bin/env python3

import sys,getopt
from struct import *
from datetime import datetime

SEP = ';'
NL = "\n"

def usage():
   print('Usage: ',sys.argv[0],' [-t] -i <file>')
   sys.exit(2)

def main(argv):

    inputfile = ''
    timestamp = 0
    try:
       opts, args = getopt.getopt(argv,"ti:",["ifile="])
    except getopt.GetoptError:
       usage(sys.argv[0])

    for opt, arg in opts:
      if opt == '-t':
         timestamp = 1
      elif opt in ("-i", "--ifile"):
         inputfile = arg

    if (inputfile == ''):
        usage()

    
    with open(inputfile, mode='rb') as file:
        fileContent = file.read();
    header = '4sIIII'
    a,b,c,size,boo = unpack(header,fileContent[:20])
    if (a.decode('ascii') != '_dtl'):
        print ("wrong file format")
        exit (-1)
    
    # preso il numero di elementi iniziamo a leggere i nomi
    # per ora non conosco i vari valori e quindi tratto tutti come float
    offset = size * 8
    p = offset + 20
    
    name, = unpack('4s',fileContent[p:p+4])
    p = p + calcsize('4s')
    name = name.decode('ascii')
    if (name == 'name'):
        headers = []
        for i in range(size):
            l, = unpack('<h',fileContent[p:p+2])
            p = p + calcsize('h')
            pf = p + l
            name, = unpack(str(l)+'s', fileContent[p:pf])
            p = p + l
            name = name.decode('ascii')
            headers.append(name)
        count = 0
        values = []
        while p < len(fileContent):
            row = {}
            row['date'],row['tr'] = unpack('IB',fileContent[p:p+5])
            p = p + calcsize('IB')
            for i in range(size):
                val, = unpack('f',fileContent[p:p+4])
                p = p + calcsize('f')
                row[headers[i]]=val
            values.append(row)
        # esportiamo il csv
        sys.stdout.write('date'+SEP+'tr')
        for i in headers:
            sys.stdout.write (SEP+i)
        sys.stdout.write (NL)
        for row in values:
            if (timestamp):
                sys.stdout.write(str(row['date']))
            else:
                sys.stdout.write(str(datetime.utcfromtimestamp(row['date'])))
            sys.stdout.write(SEP+str(row['tr']*10))
            for i in headers:
                sys.stdout.write(SEP+str(row[i]))
            sys.stdout.write(NL)
    else:
        print ("something went wrong")
        exit(-2)

if __name__ == "__main__":
    main(sys.argv[1:])
