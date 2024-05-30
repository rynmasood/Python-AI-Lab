MAX_VALUE, MIN_VALUE = 1000, -1000

def minimax(depth, node_index, is_maximizing, values, alpha, beta):
    if depth == 3:
        return values[node_index]

    if is_maximizing:
        best_value = MIN_VALUE

        for i in range(0, 2):
            value = minimax(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)

            if beta <= alpha:
                break

        return best_value

    else:
        best_value = MAX_VALUE

        for i in range(0, 2):
            value = minimax(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best_value = min(best_value, value)
            beta = min(beta, best_value)

            if beta <= alpha:
                break

        return best_value


if __name__ == "__main__":
    values=[3,5,2,9,12,5,23,24]
    print("The optimal value is:", minimax(0, 0, True, values, MIN_VALUE, MAX_VALUE))
