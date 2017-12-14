#!/usr/bin/python3
#linkExtract

#Purpose:
#linkExtract is a command-line tool which can be used to extact urls(links) from IRC log files.

#Author:Kshithij Iyer
#Email: ahole@disroot.org
#Date of Creation: 13/12/2017

#regex for links
#^((http[s]?|ftp):\/)?\/?([^:\/\s]+)((\/\w+)*\/)([\w\-\.]+[^#?\s]+)(.*)?(#[\w\-]+)?$

#Settings:
delimeter=" "#The delimeter used in the file.

#imports
import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('python3 linkExtract.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('python3 linkExtract.py -i <inputfile> -o <outputfile>')
            sys.exit(2)
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        print('Input file is ', inputfile)
        print('Output file is ', outputfile)
        if outputfile=="" or outputfile==" ":
            datafile=open(inputfile,"r")
            linkfile=open("links.txt","a")
        elif inputfile==" " or inputfile=="":
            print("Error: No input file provided!")
            sys.exit(2)
        else:
            datafile=open(inputfile,"r")
            linkfile=open(outputfile,"a")
            
        #regex and writing logic goes here
        while True:
            line=datafile.readline()
            if line:
                words=line.split(delimeter)
                for word in words:
                    print(word)
            else:
                break
        #close files goes here
        datafile.close()
        linkfile.close()

if __name__ == "__main__":
    main(sys.argv[1:])
