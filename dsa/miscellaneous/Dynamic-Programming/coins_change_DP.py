import sys


def tender_coins_DP(money, coin_denoms):
	num_min_coins = {}
	num_min_coins[0] = 0

	for m in range(1, money+1):
		num_min_coins[m] = sys.maxsize

		for coin in coin_denoms:
			if m >= coin:
				num_coins = num_min_coins[m - coin] + 1

				if num_coins < num_min_coins[m]:
					num_min_coins[m] = num_coins

	return num_min_coins[money]


if __name__=='__main__':
	coin_denoms = [1,5,6]
	money = 9

	# coin_denoms = [5, 10, 20, 25]
	# money = 40

	num_min_coins = tender_coins_DP(money, coin_denoms)
	print(num_min_coins)