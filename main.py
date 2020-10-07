# -*- coding: utf-8 -*-
import argparse, random, re


# Essa lista irá armazenar qual o número de vezes que uma
# determinada posição da memória cache foi acessada.
contador_lfu = {}


# Essa lista irá armazenar a ordem que a posição da memória
# principal foi inserida na memória cache, quando ocorre um CACHE MISS
# a posição ZERO dessa lista será removida e a nova posição de memória
# será inserida no topo da lista.
contador_fifo = {}


def existe_posicao_vazia(memoria_cache, set_size, posicao_memoria):
  """Verifica se existe na cache uma posição de memória que ainda não foi utilizada,
  se existir, essa posição é retornada.

  Arguments:
    memoria_cache {list} -- memória cache
    set_size {int} -- número de conjuntos da cache
    posicao_memoria {int} -- posição de memória que se quer armazenar na cache

  Returns:
    [int] -- com a primeira posição de memória vazia do conjunto
  """
  num_conjunto = get_num_conjuno_posicao_memoria(posicao_memoria, set_size)
  lista_posicoes = get_lista_posicoes_cache_conjunto(memoria_cache, num_conjunto, set_size)

  # verifica se alguma das posições daquele conjunto está vazia
  for x in lista_posicoes:
    if memoria_cache[x] == -1:
      return x
  return -1


def imprimir_contador_fifo():
  """Função de debug que exibe o estado do contador FIFO
  """
  print('+--------------------------------------+')
  print("| Contador FIFO                        |")
  print('+--------------------------------------+')
  print("|Conjunto | Próxima Posição Substituir |")
  print('+---------+----------------------------+')
  for index, x in enumerate(contador_fifo):
    print("|{:>9}|{:>28}|".format(index,x))
  print('+---------+----------------------------+')


def inicializar_contador_fifo():
  """Seta os valores do contador fifo para que a primeira subsitituição
  ocorra no primeiro elemento que faz parte do conjunto
  """
  # cria no contador fifo uma posição para cada conjunto
  for x in range(0, set_size):
    contador_fifo[x] = 0

  if debug:
    imprimir_contador_fifo()


def imprimir_contador_lfu():
    """Função de debug que exibe o estado do contador LFU
    """
    print('+--------------------------------------+')
    print("| Contador LFU                         |")
    print('+--------------------------------------+')
    print("|Posição Cache | Qtd Acessos           |")
    print('+---------+----------------------------+')
    for index, x in enumerate(contador_lfu):
      print("|{:>9}|{:>28}|".format(index,contador_lfu[x]))
    print('+---------+----------------------------+')


def inicializar_contador_lfu():
  """Seta os valores do contador LFU para zero, ou seja, a posição de memória que ocupa aquela
  posição da cache ainda não foi utilizada. Para cada posição da cache teremos um contador
  que será somado tada vez que houver um CACHE HIT e, será zerado quando a posição for substituida
  """
  # cria on contador LFU uma posiçõao para caqda posição de memória
  for x in range(0, size):
    contador_lfu[x] = 0

  if debug:
    imprimir_contador_lfu()


def get_num_conjuno_posicao_memoria(posicao_memoria, set_size):
  """Retorna o número do conjunto onde essa posição de memória é sempre mapeada

  Arguments:
    posicao_memoria {int} -- posição de memória que se quer acessar
    set_size {int} -- número de conjuntos que a cache possui
  """
  return int(posicao_memoria)%int(set_size)


def print_cache_direto(cache):
  """Imprime o estado da memória cache no modelo de mapeamento direto.
  """
  print("+--------------------------+")
  print("|      Cache Direto        |")
  print("+--------------------------+")
  print("|Tamanho Cache: {:>11}| ".format(len(cache)))
  print("+----------+---------------+")
  print("|Pos Cache |Posição Memória|")
  print("+----------+---------------+")
  for posicao, valor in cache.items():
    print("|{:>10}|{:>15}|".format(posicao, valor))
  print("+----------+---------------+")


