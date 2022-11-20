# Pokemon-go-list-of-cp-calculator
Python script to determine all the pokemon/level/iv combination that have a given CP count. 

Please note that I see no other use to this than a game in communities consisting of sharing screenshots of specific pokemons of specific cp.

## Installation
```console
git clone https://github.com/DrankRock/Pokemon-go-list-of-cp-calculator.git
cd Pokemon-go-list-of-cp-calculator
python3 -m pip install -r requirements.txt
python3 theGamePogo.py -i 1234
```

## Usage
```console
usage: theGamePogo.py [-h] [-m] [-n NUMBER] -i INPUT [-l MAXLEVEL] [-o OUTPUT]

Python script to determine all the pokemon/level/iv combination that have a
given CP count.

options:
  -h, --help            show this help message and exit
  -m, --mega            Authorize the research of mega pokemon.
  -n NUMBER, --number NUMBER
                        Search for a specific pokemon by number.
  -i INPUT, --input INPUT
                        input CP you are looking for.
  -l MAXLEVEL, --maxlevel MAXLEVEL
                        Sets a maximum level for found pokemons
  -o OUTPUT, --output OUTPUT
                        Output file to store results
```

## Source
Base stats can be found on [bulbapedia's list](https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_base_stats_(GO)).  
CP Multipliers have been calculated from a modified version of [pokemon.gameinfo](https://pokemon.gameinfo.io/en/tools/cp-calculator) 's javascript cp calculator.
