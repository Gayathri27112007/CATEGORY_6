# Alpha-Beta Pruning for Chess Game

## AI Course – II AIML/REC

### Category 6 – Adversarial Search for Game Playing AI Techniques

### Task 2

**Implement Alpha-Beta Pruning Algorithm for Chess Game**

---

## Aim

To implement the **Alpha-Beta Pruning algorithm** for a Chess Game using **Adversarial Search**.

---

## What is Adversarial Search?

Adversarial Search is used in games where two or more players compete against each other.

Examples:

* Chess
* Tic-Tac-Toe
* Checkers

In this program:

* **MAX player** represents our player.
* **MIN player** represents the opponent.

The MAX player tries to get the highest evaluation score, while the MIN player tries to get the lowest score.

---

# What is Alpha-Beta Pruning?

Alpha-Beta Pruning is an optimization of the **Min-Max Search algorithm**.

It avoids searching branches of the game tree that cannot affect the final decision.

This makes the search faster while producing the same result as Min-Max.

---

## Alpha and Beta

### Alpha (α)

Alpha represents the **best value found so far for the MAX player**.

Initial value:

```text
α = -∞
```

### Beta (β)

Beta represents the **best value found so far for the MIN player**.

Initial value:

```text
β = +∞
```

---

## Pruning Condition

The important condition is:

```text
if β <= α:
    prune the remaining branches
```

When this condition becomes true, the remaining branches do not need to be explored.

---

# Chess Game Tree

A simplified chess game tree is used in this program.

```text
                         MAX
                       /     \
                     MIN     MIN
                    /  \     /  \
                  MAX  MAX  MAX  MAX
                  / \  / \  / \  / \
                 3  5 6  9 1  2 0 -1
```

The numbers represent the evaluation scores of possible chess positions.

### Evaluation

* Positive value → advantage for MAX
* Negative value → advantage for MIN
* Higher value → better for MAX
* Lower value → better for MIN

---

# Working of the Algorithm

1. Start from the current chess position.
2. Generate possible moves.
3. MAX player tries to maximize the evaluation score.
4. MIN player tries to minimize the evaluation score.
5. Alpha keeps track of the best MAX value.
6. Beta keeps track of the best MIN value.
7. If `β <= α`, the remaining branch is pruned.
8. The best evaluation score is returned.
9. MAX selects the move with the best score.

---

# Example

Suppose the possible final positions have evaluation values:

```text
3, 5, 6, 9, 1, 2, 0, -1
```

The algorithm explores the game tree and removes branches that cannot improve the final decision.

The final value represents the best evaluation available to the MAX player.

---

# Advantages

* Reduces the number of nodes searched.
* Makes Min-Max search faster.
* Gives the same result as Min-Max.
* Useful for two-player games.
* Suitable for Chess and other adversarial games.

---

# Applications

Alpha-Beta Pruning can be used in:

* Chess
* Tic-Tac-Toe
* Checkers
* Connect Four
* Other two-player competitive games

---

# Technologies Used

* Python
* Adversarial Search
* Alpha-Beta Pruning
* Game Tree

---

# Conclusion

The Alpha-Beta Pruning algorithm was implemented for a simplified Chess Game.

It uses **MAX and MIN players** to represent two competing players and uses **Alpha and Beta values** to eliminate unnecessary branches.

Therefore, Alpha-Beta Pruning improves the efficiency of adversarial game search while maintaining the same optimal decision as Min-Max Search.
