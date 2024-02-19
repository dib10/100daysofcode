def formatar_nome(p_nome, u_nome):
     p_nome = p_nome.title()
     u_nome = u_nome.title()
     return print(f"{p_nome} {u_nome}")

nome = input('Digite seu primeiro nome: ')
sobrenome = input('Digite seu sobrenome: ')
formatar_nome(nome, sobrenome)

    