def sockMerchant(n, ar):
    colors = {}
    ar.sort()
    for a in ar:
        if a in colors.keys():
            colors[a] += 1
        else:
            colors[a] = 1
    pairs = 0
    print(colors)
    for i in colors.keys():
        pairs += int(colors[i] / 2)
    return pairs


if __name__ == "__main__":
    n = 5
    ar = [1, 1, 2, 3, 2]
    result = sockMerchant(n, ar)
    print(result)
