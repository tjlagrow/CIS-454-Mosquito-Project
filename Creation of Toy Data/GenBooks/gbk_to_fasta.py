"""
gbk_to_fasta.py
Author: Theodore LaGrow
Language: Python 3.5.1
Packages Needed: biopython, random
Description of Code:

"""

import sys
from Bio import SeqIO
import random	

def create_fasta():
	"""

	i = 1
	
	while i < 11:
		genBankName = "{}{}{}".format("ecoli", i, ".wg.gbk")
		fastaName = "{}{}{}".format("ecoli", i, ".fasta")
		
		input_handle = open(genBankName, "rU")
		output_handle = open(fastaName, "w")

		sequences = SeqIO.parse(input_handle, "genbank")
		count = SeqIO.write(sequences, output_handle, "")

		output_handle.close()
		input_handle.close()
	

		i += 1
		"""

def get_reed_data_forward():
	k = 1
	while k < 11:
		parse_file = "{}{}{}".format("ecoli", k, ".fasta")
		record = SeqIO.read(parse_file,'fasta')
		toyFile = open("toy_data.txt", "a")
		toyTemp = open("toy_file.txt", "r+")
		#print(record.seq) # used to test to see the sequence
		toyTemp.write(str(record.seq))
		toyTemp.close() # I just strong handed this, python was being dumb so I just closed the file and reopened it
		toyTemp = open("toy_file.txt", "r")

		count = 0
		while count < 3: # this is to go through each ecoli genome 3 times

			i = 0

			for line in toyTemp:
				while i < len(line) and (len(line) - i) > 99:
					reed_len = random.randint(100, 180)
					toyFile.write("%s\n" % line[i:(i+reed_len)])
					#print(line[i:(i+reed_len)]) #for testing
					i += reed_len

			print("{}{}{}{}{}".format("ecoli", k, ".fasta has been Aluminated using forwards parsing ", count+1, " times.")) #this is to show the program is running so it is not a silent excecution.

			
			count += 1

		toyFile.close()
		toyTemp.close()

		k += 1

def get_reed_data_backwards():
	
	k = 1
	while k < 11:
		parse_file = "{}{}{}".format("ecoli", k, ".fasta")
		record = SeqIO.read(parse_file,'fasta')
		toyFile = open("toy_data.txt", "a")
		toyTemp = open("toy_file.txt", "r+")
		#print(record.seq) # used to test to see the sequence
		toyTemp.write(str(record.seq))
		toyTemp.close()
		toyTemp = open("toy_file.txt", "r")

		count = 0
		while count < 3: # this is to go through each ecoli genome 3 times

			i = 0

			for line in toyTemp:

				reverse = line[::-1] #reverse the genome to get the back parts of the genome

				while i < len(reverse) and (len(reverse) - i) > 99:
					reed_len = random.randint(100, 180)
					new_line = reverse[i:(i+reed_len)] # put the string back to correct ordering
					toyFile.write("%s\n" % new_line[::-1])
					#print(line[i:(i+reed_len)]) #for testing
					i += reed_len

			print("{}{}{}{}{}".format("ecoli", k, ".fasta has been Aluminated using backwards parsing ", count+1, " times.")) #this is to show the program is running so it is not a silent excecution.
			
			count += 1

		toyFile.close()
		toyTemp.close()

		k += 1


if __name__ == '__main__':
	#create_fasta() # do not need this function after fasta files are already created
	get_reed_data_forward()
	get_reed_data_backwards()

