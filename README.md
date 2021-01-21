## Contingut

#### License

	Do What The F*ck You Want To Public License


#### class

	conte els fons d'escriptori per a cada assignatura

#### setup

	configura els fitxers /etc/profile i /etc/bash.bashrc per a aplicar l'script a tots els usuaris

#### .userconf.py

	script

	L'script fa 3 opcions, configura fons de pantalla, l'alias + carpetes necessaries, i el prompt

	En cas de voler una sola funcio, faria falta executar-lo utilitzant arguments

	Ex: Volem nomes configurar alias

	> "python .userconf.py 1"

	Per defecte fa les 3 funcions

##### Llegenda

	0 Escriptori

	1 Alias + carpetes necessaries

	2 Prompt

	3 Shell-login message

	D/d debugg

#### Funcionament

	L'script genera un fitxer anomenat ".sourcefile" situat a la carpeta home de l'usuari, esperat a ser utilitzat per l'usuari


#### Testing, es pot executar el fitxer amb debbug (i els nombres, no 'D' exclusivament)

	> "python .userconf.py 0 1 2 3 D"

	Per simular una hora fa falta anar a la linea 197 i comentar la variable "hour", i descomentar la variable "hour #hora simulada"
