import numpy
import ast

with open("input.txt") as input:
    for line in input:
        address1, address2 = line.split()
        text1 = open(address1, "r"); text2 = open(address2, "r")
        tx1 = ast.parse(text1.read()); tx2 = ast.parse(text2.read())

scores = open("scores.txt", 'r') #результирующий файл

def main(ast_tree): #обработка АСТ
    analysis = Analyzer()
    analysis.visit(ast_tree)
    analysis.report()


class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.stats = {"import": [], "from": []}

def levenshteinDistanceDP(token1, token2):
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    printDistances(distances, len(token1), len(token2))
    return 0


def printDistances(distances, token1Length, token2Length):
    for t1 in range(token1Length + 1):
        for t2 in range(token2Length + 1):
            print(int(distances[t1][t2]), end=" ")
        print()

