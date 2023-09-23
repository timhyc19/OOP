def coin_change(amount: int, coins: list):
    """
    :amount: amount submitted
    :coins: list of coins accepted
    :return: boolean if amount can be made using vals in coins
    """
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i == coin:
                dp[i] = 1
                break
            if i > coin:
                dp[i] = min(dp[i], 1 + dp[i - coin])
                
    return True if dp[amount] != (amount + 1) else False