def print_cache_associativo(cache):
  """Imprime o estado da memória cache no modelo de mapeamento associativo.
  """
  print("+--------------------------+")
  print("|Tamanho Cache: {:>11}| ".format(len(cache)))
  print("+----------+---------------+")
  print("|     Cache Associativo    |")
  print("+----------+---------------+")
  print("|Pos Cache |Posição Memória|")
  print("+----------+---------------+")
  for posicao, valor in cache.items():
    print("|{:>10}|{:>15}|".format(posicao, valor))
  print("+----------+---------------+")


def print_cache_associativo_conjunto(cache, set_size):
  """Imprime o estado da memória cache no modelo de mapeamento associativo por conjunto.
  """
  print("+------------------------------+")
  print("|Tamanho: {:>21}|\n|Conjuntos: {:>19}|".format(len(cache), set_size))
  print("+------------------------------+")
  print("+  Cache Associativo Conjunto  +")
  print("+-------+-------+--------------+")
  print("|#\t| Cnj\t|   Pos Memória|")
  print("+-------+-------+--------------+")
  for posicao, valor in cache.items():
    num_conjunto = get_num_conjuno_posicao_memoria(posicao, set_size)
    print("|{} \t|{:4}\t|\t   {:>4}|".format(posicao, num_conjunto, valor))
  print("+-------+-------+--------------+")


def inicializar_cache(size):
  """Cria uma memória cache zerada utilizando dicionários (chave, valor) e com
  valor padrão igual a '-1'

  Arguments:
    size {int} -- tamanho total de palavras da cache

  Returns:
    [list] -- [dicionário]
  """
  # zera tota a memória cache
  memoria_cache = {}

  # popula a memória cache com o valor -1, isso indica que a posição não foi usada
  for x in range(0, size):
    memoria_cache[x] = -1

  return memoria_cache


def verifica_posicao_em_cache_associativo_conjunto(memoria_cache, set_size, posicao_memoria,):
  """Verifica se uma determinada posição de memória está na cache
    no modo associativo / associativo por conjunto

  Arguments:
    memoria_cache {list} -- memória cache
    set_size {int} -- número de conjuntos do cache
    posicao_memoria {int} -- posição que se deseja acessar
  """
  num_conjunto = int(posicao_memoria)%int(set_size)

  while num_conjunto < len(memoria_cache):
    if memoria_cache[num_conjunto] == posicao_memoria:
      return num_conjunto

    num_conjunto += set_size

  # não achou a posição de memória na cache
  return -1


def get_lista_posicoes_cache_conjunto(memoria_cache, num_conjunto, set_size):
  """Retorna uma lista com todas as posições da memória cache que fazem
  parte de um determinado conjunto.

  Arguments:
    memoria_cache {list} -- memória cache
    num_conjunto {int} -- número do conjunto que se quer saber quais são os endereçamentos associados com aquele conjunto
    set_size {int} -- quantidade total de conjuntos possíveis na memória

  Returns:
    [list] -- lista de posições de memória associada com um conjunto em particular
  """
  lista_posicoes = []
  posicao_inicial = num_conjunto
  while posicao_inicial < len(memoria_cache):
    lista_posicoes.append(posicao_inicial)
    posicao_inicial += set_size
  return lista_posicoes


def algorithm_RANDOM(memoria_cache, set_size, posicao_memoria):
  """Nessa algoritmo, no momento que ocorrer um CACHE MISS,
  será sorteado um elemento do conjunto para ser substituído pela nova posição
  de memória.

  Arguments:
    memoria_cache {list} -- memóiria cache
    set_size {int} -- quantidade de conjuntos
    posicao_memoria {int} -- posição de memória que será acessada
  """
  num_conjunto = int(posicao_memoria)%int(set_size)

  lista_posicoes = get_lista_posicoes_cache_conjunto(memoria_cache,num_conjunto, set_size)

  # seleciona de forma aleatória uma das posições de memória
  # que fazem parte do conjunto em particular e armazena dentro
  # daquela posição o valor da memória principal
  posicao_memoria_cache_para_trocar = random.choice(lista_posicoes)

  if debug:
    print('Posição de memória cache que será trocada é: {}'.format(posicao_memoria_cache_para_trocar))

  memoria_cache[posicao_memoria_cache_para_trocar] = posicao_memoria


