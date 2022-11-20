# Pokemon-go-list-of-cp-calculator
Python script to determine all the pokemon/level/iv combination that have a given CP count. 

Please note that I see no other use to this than a game in communities consisting of sharing screenshots of specific pokemons of specific cp.

Format of the output :  
`<number> : <name> [<level>] - ATK:<attack> - DEF:<defense> - STA:<stamina>`

## Installation
```console
git clone https://github.com/DrankRock/Pokemon-go-list-of-cp-calculator.git
cd Pokemon-go-list-of-cp-calculator
python3 -m pip install -r requirements.txt
```

## Usage
```console
usage: theGamePogo.py [-h] [-m] [-n NUMBER] -i INPUT [-l MAXLEVEL] [-x MINLEVEL] [-o OUTPUT]

Python script to determine all the pokemon/level/iv combination that have a given CP count.

options:
  -h, --help            show this help message and exit
  -m, --mega            Authorize the research of mega pokemon.
  -n NUMBER, --number NUMBER
                        Search for a specific pokemon by number.
  -i INPUT, --input INPUT
                        input CP you are looking for.
  -l MAXLEVEL, --maxlevel MAXLEVEL
                        Sets a maximum level for found pokemons
  -x MINLEVEL, --minlevel MINLEVEL
                        Sets a minimum level for found pokemons
  -o OUTPUT, --output OUTPUT
                        Output file to store results
```
## Example 
```console
drankrock@BigDen:$ python3 theGamePogo.py -i 4000 --minlevel 45 --maxlevel 48
149 : Dragonite  [45.0] - ATK:15 - DEF:15 - STA:11
149 : Dragonite  [45.5] - ATK:14 - DEF:12 - STA:13
149 : Dragonite  [45.5] - ATK:14 - DEF:13 - STA:12
... (total results : 825)
```

## Source
Base stats can be found on [bulbapedia's list](https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_base_stats_(GO)).  
CP Multipliers have been calculated from a modified version of [pokemon.gameinfo](https://pokemon.gameinfo.io/en/tools/cp-calculator) 's javascript cp calculator.
