#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <unistd.h>
#include <inttypes.h>

static char * version = "@(#) format binary uint32 read from stdin in decimal";

void usage (char *prgname)
{
  fprintf(stderr, "%s [-n <nb_of_uint32_by_line>]"
		  " [-t <separator>]"
		  " [-f <format>]\n"
		  "\tfirst character of <separator> will be used between two numbers on a line\n"
		  "\t<format> will be used to format (printf) numbers and should match uint32\n",
	  prgname);
} /* usage */

int main (int argc, char * argv[])
{
  char * prgname; /* name of launched program */
  char * format = "%"PRIu32;
  char * opt_t  = "\t";
  int opt_n = 1; /* number of printed ints by line */

  {
  if ((prgname = strrchr(argv[0], '/')))
    prgname++;
  else
    prgname=argv[0];
  }

  { /* Option analysis */
  int ch;

  while ((ch = getopt(argc, argv, "n:t:f:")) != -1)
    {
    switch (ch)
      {
      case 'n': opt_n = atoi(optarg); break;
      case 'f': format = optarg; break;
      case 't': opt_t = optarg; break;

      case '?':
      default:
	usage(prgname);
	exit(EXIT_FAILURE);
      }
    }
  }

  {
  uint32_t x;

  int first_on_line = 1;
  int count = 0;
  while (fread(&x, sizeof(uint32_t), 1, stdin) == 1)
    {
    if (first_on_line)
      first_on_line=0;
    else
      putchar(opt_t[0]);
    printf(format, x);
    count++;
    if (count == opt_n)
      {
      count=0;
      putchar('\n');
      first_on_line = 1;
      }
    }
  if (! first_on_line)
    putchar('\n');
  }
return EXIT_SUCCESS;
} /* main */
