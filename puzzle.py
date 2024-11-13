from logic import *  # Importa classes e funções de lógica proposicional do logic.py

# Definição de símbolos para representar cada personagem
AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
knowledge0 = And(
    Biconditional(AKnight, Not(AKnave)),
    Implication(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
knowledge1 = And(
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Or(AKnight, BKnight))
)

# Puzzle 2
knowledge2 = And(
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    Implication(AKnight, Biconditional(AKnight, BKnight)),
    Implication(AKnave, Not(Biconditional(AKnight, BKnight))),
    Implication(BKnight, Not(Biconditional(AKnight, BKnight))),
    Implication(BKnave, Biconditional(AKnight, BKnight))
)

knowledge3 = And(
    # A, B and C are knights or knaves but not both:
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))),
    # If B is a knight, A said 'I am a knave', and C is a knave:
    Implication(BKnight, CKnave),
    Implication(BKnight, And(
      # A then said 'I am a Knave', A may be a Knight or a Knave:
      Implication(AKnight, AKnave),
      Implication(AKnave, Not(AKnave)),
    )),
    # If B is a knave, A said 'I am a knight' C is not a knave:
    Implication(BKnave, Not(CKnave)),
    Implication(BKnave, And(
      # A then said 'I am a Knight', A may be a Knight or a Knave:
      Implication(AKnight, AKnight),
      Implication(AKnave, Not(AKnight))
    )),
    # If C is a knight, A is a knight:
    Implication(CKnight, AKnight),
    # If C is a knave, A is not a knight:
    Implication(CKnave, Not(AKnight))
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
