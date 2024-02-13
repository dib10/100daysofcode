alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direcao = input("Digite 'codificar' para criptografar, digite 'decodificar' para descriptografar:\n").lower()

texto = input("Digite sua mensagem:\n").lower()
deslocamento = int(input("Digite o número de deslocamento:\n"))
if deslocamento > 26:
    deslocamento = deslocamento % 26 
    #se o número de deslocamento for maior que 26, o resto da divisão por 26 será o número de deslocamento, ou seja 27 % 26 = 1

def caesar(texto,deslocamento,direcao):
    texto_criptografado = ""
    for letra in texto:
        posicao = alfabeto.index(letra)
        nova_posicao = posicao + deslocamento
        if direcao == "decodificar":
            nova_posicao -= 2*deslocamento
        texto_criptografado += alfabeto[nova_posicao]
    print(f"O texto '{texto}' {direcao} é: {texto_criptografado}")

caesar(texto,deslocamento,direcao)