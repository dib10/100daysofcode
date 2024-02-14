from arte import logo
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
print("Bem-vindo ao Cifra de César")

def caesar(texto,deslocamento,direcao):
    texto_criptografado = ""
    if direcao == "decodificar":
        deslocamento *= -1
    for letra in texto:
        if letra not in alfabeto:
            texto_criptografado += letra
            continue
        posicao = alfabeto.index(letra)
        nova_posicao = posicao + deslocamento
        texto_criptografado += alfabeto[nova_posicao]
    print(f"O texto '{texto}' {direcao} é: {texto_criptografado}")

continuar = "sim"
while continuar == "sim":
    direcao = input("Digite 'codificar' para criptografar, digite 'decodificar' para descriptografar:\n").lower()
    texto = input("Digite sua mensagem:\n").lower()
    deslocamento = int(input("Digite o número de deslocamento:\n"))
    if deslocamento > 26:
        deslocamento = deslocamento % 26
    caesar(texto,deslocamento,direcao)
    continuar = input("Deseja continuar? sim ou não\n").lower()