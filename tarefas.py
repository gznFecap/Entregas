# Sistema de gerenciamento de tarefas
# Permite cadastrar, listar e organizar tarefas

import argparse
import json
from pathlib import Path

CAMINHO_PADRAO = Path('tarefas.json')


def carregar(caminho):
    if not caminho.exists():
        return []
    return json.loads(caminho.read_text(encoding='utf-8'))


def salvar(caminho, tarefas):
    caminho.write_text(json.dumps(tarefas, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def adicionar(tarefas, titulo, prioridade='media'):
    if not titulo.strip():
        raise ValueError('O título não pode ficar vazio.')
    if prioridade not in ('baixa', 'media', 'alta'):
        raise ValueError('Prioridade inválida.')
    codigo = max((t['id'] for t in tarefas), default=0) + 1
    tarefa = {'id': codigo, 'titulo': titulo.strip(), 'concluida': False, 'prioridade': prioridade}
    tarefas.append(tarefa)
    return tarefa


def concluir(tarefas, codigo):
    for tarefa in tarefas:
        if tarefa['id'] == codigo:
            tarefa['concluida'] = True
            return tarefa
    raise ValueError('Tarefa não encontrada.')


def main():
    parser = argparse.ArgumentParser(description='Sistema simples de gerenciamento de tarefas')
    parser.add_argument('--arquivo', type=Path, default=CAMINHO_PADRAO)
    sub = parser.add_subparsers(dest='comando', required=True)
    add = sub.add_parser('adicionar', help='Cadastrar uma tarefa')
    add.add_argument('titulo')
    add.add_argument('--prioridade', choices=['baixa', 'media', 'alta'], default='media')
    listar = sub.add_parser('listar', help='Mostrar tarefas')
    listar.add_argument('--status', choices=['todas', 'pendentes', 'concluidas'], default='todas')
    done = sub.add_parser('concluir', help='Concluir uma tarefa')
    done.add_argument('id', type=int)
    args = parser.parse_args()
    tarefas = carregar(args.arquivo)
    try:
        if args.comando == 'adicionar':
            item = adicionar(tarefas, args.titulo, args.prioridade)
            salvar(args.arquivo, tarefas)
            print(f'Tarefa #{item["id"]} adicionada.')
        elif args.comando == 'concluir':
            item = concluir(tarefas, args.id)
            salvar(args.arquivo, tarefas)
            print(f'Tarefa #{item["id"]} concluída.')
        else:
            if not tarefas:
                print('Nenhuma tarefa cadastrada.')
            for item in tarefas:
                if args.status == 'pendentes' and item['concluida']:
                    continue
                if args.status == 'concluidas' and not item['concluida']:
                    continue
                marca = 'x' if item['concluida'] else ' '
                print(f'[{marca}] #{item["id"]} - {item["titulo"]} (prioridade: {item.get("prioridade", "media")})')
    except ValueError as erro:
        parser.error(str(erro))


if __name__ == '__main__':
    main()
