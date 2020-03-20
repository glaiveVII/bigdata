#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <errno.h>
#include <string.h>
#include <unistd.h>
#include <inttypes.h>
#include <float.h>
#include <getopt.h>

#include <sys/stat.h>
#include <sys/mman.h>

size_t read_human_size(char * s);


int main (int argc, char *argv[])
{
  printf("entrer dans le programme : ");

  /* on recupere le nom du fichier à la fin */

  char *nom_fichier = argv[argc-1];
  printf("%s \n", nom_fichier);

  /* on arrive bien à lire le fichier */

  /* Option parsing */
  size_t opt_s = 10;
  int opt_B = 0;
  int ch;

  printf("\n");
  printf("On est ici");
  printf("\n");

  /*printf("%d\n", getopt(argc, argv, "Bs:")); */

  while ((ch = getopt(argc, argv, "Bs:")) != -1)
    {
      printf("\n");
      printf("entering the while loop");
      printf("\n");
      switch (ch)
        {
          /* si opt_B vaut 1 c'est qu'il présent donc on fait l'option sinon non */
          case 'B': opt_B = 1; break;
          case 's':
          opt_s = read_human_size(optarg);
            if (opt_s == 0)
              {
                printf("taille non valide");
                exit(EXIT_FAILURE);
              }
            break;
          default:
            {
              printf("cas par default");
              exit(EXIT_FAILURE);
            }
        }
        printf("taille du opt_s %ld \n", opt_s);
    }
    if (opt_B == 1)
      {
        printf("ecriture en binaire requested");
      }

    FILE *fp;
    fp = fopen(nom_fichier, "r");
    if (fp != NULL)
      {
        printf("XXX");
      }

    else
      {
        printf("YYY");
      }
    fprintf(fp, "Testing...\n");

    fclose(fp);
  return(0);
}



size_t read_human_size (char * s)
{
char *endp;
int sh;
uintmax_t x;
errno = 0; x = strtoumax(s, &endp, 10);
if (errno || endp == s) goto error;
switch(*endp) {
  case 'k': sh=10; break;
  case 'M': sh=20; break;
  case 'G': sh=30; break;
  case 0: sh=0; break;
  default: goto error;
}
if (sh && endp[1]) goto error;
if (x > SIZE_MAX>>sh) goto error;
return x <<= sh;
error:
  errno=EDOM;
  return 0;
} /* read_human_size */
