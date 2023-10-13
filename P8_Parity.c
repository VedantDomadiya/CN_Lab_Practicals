#include<stdio.h>             
#include<string.h>         
void main(){
        char binary_String[100];
        printf("Enter the String");
        scanf("%s",binary_String);
        int onescount = 0;
        
        for (int i = 0; i<strlen(binary_String); i++)
        {
            if(binary_String[i] == '1'){
                onescount++;
            }
        }
        if (onescount % 2 == 0)
        {
            printf("even parity : %d ones are present in the string",onescount );
        }
        else{
            printf("Odd parity : %d ones are present in the string",onescount);
        }
        
}
