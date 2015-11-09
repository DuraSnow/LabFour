#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 50
#define maxlenth 200
typedef struct makmap{
    int ft[20][200];
    int l[20];
}findt;


void print(char s[], char t[])
{
    int k,m,i,j;
    char listl[] = "abcdefghij";
    int a[127]={0};
    findt mapl;
    int max,max_n,temp;
    int d[maxlenth][maxlenth];
    int dx[400]={0};
    memset(&mapl,0,sizeof(findt));

    m = 0;
    for(k=0;k<10;k++)
    {
        a[listl[k]] = m;
        m++;
    }

    for(i=0;;i++)
    {
        if(s[i]==0) break;
        mapl.ft[ a[ s[i] ] ][ mapl.l[ a [s [i] ] ] ] = i+1;
        mapl.l[a[s[i]]]++;
    }



    for(i=0;;i++){
        if(t[i]==0) break;
        for(j=0;;j++){
            if(mapl.ft[a[t[i]]][j]==0)  break;
            d[i][j]=mapl.ft[a[t[i]]][j] - 1 - i;
            dx[d[i][j]+199]=dx[d[i][j]+199]+1;
        }
        d[i][j]='\0';
    }//Œª“∆±ÌµƒΩ®¡¢


    max=dx[0];
    max_n=0;
    for(i=1;i<400;i++){
        if(max<dx[i]){
            max=dx[i];
            max_n=i;
        }
    }

    printf("\n◊Ó¥Û∆•≈‰Œª“∆Œ™£∫%d\n",-(max_n-199));
    printf("∆•≈‰ ˝Œ™£∫%d\n",max);

}

int main()
{
    char str_database[] = "aaaaabbbbbcccccdddddeeeeefffffggggghhhhhhiiiiijjjjj";
    char str_test1[] = "bbbbbccaaa";
    char str_test2[] = "bbbefcahcj";
    char str_test3[] = "ahidebejia";
    print(str_test1, str_database);
    print(str_test2, str_database);
    print(str_test3, str_database);

    return 0;
}s