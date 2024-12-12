def is_pattern(S, P):
    n, m = len(S), len(P)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    dp[0][0] = True
    for j in range(1, m + 1):
        if P[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if P[j - 1] == '?' or P[j - 1] == S[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif P[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return dp[n][m]

if __name__ == "__main__":
    with open('input.txt', 'r') as input_file:
        P = input_file.readline().strip()
        S = input_file.readline().strip()

    pattern = is_pattern(S, P)

    with open('output.txt', 'w') as output_file:
        if pattern:
            output_file.write("YES")
        else:
            output_file.write("NO")
