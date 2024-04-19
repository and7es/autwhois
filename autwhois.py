#!/usr/bin/env python

import sys
import os
import argparse

#Menu
parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -n MyCompany -d domains_list.txt\r\n")
parser.add_argument('-n', '--name', help="Domain name to check (example: company name)", required=True)
parser.add_argument('-d', '--domainslist', help="Path to list with domains extensions", required=True)
parser.add_argument('-o', '--output', help="Print the result in a file")
parser.add_argument("-v", "--verbose", help="Increase output verbosity and show Registry Domain ID", action="store_true")
args = parser.parse_args()

#Reading the domain extensions file
with open(args.domainslist, "r") as f:
	domainlist = f.read().splitlines()

	#Opening of the results file if it has been selected
	if args.output:
		fileoutput = open(args.output, 'w')

	#Recursive Whois
	for lastdomain in domainlist:

		#Checking verbosity
		if args.verbose:
			print('whois ' + args.name + '.' + lastdomain)

		#Whois command - Checking if there is a Registry Domain ID
		command = 'whois ' + args.name + '.' + lastdomain + ' | grep "Registry Domain ID" -m 1 | cut -d ":" -f1,2'
		result= os.popen(command).read()
		
		if result:
			
			#Checking verbosity
			if args.verbose:
				print(args.name + '.' + lastdomain + ' --> ' + result)
			else:
				print(args.name + '.' + lastdomain)

			#Writing results
			if args.output:
				fileoutput.writelines(args.name + '.' + lastdomain + '\n')

	#Closing results file when finished
	if args.output:
		fileoutput.close()

