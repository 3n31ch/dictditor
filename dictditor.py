__version__ = "1.0"
__author__ = "3n31ch"
__website__ = "http://www.elhacker.net/"

import re
from optparse import OptionParser

def printError(error):
	print "[ERROR] ", error

def dictditor(inputPath, outputPath, regex):
	inputFile = open(inputPath, "r")
	outputFile = open(outputPath, "w")
	pattern = re.compile(regex)
	for line in inputFile:
		word = line.replace("\n", "")
		if(pattern.match(word)):
			outputFile.write(line)
	inputFile.close()
	outputFile.close()
	return;


def main():

	print "DICTDITOR - Dictionary Editor"
	print "Author: ",__author__
	print __website__
	
	parser = OptionParser(usage="usage: python %prog [options]",
                          version= "%prog "+__version__ )
	parser.add_option("-i", "--input", 
		dest="input", 
		help="Dictionary to modify",
		metavar="FILE");
	parser.add_option("-o", "--output", 
		dest="output", 
		help= 'Modified dictionary.',
		metavar="PATH");
	parser.add_option("-r", "--regex", 
		dest="regex", 
		help= 'Regular expression to apply.',
		metavar="REGEX");

	(options, args) = parser.parse_args()

	if options.input and options.output and options.regex:
		dictditor(options.input, options.output, options.regex)
	else:
		printError("All options are necessary");
		parser.print_help()


if __name__ == '__main__':
	main()