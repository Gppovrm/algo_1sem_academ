def levenshtein(A, B):
    n, m = len(A), len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

    return dp[n][m]


if __name__ == "__main__":
    with open('input.txt', 'r') as input_file:
        A = input_file.readline().strip()
        B = input_file.readline().strip()

    distance = levenshtein(A, B)

    with open('output.txt', 'w') as output_file:
        output_file.write(f"{distance}")
