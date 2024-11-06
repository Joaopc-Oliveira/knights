from cavaleiros import *  # Certifique-se de que cavaleiros.py contém todas as classes necessárias.

# Definição de símbolos para representar cada personagem
AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A diz "Eu sou ambos um cavaleiro e um patife."
knowledge0 = And(
    Biconditional(AKnight, Not(AKnave)),  # A é cavaleiro se, e somente se, não é patife
    Implication(AKnight, And(AKnight, AKnave))  # Se A é cavaleiro, ele diz a verdade, mas isso é uma contradição
)

# Puzzle 1
# A diz "Nós somos ambos patifes." B não diz nada.
knowledge1 = And(
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    Implication(AKnight, And(AKnave, BKnave))  # Se A é cavaleiro, ele diz a verdade que ambos são patifes
)

# Puzzle 2
# A diz "Nós somos do mesmo tipo." B diz "Nós somos de tipos diferentes."
knowledge2 = And(
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(AKnight, BKnight),  # A diz que ambos são do mesmo tipo
    Biconditional(BKnight, Not(AKnight))  # B diz que são de tipos diferentes
)

# Puzzle 3
# A diz "Eu sou cavaleiro" ou "Eu sou patife". 
# B diz "A disse que é patife" e "C é patife".
# C diz "A é cavaleiro".
knowledge3 = And(
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(CKnight, Not(CKnave)),
    
    Or(AKnight, AKnave),  # A diz que é cavaleiro ou patife
    Implication(BKnight, Not(AKnight)),  # B diz que A disse "sou patife"
    Implication(BKnight, CKnave),  # B diz que C é patife
    Implication(CKnight, AKnight)  # C diz que A é cavaleiro
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