def algorithm_FIFO(memoria_cache, set_size, posicao_memoria):
  """Nessa algoritmo, o primeiro elemento que entra é o primeiro elemento que sai,
  funciona exatamente como uma fila.

  Arguments:
    memoria_cache {list} -- memóiria cache
    set_size {int} -- quantidade de conjuntos
    posicao_memoria {int} -- posição de memória que será acessada
  """
  num_conjunto = int(posicao_memoria)%int(set_size)
  posicao_substituir = contador_fifo[num_conjunto]
  lista_posicoes = get_lista_posicoes_cache_conjunto(memoria_cache,num_conjunto, set_size)

  if debug:
    imprimir_contador_fifo()
    print('Posição Memória: {}'.format(posicao_memoria))
    print('Conjunto: {}'.format(num_conjunto))
    print('Lista posições: {}'.format(lista_posicoes))
    print('Posição para subistituição: {}'.format(posicao_substituir))

  memoria_cache[lista_posicoes[posicao_substituir]] = posicao_memoria

  contador_fifo[num_conjunto] += 1

  if contador_fifo[num_conjunto] >= (len(memoria_cache)/set_size):
    contador_fifo[num_conjunto] = 0

  if debug:
    print('Posição de memória cache que será trocada é: {}'.format(lista_posicoes[posicao_substituir]))


def algorithm_LFU(memoria_cache, set_size, posicao_memoria):
  """Nessa algoritmo, o elemento que é menos acessado é removido da
  memória cache quando ocorrer um CACHE MISS. A cada CACHE HIT a posição do HIT ganha um ponto
  de acesso, isso é usado como contador para saber qual posição deve ser removida no caso de
  CACHE MISS.

  Arguments:
    memoria_cache {list} -- memóiria cache
    set_size {int} -- quantidade de conjuntos
    posicao_memoria {int} -- posição de memória que será acessada
  """
  num_conjunto = int(posicao_memoria)%int(set_size)
  lista_posicoes = get_lista_posicoes_cache_conjunto(memoria_cache,num_conjunto, set_size)

  # descobrir dentro do conjunto qual posição da cache tem menos acesso
  posicao_substituir = 0
  if len(lista_posicoes) > 1:

    if debug:
      imprimir_contador_lfu()

    # descobrir qual das posições é menos usada
    lista_qtd_acessos = []
    for qtd_acessos in lista_posicoes:
      lista_qtd_acessos.append(contador_lfu[qtd_acessos])

    posicoes_com_menos_acesso = min(lista_qtd_acessos)
    candidatos_lfu = []

    for qtd_acessos in lista_posicoes:
      if contador_lfu[qtd_acessos] == posicoes_com_menos_acesso:
        candidatos_lfu.append(qtd_acessos)

    # para garantir ordem aleatória de escolha caso duas ou mais posições
    # tenham o mesmo número de acessos
    posicao_substituir = random.choice(candidatos_lfu)

  # zera o número de acessos a posição que foi substituida
  contador_lfu[posicao_substituir] = 0

  # altera a posição de memória que está na cache
  memoria_cache[posicao_substituir] = posicao_memoria

  if debug:
    print('Posição Memória Lida No Arquivo: {}'.format(posicao_memoria))
    print('Conjunto: {}'.format(num_conjunto))
    print('Número de Acesso Da Posição com Menos Acesso: {}'.format(posicoes_com_menos_acesso))
    print('Lista Posições do Conjuno: {}'.format(lista_posicoes))
    print('Lista com as posições menos acessadas do conjunto: {}'.format(candidatos_lfu))
    print('Posição Cache Substituir: {}'.format(posicao_substituir))
    print('Posição de memória cache que será trocada é: {}'.format(posicao_substituir))


