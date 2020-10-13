# PageReplacementAlgorithms

Esse script permite que você visualize de forma didática como ocorre a escolha e a substituição de uma posição de memória no cache em três modelos diferentes de mapeamento de memória.

# O que foi implementado
--
O projeto consiste em um algoritmos de subsituição de páginas de memória em cache. O simulador recebe como entrada a sequência de referências ás páginas de memória (endereços), e simula as substituições realizadas em cache após a ocorrência de um Miss/Hit, para os algoritmos FIFO, LFU, LRU e RANDOM. O simulador assume um cache operando com o esquema de mapeamento associativo. O programa recebe como parâmetro a capacidade total da memória cache (número total de páginas), além do caminho, nome do arquivo a ser lido pelo programa, contendo as sequências de referÊncias aos acessos de páginas da memória.

No simulador, você poderá escolher qual será a política de substituição de páginas da memória cache. 
São 4 algoritmos de substituição, sendo eles:

* FIFO
* LFU
* LRU
* RANDOM

No simulador, a memória cache poderá ser organizada em três diferentes esquemas, sendo eles:

* AC - Associativo por contjunto
* DI - Direto
* AS - Associativo

* Arquivo de Referencia: [Page_Replacement_Algorithms] (http://www.idc-online.com/technical_references/pdfs/information_technology/Page_Replacement_Algorithms.pdf)

Pré-Requisitos
--

O único pré-requisito é que sua maquina rode python 3.8+

Para saber qual versão do python que você tem instalado acesse o seu terminal e digite:

```
$ python3 --version
```

Como resultado desejado deve aparecer algo do tipo

```
Python 3.8.2
```

Agora, para acessar o help da aplicação, basta digitar no terminal o comando a seguir:

```
$ python main.py -h
```

```
usage: Simulador de Substituição de Paginas [-h] [--size SIZE]
                                              [--mapping MAPPING]
                                              [--algorithm ALGORITHM]
                                              [--set_size SET_SIZE]
                                              [--path PATH]
                                              [--debug DEBUG]

optional arguments:
  `-h, --help` : show this help message and exit.
  `--size SIZE` : Número total de páginas da memória cache.
  `--mapping MAPPING` : Valores aceitos para esse parâmetro são: DI / AS / AC - Tipos do mapeamento desejado.
  `--algorithm ALGORITHM` : Valores aceitos para esse parâmetro são: RANDOM / FIFO / LRU / LFU - Qual será a política de
                        substituição da memória que será utilizada
  `--set_size SET_SIZE` : Quando for escolhido o tipo de mapeamento AC deve-se informar quantos conjuntos devem ser criados dentro da memória cache.
  `--path PATH` : Nome do arquivo que possui as posições da memória principal que serão acessadas, formato de número inteiro e uma posição de memória principal por linha.
  `--debug DEBUG` : Por padrão vem setado como 0, caso queira exibir os debugs basta passar --debug 1

```

## Executando

Para executar os testes, siga os passos abaixo conforme cada tipo de algoritmo.

## 1 - Mapeamento Associativo

No mapeamento associativo não existe uma relação pré-estabelecida entre a posição da memória principal e a posição da memória cache, ou seja, não existe determinismo entre a posição da memória principal e a posição da memória cache. Dessa forma para saber se uma posição da memória principal está na memória cache é necessário percorrer toda a memória cache a fim de verificar se a posição da memória principal está ou não na cache.

Caso a posição de memória principal esteja na memória cache então ela é retornada como um CACHE HIT, caso ela não esteja armazenada então é necessário que seja escolhida uma posição de memória cache para ser removida, para que a nova posição da memória principal possa ser armazenada na memória cache.

A vantagem desse modelo de mapeamento em relação ao modelo direto é que não corremos o risco de ter cache ociosa, em contrapartida, o custo para identificar se uma posição da memória principal está na memória cache é maior pois temos que verificar todas as posições da memória cache.

A baixo serão apresentados alguns exemplos de uso do simulador onde é utilizado o esquema de mapeamento associativo juntamente com esquemas diversos de substituição de memória.

### RANDOM

Nesse existe a escolha aleatória sobre qual elemento da cache deve ser substituída.

* Executando o comando:
```
python main.py --size 4 --mapping=AS --path=file_test/associativo_100_hit.txt --debug 1 --algorithm RANDOM
```

É interessante observar que duas execuções consecutivas podem ter resultados distintos tanto no estado final da cache como também na sua taxa de CACHE HIT.


O arquivo file_test/associativo_101_hit.txt é composto por:

```
0
1
2
3
4
4
5
6
```

* Executando o comando duas vezes:
```
$ python main.py --size 4 --mapping=AS --path=file_test/associativo_101_hit.txt --debug 1 --algorithm RANDOM
```

Note que a saída não necessariamente será igual a saída apresentada a baixo uma vez que a escolha do elemento da cache que será removido é aleatória.

#### Execução A
```
+--------------------------+
|Tamanho Cache:           4| 
+----------+---------------+
|     Cache Associativo    |
+----------+---------------+
|Pos Cache |Posição Memória|
+----------+---------------+
|         0|              0|
|         1|              1|
|         2|              6|
|         3|              5|
+----------+---------------+


-----------------
Resumo Mapeamento Associativo
-----------------
Política de Substituição: RANDOM
-----------------
Total de memórias acessadas: 8
Total HIT 1
Total MISS 7
Taxa de Cache HIT 0.00%
```

#### Execução B

```
+--------------------------+
|Tamanho Cache:           4| 
+----------+---------------+
|     Cache Associativo    |
+----------+---------------+
|Pos Cache |Posição Memória|
+----------+---------------+
|         0|              0|
|         1|              4|
|         2|              6|
|         3|              3|
+----------+---------------+


-----------------
Resumo Mapeamento Associativo
-----------------
Política de Substituição: RANDOM
-----------------
Total de memórias acessadas: 8
Total HIT 1
Total MISS 7
Taxa de Cache HIT 0.00%
```

### FIFO

Primeiro elemento que entra é o primeiro elemento que sai.

O arquivo file_test/associativo_100_hit.txt é composto por:

```
0
1
2
3
4
5
6
6
6
10
```

* Executando o comando:
```
$ python main.py --size 4 --mapping=AS --path=file_test/associativo_100_hit.txt --debug 1 --algorithm FIFO
```

* Saída:
```
Interação número: 10
Cache MISS: posiçao de memória 10
Posição da cache ainda não utilizada: -1

Leitura linha 9, posição de memória 10.
+--------------------------------------+
| Contador FIFO                        |
+--------------------------------------+
|Conjunto | Próxima Posição Substituir |
+---------+----------------------------+
|        0|                           0|
|        1|                           1|
+---------+----------------------------+
Posição Memória: 10
Conjunto: 0
Lista posições: [0, 1, 2, 3]
Posição para subistituição: 3
Posição de memória cache que será trocada é: 3
+--------------------------+
|Tamanho Cache:           4| 
+----------+---------------+
|     Cache Associativo    |
+----------+---------------+
|Pos Cache |Posição Memória|
+----------+---------------+
|         0|              4|
|         1|              5|
|         2|              6|
|         3|             10|
+----------+---------------+


-----------------
Resumo Mapeamento Associativo
-----------------
Política de Substituição: FIFO
-----------------
Total de memórias acessadas: 10
Total HIT 2
Total MISS 8
Taxa de Cache HIT 0.00%


--------------------------------------------------------------------------------
Parâmetros da Simulação
--------------------------------------------------------------------------------
Arquivo com as posições de memória: file_test/associativo_100_hit.txt
Número de posições de memória: 10
As posições são: [0, 1, 2, 3, 4, 5, 6, 6, 6, 10]
Tamanho total da cache: 4
Tipo Mapeamento: AS
Política de Substituição: FIFO
Debug: 1
Step: 0
-------------------------------------------------------------------------------
```

### LRU

Nesse quando ocorre um CACHE MISS é necessário trazer uma nova posição da memória principal, para a memória cache então será removido a posição de memória que está na cache que foi usada há mais tempo.

O algoritmo trabalha da seguinte forma: Se houver um CACHE HIT, então essa posição da CACHE vai para o topo da pilha, caso ocorra um CACHE MISS o primeiro elemento da fila é removido, e no seu lugar é colocado a posição da memória principal e esse local passa a ser o novo topo da pilha.

* Executando o comando:
```
$ python main.py --size 4 --mapping=AS --path=file_test/associativo_101_hit.txt --debug 1 --algorithm LRU
```

* Saída:

```
Interação número: 8
Cache MISS: posiçao de memória 6
Posição da cache ainda não utilizada: -1

Leitura linha 7, posição de memória 6.
Posição Memória: 6
Conjunto: 0
Lista posições: [0, 1, 2, 3]
+--------------------------+
|Tamanho Cache:           4| 
+----------+---------------+
|     Cache Associativo    |
+----------+---------------+
|Pos Cache |Posição Memória|
+----------+---------------+
|         0|              3|
|         1|              4|
|         2|              5|
|         3|              6|
+----------+---------------+


-----------------
Resumo Mapeamento Associativo
-----------------
Política de Substituição: LRU
-----------------
Total de memórias acessadas: 8
Total HIT 1
Total MISS 7
Taxa de Cache HIT 0.00%


-------------------------------------------------------------------------------
Parâmetros da Simulação
-------------------------------------------------------------------------------
Arquivo com as posições de memória: file_test/associativo_101_hit.txt
Número de posições de memória: 8
As posições são: [0, 1, 2, 3, 4, 4, 5, 6]
Tamanho total da cache: 4
Tipo Mapeamento: AS
Política de Substituição: LRU
Debug: 1
Step: 0
-------------------------------------------------------------------------------
```

### LFU

Esse é esquema de substituição exige que exista um contador para cada posição da memória cache, esse contador é incrementado toda vez que a posição é acessada e é zerado toda vez que uma nova posição da memória principal é vinculada com aquela posição da memória cache.

A ideia aqui é aproveitar a localidade temporal, ou seja, aquela localidade que diz respeito a reusar posições que foram recentemente utilizadas.

* Executando o comando:
```
$ python main.py --size 4 --mapping=AS --path=file_test/associativo_101_hit.txt --debug 1 --algorithm LFU
```

* Saída:
```
Posição Memória Lida No Arquivo: 6
Conjunto: 0
Número de Acesso Da Posição com Menos Acesso: 0
Lista Posições do Conjuno: [0, 1, 2, 3]
Lista com as posições menos acessadas do conjunto: [1, 2, 3]
Posição Cache Substituir: 2
Posição de memória cache que será trocada é: 2
+--------------------------+
|Tamanho Cache:           4| 
+----------+---------------+
|     Cache Associativo    |
+----------+---------------+
|Pos Cache |Posição Memória|
+----------+---------------+
|         0|              4|
|         1|              1|
|         2|              6|
|         3|              5|
+----------+---------------+
+--------------------------------------+
| Contador LFU                         |
+--------------------------------------+
|Posição Cache | Qtd Acessos           |
+---------+----------------------------+
|        0|                           1|
|        1|                           0|
|        2|                           0|
|        3|                           0|
+---------+----------------------------+


-----------------
Resumo Mapeamento Associativo
-----------------
Política de Substituição: LFU
-----------------
Total de memórias acessadas: 8
Total HIT 1
Total MISS 7
Taxa de Cache HIT 0.00%


-------------------------------------------------------------------------------
Parâmetros da Simulação
-------------------------------------------------------------------------------
Arquivo com as posições de memória: file_test/associativo_101_hit.txt
Número de posições de memória: 8
As posições são: [0, 1, 2, 3, 4, 4, 5, 6]
Tamanho total da cache: 4
Tipo Mapeamento: AS
Política de Substituição: LFU
Debug: 1
Step: 0
-------------------------------------------------------------------------------
```

## 2 - Mapeamento Associativo por Conjuntos

Nesse modo, a memória cache é dividida em conjuntos, ou seja, uma posição da memória principal é mapeada sempre para um mesmo conjunto e isso permite uma consulta mais rápida na cache se uma dada posição de memória está ou não nela.

No exemplo abaixo é aplicado o mapeamento por conjunto, utilizando como número de conjuntos o valor 2 e como política de substituição da memória está sendo utilizado o tipo RANDOM.

Existem diversas formas de se organizar um conjunto dentro da cache, neste  simulador utilizamos o módulo (MOD) da quantidade de conjuntos em relação ao tamanho da cache, para determinar qual posição da cache faz parte de cada conjunto. Em uma cache de tamanho 4 com 2 conjuntos, as posições do conjunto ZERO são {0, 2}, ao passo que o conjunto UM está associado aos elementos {1, 3}, como pode ser observado abaixo.


```
+------------------------------+
|Tamanho:                     4|
|Conjuntos:                   2|
+------------------------------+
+  Cache Associativo Conjunto  +
+-------+-------+--------------+
|#      | Cnj   |   Pos Memória|
+-------+-------+--------------+
|0      |   0   |            -1|
|1      |   1   |            -1|
|2      |   0   |            -1|
|3      |   1   |            -1|
+-------+-------+--------------+
```

Desta forma, podemos observar que o comportamento do modo associativo por conjunto quando o conjunto é igual a 1 é exatamente igual ao modo associativo, pois no modo associativo existe apenas um único conjunto para toda a cache.

Quando temos dois conjuntos, por exemplo, toda posição de memória principal cujo identificador é par será associado a algum elemento do conjunto ZERO, ao passo que toda posição de memória ímpar será associada a algum elemento do conjunto UM.

Todos os modos de substituição de memória, RANDOM, FIFO, LRU e LFU apresentados anteriormente no modo associativo funcionarão exatamente da mesma forma, a diferença é que ao invés de utilizar todos os elementos, foi usado apenas os elementos que pertencem ao conjunto associado com a posição de memória que está sendo acessada.

Para mais detalhes, acesse o código fonte para entender um pouco mais sobre como essas políticas são implementadas. É importante observar que não estamos preocupados com eficiência, ou uso da melhor estrutura de dados para cada tipo de algoritmo de substituição de memória, o intuito é apresentar como cada um se comporta, seus pontos positivos e negativos.

```
$ python main.py --size 10 --mapping=AC --path=file_test/acesso_associativo_100_hit.txt --set_size 2 --debug 1 --algorithm RANDOM
```

No segundo exemplo estamos utilizando a política de substituição conhecida como FIFO, ou seja, a primeira posição de memória que entra no conjunto e a primeira que será substituída quando houver um cache miss.

```
$ python main.py --size 10 --mapping=AC --path=file_test/acesso_associativo_100_hit.txt --set_size 2 --debug 1 --algorithm FIFO
```

Nesse exemplo há alguns cache hit obrigando assim que o contador da posição a ser substituída não seja incrementado.

```
$ python main.py --size 10 --mapping=AC --path=file_test/acesso_associativo_conjunto_51_hit.txt --set_size 2 --debug 1 --algorithm FIFO
```

O próximo exemplo simula o processo do tipo de mapeamento associativo por conjunto, com um total de 6 posições de cache e dois conjuntos.

```
$ python main.py --size 6 --mapping=AC --path=file_test/acesso_associativo_conjunto_51_hit.txt --debug 1 --algorithm FIFO --set_size 2
```

Nesse exemplo temos leituras de memórias em dois conjuntos distintos, mostrando que primeiro é substituído a posição que está há mais tempo na memória cache, respeitando a ordem do conjunto.

```
python main.py --size 6 --mapping=AC --path=file_test/acesso_associativo_conjunto_52_hit.txt --debug 1 --algorithm FIFO --set_size 2
```


No exemplo de substituição utilizando o LRU, é necessário que haja um controle individual sobre cada posição da cache para saber quantas vezes ela já foi acessada dentro do seu conjunto.

* Executando o comando:
```
$ python main.py --size 10 --mapping=AC --path=file_test/lru_0.txt --debug 1 --algorithm LRU --set_size 1
```

* Saída:
```
Interação número: 17
Cache HIT: posiçao de memória 1, posição cache 7
Posição Memória: 1
Conjunto: 0
Lista posições: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
+--------------------------+
|Tamanho Cache:          10| 
+----------+---------------+
|     Cache Associativo    |
+----------+---------------+
|Pos Cache |Posição Memória|
+----------+---------------+
|         0|             -1|
|         1|             -1|
|         2|             -1|
|         3|             -1|
|         4|             -1|
|         5|             -1|
|         6|              0|
|         7|              2|
|         8|              3|
|         9|              1|
+----------+---------------+


-----------------
Resumo Mapeamento Associativo
-----------------
Política de Substituição: LRU
-----------------
Total de memórias acessadas: 17
Total HIT 13
Total MISS 4
Taxa de Cache HIT 0.00%


--------------------------------------------------------------------------------
Parâmetros da Simulação
--------------------------------------------------------------------------------
Arquivo com as posições de memória: file_test/lru_0.txt
Número de posições de memória: 17
As posições são: [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 1]
Tamanho total da cache: 10
Tipo Mapeamento: AC
Quantidade de Conjuntos: 1
Política de Substituição: LRU
Debug: 1
Step: 0
--------------------------------------------------------------------------------
```

Mostrando então que houve a computação do número de acesso para cada uma das posições acessadas em relação ao conjunto que ela ocupa dentro da cache.


No próximo exemplo temos um total de 4 posições da memória cahce e dois conjuntos, nese caso, duas posições tem o mesmo número de acesso então é feito um sorteio para ver qual será a posição descartada.

```
$ python main.py --size 4 --mapping=AC --path=file_test/lru_3.txt --debug 1 --algorithm LRU --set_size 2
```

A forma como os algoritmos de paginação são executados no mapeamento associativo por conjunto é exatamente igual ao modo associativo. A única diferença é que ao invés de fazer a substituição de página dentro de toda a cache, como no associativo, no associativo por conjunto, a substituição de página é feita apenas dentro do conjunto onde a posição de memória deveria ter sido mapeada.

## 3 - Mapeamento Direto

O mapeamento direto da memória cache, é aquele que associa cada posição da memória principal, com uma posição específica da memória cache. Na aplicação essa associação foi implementada utilizando o mod como método de separação dos blocos, porém, caso o endereçamento de memória seja binário em geral é utilizado um conjunto dos primeiros blocos do endereçamento da posição de memória. Como referência na posição da memória cache, o tamanho da memória cache definirá a quantidade de bits que serão selecionados.
Nessa aplicação como exemplo, foram criados quatro arquivos com cenários (entradas) diferentes com relação ao uso do mapeamento direto, objetivando exibir aqui as principais situações de cache hit e cache miss.
No primeiro exemplo não ocorre CACHE HIT, ou seja, para cada posição de memória desejada será necessário ir acessar e buscar na memória principal.

O arquivo direto_0_hit.txt é composto por:
```
1
11
3
2
15
13
7
6
14
12
```

* Executando o comando:
```
$ python main.py --size 10 --mapping=DI --path=file_test/direto_0_hit.txt
```

* Saída:
```
Leitura linha 9,  posição de memória desejada 12.
       Status: Miss
+--------------------------+
|      Cache Direto        |
+--------------------------+
|Tamanho Cache: 10| 
+----------+---------------+
|Pos Cache |Posição Memória|
+----------+---------------+
|         0|             -1|
|         1|             11|
|         2|             12|
|         3|             13|
|         4|             14|
|         5|             15|
|         6|              6|
|         7|              7|
|         8|             -1|
|         9|             -1|
+----------+---------------+


------------------------
Resumo Mapeamento Direto
------------------------
Total de memórias acessadas: 10
Total HIT: 0
Total MISS: 10
Taxa de Cache HIT: 0.00%

```

É importante ressaltar que nesse exemplo algumas posições da memória cache não foram utilizadas, pois nenhuma das posições de memória solicitadas estavam associadas com as posições de memória vazias, com -1. Isso mostra que a associação direta ganha em tempo de computação, mas em contrapartida, pode perder em flexibilidade uma vez que mesmo havendo posições de memória cache disponível, foi necessário fazer a substituição de uma página de memória na memória cache.

Caso o mesmo arquivo seja executado utilizando, por exemplo, um esquema de cache associativo, o resultado final será:

```
+--------------------------+
|Tamanho Cache:          10|
+----------+---------------+
|     Cache Associativo    |
+----------+---------------+
|Pos Cache |Posição Memória|
+----------+---------------+
|         0|              1|
|         1|              2|
|         2|              3|
|         3|             11|
|         4|             12|
|         5|             13|
|         6|             14|
|         7|              6|
|         8|              7|
|         9|             15|
+----------+---------------+
```

É possível observar que o tamanho da cache é exatamente igual a quantidade de posições de blocos diferentes na memória principal, isso é bom pois assim é utilizando a cache de maneira integral e ambas as memórias.
No segundo exemplo, duas posições são consecutivamente acessadas, então ocorre cache miss apenas no primeiro acesso e em seguida, todos os demais acessos são CACHE HIT.

O arquivo file_test/direto_50_hit.txt é composto por:
```
1
2
1
2
1
2
1
2
1
2
```

* Executando o comando:
```
$ python main.py --size 10 --mapping=DI --path=file_test/direto_50_hit.txt
```

* Saída:
```
Leitura linha 9,  posição de memória desejada 2.
       Status: Hit
+--------------------------+
|      Cache Direto        |
+--------------------------+
|Tamanho Cache: 10| 
+----------+---------------+
|Pos Cache |Posição Memória|
+----------+---------------+
|         0|             -1|
|         1|              1|
|         2|              2|
|         3|             -1|
|         4|             -1|
|         5|             -1|
|         6|             -1|
|         7|             -1|
|         8|             -1|
|         9|             -1|
+----------+---------------+


------------------------
Resumo Mapeamento Direto
------------------------
Total de memórias acessadas: 10
Total HIT: 8
Total MISS: 2
Taxa de Cache HIT: 0.00%
```

Observe que nesse caso temos uma alta taxa de CACHE HIT e novamente um uso limitado da cache.
No terceiro exemplo temos uma mesma posição sendo acessada consecutivamente, assim, ocorre apenas um miss e o restante é hit.
No terceiro exemplo apresentamos um cenário onde a ineficiência do mapeamento direto é apresentada. Apesar de existir um número grande de memória, o número de CACHE MISS é elevado, uma vez que está sendo feita um alto uso de memória, de uma mesma localidade de memória, com sombreamento entre si, gerando assim um fenômeno onde existe cache disponível, mas o modo como o mapeamento é feito, no caso, associativo, impede o uso da totalidade da cache.

O arquivo file_test/direto_misto_hit.txt é composto por:
```
0
1
2
2
22
32
42
20
1
10
11
12
13
```

* Executando o comando:
```
$ python main.py --size 10 --mapping=DI --path=file_test/direto_misto_hit.txt
```

* Saída:
```
Leitura linha 12,  posição de memória desejada 13.
       Status: Miss
+--------------------------+
|      Cache Direto        |
+--------------------------+
|Tamanho Cache: 10| 
+----------+---------------+
|Pos Cache |Posição Memória|
+----------+---------------+
|         0|             10|
|         1|             11|
|         2|             12|
|         3|             13|
|         4|             -1|
|         5|             -1|
|         6|             -1|
|         7|             -1|
|         8|             -1|
|         9|             -1|
+----------+---------------+


------------------------
Resumo Mapeamento Direto
------------------------
Total de memórias acessadas: 13
Total HIT: 2
Total MISS: 11
Taxa de Cache HIT: 0.00%
```

Sobre o método de mapeamento direto
--

No método de mapeamento direto não existem políticas de substituição de cache, uma vez que a posição da memória principal sempre estará mapeada com a mesma posição da memória cache. Em contrapartida, nos modos associativo e associativo por conjunto essa relação direta entre as duas memórias existe, mas com granularidade menor, e com isso, surge a necessidade que sejam implementados mecanismos para escolher (em caso de falta de espaço na memória cache), para armazenar uma posição da memória principal, na qual a posição será descartada para que a nova posição seja ocupada.