# PageReplacementAlgorithms

Esse script permite que você visualize de forma didática como ocorre a escolha e a substituição de uma posição de memória no cache em três modelos diferentes de mapeamento de memória.

Instalação
--

O único pré-requisito do script é que sua maquina rode python 3.7+

Para saber qual versão do python que você tem instalado acesse o seu terminal e digite:

```
$ python3 --version
```

Como resultado desejado deve aparecer algo do tipo

```
Python 3.8.2
```

Após a instalação do script para acessar o help da aplicação, basta digitar no console o comando a seguir:

```
$ python main.py -h
```

```
usage: Simulador de Substituição de Paginas [-h] [--total_cache TOTAL_CACHE]
                                              [--tipo_mapeamento TIPO_MAPEAMENTO]
                                              [--politica_substituicao POLITICA_SUBSTITUICAO]
                                              [--qtd_conjuntos QTD_CONJUNTOS]
                                              [--arquivo_acesso ARQUIVO_ACESSO]
                                              [--debug DEBUG]

optional arguments:
  -h, --help            show this help message and exit
  --total_cache TOTAL_CACHE
                        Número total de páginas da memória cache
  --tipo_mapeamento TIPO_MAPEAMENTO
                        Valores aceitos para esse parâmetro são: DI / AS /
                        AC - Tipos do mapeamento desejado
  --politica_substituicao POLITICA_SUBSTITUICAO
                        Valores aceitos para esse parâmetro são: RANDOM /
                        FIFO / LRU / LFU - Qual será a política de
                        substituição da memória que será utilizada
  --qtd_conjuntos QTD_CONJUNTOS
                        Quando for escolhido o tipo de mapeamento AC deve-se
                        informar quantos conjuntos devem ser criados dentro da
                        memória cache.
  --arquivo_acesso ARQUIVO_ACESSO
                        Nome do arquivo que possui as posições da memória
                        principal que serão acessadas, formato de número
                        inteiro e uma posição de memória principal por
                        linha.
  --debug DEBUG         Por padrão vem setado como 0, caso queira exibir os
                        debugs basta passar --debug 1

```