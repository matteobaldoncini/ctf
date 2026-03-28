#include <stdio.h>

int main(int argc, char** argv){

  printf("indirizzo argv[0]: %p\n", argv);
  char ** argv1 = argv+1;
  printf("indirizzo argv[1]: %p\n", argv1);
  char* ind_argv1 = *argv1;
  printf("indirizzo contenuto in argv[1]: %p\n", ind_argv1);
  
  printf("stringa contenuta in argv[1]: "); 
  while(*ind_argv1 != '\0'){
    printf("%c", *ind_argv1++);
  }

  return 0;
}
