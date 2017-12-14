#!/usr/bin/python3
#linkExtract

#Purpose:
#linkExtract is a command-line tool which can be used to extact urls(links) from IRC log files.

#Author:Kshithij Iyer
#Email: ahole@disroot.org
#Date of Creation: 13/12/2017

#Settings:
delimeter=" " #The delimeter used in the file.

#imports
import sys, getopt, re 

def main(argv):
    input_file=''
    output_file=''

    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print("Error: Unable to identify the given argument!")
        print('python3 linkExtract.py -i <input_file> -o <output_file>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('python3 linkExtract.py -i <input_file> -o <output_file>')
            sys.exit(2)
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg

        #Printing infromation about the input and output files 
        print("*"*40)
        print('Input file:',input_file)
        print('Output file:',output_file)
        print("*"*40)

        #Setting the input and output files 
        if output_file=="" or output_file==" ":
            log_file=open(input_file,"r")
            link_file=open("links.txt","a")
        elif input_file==" " or input_file=="":
            print("Error: No input file provided!")
            sys.exit(2)
        else:
            log_file=open(input_file,"r")
            link_file=open(output_file,"a")

        #Reading the input file line by line and extracting the links and writing them to output file 
        while True:
            line=log_file.readline()
            if line:
                words=line.split(delimeter)
                for word in words:
                    link_regex=re.compile("^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$")
                    link_match=link_regex.match(word)
                    if link_match:
                        link=link_match.group()+"\n"
                        link_file.write(link)
            else:
                break

            
        #closing files
        log_file.close()
        link_file.close()

        #Final termination message
        print("Extraction completed!")

if __name__ == "__main__":
    main(sys.argv[1:])
