from itertools import chain
import json


class Component:
    def __init__(self, *algorithm_list):
        self.algorithm_list = algorithm_list
        self.visitedList = []

    def __call__(self, source_object):
        result = []
        queue = [source_object]
        while queue:
            result.extend(queue)
            queue = list(chain.from_iterable(
                algorithm(item)
                for item in queue
                for algorithm in self.algorithm_list
            ))
        return result

    def find_index(self, list_types, source_object):
        for i in list_types:
            if isinstance(source_object, type(i)):
                return list_types.index(i)

    def depth_first(self, graph, current_vertex, visited):
        visited.append(current_vertex)
        for vertex in range(len(graph[0])):
            if graph[current_vertex][vertex] == 1 and vertex not in visited:
                self.depth_first(graph, vertex, visited.copy())
        self.visitedList.append(visited)

    def print_all_paths(self, types):
        for i in self.visitedList:
            for j in i:
                print("/", type(types[j]).__name__, end='', sep='')
            print()

    def my_code(self, source_object):
        types = [source_object]
        all_ways = []
        temp = []
        for obj_type in types:
            result = self.__call__(obj_type)
            for i in result:
                flag_for_types = False
                flag_for_temp = False
                for j in types:
                    if isinstance(i, type(j)):
                        flag_for_types = True
                        break
                for j in temp:
                    if isinstance(i, type(j)):
                        flag_for_temp = True
                        break
                if not flag_for_types:
                    types.append(i)
                if not flag_for_temp:
                    temp.append(i)
            if temp:
                all_ways.append(temp)
            temp = []

        table = [0] * len(types)
        for i in range(len(types)):
            table[i] = [0] * len(types)
        for i in range(len(types)):
            for j in all_ways[i][1:]:
                index = self.find_index(types, j)
                table[i][index] = 1
        self.depth_first(table, 0, [])
        print(self.visitedList)
        self.print_all_paths(types)
        return []

class Apple:
    pass


class Orange:
    def __init__(self, number):
        self.number = number


class Lemon:
    pass


class FirstAlgorithm:
    SPECIFICATION = {
        Orange: [Apple],
        Lemon: [Orange, Apple]
    }

    def __call__(self, source_object):
        if isinstance(source_object, Orange):
            return [Apple() for _ in range(source_object.number)]
        if isinstance(source_object, Lemon):
            return [Orange(3), Apple()]
        return []


class EmptyAlgorithm:
    SPECIFICATION = {}

    def __call__(self, source_object):
        return []


component = Component(FirstAlgorithm())
t = Lemon()
(component.my_code(t))
