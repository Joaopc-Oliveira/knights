from logic import *


AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
#Puzzle 0 is the puzzle from the Background. It contains a single character, A.
#A says “I am both a knight and a knave.”
knowledge0 = And(
    Biconditional(AKnight, Not(AKnave)),
    Implication(AKnight, And(AKnight, AKnave))
)


# Puzzle 1 has two characters: A and B.
# A says “We are both knaves.”
# B says nothing.
knowledge1 = And(
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, BKnight)
)



# Puzzle 2 has two characters: A and B.
# A says “We are the same kind.”
# B says “We are of different kinds.”
knowledge2 =  And(
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    Implication(AKnight, BKnight),
    Implication(AKnave, Or(AKnight, BKnight)),
    Implication (BKnight, AKnave),
    Implication(BKnave, AKnave)

)
# Puzzle 3 has three characters: A, B, and C.
knowledge3 = And(
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(CKnight, Not(CKnave)),
# A says either “I am a knight.” or “I am a knave.”, but you don’t know which.
    Or(AKnight, AKnave),

# B says “A said ‘I am a knave.’”
    Implication(BKnave,AKnight),
    Implication(BKnight, AKnave),

# B then says “C is a knave.”
    Implication(BKnight, CKnave),
    Implication(BKnave, CKnight),

# C says “A is a knight.”
    Implication(CKnight, AKnight),
    Implication(CKnave, AKnight)
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
