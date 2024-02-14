pais = input("Nome do país: ") # Adicione o nome do país
visitas = int(input("Digite o número de visitas: ")) # Número de visitas
lista_de_cidades = eval(input()) # crie uma lista a partir de uma string formatada, mas a inserção do usuário deve ser do tipo: ["cidade1", "cidade2", "cidade3"]

registro_de_viagens = [ # colchete é uma lista, chave é um dicionário
  {
    "pais": "França",
    "visitas": 12,
    "cidades": ["Paris", "Lille", "Dijon"]
  }, #isso é uma lista de dicionários
  {
    "pais": "Alemanha",
    "visitas": 5,
    "cidades": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Não mude o código acima 👆

# TODO: Escreva a função que permitirá a adição de novos países
# ao registro_de_viagens.
def add_novo_pais(pais,visitas,lista_de_cidades):
    novo_pais = {}
    novo_pais["pais"] = pais #aqui novo_pais é um dicionário e pais é uma chave 
    novo_pais["visitas"] = visitas
    novo_pais["cidades"] = lista_de_cidades
    registro_de_viagens.append(novo_pais)

# Não mude o código abaixo 👇
add_novo_pais(pais, visitas, lista_de_cidades)
print(f"Eu estive em {registro_de_viagens[2]['pais']} {registro_de_viagens[2]['visitas']} vezes.") # [2] é o índice do novo país, pois a lista começa em 0, e o novo país é o terceiro país
print(f"Minha cidade favorita foi {registro_de_viagens[2]['cidades'][0]}.") #aqui o 0 é o índice da cidade favorita, pois a lista começa em 0   