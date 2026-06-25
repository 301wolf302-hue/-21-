"""
Задание №17. Задача "Почтальон" - минимальное количество извинений.
"""

import sys
sys.setrecursionlimit(1000000)


def read_graph(filename):
    """
    Читает граф из файла.
    Возвращает: список смежности, список писем, количество вершин
    """
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    n = int(lines[0])
    adj = [[] for _ in range(n + 1)]
    letters = [0] * (n + 1)
    
    for i in range(1, n + 1):
        parts = list(map(int, lines[i].split()))
        ni = parts[0]      # количество соседей
        li = parts[1]      # количество писем
        letters[i] = li
        
        # Добавляем ребра к соседям
        for j in range(ni):
            neighbor = parts[2 + j]
            adj[i].append(neighbor)
    
    return adj, letters, n


def dfs(u, parent, adj, letters):
    """
    Обход дерева.
    Возвращает: (количество ребер с письмами, максимальная глубина до письма)
    """
    edges = 0
    max_depth = -1  # -1 значит нет писем
    
    # Проверяем письмо в текущей вершине
    if letters[u] > 0:
        max_depth = 0
    
    # Обходим соседей
    for v in adj[u]:
        if v == parent:
            continue
        
        child_edges, child_depth = dfs(v, u, adj, letters)
        
        # Если у ребенка есть письма, учитываем ребро
        if child_depth != -1:
            edges += 1 + child_edges
            if child_depth + 1 > max_depth:
                max_depth = child_depth + 1
    
    return edges, max_depth


def solve(filename):
    """
    Решает задачу.
    Формула: 2 * ребер - максимальная_глубина
    """
    adj, letters, n = read_graph(filename)
    
    # Запускаем DFS от корня (вершина 1)
    edges, max_depth = dfs(1, 0, adj, letters)
    
    if max_depth == -1:
        return 0
    
    return 2 * edges - max_depth


def main():
    print("Задача 'Почтальон' - минимальное количество извинений")
    print("Пример файла:")
    print("5")
    print("3 2 2 5 4")
    print("1 1 1")
    print("1 1 4")
    print("2 2 3 1")
    print("1 3 1")
    print()
    
    while True:
        filename = input("Введите имя файла (или 'exit'): ").strip()
        
        if filename.lower() == 'exit':
            print("До свидания!")
            break
        
        if not filename:
            print("Ошибка: имя файла не может быть пустым")
            continue
        
        try:
            result = solve(filename)
            print(f"Минимальное количество извинений: {result}\n")
        except FileNotFoundError:
            print(f"Ошибка: файл '{filename}' не найден\n")
        except Exception as e:
            print(f"Ошибка: {e}\n")


if __name__ == "__main__":
    main()