# -*- coding: utf-8 -*-

import argparse, random, re

class Dado():
    def __init__(self, memory_position, access_number, life_cycles, reading_order):

    def printCacheDirect(cache):
        print("+------- Cache -----+")
        print("|#\t|\t Data|")
        print("+----------------------")
        for position, value in cache.items():
            print("|{} \t|\t    {}|".format(position, value))
        print("+---------------------+")

    def printCacheAssociationSet(cache, amount_set):
        print("+------- Cache -----+")
        print("|#\t|Cnj\t|\t Data|")
        print("+----------------------")
        for position, value in cache.items():
            number_set = int(position)%int(amount_set)
            print("|{} \t|{}\t|\t    {}|".format(position, number_set, value))
        print("+---------------------+")

    def initializeCache(total_cache):
        memory_cache = {}
    
        for x in range(0, total_cache):
            memory_cache[x] = -1

        return memory_cache