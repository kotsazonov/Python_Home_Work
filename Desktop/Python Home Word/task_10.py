#Задача 10: На столе лежат n монеток. Некоторые из
# них лежат вверх решкой, а некоторые – гербом. Определите
# минимальное число монеток, которые нужно перевернуть, чтобы все
# монетки были повернуты вверх одной и той же стороной. Выведите
# минимальное количество монет, которые нужно перевернуть

def min_coin_flips(coins):
    heads_count = 0
    tails_count = 0

    for coin in coins:
        if coin == 'H':
            heads_count += 1
        elif coin == 'T':
            tails_count += 1

    return min(heads_count, tails_count)

coins = ['H', 'T', 'T', 'H', 'H']
flips = min_coin_flips(coins)
print("Минимальное количество монет, которые нужно перевернуть:", flips)