def algorithm_LRU_miss(memoria_cache, set_size, posicao_memoria):
  """Nessa algoritmo quando ocorre um HIT a posição vai para o topo da fila,
  se ocorrer um MISS remove o elemento 0 e a posição da cache onde a memória foi alocada é
  colocada no topo da fila

  Arguments:
    memoria_cache {list} -- memóiria cache
    set_size {int} -- quantidade de conjuntos
    posicao_memoria {int} -- posição de memória que será acessada
  """
  num_conjunto = get_num_conjuno_posicao_memoria(posicao_memoria, set_size)
  lista_posicoes = get_lista_posicoes_cache_conjunto(memoria_cache,num_conjunto, set_size)

  # copiar os valores de cada posição da cache do conjunto em questão uma posição para traz
  for posicao_cache in lista_posicoes:
    proxima_posicao = posicao_cache+set_size
    if proxima_posicao < len(memoria_cache):
      memoria_cache[posicao_cache] = memoria_cache[proxima_posicao]

  # coloca a posição que acabou de ser lida na topo da lista, assim, ela nesse momento é a última que será removida
  memoria_cache[lista_posicoes[-1]] = posicao_memoria

  if debug:
    print('Posição Memória: {}'.format(posicao_memoria))
    print('Conjunto: {}'.format(num_conjunto))
    print('Lista posições: {}'.format(lista_posicoes))


def algorithm_LRU_hit(memoria_cache, set_size, posicao_memoria, posicao_cache_hit):
  """Nessa algoritmo quando ocorre um HIT a posição vai para o topo da fila,
  se ocorrer um MISS remove o elemento 0 e a posição da cache onde a memória foi alocada é
  colocada no topo da fila

  Arguments:
    memoria_cache {list} -- memóiria cache
    set_size {int} -- quantidade de conjuntos
    posicao_memoria {int} -- posição de memória que será acessada
    posicao_cache_hit {int} -- posição de memória cache onde o dados da memória principal está
  """
  num_conjunto = get_num_conjuno_posicao_memoria(posicao_memoria, set_size)
  lista_posicoes = get_lista_posicoes_cache_conjunto(memoria_cache,num_conjunto, set_size)

  # copiar os valores de cada posição da cache do conjunto em questão uma posição para traz
  for posicao_cache in lista_posicoes:
    if posicao_cache_hit <= posicao_cache:
      # em uma cache com 4 conjuntos e 20 posições, as posições do 'conjunto 0' são:
      # [0, 4, 8, 12, 16], se o hit for na poição 4, então, então, será necessário copiar os dados da posição
      # 0 não faz nada
      # 4 <- 8
      # 8 <- 12
      # 12 <- 16
      # 16 <- 4
      proxima_posicao = posicao_cache+set_size
      if proxima_posicao < len(memoria_cache):
        memoria_cache[posicao_cache] = memoria_cache[proxima_posicao]

  # coloca no topo da pilha a posição de memória que acabou de ser lida
  memoria_cache[lista_posicoes[-1]] = posicao_memoria

  if debug:
    print('Posição Memória: {}'.format(posicao_memoria))
    print('Conjunto: {}'.format(num_conjunto))
    print('Lista posições: {}'.format(lista_posicoes))


