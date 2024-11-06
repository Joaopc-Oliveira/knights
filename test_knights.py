import unittest
from cavaleiros import Symbol, And, Or, Not, Implication, Biconditional, model_check

class TestLogicalSentences(unittest.TestCase):

    def test_symbol(self):
        model = {"A": True}
        A = Symbol("A")
        self.assertTrue(A.evaluate(model))
        self.assertEqual(A.formula(), "A")

    def test_not(self):
        model = {"A": False}
        A = Symbol("A")
        not_A = Not(A)
        self.assertTrue(not_A.evaluate(model))
        self.assertEqual(not_A.formula(), "¬A")

    def test_and(self):
        A = Symbol("A")
        B = Symbol("B")
        model = {"A": True, "B": True}
        and_expr = And(A, B)
        self.assertTrue(and_expr.evaluate(model))
        self.assertEqual(and_expr.formula(), "(A) ∧ (B)")

    def test_model_check(self):
        A = Symbol("A")
        knowledge = And(A)  # Exemplo onde sabemos que A é verdadeiro
        query = A
        self.assertTrue(model_check(knowledge, query))


if __name__ == "__main__":
    unittest.main()
