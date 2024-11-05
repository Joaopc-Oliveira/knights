from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Rules that apply to all puzzles
# Each character can only be a Knight or a Knave, but not both
characters = And(
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave), Not(And(CKnight, CKnave))
)

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    characters,
    Implication(AKnight, And(AKnight, AKnave))  # If A is a knight, then A must be both knight and knave, which is a contradiction
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    characters,
    Implication(AKnight, And(AKnave, BKnave))  # If A is a knight, then both A and B must be knaves
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    characters,
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),  # If A is a knight, A and B are the same kind
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight)))    # If B is a knight, A and B are of different kinds
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    characters,
    Or(Implication(AKnight, AKnight), Implication(AKnight, AKnave)),  # A says either "I am a knight" or "I am a knave"
    Implication(BKnight, AKnave),  # B says "A said 'I am a knave'"
    Implication(BKnight, CKnave),  # B says "C is a knave"
    Implication(CKnight, AKnight)  # C says "A is a knight"
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