def executar_mapeamento_associativo_conjunto(size, set_size, posicoes_memoria_para_acessar, algorithm='RANDOM'):
  """Executa a operação de mapeamento associativo, ou seja, não existe uma posição específica
  para o mapemento de uma posição de memória.

  Arguments:
    size {int} -- tamanho total de palavras da cache
    set_size {int} -- quantidade de conjuntos na cache
    posicoes_memoria_para_acessar {list} -- quais são as posições de memória que devem ser acessadas
    algorithm {str} -- Qual é a política para substituição caso a posição de memória desejada não esteja na cache E não exista espaço vazio
  """

  memoria_cache = inicializar_cache(size)

  # se o número de conjuntos for igual a zero, então estamos simulando
  # com a cache associativo!
  nome_mapeamento = 'Associativo'
  if set_size == 1:
    print_cache_associativo(memoria_cache)
  else:
    nome_mapeamento = 'Associativo Por Conjunto'
    print_cache_associativo_conjunto(memoria_cache, set_size)

  num_hit = 0
  num_miss = 0

  # se a política for fifo então inicializa a lista de controle
  if algorithm == 'FIFO':
    inicializar_contador_fifo()

  # se a política for fifo então inicializa a lista de controle
  if algorithm == 'LFU':
    inicializar_contador_lfu()

  # percorre cada uma das posições de memória que estavam no arquivo
  for index, posicao_memoria in enumerate(posicoes_memoria_para_acessar):
    print('\n\n\nInteração número: {}'.format(index+1))
    # verificar se existe ou não a posição de memória desejada na cache
    inserir_memoria_na_posicao_cache = verifica_posicao_em_cache_associativo_conjunto(memoria_cache, set_size, posicao_memoria)

    # a posição desejada já está na memória
    if inserir_memoria_na_posicao_cache >= 0:
      num_hit += 1
      print('Cache HIT: posiçao de memória {}, posição cache {}'.format(posicao_memoria, inserir_memoria_na_posicao_cache))

      # se for LFU então toda vez que der um HIT será incrementado o contador daquela posição
      if algorithm == 'LFU':
        contador_lfu[inserir_memoria_na_posicao_cache] += 1
        imprimir_contador_lfu()

      # se for LRU então toda vez que der um HIT será incrementado o contador daquela posição
      if algorithm == 'LRU':
        algorithm_LRU_hit(memoria_cache, set_size, posicao_memoria, inserir_memoria_na_posicao_cache)

    else:
      num_miss += 1
      print('Cache MISS: posiçao de memória {}'.format(posicao_memoria))

      # verifica se existe uma posição vazia na cache, se sim aloca nela a posição de memória
      posicao_vazia = existe_posicao_vazia(memoria_cache, set_size, posicao_memoria)

      if debug:
        print('Posição da cache ainda não utilizada: {}'.format(posicao_vazia))
        print('\nLeitura linha {}, posição de memória {}.'.format(index,posicao_memoria))

      ########
      # se posicao_vazia for < 0 então devemos executar as políticas de substituição
      ########
      if posicao_vazia >= 0:
        memoria_cache[posicao_vazia] = posicao_memoria
      elif algorithm == 'RANDOM':
        algorithm_RANDOM(memoria_cache,set_size,posicao_memoria)
      elif algorithm == 'FIFO':
        algorithm_FIFO(memoria_cache,set_size,posicao_memoria)
      elif algorithm == 'LFU':
        algorithm_LFU(memoria_cache,set_size,posicao_memoria)
      elif algorithm == 'LRU':
        algorithm_LRU_miss(memoria_cache,set_size,posicao_memoria)


    if set_size == 1:
      print_cache_associativo(memoria_cache)
    else:
      print_cache_associativo_conjunto(memoria_cache, set_size)

    if step:
      print('Tecle ENTER para processar o próximo passo:');
      input()

  # se for LFU e com debug imprimir os dados computador no contador LFU
  if algorithm == 'LFU' and debug:
    imprimir_contador_lfu()

  print('\n\n-----------------')
  print('Resumo Mapeamento {}'.format(nome_mapeamento))
  print('-----------------')
  print('Política de Substituição: {}'.format(algorithm))
  print('-----------------')
  print('Total de memórias acessadas: {}'.format(len(posicoes_memoria_para_acessar)))
  print('Total HIT {}'.format(num_hit))
  print('Total MISS {}'.format(num_miss))
  taxa_cache_hit = (num_hit / len(posicoes_memoria_para_acessar))*100
  print('Taxa de Cache HIT {number:.{digits}f}%'.format(number=taxa_cache_hit, digits=2))


def executar_mapeamento_associativo(size, posicoes_memoria_para_acessar, algorithm):
  """O mapeamento associativo é um tipo de mapeamento associativo por conjunto
  ou o número de conjunto é igual a 1

  Arguments:
    size {int} -- tamanho total de palavras da cache
    posicoes_memoria_para_acessar {list} - quais são as posições de memória que devem ser acessadas
    algorithm {str} -- qual será a política de subistituição
  """
  # o número 1 indica que haverá apenas um único conjunto no modo associativo por conjunto
  # que é igual ao modo associativo padrão! :) SHAZAM
  executar_mapeamento_associativo_conjunto(size, 1, posicoes_memoria_para_acessar, algorithm)


