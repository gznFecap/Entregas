# Gerenciador de Tarefas

Sistema feito em Python para organizar tarefas do dia a dia.

## Funcionalidades

- Adicionar tarefas.
- Listar tarefas cadastradas.
- Mostrar apenas tarefas pendentes ou concluídas.
- Definir prioridade baixa, média ou alta.
- Marcar tarefas como concluídas.

As tarefas ficam salvas em um arquivo `tarefas.json`.

## Como usar

Abra o terminal na pasta do projeto e execute:

```bash
py tarefas.py adicionar "Estudar Git"
py tarefas.py listar
py tarefas.py concluir 1
```

Para listar só as tarefas pendentes:

```bash
py tarefas.py listar --status pendentes
```

Para adicionar uma tarefa com prioridade:

```bash
py tarefas.py adicionar "Fazer trabalho" --prioridade alta
```

## Tecnologias

Python e Git/GitHub.
