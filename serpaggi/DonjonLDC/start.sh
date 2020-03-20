#!/bin/bash
#set -x

txt() {
cat <<- EOM
.TH DonjonLDC 6 "Mars 2019"
.SH NOM
DonjonLDC \- découvrir les commandes de manipulation de fichiers.
.SH DESCRIPTION
Vous voici dans une petit jeu/tutoriel pour découvrir l'arborescence des fichiers et les commandes de base de Linux.
.PP
Vous débutez avec 3 commandes à disposition :
.TP
.B ls
permet de lister le contenu du répertoire courant.
.TP
.B cat \fIfichier
permet d'afficher le contenu du fichier dont le nom est passé en paramètre.
.TP
.B cd \fIrépertoire
permet de se déplacer dans le répertoire dont le nom est passé en paramètre.
.PP
Dans chaque répertoire vous trouverez un ou plusieurs fichiers à lire vous permettant d'apprendre de nouvelles commandes. Elles vous permettront de passer à la suite et ainsi d'avancer dans le
.I jeu.
.SH DÉBUTER
Avec la commande
.B cd
rendez-vous dans le répertoire
.B niveau_1
pour commencer.
EOM
}

NL=$(txt | wc -l | cut -d' ' -f1)

if [[ "$OSTYPE" == "darwin" ]]
then
	echo -e "\nNOTE: Vous voyez ce texte en mode degrade sans accents.\n"
	myconv() {
		sed -e 'y/àäâçéèêëïîôöûüùÀÄÂÇÉÈÊËÏÎÔÖÛÜÙ/aaaceeeeiioouuuAAACEEEEIIOOUUU/'
	}
	CONV=myconv
else
	myconv() {
		preconv
	}
fi

echo $CONV

if [ "$1" == "-p" ];
then
	txt | myconv | groff -Tutf8 -man | cat
else
	txt | myconv | groff -Tutf8 -man | less -X -E -F -d
fi
