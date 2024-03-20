notas = []

while True:
    nome = input("Nome: ").strip()
    if nome == "":
        break

    while True:
        ra = input("RA: ").strip()
        if not ra.isnumeric():
            print("RA inválido, digite novamente.")
            continue
        if len(ra) < 9:
            print("RA inválido, digite novamente")
            continue
        break

    resultados = []
    for resultado in range(3):
        avaliacao = -1
        while avaliacao < 0:
            try:
                avaliacao = int(input(f"A{resultado+1}: "))
                if avaliacao < 0:
                    print(f"Nota A{resultado+1} inválida")
            except ValueError:
                print(f"Nota A{resultado+1} inválida")
                continue
        resultados.append(avaliacao)

    a1, a2, a3 = resultados
    notas.append(
        (nome, ra, a1, a2, a3, sum(resultados))
    )

    # nota = sum(resultados)
    # notas.append(
    #     (nome, ra, resultados[0], resultados[1], resultados[2], nota)
    # )


print(f"{'Nome':40s} | {'RA':9s} | {'A1':3s} | {'A2':3s} | {'A3':3s} | {'Final':3s}")

for nome, ra, a1, a2, a3, nota in notas:
    print(f"{nome:40s} | {ra:9s} | {a1:-3d} | {a2:-3d} | {a3:-3d} | {nota:-5d}")


"""
 +-----,
 o     |
/|\    |
/ \    |
-------+---
1. cabeça
2. tronco
3. braço esq.
4. braço dir.
5. perna esq.
6. perna dir.

20 palavras entre 5 e 12 letras
ignora acentos, maiúsculas, minúsculas, símbolos e números
"""
