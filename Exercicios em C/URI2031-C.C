#include <stdio.h>
#include <string.h>
int ppa(char primeiro[10],char segundo[10]){
	 	
		int i=0;
	 	char p[10]="pedra",at[10]="ataque",pp[10]="papel";
	 	
        if ((strcmp (primeiro,p)==0) && (strcmp (segundo,p)==0)){
        	return 1;
        }else
    
		if ((strcmp (primeiro,at)==0) && (strcmp (segundo,at)==0)){
			return 2;
		}else
		
		if ((strcmp (primeiro,pp)==0) && (strcmp (segundo,pp)==0)){
			return 3;
		}else 
		
		if ((strcmp (primeiro,at)==0) && (strcmp (segundo,pp)==0) ||(strcmp (primeiro,at)==0) && (strcmp (segundo,p)==0) || (strcmp (primeiro,p)==0) && (strcmp (segundo,pp)==0)){
           return 4;
    	}else 
		
		if ((strcmp (primeiro,p)==0) && (strcmp (segundo,at)==0) || (strcmp (primeiro,pp)==0) && (strcmp (segundo,at)==0)||(strcmp (primeiro,pp)==0) && (strcmp (segundo,p)==0)){
        	return 5;
    }
	}
	
int main (){
    int j,n,result;
    char p[10],s[10];
    scanf ("%d", &n);
    for(j=0;j<n;j++){
        scanf ("%s",p);
        scanf ("%s", s);
        result = ppa(p,s);
    if (result==1){
        printf("Sem ganhador\n");
	}else
        if (result==2){
        printf("Aniquilacao mutua\n");
    }else
        if (result==3){
        printf("Ambos venceram\n");
      
    }else
        if (result==4){
        printf("Jogador 1 venceu\n");
        
    }else
        if (result==5){
        printf("Jogador 2 venceu\n");
	}
	}
	return 0;
	}
