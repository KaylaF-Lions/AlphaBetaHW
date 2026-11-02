def alpha_beta(depth, index, is_max, alpha, beta, values):
    if depth == 3:
        return values[index]

    if is_max:
        best = float('-inf')

        for i in range(2):
            val = alpha_beta(depth + 1, index * 2 + i, False, alpha, beta, values)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                print(f"Pruning remaining branches at Depth {depth}, Node Index {index}")
                break
        return best

    else:
        best = float('inf')

        for i in range(2):
            val = alpha_beta(depth + 1, index * 2 + i, True, alpha, beta, values)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                print(f"Pruning remaining branches at Depth {depth}, Node Index {index}")
                break
        return best


leaf_values = [3, 5, 17, 8, -2, 5, -1, 7]

print("Starting Alpha-Beta Pruning Search...\n")

optimal_value = alpha_beta(0, 0, True, float('-inf'), float('inf'), leaf_values)

print(f"\nThe optimal value determined by the algorithm is: {optimal_value}")