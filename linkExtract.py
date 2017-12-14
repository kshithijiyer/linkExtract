#linkExtract

#Purpose:
#linkExtract is a command-line tool which can be used to extact urls(links) from IRC log files.

#Author:Kshithij Iyer
#Email: ahole@disroot.org
#Date of Creation: 13/12/2017

#regex for links
#^((http[s]?|ftp):\/)?\/?([^:\/\s]+)((\/\w+)*\/)([\w\-\.]+[^#?\s]+)(.*)?(#[\w\-]+)?$

#Settings:
#The delimeter used in the file.
delimeter=" "

#imports
import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('linkExtract.py -i <inputfile> -o <outputfile>')
         sys.exit()
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
      return
   else:
      datafile=open(inputfile,"r")
      linkfile=open(outputfile,"a")
      

if __name__ == "__main__":
   main(sys.argv[1:])
