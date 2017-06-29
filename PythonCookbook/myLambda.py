



if __name__ == '__main__':
    a = map(lambda x: x * x, [y for y in range(10)])
    print(max(a))

    prices = {
        'ACME': 45.32,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    print(max(prices, key=lambda k: prices[k]))
    print(min(zip(prices.values(), prices.keys())))

    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }
    b = {
        'w': 10,
        'x': 11,
        'y': 4
    }

    print(a.keys() & b.keys())