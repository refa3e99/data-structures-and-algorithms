import pytest
from graph.graph import *


def test_exists_graph():

    assert Graph


def test_empty_graph(empty_graph):

    actual = empty_graph.size()
    expected = 0
    assert actual == expected


def test_depth_first_one(graph):

    actual = graph[0].depth_first(graph[1])
    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'F', 'H']
    assert actual == expected


def test_depth_first_two(graph):

    actual = graph[0].depth_first(graph[2])
    expected = ['B', 'A', 'D', 'E', 'F', 'H', 'C', 'G']
    assert actual == expected


def test_depth_first_three(graph):

    actual = graph[0].depth_first(graph[3])
    expected = ['E', 'D', 'A', 'B', 'C', 'G', 'F', 'H']
    assert actual == expected



@pytest.fixture
def empty_graph():
    empty_graph = Graph()
    return empty_graph


@pytest.fixture
def graph():
    graph = Graph()
    A = graph.add_node('A')
    B = graph.add_node('B')
    C = graph.add_node('C')
    D = graph.add_node('D')
    E = graph.add_node('E')
    F = graph.add_node('F')
    G = graph.add_node('G')
    H = graph.add_node('H')

    graph.add_edge(A, B)
    graph.add_edge(A, D)
    graph.add_edge(B, C)
    graph.add_edge(C, G)
    graph.add_edge(D, E)
    graph.add_edge(D, F)
    graph.add_edge(D, H)

    graph.add_edge(B, D)
    graph.add_edge(F, H)
    return graph, A, B, E