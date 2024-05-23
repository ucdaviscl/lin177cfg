from nltk import PCFG
from nltk.parse import pchart
import pcfg

class grammar:
    def __init__(self, instr):
        self.g = PCFG.fromstring(instr)
        self.parser = parser(self.g)
        self.generator = generator(instr)

    def parse(self, s, n=10):
        self.parser.parse(s, n)

    def generate(self, n=1):
        self.generator.generate(n)

class parser:
    p = None
    def __init__(self, g):
        self.p = pchart.InsideChartParser(g)

    def parse(self, s, n=10):
        tokens = s.split()
        trees = list(self.p.parse(tokens))
        if n > len(trees):
            n = len(trees)
        print("Found ", len(trees), "trees. Printing top", n)
        print()
        for i in range(n):
            print("Tree", i)
            print(trees[i])
            print()

class generator:
    gen = None
    def __init__(self, g):
        self.gen = pcfg.PCFG.fromstring(g)
    
    def generate(self, n=1):
        for s in self.gen.generate(n):
            print(s)





