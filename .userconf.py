#!/bin/python3

##
#Author: Oriol Filter
##



from subprocess import Popen, PIPE, run
from os import system
from random import randint

import glob
from datetime import datetime

import os
import getpass

from sys import argv

# Visible output, disabled, testing
#print("UID: ",os.getuid())
#print("HOME: ",os.path.expanduser('~'))
#print("USER: ",getpass.getuser())

from pathlib import Path

# https://stackoverflow.com/questions/39358092/range-as-dictionary-key-in-python
# $HOME/.prompt.py  && source $HOME/.sourcefile  # Insertar en bashrc

def changeBackground(img):
	if "gnome" in os.environ["DESKTOP_SESSION"]:
	        Popen(f"gsettings set org.gnome.desktop.background picture-uri '{img}'".split(" "), stdout=PIPE, stderr=PIPE)
	else:
	        Popen(['feh', '{}'.format(img), '--bg-max'], stdout=PIPE, stderr=PIPE)

def retriveFiles(path,extension):
        files=[]
        for ext in extension:files.extend(glob.glob(pathname=path+ext))
        return files

def returnRandom(list):
        return list[randint(0, len(list) - 1)]


class_img_folder="/shared/wallpapers/class"
class_folder="$HOME/class"


class Config:
	def __init__(self):
		self.module='-1' # No te classe
		# Generate config

	def generate_config(self,options=['0','1','2','3']):
		color= {"red": "\[$(tput setaf 1)\]", #Bash color picker
			"green": "\[$(tput setaf 2)\]",
			"yellow": "\[$(tput setaf 3)\]",
			"blue": "\[$(tput setaf 4)\]",
			"pink": "\[$(tput setaf 5)\]",
			"cyan": "\[$(tput setaf 6)\]",
			"light_gray": "\[$(tput setaf 7)\]",
			"drak_gray": "\[$(tput setaf 8)\]",
			"light_red": "\[$(tput setaf 9)\]",
			"light_green": "\[$(tput setaf 10)\]",
			"light_yellow": "\[$(tput setaf 11)\]",
			"light_blue": "\[$(tput setaf 12)\]",
			"light_pink": "\[$(tput setaf 13)\]",
			"light_cyan": "\[$(tput setaf 14)\]",
			"white": "\[$(tput setaf 15)\]",
			"black": "\[$(tput setaf 16)\]",
			"reset": "\[$(tput init)\]",

		}

		source_file='' # Build config file, after running this script srouce 'file'

		# If Path does not exist, create folder

		# Dict
		alias_dic={	0:None,
				8:{'alias py="python3"'},
				11:{'alias vb="virtualbox"'},
				9:{'alias fire="firefox"',
				   'alias jet="jetbrains-toolbox"'}
		}

		if '0' in options:	# Deskop Image/config
			if 'd' in options or 'D' in options: print("Generated desktop #D")
			if self.module=='-1':	self.img_folder=f"{class_img_folder}/{self.module[0]}/"
			else:	self.img_folder="/shared/wallpapers/class/{}/".format(self.module[0])  # En cas de varies classes agafa nomes la primera
			imgExtensions=["*.jpg","*.png","*.tiff","*.webp","*.jpeg"] 
			imgList=retriveFiles(self.img_folder,imgExtensions)
			if imgList: changeBackground(returnRandom(imgList))

		if '1' in options:	# Alias/functions
			if 'd' in options or 'D' in options: print("Generated alias #D")
			if self.module == '-1': work_folder=f"{class_folder}/{self.module[0]}"
			else: work_folder=f"{class_folder}/{self.module[0]}" # Agafa la primera igual que l'escriptori

			os.system(f"mkdir {work_folder} -p ") # Create dir # Si es fa el directory en bash, no fa falta limitar a python3.5
