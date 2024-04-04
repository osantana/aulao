import sqlite3

cursos = [
    "Português",
    "Inglês I",
    "Inglês II",
    "Inglês III",
    "Inglês IV",
    "Geografia",
    "Bioquímica",
    "Materiais",
]

con = sqlite3.connect("iolife.db")
cur = con.cursor()

for curso in cursos:
    cur.execute("INSERT INTO cursos (nome) VALUES (?)", (curso,))

con.commit()
