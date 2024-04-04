import csv

arquivo = input("Informe o nome do arquivo CSV:")
arquivo = open(arquivo)

arquivo_csv = csv.reader(arquivo)

registros_ordenados = sorted(arquivo_csv, key=lambda x: (x[2], x[3]))

print(f"{'Nome':30s} | {'RA':9s} | {'Curso':25s} | {'UC':30s} | {'A1':3s} | {'A2':3s} | {'A3':3s} | {'Final':3s}")

for registro in registros_ordenados:
    if not registro:
        continue

    nome, ra, curso, uc, a1, a2, a3 = registro

    if nome == "Nome":
        continue

    a1 = int(a1)
    a2 = int(a2)
    a3 = int(a3)
    nota = a1 + a2 + a3

    print(f"{nome:30s} | {ra:9s} | {curso:25s} | {uc:30s} | {a1:-3d} | {a2:-3d} | {a3:-3d} | {nota:-5d}")

"""
Atividade:
Gerar o relatório agrupado por turma (turma == Curso + UC)
"""
