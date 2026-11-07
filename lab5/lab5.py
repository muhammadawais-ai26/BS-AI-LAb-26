# Lab 5: Minimax and Alpha-Beta Pruning

def minimax(depth, index, is_max, scores, target_depth, counter):

    if depth == target_depth:
        counter[0] += 1
        return scores[index]

    if is_max:
        left = minimax(depth + 1, index * 2, False,
                       scores, target_depth, counter)

        right = minimax(depth + 1, index * 2 + 1, False,
                        scores, target_depth, counter)

        return max(left, right)

    else:
        left = minimax(depth + 1, index * 2, True,
                       scores, target_depth, counter)

        right = minimax(depth + 1, index * 2 + 1, True,
                        scores, target_depth, counter)

        return min(left, right)


def alpha_beta(depth, index, is_max, scores, target_depth,
               alpha, beta, counter):

    if depth == target_depth:
        counter[0] += 1
        return scores[index]

    if is_max:

        value = float("-inf")

        for child in range(2):

            value = max(
                value,
                alpha_beta(depth + 1, index * 2 + child,
                           False, scores, target_depth,
                           alpha, beta, counter)
            )

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:

        value = float("inf")

        for child in range(2):

            value = min(
                value,
                alpha_beta(depth + 1, index * 2 + child,
                           True, scores, target_depth,
                           alpha, beta, counter)
            )

            beta = min(beta, value)

            if alpha >= beta:
                break

        return value


def run_test(title, scores):

    depth = 3

    minimax_counter = [0]
    pruning_counter = [0]

    minimax_value = minimax(
        0, 0, True, scores, depth, minimax_counter
    )

    pruning_value = alpha_beta(
        0, 0, True, scores, depth,
        float("-inf"), float("inf"), pruning_counter
    )

    print("\n" + title)
    print("Leaf scores:", scores)

    print("Minimax value:", minimax_value)
    print("Minimax evaluated leaves:", minimax_counter[0])

    print("Alpha-Beta value:", pruning_value)
    print("Alpha-Beta evaluated leaves:", pruning_counter[0])

    print("Both algorithms agree:", minimax_value == pruning_value)

if __name__ == "__main__":

    original_order = [3, 5, 2, 9, 8, 7, 6, 4]

    reordered = [8, 7, 6, 4, 3, 5, 2, 9]

    run_test("TEST 1: Original branch order", original_order)

    run_test("TEST 2: Reordered branches", reordered)