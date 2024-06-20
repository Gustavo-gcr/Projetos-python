num=int(input('Escolha um número que vc deseja saber a taboada, se for negativo o projeto ira ser fechado:'))
while num>0:
    for c in range(10,0,-1):
        print(c*num)
        c-=1
    num=int(input('Escolha um número que vc deseja saber a taboada, se for negativo o projeto ira ser fechado:'))
print('Fim do teste\n')
#--------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------Codigo ---------------------------------------------------
class Pessoa:
    def __init__(self, nome, idade, sexualidade):
        self.nome = nome
        self.idade = idade
        self.sexualidade = sexualidade

# Lista para armazenar as pessoas cadastradas
lista_pessoas = []

# Loop para cadastrar as pessoas
for i in range(1, 9):  # de 1 a 8
    nome = input(f'Olá, por favor escreva o nome da pessoa {i}: ')
    idade = int(input('Escreva a idade: '))
    sexualidade = input('Escreva a sexualidade: ')
    pessoa = Pessoa(nome, idade, sexualidade)
    lista_pessoas.append(pessoa)
    print(f'Pessoa {i} cadastrada.')

# Contagem de homens
cont_homem = sum(1 for p in lista_pessoas if p.sexualidade == 'm')

# Contagem de pessoas maiores de idade
cont_maior_idade = sum(1 for p in lista_pessoas if p.idade >= 18)

# Contagem de mulheres maiores de idade
cont_mulher_maior_idade = sum(1 for p in lista_pessoas if p.idade >= 18 and p.sexualidade == 'f')

# Saídas
print(f'O número de homens cadastrados é {cont_homem} e de mulheres é {len(lista_pessoas) - cont_homem}.')
print(f'O número de pessoas maiores de idade cadastradas é {cont_maior_idade} e de menores é {len(lista_pessoas) - cont_maior_idade}.')
print(f'O número de mulheres maiores de idade cadastradas é {cont_mulher_maior_idade} e de menores ou homens é {len(lista_pessoas) - cont_mulher_maior_idade}.')

