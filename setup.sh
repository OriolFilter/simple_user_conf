#!/bin/bash
SCRIPTFOLDER="$(dirname $0)"


#actualitzar a variables? no

mkdir -p /shared/wallpapers
mkdir -p /shared/scripts

# Setup files
sudo cp $SCRIPTFOLDER/class /shared/wallpapers/ -r
sudo cp $SCRIPTFOLDER/.userconf.py /shared/scripts/
sudo chmod 755 /shared -R

# Setup on login
printf "python3 /shared/scripts/.userconf.py 0 \n" | sudo tee -a /etc/profile > /dev/null # Nomes genera fons de pantalla

# Setup on terminal-session
printf "python3 /shared/scripts/.userconf.py 1 2 3 && source \$HOME/.sourcefile \n" | sudo tee -a /etc/bash.bashrc > /dev/null # only prompt, alias ,folders and shell-login message

printf "IMPORTANT, llegir README.md\nNo es pot fer de forma viable, ja que primer s'executa aquest, i despres el situat a la carpeta d'usuari, per a fer funcionar aquest faria falta eliminar el $HOME/.bashrc (o moure de forma temporal, o es podria comentar la linea on configura la variable PS1, per aixo fara falta modificar el fitxer de forma MANUAL)\n"
