#include <stdio.h>

int main(void) {
  int c;
  scanf("%d", &c);
  for(int a=0; a<=100; a++){
    for(int b=0; b<=100; b++){
      if(a>=b && c>a)
      printf("%c", '*');
    }
    printf("\n");
  }
  return 0;
}