def executar_mapeamento_direto(size, posicoes_memoria_para_acessar):
  """Executa a operação de mapeamento direto.

  Arguments:
    size {int} -- tamanho total de palavras da cache
    posicoes_memoria_para_acessar {list} - quais são as posições de memória que devem ser acessadas
  """
  # zera tota a memória cache
  memoria_cache = inicializar_cache(size)

  print('Situação Inicial da Memória Cache')
  print_cache_direto(memoria_cache)

  hitoumiss = ''
  num_hit = 0;
  num_miss = 0
  for index, posicao_memoria in enumerate(posicoes_memoria_para_acessar):
    # no mapeamento direto, cada posição da memória principal tem uma posição
    # específica na memória cache, essa posição será calculada em função
    # do mod da posição acessada em relação ao tamanho total da cache
    posicao_cache = posicao_memoria % size

    # se a posição de memória principal armazenada na linha da cache for a posição
    # desejada então dá hit, caso contrário da miss
    if memoria_cache[posicao_cache] == posicao_memoria:
      num_hit += 1
      hitoumiss = 'Hit'
    else:
      num_miss += 1
      hitoumiss = 'Miss'

    memoria_cache[posicao_cache] = posicao_memoria

    print('\nLeitura linha {},  posição de memória desejada {}.'.format(index,posicao_memoria))
    print('       Status: {}'.format(hitoumiss))
    print_cache_direto(memoria_cache)

    if debug:
      print('Poisição de Memória: {} \nPosição Mapeada na Cache: {}'.format(posicao_memoria, posicao_cache))

  print('\n\n------------------------')
  print('Resumo Mapeamento Direto')
  print('------------------------')
  print('Total de memórias acessadas: {}'.format(len(posicoes_memoria_para_acessar)))
  print('Total HIT: {}'.format(num_hit))
  print('Total MISS: {}'.format(num_miss))
  taxa_cache_hit = (num_hit / len(posicoes_memoria_para_acessar))*100
  print('Taxa de Cache HIT: {number:.{digits}f}%'.format(number=taxa_cache_hit, digits=2))

##########################
# O programa começa aqui!
##########################

# parse dos parâmetros passados no comando
parser = argparse.ArgumentParser(prog='Simulador de Substituição de Paginas')
parser.add_argument('--size', required=True, type=int, help='Número total de posições da memória cache.')
parser.add_argument('--mapping', required=True, help='Valores aceitos para esse parâmetro são: DI / AS / AC - Tipos do mapeamento desejado.')
parser.add_argument('--algorithm', default='ALL', help='Valores aceitos para esse parâmetro são: RANDOM / FIFO / LRU / LFU - Qual será a política de substituição da memória que será utilizada.')
parser.add_argument('--set_size', type=int, default=2, help='Quando for escolhido o tipo de mapeamento AC deve-se informar quantos conjuntos devem ser criados dentro da memória cache.e.')
parser.add_argument('--path', required=True, default='', help='Nome do arquivo que possui as posições da memória principal que serão acessadas. Para cada linha do arquivo deve-se informar um número inteiro.')
parser.add_argument('--debug', default=0, help='Por padrão vem setado como 0, caso queira exibir as mensagens de debugs basta passar --debug 1.')
parser.add_argument('--step', default=0, help='Solicita a interação do usuário após cada linha processada do arquivo --step 1.')

args = parser.parse_args()

# recuperar toos os parâmetros passados
size = args.size
mapping = args.mapping
path = args.path
set_size = args.set_size
algorithm  = args.algorithm.upper()
debug = args.debug
step = args.step

if set_size <= 0:
  print('\n\n------------------------------')
  print('ERRO: O número de conjuntos não pode ser 0.')
  print('------------------------------')
  exit()


