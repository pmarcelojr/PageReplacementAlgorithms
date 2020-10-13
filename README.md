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

* Saída
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