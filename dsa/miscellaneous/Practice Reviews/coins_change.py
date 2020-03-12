import sys

def compute_coins_change(money, coin_denominations):
	num_min_coins = {}
	num_min_coins[0] = 0

	for m in range(1, money+1):
		num_min_coins[m] = sys.maxsize

		for coin in coin_denominations:
			if m >= coin:
				num_coins = 1 + num_min_coins[m - coin]

				if num_coins < num_min_coins[m]:
					num_min_coins[m] = num_coins

	return num_min_coins[money]


if __name__=='__main__':
	money = 40
	coins = [5, 10, 20, 25]

	money = 40
	coins = [5, 10, 15, 50]

	print(compute_coins_change(money, coins))