if path == '':
  print('\n\n------------------------------')
  print('ERRO: É necesário informar o nome do arquivo que será processado, o parâmetro esperado é --path seguido do nome do arquivo.')
  print('------------------------------')
  exit()

# lê o arquivo e armazena cada uma das posições de memória que será lida em uma lista
try:
  f = open(path, "r")
  posicoes_memoria_para_acessar = []
  for posicao_memoria in f:
    posicoes_memoria_para_acessar.append(int(re.sub(r"\r?\n?$", "", posicao_memoria, 1)))
  f.close()
except IOError as identifier:
  print('\n\n------------------------------')
  print('ERRO: Arquivo \'{}\'não encontrado.'.format(path))
  print('------------------------------')
  exit()

if len(posicoes_memoria_para_acessar) == 0:
    print('\n\n------------------------------')
    print('ERRO: o arquivo {} não possui nenhuma linha com números inteiros.'.format(path))
    print('------------------------------')
    exit()

print('+====================+')
print('| SIMULADOR DE CACHE |')
print('+====================+')
print('+ Setando parâmetros iniciais da cache+')


if mapping != 'DI':
  if algorithm != 'RANDOM' and algorithm != 'FIFO' and algorithm != 'LRU' and algorithm != 'LFU' and algorithm != 'ALL':
    print('\n\n------------------------------')
    print('ERRO: A política de substituição {} não existe.'.format(algorithm))
    print('------------------------------')
    exit()

# se o tipo do mapeamento for direto DI
if mapping == 'DI':
  executar_mapeamento_direto(size, posicoes_memoria_para_acessar)
elif mapping == 'AS':
  if (algorithm == 'ALL'):
    executar_mapeamento_associativo(size, posicoes_memoria_para_acessar, 'RANDOM')
    executar_mapeamento_associativo(size, posicoes_memoria_para_acessar, 'FIFO')
    executar_mapeamento_associativo(size, posicoes_memoria_para_acessar, 'LRU')
    executar_mapeamento_associativo(size, posicoes_memoria_para_acessar, 'LFU')
  else:
    executar_mapeamento_associativo(size, posicoes_memoria_para_acessar, algorithm)

elif mapping == 'AC':
  # o número de conjuntos deve ser um divisor do total da memória
  if size%set_size != 0:
    print('\n\n------------------------------')
    print('ERRO: O número de conjuntos {} deve ser obrigatoriamente um divisor do total de memória cache disponível {}.'.format(set_size, size))
    print('------------------------------')
    exit()

  if (algorithm == 'ALL'):
    executar_mapeamento_associativo_conjunto(size, set_size, posicoes_memoria_para_acessar, 'RANDOM')
    executar_mapeamento_associativo_conjunto(size, set_size, posicoes_memoria_para_acessar, 'FIFO')
    executar_mapeamento_associativo_conjunto(size, set_size, posicoes_memoria_para_acessar, 'LRU')
    executar_mapeamento_associativo_conjunto(size, set_size, posicoes_memoria_para_acessar, 'LFU')
  else:
    executar_mapeamento_associativo_conjunto(size, set_size, posicoes_memoria_para_acessar, algorithm)
else:
  print('\n\n------------------------------')
  print('ERRO: O tipo de mapeamento \'{}\'não foi encontrado. \nOs valores possíveis para o parâmetro --mapping são: DI / AS / AC'.format(mapping))
  print('------------------------------')
  exit()

if debug:
  print('\n')
  print('-'*80)
  print('Parâmetros da Simulação')
  print('-'*80)
  print("Arquivo com as posições de memória: {}".format(path))
  print('Número de posições de memória: {}'.format(len(posicoes_memoria_para_acessar)))
  print('As posições são: {}'.format(posicoes_memoria_para_acessar))
  print('Tamanho total da cache: {}'.format(size))
  print("Tipo Mapeamento: {}".format(mapping))
  if mapping != 'AS':
    print("Quantidade de Conjuntos: {}".format(set_size))
  print("Política de Substituição: {}".format(algorithm))
  print("Debug: {}".format(debug))
  print("Step: {}".format(step))
  print('-'*80)

