import random


def generate_random_graph(num_vertices, num_edges, flag):
    # Проверка: количество рёбер не может превышать максимальное возможное количество рёбер в графе
    max_possible_edges = num_vertices * (num_vertices - 1) // 2
    if num_edges > max_possible_edges:
        print("Количество рёбер превышает максимальное возможное количество рёбер в графе.")
        return

    # Используем set для хранения рёбер, чтобы избежать дубликатов
    edges = set()

    # Используем список для отслеживания представителя в остовном дереве
    parent = list(range(num_vertices + 1))

    def find(vertex):
        """Находим корневого представителя для вершины."""
        if parent[vertex] != vertex:
            parent[vertex] = find(parent[vertex])
        return parent[vertex]

    def union(vertex1, vertex2):
        """Объединяем два множества в одно."""
        root1 = find(vertex1)
        root2 = find(vertex2)
        if root1 != root2:
            parent[root2] = root1

    # Если flag == True, нужно сгенерировать граф с циклом
    if flag:
        # Начнем с остовного дерева, чтобы гарантировать, что граф начнет без циклов
        for i in range(1, num_vertices):
            union(i, i + 1)
            edges.add((i, i + 1))

        # Добавим циклы до достижения количества рёбер
        while len(edges) < num_edges:
            vertex1 = random.randint(1, num_vertices)
            vertex2 = random.randint(1, num_vertices)

            if vertex1 != vertex2:
                # Проверяем, что ребро не уже существует
                if (vertex1, vertex2) not in edges and (vertex2, vertex1) not in edges:
                    edges.add((vertex1, vertex2))

    # Если flag == False, нужно сгенерировать граф без циклов
    else:
        # Создаем случайное остовное дерево
        while len(edges) < num_vertices - 1:
            vertex1 = random.randint(1, num_vertices)
            vertex2 = random.randint(1, num_vertices)

            # Убедимся, что вершины различны и не создается цикл
            if vertex1 != vertex2 and find(vertex1) != find(vertex2):
                edges.add((vertex1, vertex2))
                union(vertex1, vertex2)

        # Добавляем дополнительные рёбра без циклов, если нужно
        remaining_edges = num_edges - len(edges)
        while remaining_edges > 0:
            vertex1 = random.randint(1, num_vertices)
            vertex2 = random.randint(1, num_vertices)

            # Убедимся, что вершины различны и не создается цикл
            if vertex1 != vertex2 and find(vertex1) != find(vertex2):
                edges.add((vertex1, vertex2))
                remaining_edges -= 1

    # Печать количества вершин и рёбер
    print(num_vertices, num_edges)

    # сохранение рёбер
    f = open("input.txt",'w')
    f.write(f'{num_vertices} {num_edges}\n')
    for edge in edges:
        f.write(f'{edge[0]} {edge[1]}\n')
    f.write(f'{random.randint(1, num_vertices)}')
    f.close()


def main():
    # Укажите количество вершин и рёбер, которые вы хотите сгенерировать

    num_vertices, num_edges, flag = map(int, input().split())  # Например, 13 вершин
    # Например, 12 рёбер
    # True для графа с циклом, False для графа без цикла

    # Генерация случайного графа
    generate_random_graph(num_vertices, num_edges, flag)


if __name__ == "__main__":
    main()
