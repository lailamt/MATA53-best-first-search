## Table of contents:
 - [MATA53-best-first-search](#mata53-best-first-search)
 - [Best First Search Algorithm](#best-first-search-algorithm)
 - [Pseudocódigo](#pseudoc%C3%B3digo)
 - [Execução do Programa](#execu%C3%A7%C3%A3o-do-programa)
 - [A Interface visual](#a-interface-visual)
 - [Google Colaboratory](#google-colaboratory)

# MATA53-best-first-search
Atividade da disciplina de Teoria dos Grafos (MATA53) da Universidade Federal da Bahia (UFBA), no primeiro semestre de 2021.

Discente: Laila Pereira Mota Santos

Matrícula: 218125095

### [**Link do YouTube com vídeo da execução da ferramenta**](https://www.youtube.com)

# Best First Search Algorithm

O **Algoritmo Best First Search** (BestFS) usa o conceito de fila prioritária e pesquisa heurística. É um algoritmo de busca que funciona em uma regra específica. O objetivo é alcançar o destino desde o estado inicial pelo caminho mais curto ou menos custoso.

Trata-se de um algoritmo informado (ou heurístico), em que a pesquisa é realizada usando informações adicionais para determinar o próximo passo para encontrar a solução. Se considerarmos a pesquisa como uma forma de travessia em um grafo, um algoritmo de pesquisa desinformado atravessaria cegamente para o próximo nó de uma determinada maneira, sem considerar o custo associado a essa ação. Uma pesquisa informada por outro lado, usaria uma função de avaliação para decidir qual entre os vários nós disponíveis é o mais promissor antes de atravessar para esse nó.

BestFS usa o conceito de fila de prioridade e pesquisa heurística. Para traçar o caminho do grafo, o método BFS usa duas listas para rastrear a travessia. Uma lista que mantém o controle dos nós "imediatos" atuais disponíveis para passagem e uma lista que mantém o controle dos nós já atravessados.
Este algoritmo percorrerá o caminho menos custoso primeiro na fila (no caso da implementação dessa interface). A complexidade de tempo do algoritmo BestFS é dada por `O(n logn)` no pior caso. 

Esse algoritmo é frequentemente usado para encontrar caminhos na busca combinatória. 

São variantes do BestFS os algoritmos de **BestFS Guloso** e o **A* **.

### Pseudocódigo
// This pseudocode is adapted from below 
// source:
// [https://courses.cs.washington.edu/]

    Best-First-Search(Grah g, Node start)
        1) Create an empty PriorityQueue
           PriorityQueue **pq**;
        2) Insert "start" in pq.
           pq.insert(start)
        3) Until PriorityQueue is empty
              u = PriorityQueue.DeleteMin
              If u is the goal
                 Exit
              Else
                 Foreach neighbor v of u
                    If v "Unvisited"
                        Mark v "Visited"                    
                        pq.insert(v)
                 Mark u "Examined"                    
    End procedure
Fonte: [Geeks4Geeks](https://www.geeksforgeeks.org/best-first-search-informed-search/)

# Execução do Programa
O código de programa pode ser executado de duas formas:
 1. Executar diretamente o arquivo fonte da aplicação .py
 - Faça download do arquivo .zip do repositório e descompacte.
 - Em seu terminal navegue até o diretório [MATA53-best-first-search](https://github.com/lailamt/MATA53-best-first-search)/[BestFS](https://github.com/lailamt/MATA53-best-first-search/tree/main/BestFS)/**source**/
 - Execute o código-fonte através do comando `$ py BestFS.py`
 
 **!!** Caso decida utilizar o terminal para a execução da interface esteja atento as dependências do projeto. Todas as dependências utilizadas neste projeto estão enunciadas no arquivo **requirements.txt**.

 3. Executar o arquivo .exe
- Faça download do arquivo .zip do repositório e descompacte.
- Navegue até o diretório [MATA53-best-first-search](https://github.com/lailamt/MATA53-best-first-search)/[BestFS](https://github.com/lailamt/MATA53-best-first-search/tree/main/BestFS)
- Execute o arquivo BestFS.exe

**!!** É possível que o seu SO reporte o arquivo como perigoso. Entretanto este é um procedimento normal visto que o executável deste repositório não possui assinatura. Você pode encontrar o código-fonte no repositório, caso queira inspecioná-lo. Mais informações sobre isto [nesse link](https://stackoverflow.com/questions/43777106/program-made-with-pyinstaller-now-seen-as-a-trojan-horse-by-avg) e [nesse outro link](https://www.defcon-lab.org/se-python-entao-virus/).

# A Interface visual
A interface visual foi desenvolvida com o auxílio da biblioteca PyQT5 e o aplicativo QTDesigner.

Abaixo alguns prints com informações relevantes sobre sua utilização.
- Ao descompactar os arquivos você encontrará dentro do diretório BestFS o seguinte arquivo executável. Abra o arquivo para ter acesso a interface.

![Diretório BestFS](https://i.ibb.co/Kq79sgs/arvore-dir.png)
- Ao executar o arquivo `BestFS.exe` a seguinte interface irá abrir

![Interface visual](https://i.ibb.co/mG7rX7g/application.png)
1. Instruções da interface
2. Campo para ser preenchido com a quantidade total de vértices do grafo
3. Campo a ser preenchido com os valores de **(nó de saída, nó de chegada, custo da aresta)** conforme exemplo, para todas as arestas do grafo.
4. Campo a ser preenchido com o nó de saída e o nó de destino a ser percorrido pelo algoritmo.
5. Botão para executar o algoritmo.
6. Saída
7. Botão para gerar valores aleatórios para o caminho.
- Após a execução do algoritmo o seguinte botão é habilitado

![botão gerar grafo](https://i.ibb.co/KzH62gP/application2.png)
8. Botão que gera o grafo com os nós e arestas visitadas em vermelho.
- O botão "Generate graph with path" abre uma nova janela conforme imagem abaixo.

![Janela do grafo gerado](https://i.ibb.co/7SxTJ0W/graph.png)
1. Menu de interação com o grafo.
2. Área do grafo gerado. Ao salvar o grafo por esta janela, a imagem irá conter apenas os elementos presentes dentro da área do retângulo. 

# Google Colaboratory
No diretório ## [MATA53-best-first-search](https://github.com/lailamt/MATA53-best-first-search)/**MATA53_Best_First_Search_Algorithm.ipynb** pode ser encontrado o arquivo .ipynb do algoritmo em sua fase de prototipação e testes com link de acesso e alguns casos de teste.
