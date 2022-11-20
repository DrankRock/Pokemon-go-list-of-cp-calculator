import numpy as np
import argparse
from math import floor
import sys

CHERCHER_NUMERO=-1
MAX_LEVEL = 50
useFile = False

parser = argparse.ArgumentParser(description='Check if a set of weekly activities would overlap if put together.')
parser.add_argument('-m', '--mega', help='Authorize the research of mega pokemon.', required=False, action='store_true')
parser.add_argument('-n', '--number', help='Search for a specific pokemon by number.', required=False, action='store', nargs=1)
parser.add_argument('-i', '--input', help='input CP you are looking for.', required=True, action='store', nargs=1)
parser.add_argument('-l', '--maxlevel', help='Sets a maximum level for found pokemons', required=False, action='store', nargs=1)
parser.add_argument('-o', '--output', help='Output file to store results', required=False, action='store', nargs=1)

args = parser.parse_args()

CHERCHER_MEGA=args.mega

if args.number != None :
	CHERCHER_NUMERO = int(args.number[0])

search_CP = int(args.input[0])
if args.maxlevel != None :
	MAX_LEVEL = int(args.maxlevel[0])

if args.output != None :
	outputfile = open(args.output[0], 'w')
	useFile = True
	

def can_convert_to_int(string):
    try:
        int(string)

        return True
    except ValueError:
        return False


multipliers = {}
with open("CP_multiplier.csv", 'r') as f:
	for line in f :
		current = line.rstrip().split(' ')
		multipliers[str(float(current[0]))] = float(current[1])

numberOfCorresponding = 0
with open("Base_Pogo_Stats.csv", 'r') as f :
	for line in f :
		current = line.rstrip().split('\t')
		add=0
		search = True
		if not can_convert_to_int(current[3]):
			add=1
			name = str(current[2])+" "+str(current[3])
			if not CHERCHER_MEGA:
				search = False
		else :
			name = str(current[2])

		num = int(current[0])
		if useFile :
			print("\r[{}] - matches : {}".format(num, numberOfCorresponding),end="", flush=True)
		if CHERCHER_NUMERO != -1 and num != CHERCHER_NUMERO :
			search = False
		hp = int(current[3+add])
		atk = int(current[4+add])
		defn = int(current[5+add])
		if search:
			for level in np.arange(1, 50.5, 0.5):
				if level <= MAX_LEVEL:
					for individual_atk in range(1, 16) :
						for individual_def in range(1, 16) :
							for individual_hp in range(1, 16) :
								cp_mult = multipliers[str(level)]
								attack = floor((atk+individual_atk)*cp_mult)
								defense = floor((defn+individual_def)*cp_mult)
								stamina = floor((hp+individual_hp)*cp_mult )
								CP = floor(.1 * pow((hp+individual_hp)*cp_mult, .5) * (atk+individual_atk) * cp_mult * pow((defn+individual_def)*cp_mult, .5) )				
								CP = round(CP)
								if CP == search_CP :
									numberOfCorresponding+=1
									if useFile :
										print("{} : {} [{}] - ATK:{} - DEF:{} - STA:{}".format(num, name, level,individual_atk, individual_def, individual_hp), file=outputfile)
									else: 
										print("{} : {} [{}] - ATK:{} - DEF:{} - STA:{}".format(num, name, level,individual_atk, individual_def, individual_hp))

print("number of matches : "+str(numberOfCorresponding))