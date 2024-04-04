# Banco de Dados

* Ferramenta: editor de tabelas para sqlite

## Alunos

* `id` (PK)
* `nome`
* `ra`
* `curso` 1-N FK(Cursos)
* *turmas* N-N (ver abaixo)

| id | nome    | ra  | curso
|----|---------|-----|--------
| 1  | Fulano  | 123 | 2 (vet)
| 2  | Cicrano | 456 | 1 (med)

1. 1-N: Sempre o lado com N elementos referencia o 1 elemento
2. Chave Primária (Primary Key PK)
3. Chave Estrangeira (Foreign Key FK)
4. N-N: Tabela intermediária
    `Aluno (N) <----[AlunoTurma]----> (N) Turmas`


```sql
CREATE TABLE "alunos" (
	"id"	INTEGER NOT NULL,
	"nome"	TEXT NOT NULL,
	"ra"	TEXT  NOT NULL UNIQUE,
	"cursos"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("cursos") REFERENCES cursos(id)
);
```

## AlunoTurma

* `id` (PK)
* `aluno` FK(alunos)
* `turma` FK(turmas)


| id | aluno       | turma
|----|-------------|------------------
| 1  | 1 (fulano)  | 1 (biomedicina)
| 2  | 2 (cicrano) | 1 (biomedicina)

```sql
CREATE TABLE "aluno_turma" (
	"id"	INTEGER NOT NULL,
	"aluno"	INTEGER NOT NULL,
	"turma"	INTEGER NOT NULL,
	UNIQUE("aluno","turma"),
	PRIMARY KEY("id" AUTOINCREMENT)
  	FOREIGN KEY("aluno") REFERENCES alunos(id),
  	FOREIGN KEY("turma") REFERENCES turmas(id)
);
```

## Cursos

* `id` (PK)
* `nome`
* *ucs* N-N
  `Cursos <---[CursosUCs]---> UCs`

| id | nome
|----|--------------
| 1  | Medicina
| 2  | Veterinária

```sql
CREATE TABLE "cursos" (
	"id"	INTEGER NOT NULL,
	"nome"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
```

### Inserindo registros

```sql
INSERT INTO cursos
    (nome)
VALUES
    ("Biomedicina");

INSERT INTO cursos
    (nome)
VALUES
    ("Química"),
    ("Física"),
    ("Estatística");
```

### Mostrando registros

```sql
SELECT id, nome  -- ou SELECT * para todas as colunas
FROM cursos -- FROM [nome-da-tabela]
```

## CursosUCs

* `id` (PK)
* `curso` FK(Cursos)
* `uc` FK(UCs)

## UCs

* `id` (PK)
* `nome`

| id | nome
|----|--------------
| 1  | Biomedicina
| 2  | Química

## Turmas

* `id` (PK)
* `nome`
* `uc` FK(UCs)

| id | nome          | uc
|----|---------------|-------------
| 1  | BIOM-NOT-CAMP | 1 (biom)
| 2  | QUIM-MAT-VIRT | 2 (química)

## Avaliacoes

* `id` (PK)
* `aluno` FK(Alunos)
* `turma` FK(Turma)
* `codigo`
* `nota`

id | aluno   | turma    | codigo | nota
---|---------|----------|--------|-------
1  | 1 (ful) | 1 (biom) | A1     | 20
2  | 1 (ful) | 1 (biom) | A2     | 30
3  | 1 (ful) | 1 (biom) | A3     | 40
4  | 2 (ful) | 2 (quim) | A1     | 20
5  | 2 (ful) | 2 (quim) | A2     | 30
6  | 2 (ful) | 2 (quim) | A3     | 40
