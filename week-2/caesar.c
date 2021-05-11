# include<stdio.h>
# include<string.h>
# include<stdlib.h>

void caesar(char* p_text,int key){
    int i=0;
    int cyphervalue;
    while(p_text[i] != '\0' && i < strlen(p_text)-1){
        cyphervalue = (((int)p_text[i] -97  + key) % 26 + 97 );
        printf("%c",(char)cyphervalue);
        i++;
    }
    printf("\n");
}

int main(){
    int key = 1;
    char plaintext[50];
    printf("enter your plaintext: ");
    fgets(plaintext, sizeof(plaintext),stdin);
    printf("your ciphered text is: ");
    caesar(plaintext,key);
}