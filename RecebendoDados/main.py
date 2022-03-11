"""
AULA 12 - SEÇÃO 3
GABRIELA MARCULINO.

    Nesta aula aprendemos todas as formas possíveis para receber dados do usuário,
desde a forma mais antiga até a mais atual e também obteve-se uma breve introdução
sobre tipagens de dados e formatação. Dentre todas as informações adquiridas, vale
ressaltar algumas que veremos a seguir:

    Em python, tudo que estiver dentro de uma função input() é retornado como uma
String (um tipo de dado do qual o computador reconhece apenas como letras, ou seja,
independente se for um número não será possível realizar cálculos).

    Tudo que estiver entre aspas, seja ela simples, duplas, triplas ou duplas triplas
será reconhecido como uma String também.
"""

# Exemplos de entradas de dados
# SIMPLES

'''
print("Qual o seu nome? ")
nome = input()
'''

# MAIS COMUMENTE UTILIZADO
nome = input("Qual o seu nome? ")
print(f'Seja bem-vindo(a) {nome}')

# O int utilizado após o nome da variável é para converter a String para o tipo inteiro e assim,
# podemos utilizar o dado armazenado na idade para futuros cálculos.
idade = int(input("Qual a sua idade? "))
print(f'A {nome} tem {idade} anos')
print(f'A {nome} nasceu em {2022 - idade}')
