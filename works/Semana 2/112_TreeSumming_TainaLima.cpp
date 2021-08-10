#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int RESP;

int existsPathSum(int sum, int value, char *tree_pointer){
    int node_value, is_not_leaf, is_neg_number;
    while(*tree_pointer == ' ' || *tree_pointer == '\n')
		*tree_pointer = getchar();

    if(*tree_pointer == '('){
        node_value = 0, is_not_leaf = 0, is_neg_number = 1;

        while(true){
            *tree_pointer = getchar();
            if(*tree_pointer >= '0' && *tree_pointer <= '9'){ //Verifica se o pointeiro é um número
                node_value = node_value*10 + *tree_pointer-'0'; //Se sim, converte ele pra número 
                is_not_leaf = 1; //Como achei um número após um (, ainda não é folha

            }
            else{
                if(*tree_pointer == '-'){ //Caso o número seja negativo
                    is_neg_number = -1;
                }
                else{
                    break;
                }
            }
        }
        node_value *= is_neg_number;
        while(*tree_pointer == ' ' || *tree_pointer == '\n')
		    *tree_pointer = getchar();

		if(is_not_leaf == 0) {
			return 0; // Se já cheguei na folha daquele caminho em específico, volta a recursão
		}

        int left_path = existsPathSum(sum+node_value, value, tree_pointer); //Verifico se a soma bate indo pelo caminho da esquerda
		while((*tree_pointer = getchar()) != '(');

		int right_path = existsPathSum(sum+node_value, value, tree_pointer); //Verifico se a soma bate indo pelo caminho da direita
		while((*tree_pointer = getchar()) != ')');

		if(left_path == 0 && right_path == 0) { // Se eu já verifiquei os dois caminhos
			if(sum+node_value == value) // E a soma do nó atual com o acumulador é o valor pedido
				RESP = 1; //Altero a var global de resposta
		}
		return 1;

    }
}


string readEntry(char *curr_char){
    int diffBrackets = 0;
    int openB = 0;
    int closedB = 0;
    string entry = "";

    while(*curr_char == ' ' || *curr_char == '\n'){
		*curr_char = getchar();
    }
    if(*curr_char == '('){
        openB++;
        diffBrackets += openB - closedB;
        entry.push_back(*curr_char);

        while(diffBrackets != 0){
            //printf("entrei aqui2");
            *curr_char = getchar();

            if(*curr_char >= '0' && *curr_char <='9'){
                entry.push_back(*curr_char);
            }
            else if (*curr_char == '('){
                entry.push_back(*curr_char);
                openB++;
            }
            else if (*curr_char == ')'){
                entry.push_back(*curr_char);
                closedB++;
            }
            diffBrackets = openB - closedB;
        }
    }
    return entry;
}


int main(){
    int value;
    char curr_char;
    string tree;
    char c;
    const char* tree_;
    int count_b;
    vector<int> results;

    while(scanf("%d", &value) != EOF){
        RESP = 0;
        curr_char = getchar();

        //tree = readEntry(&curr_char);
        //tree_ = tree.c_str();
        //c = tree_
        //cout << tree;
        existsPathSum(0, value, &curr_char);
        results.push_back(RESP);
    }

    for(int i; i < results.size(); i++){
        if(results[i] == 0) printf("no\n");
        else printf("yes\n");
    }

    return 0;
}