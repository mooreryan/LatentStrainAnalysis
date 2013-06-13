#!/usr/bin/env python

import sys, getopt
import glob,os

help_message = 'usage example: python merge_partition_parts.py -i /project/home/cluster_vectors/ -o read_partitions/'
if __name__ == "__main__":
	try:
		opts, args = getopt.getopt(sys.argv[1:],'hi:o:',["inputdir="])
	except:
		print help_message
		sys.exit(2)
	for opt, arg in opts:
		if opt in ('-h','--help'):
			print help_message
			sys.exit()
		elif opt in ('-i','--inputdir'):
			inputdir = arg
			if inputdir[-1] != '/':
				inputdir += '/'
		elif opt in ('-o','--outputdir'):
			outputdir = arg
			if outputdir[-1] != '/':
				outputdir += '/'
	FP = glob.glob(os.path.join(inputdir,'*.fastq.*'))
	FPl = list(set([fp[fp.rfind('/')+1:fp.index('.fastq')] for fp in FP]))
	FPl.sort()
	for group in FPl:
		gp = [fp for fp in FP if inputdir+group+'.fastq' == fp[:fp.rfind('.')]]
		gp = [fp for fp in gp if '.empty' not in fp]
		if len(gp) > 0:
			os.system('cat '+' '.join(gp)+' > '+outputdir+group+'.fastq')
			os.system('touch %s.empty' % (gp[0]))
			os.system('rm '+' '.join(gp))