from nltk import grammar, CFG, PCFG, Nonterminal
from nltk.parse import pchart, BottomUpChartParser, FeatureChartParser
from nltk.parse.generate import generate
import random

class cfg:
    def __init__(self, instr):
        self.g = CFG.fromstring(instr)
        self.parser = cfg_parser(self.g)

    def parse(self, s, n=10):
        self.parser.parse(s, n)

    def generate(self, n=100, depth=7):
        print("Generating at most", n, "sentences with depth limit", depth, ":")
        print()
        cnt = 0
        for s in generate(self.g, n=n, depth=depth):
            cnt += 1
            print(' '.join(s))
        print()
        print("Generated", cnt, "sentences.")

class ucfg:
    def __init__(self, instr):
        self.g = grammar.FeatureGrammar.fromstring(instr)
        self.parser = ucfg_parser(self.g)

    def parse(self, s, n=10):
        self.parser.parse(s, n)

    def generate(self, n=100, depth=7):
        gen = {}
        print("Generating at most", n, "sentences with depth limit", depth, ":")
        print()
        cnt = 0
        for s in generate(self.g, n=n*1000, depth=depth):
            t = list(self.parser.p.parse(s))
            if len(t) == 0:
                continue
            sentence = ' '.join(s)
            if sentence in gen:
                continue
            gen[sentence] = 1
            cnt += 1
            print(' '.join(s))
            if cnt == n:
                break
        print()
        print("Generated", cnt, "sentences.")

class pcfg:
    def __init__(self, instr):
        self.g = PCFG.fromstring(instr)
        self.parser = parser(self.g)

    def parse(self, s, n=10):
        self.parser.parse(s, n)

    def generate(self, n=1):
        self.generator.generate(n)

    def generate(self, n=1):
        def expand(symbol):
            if isinstance(symbol, str):
                return symbol
            productions = self.g.productions(lhs=symbol)
            selected_production = random.choices(productions, weights=[p.prob() for p in productions])[0]
            return ''.join(expand(sym) for sym in selected_production.rhs())

        start_symbol = self.g.start()
        return [expand(start_symbol) for _ in range(n)]
    

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

class cfg_parser:
    p = None
    def __init__(self, g):
        self.p = BottomUpChartParser(g)

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

class ucfg_parser:
    p = None
    def __init__(self, g):
        self.p = FeatureChartParser(g)

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






