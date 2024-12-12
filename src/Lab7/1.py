def min_coins(money, coins):
    dp = [float('inf')] * (money + 1)
    dp[0] = 0

    for i in range(1, money + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[money]


if __name__ == "__main__":
    with open('input.txt', 'r') as input_file:
        money, k = map(int, input_file.readline().split())
        coins = list(map(int, input_file.readline().split()))

    result = min_coins(money, coins)

    with open('output.txt', 'w') as output_file:
        output_file.write(f"{result}")
