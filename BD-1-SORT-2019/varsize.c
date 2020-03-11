#include <stdio.h>

int main (void)
{
  printf("%16s=%zu\n", "sizeof(char)", sizeof(char));
  printf("%16s=%zu\n", "sizeof(short)", sizeof(short));
  printf("%16s=%zu\n", "sizeof(int)", sizeof(int));
  printf("%16s=%zu\n", "sizeof(long)", sizeof(long));
  return 0;
} /* main */
