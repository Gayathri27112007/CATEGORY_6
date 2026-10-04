# Alpha-Beta Pruning for Chess Game
# Adversarial Search Technique

def alpha_beta(depth, node, maximizing_player, alpha, beta):
    
    # Leaf node: return evaluation score
    if depth == 3:
        return node

    if maximizing_player:
        best = float('-inf')

        # MAX player tries to maximize the score
        for child in node:
            value = alpha_beta(
                depth + 1,
                child,
                False,
                alpha,
                beta
            )

            best = max(best, value)
            alpha = max(alpha, best)

            # Alpha-Beta pruning
            if beta <= alpha:
                print("Branch pruned at MAX node")
                break

        return best

    else:
        best = float('inf')

        # MIN player tries to minimize the score
        for child in node:
            value = alpha_beta(
                depth + 1,
                child,
                True,
                alpha,
                beta
            )

            best = min(best, value)
            beta = min(beta, best)

            # Alpha-Beta pruning
            if beta <= alpha:
                print("Branch pruned at MIN node")
                break

        return best


# Simplified chess game tree
#
# Each number represents the evaluation
# of a possible chess position.
#
# Positive value  -> advantage for MAX
# Negative value  -> advantage for MIN

game_tree = [
    [
        [3, 5],
        [6, 9]
    ],
    [
        [1, 2],
        [0, -1]
    ]
]


print("====================================")
print(" Alpha-Beta Pruning for Chess Game")
print(" Adversarial Search")
print("====================================")

alpha = float('-inf')
beta = float('inf')

best_score = alpha_beta(
    0,
    game_tree,
    True,
    alpha,
    beta
)

print("\nBest evaluation score:", best_score)
print("Best move is selected by MAX player.")