# Shell command cheat sheet :

Unzip file
```
$> gunzip data.gz
```

Type data file
```
$> file data
```

Info sur un document
```
ls -l data
```

Nb ligne du doc
```
$> wc -l data
```

Obtenir le contenu d'une variable
```
$> echo X
```

Obtenir le contenu d'un file
```
$> cat <file>
```

Dowload file
```
$> curl -O <URL_TO_FILE>
```

Find things in file
```
$> grep <file>
```

Usefull if you want to clean your laptop activity :

all running process
```
$> ps ax
```

info of all important running process
```
$> top
```

trouver doc dans un fichier utiliser la commande 'find' et 'find(1)' pour de la doc


info of all running process
```
$> ps
```
afficher le contenu du fichier
```
$> cat <file>
```

savoir le type du fichier
```
$> file <file>
```

acceder au manuel d'une commande
```
$> man command
```

equivalent de cat pour les fichiers longs
```
$> less <file>
```

avoir plus d'info sur les fichiers du repertoire
```
$> ls -l
```

```
$> rm - pour supprimer des fichiers
$> rmdir - pour supprimer des répertoires
```


kill process by giving the id
```
$> kill <pid>
```

Command annexe :
```
!! : execute la derniere commande

```

Copy element :
```
$> cp file path_to_dir
```

```
find [options] [répertoires] [critère] [action]
```

```
 ps - Afficher l'état des processus en cours.
```

unzip file
```
gunzip XXX.gz
```

word count : use -c to get number of byte and -l number of line
```
wc file
```

ues to tail to print the last n lines of the file

The grep utility searches any given input files, selecting lines that
     match one or more patterns.

Mesure the time of a command :grep -i mobile 20190222-dump.csv > mobiles.csv
```
time command
```

```
X=10
echo $X : return 10
```

Commentaire : tte commande commencant par #

get all element starting with the expression
```
grep [options] <expression> <fichiers>...
```

```
La commande find(1), contrairement à grep, va rechercher un ensemble de fichiers dontles caractéristiques (nom, droits, date de création, ...) correspondent à certains critères. Lecontenu de ces fichiers n'est donc pas examiné.
```


Other useful commands :

```
kill
top
man
echo
chmod
date
sort
cut
uniq

```













