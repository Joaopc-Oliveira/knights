import itertools
from functools import lru_cache
import re


class Sentence:
    """Base for logical sentences with common methods."""

    @lru_cache(maxsize=None)
    def evaluate(self, model):
        """Evaluates the logical sentence in a given model."""
        raise NotImplementedError("Must implement evaluate in subclass")

    def formula(self):
        """Returns a string formula representing the logical sentence."""
        return ""

    def symbols(self):
        """Returns a set of all symbols in the logical sentence."""
        return set()

    @classmethod
    def validate(cls, sentence):
        if not isinstance(sentence, Sentence):
            raise TypeError("Must be a logical sentence")

    @classmethod
    def parenthesize(cls, s):
        """Adds parentheses to an expression only if necessary."""
        return s if re.match(r"^[a-zA-Z0-9_()]+$", s) else f"({s})"


class Symbol(Sentence):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Symbol) and self.name == other.name

    def __hash__(self):
        return hash(("symbol", self.name))

    def __repr__(self):
        return self.name

    def evaluate(self, model):
        return model.get(self.name, False)

    def formula(self):
        return self.name

    def symbols(self):
        return {self.name}


class Not(Sentence):
    def __init__(self, operand):
        Sentence.validate(operand)
        self.operand = operand

    def __eq__(self, other):
        return isinstance(other, Not) and self.operand == other.operand

    def __hash__(self):
        return hash(("not", hash(self.operand)))

    def __repr__(self):
        return f"Not({self.operand})"

    def evaluate(self, model):
        return not self.operand.evaluate(model)

    def formula(self):
        return "¬" + Sentence.parenthesize(self.operand.formula())

    def symbols(self):
        return self.operand.symbols()


class And(Sentence):
    def __init__(self, *conjuncts):
        for conjunct in conjuncts:
            Sentence.validate(conjunct)
        self.conjuncts = list(conjuncts)

    def __eq__(self, other):
        return isinstance(other, And) and self.conjuncts == other.conjuncts

    def __hash__(self):
        return hash(("and", tuple(hash(conjunct) for conjunct in self.conjuncts)))

    def __repr__(self):
        return f"And({', '.join(map(str, self.conjuncts))})"

    def evaluate(self, model):
        return all(conjunct.evaluate(model) for conjunct in self.conjuncts)

    def formula(self):
        return " ∧ ".join(Sentence.parenthesize(conjunct.formula()) for conjunct in self.conjuncts)

    def symbols(self):
        return set.union(*[conjunct.symbols() for conjunct in self.conjuncts])


class Or(Sentence):
    def __init__(self, *disjuncts):
        for disjunct in disjuncts:
            Sentence.validate(disjunct)
        self.disjuncts = list(disjuncts)

    def __eq__(self, other):
        return isinstance(other, Or) and self.disjuncts == other.disjuncts

    def __hash__(self):
        return hash(("or", tuple(hash(disjunct) for disjunct in self.disjuncts)))

    def __repr__(self):
        return f"Or({', '.join(map(str, self.disjuncts))})"

    def evaluate(self, model):
        return any(disjunct.evaluate(model) for disjunct in self.disjuncts)

    def formula(self):
        return " ∨ ".join(Sentence.parenthesize(disjunct.formula()) for disjunct in self.disjuncts)

    def symbols(self):
        return set.union(*[disjunct.symbols() for disjunct in self.disjuncts])


class Implication(Sentence):
    def __init__(self, antecedent, consequent):
        Sentence.validate(antecedent)
        Sentence.validate(consequent)
        self.antecedent = antecedent
        self.consequent = consequent

    def __eq__(self, other):
        return isinstance(other,
                          Implication) and self.antecedent == other.antecedent and self.consequent == other.consequent

    def __hash__(self):
        return hash(("implies", hash(self.antecedent), hash(self.consequent)))

    def __repr__(self):
        return f"Implication({self.antecedent}, {self.consequent})"

    def evaluate(self, model):
        return not self.antecedent.evaluate(model) or self.consequent.evaluate(model)

    def formula(self):
        antecedent = Sentence.parenthesize(self.antecedent.formula())
        consequent = Sentence.parenthesize(self.consequent.formula())
        return f"{antecedent} => {consequent}"

    def symbols(self):
        return self.antecedent.symbols() | self.consequent.symbols()


class Biconditional(Sentence):
    def __init__(self, left, right):
        Sentence.validate(left)
        Sentence.validate(right)
        self.left = left
        self.right = right

    def __eq__(self, other):
        return isinstance(other, Biconditional) and self.left == other.left and self.right == other.right

    def __hash__(self):
        return hash(("biconditional", hash(self.left), hash(self.right)))

    def __repr__(self):
        return f"Biconditional({self.left}, {self.right})"

    def evaluate(self, model):
        left_eval = self.left.evaluate(model)
        right_eval = self.right.evaluate(model)
        return left_eval == right_eval

    def formula(self):
        left = Sentence.parenthesize(self.left.formula())
        right = Sentence.parenthesize(self.right.formula())
        return f"{left} <=> {right}"

    def symbols(self):
        return self.left.symbols() | self.right.symbols()


def model_check(knowledge, query):
    """Returns True if the knowledge base entails the query."""

    def evaluate_models(symbols, model):
        """Recursively evaluate all possible models of symbols."""
        if not symbols:
            return not knowledge.evaluate(model) or query.evaluate(model)
        p, *remaining = symbols
        return (evaluate_models(remaining, {**model, p: True}) and
                evaluate_models(remaining, {**model, p: False}))

    # Get all unique symbols from knowledge and query
    symbols = list(knowledge.symbols() | query.symbols())
    return evaluate_models(symbols, {})
