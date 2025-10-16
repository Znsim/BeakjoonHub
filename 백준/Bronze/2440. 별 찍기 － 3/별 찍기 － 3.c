#include <stdio.h>

int main() { //여기에 코드넣기
  int a;
  scanf("%d", &a);
  for(int b=a; b>0; b--){ //입력값에서 부터 1나씩 -1.
    for(int c=0; c<b; c++){//
      printf("*");
    }
    printf("\n");
  }
  return 0;
}