## Details command :

Unzip a .tgz file :
```
tar -xvzf /path/to/yourfile.tgz
```

For me :

```
tar -xvzf /Users/pel_btc_coding/code/PelDoingCode/bigdata/BD-1-SORT-2019.tgz
```

then : comme on a un makefile deja tout fait ici

```
cd BD-1-SORT-2019
# then compile files
make
```

### Exercice 1 :

Ca nous genere des files generate :

Compiller un executable :
```
./nom_executable
```


Commande avancée :
```
./generate -r 100 -s 50
```

genere 50 element compris entre 0 et 100

```
./generate -r 100 -s 50 -B
```

-B : permet de donner les elements generer en code ascii

```
```
./generate -r 100 -s 50 -B > foo
```

```
# prend ce qui a dans le fichier foo pour le reecrire selon bin2asc
./bin2asc < foo
```

```
./generate -B > foo
./bin2asc -n 2 < foo
```

rq : on a un generateur pseudo aléatoire : on genere tjrs la meme sequence, sinon il faudrait initialiser le generateur aleatoire






