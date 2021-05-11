#include <stdio.h>
#include <string.h>

void x_encrypt(char *input, char *output) {
	char key[1] = {'s'};

	int u;
	for(int i = 0; i < strlen(input); ++i) {
		output[i] = input[i] ^ (int)key[0];
	}
	int z = strlen(output);
    for(u=0;u< z;++u) {
        printf("%x ",output[u]);
    }
    printf("\n");
}

int main (int argc, char *argv[]) {
	char input[] = "Hello";
	
	char length[strlen(input)];
	x_encrypt(input, length);
	return 0;
}

