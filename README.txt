# Positive_Technologies_Test

1я задача
изменила немного формат вывода, потому что для больших json файлов(содержащих словарь, в котором value содержит list, который в свою очередь содержит словарь) вывод каждого ключа для словаря с использованием отступа выглядел не так красиво, как через '::'

алгоритм для 3ей задачи:

1. Создаем список, содержащий списки объектов, которые возможно получить, подавая на вход имеющимся алгоритмам каждый из существующих объектов.
2. Превращаем этот список в матрицу смежности, где 0 означает, что из индекса строки, соответствующего какому-то определенному объекта, не получить индекс столбца, соотвествующий определенному объекту, а 1 означает возможность получить из объекта строки объект столбца.
3. Представим, что у нас есть дерево путей. 
Например
Lemon
|      \        \
Orange  Orange  Apple
|
Apple
Нам нужен обход в глубину для получения всех возможных путей. 
То же дерево можно представить в виде матрицы смежности:
0  1  2  3
1  0  1  1
2  0  0  1
3  0  0  0
Матрица смежности для нашего дерева путей получена в пункте 2. Соответственно остается совершить обход в глубину для получаения окнчательно результата
/Lemon/Orange/Apple
/Lemon/Orange
/Lemon/Apple
/Lemon