#			print(f"mkdir {work_folder} -p ") # Create dir # Si es fa el directory en bash, no fa falta limitar a python3.5

			# Default funtions
			if self.module=='-1':	pass
			else:
				source_file+=f'alias work="cd $WORKFOLDER"\n'
				source_file+=f'export WORKFOLDER={work_folder}\n'


			for module in self.module:
				try:
					for alias in alias_dic[module]:
						#print (alias)
						source_file+=alias+"\n"
				except KeyError: pass

		if '2' in options:	# Prompt
			if 'd' in options or 'D' in options: print("Generated prompt #D")

			if self.module=='-1':
				source_file+="""PS1="[\\u@\\h \\W]\\$" \n"""
			else: 	
#				source_file+=f"""PS1="{color["light_blue"]}{[f"M{module:>02}" for module in self.module]}{color["light_red"]}~~{color["green"]}{[dic_mod[module] for module in self.module]}{color["pink"]}\\$> {color["reset"]}"\n"""
				source_file+=f"""PS1="{color["light_blue"]}{[f"M{module:>02}" for module in self.module]}{color["light_red"]}~~{color["light_green"]}{[dic_mod[module] for module in self.module]}{color["light_yellow"]}\\W \\u> {color["reset"]}"\n"""
		if '3' in options:	# Shell-login  message # No volem personalitzar amb colors i assignatures ja que aixo pot arribar a ser molest al haber varies linies i treballar en varis terminals
			if 'd' in options or 'D' in options: print("Shell-login message #D")
			source_file+='printf "###########$USER############\n########$HOME#############\n########$UID######\n"\n'
			

		# for x in sys.argv[1]: if x=True: change all; else: change background


		os.system(f"echo '{source_file}'>{os.path.expanduser('~')}/.sourcefile") #Escriure be el fitxer estaria bastant be


def return_range(a,b):
	for x in range(a,b):
		print (x)
	return range(a,b)

class RangeDict(dict):
    def __getitem__(self, item):
        if not isinstance(item, range):
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item)



stealth_check = {
			1: RangeDict({range(1550,1730): [8,11],
				    range(1730,1910): [9]
			}),
			2: RangeDict({range(1550,1730): [8,11], #Dimarts
				    range(1730,1910): [16,17]
			}),
			3: RangeDict({range(1550,1730): [5], #Dimecres
				    range(1730,1910): [8,11]
			}),
			4: RangeDict({range(1550,1730): [8,11], #Dijous
				    range(1730,1910): [16,17]
			}),
			5: RangeDict({range(1640,1820): [5], #Divendres
				    range(1820,1910): [0] # Tutoria
			})
##			6: ({RangeDict({range(1,6): 'thunderstorm', range(6,11): 'tip-toe'})
}

dic_mod=({0:'Tutoria', # Diumenge # BASH
	6:'Sistemes informatics', # Dilluns	
	8:'Serveis de xarxa',
	5:'Fonaments del maquinari',
	16:'Ciberseguretat',
	11:'Seguretat i alta disponivilitat',
	9:'Implementacio de sistemes operatius'
})

dicDays=({7:'Diumenge',
	1:'Dilluns',
	2:'Dimarts',
	3:'Dimecres',
	4:'Dijous',
	5:'Divendres',
	6:'Dissabte'
})


# Get Current Weekday,And,Hour

### MAIN 

#arguments=[element for element in argv[1:]]


#print ("AAARRRRR ",arguments)

now = datetime.now() #Init
hour=now.strftime("%H%M") # No es necessari
#hour=1700 #Hora simulada ## Ideal del format hora-minuts copiada a l'Irena
#print(hour)

#dayNumber=int(Popen(['date', '+%w'], stdout=PIPE, stderr=PIPE, stdin=PIPE).stdout.read().decode().replace('\n','')) #BASH
dayNumber=int(now.strftime("%V")) # No es necessari

config=Config()


try:
	config.module=stealth_check[dayNumber][int(hour)]
except KeyError: pass #Fora d'horaris
if  argv[1:] == []:	config.generate_config()
else:  	config.generate_config(argv[1:])


#print(dicDays[dayNumber])
