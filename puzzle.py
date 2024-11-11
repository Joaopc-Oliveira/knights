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
    Biconditional(AKnight, Not(AKnave)),  # A é cavaleiro se, e somente se, não é patife
    Biconditional(BKnight, Not(BKnave)),  # B é cavaleiro se, e somente se, não é patife
    Biconditional(CKnight, Not(CKnave)),  # C é cavaleiro se, e somente se, não é patife

    Or(AKnight, AKnave),  # A diz "Eu sou cavaleiro ou patife" (sempre verdadeiro)

    # Se B é cavaleiro, ele diz a verdade sobre A ter dito "Eu sou patife"
    Implication(BKnight, AKnave),

    # Se B é cavaleiro, ele também diz a verdade sobre C ser patife
    Implication(BKnight, CKnave),

    # Se C é cavaleiro, ele diz a verdade sobre A ser cavaleiro
    Implication(CKnight, AKnight)
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
