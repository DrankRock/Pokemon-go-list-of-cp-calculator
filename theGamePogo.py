import numpy as np
import argparse
from math import floor
import sys

CHERCHER_NUMERO=-1
MAX_LEVEL = 50

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
	f = open(args.output[0], 'w')
	sys.stdout = f

def can_convert_to_int(string):
    try:
        int(string)

        return True
    except ValueError:
        return False

# init multipliers dictionnary

multipliers = {}
with open("CP_multiplier.csv", 'r') as f:
	for line in f :
		current = line.rstrip().split(' ')
		multipliers[str(float(current[0]))] = float(current[1])

# puis ils appliquent : 
# e % 2 ? Math.pow((Math.pow(t[(e - 1) / 2 - 1], 2) + Math.pow(t[(e - 1) / 2], 2)) / 2, .5) : t[e / 2 - 1]

# 0 false, 1 true
# donc si niveu = 15, e%2 = true, et on effectue : 
# pow( ( power (armult[niveau-1])/2 -1 ), 2  ) + power()
# avec e = niveau*2. Donc en fait, si le niveau est pa
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
		if CHERCHER_NUMERO != -1 and num != CHERCHER_NUMERO :
			search = False
		hp = int(current[3+add])
		atk = int(current[4+add])
		defn = int(current[5+add])
		if search:
			# print(num, name, hp, atk, defn)
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
								# print("CP : {}\nPartie 1 : {}\nPartie 2 : {}\n Partie 3 : {}\n".format(CP, pow((hp+individual_hp)*cp_mult, .5) , (atk+individual_atk) * cp_mult , pow((defn+individual_def)*cp_mult, .5)))
													
								CP = round(CP)
								# print(name," ",CP," ")
								# print(round(CP))
								if CP == search_CP :
									numberOfCorresponding+=1
									print("{} : {} [{}] - ATK:{} - DEF:{} - STA:{}".format(num, name, level,individual_atk, individual_def, individual_hp))
									#print("{}\t{}\t{}\t{}\t{}".format(name, level,individual_atk, individual_def, individual_hp))
									#print("CP : {}\nPartie 1 : {}\nPartie 2 : {}\n Partie 3 : {}\n".format(CP, pow((hp+individual_hp)*cp_mult, .5) , (atk+individual_atk) * cp_mult , pow((defn+individual_def)*cp_mult, .5)))
									#print("CP mult : ",cp_mult)
print("number of matches : "+str(numberOfCorresponding))