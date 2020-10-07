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
  -h, --help            show this help message and exit
  --size SIZE
                        Número total de páginas da memória cache
  --mapping MAPPING
                        Valores aceitos para esse parâmetro são: DI / AS /
                        AC - Tipos do mapeamento desejado
  --algorithm ALGORITHM
                        Valores aceitos para esse parâmetro são: RANDOM /
                        FIFO / LRU / LFU - Qual será a política de
                        substituição da memória que será utilizada
  --set_size SET_SIZE
                        Quando for escolhido o tipo de mapeamento AC deve-se
                        informar quantos conjuntos devem ser criados dentro da
                        memória cache.
  --path PATH
                        Nome do arquivo que possui as posições da memória
                        principal que serão acessadas, formato de número
                        inteiro e uma posição de memória principal por
                        linha.
  --debug DEBUG         Por padrão vem setado como 0, caso queira exibir os
                        debugs basta passar --debug 1

```
