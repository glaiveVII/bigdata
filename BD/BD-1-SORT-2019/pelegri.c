#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>
#include <unistd.h>
#include <assert.h>
#include <string.h>
#include <getopt.h>
#include <math.h>

struct item { uint32_t u[2]; };

/*comparison function for qsort*/

int compare(const void* A, const void* B)
{
	const uint32_t *a = A;
	const uint32_t *b = B;

	if (a[0] < b[0]) { return (-1); }
	if (a[0] > b[0]) { return (1); }

  if (a[0] == b[0])
	{
		if (a[1] < b[1])
		{
			return(-1);
		}
		if (a[1] > b[1])
		{
			return(1);
		}
		if (a[1] == b[1])
		{
			return(0);
		}
	}
	return(0);
}

/* ASCII output */
void item_print (struct item * v)
{
  printf("%"PRIu32" %"PRIu32, v->u[0], v->u[1]);
}

/* binary output */
void item_write (struct item * v)
{
  fwrite(v, sizeof(struct item), 1, stdout);
}

size_t getFilesize(const char* filename)
{
	struct stat s;
	stat(filename, &s);
	if (stat == -1)
	{
		perror("fstat failed\n");
		exit(EXIT_FAILURE);
	}
	return s.st_size;
}

struct item* merge(struct item* A, struct item* B)
{
	/*  */
}

int main(int argc, char *argv[])
{
	char * prgname; /* name of launched program */

	{ /* getting the name of the launched program */
		if ((prgname = strrchr(argv[0], '/')))
			prgname++;
		else
			prgname = argv[0];
	}

	size_t opt_s; /* opt_s is the size of a chunk */
	char* filename; /* name of the file to sort */

	{ /* Option parsing */
		int ch;
		int opt_B = 0; /* 0 for ASCII output, 1 for binary output */

		while ((ch = getopt(argc, argv, "Bs:")) != -1)
		{
			switch (ch)
			{
			case 'B':
				opt_B = 1;
				break;
			case 's':
				opt_s = atoi(optarg);
				if (opt_s == 0)
				{
					perror("error");
					exit(EXIT_FAILURE);
				}
				break;
			case '?':
				filename = optarg;
				break;
			}
		}
	}

	int fichier = open(filename, O_RDWR);

	if (fichier == -1)
	{
		perror("open failed\n");
		exit(EXIT_FAILURE);
	}

	size_t filesize = getFilesize(filename);
	struct item* file = mmap(NULL, filesize, PROT_READ, MAP_PRIVATE, fichier, 0);

	if (file == MAP_FAILED)
	{
		perror("mmap failed %d\n");
		exit(EXIT_FAILURE);
	}
	else
	{
		printf("Size of file:\n");
		printf("%jd bytes\n", filesize);
	}

	{ /* slicing file, sorting and merging */
		size_t n = ceil(filesize / opt_s); /* number of chunks*/
		size_t i = 1; /* counter */

		while (i != n)
		{
			size_t j;

			for (j = (i - 1)*opt_s; j < n*opt_s; j++) /* j is the beginning of the chunk to sort */
			{
				struct item* fragment = mmap(j, j+opt_s-1, PROT_READ, MAP_PRIVATE, fichier, 0);
				qsort(fragment, opt_s, sizeof(struct item *), *compare);
				i = i + 1;
			}
		}

		/* merging the sorted chunks */
		size_t k = n; /* number of chunks */
		size_t m = 0; /* counter of steps */

		while (k != 1)
		{
			size_t l;

			for (l = 1; l < k+1; l = l+2)
			{
				struct item* A = mmap((l-1)*opt_s, l*opt_s - 1, PROT_READ, MAP_PRIVATE, fichier, 0);
				struct item* B = mmap(l*opt_s, (l + 1)*opt_s - 1, PROT_READ, MAP_PRIVATE, fichier, 0);
				merge(A, B);
				k = ceil(k / 2); /* after the merger, the number of chunk is divided by 2 */
				m = m + 1;
			}
		}
	}

	printf("File successfully sorted\n");

	return(0);
}
