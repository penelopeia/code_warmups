def wrap_og(string, max_width):
    """
    O(n)
    """
    result = ""
    for i, n in enumerate(string):
        if i%max_width or i == 0:
            result += n
        else:
            result += "\n"
            result += n
    return result

# refactor
def wrap(string, max_width):
    """
    O(n/max_width)
    """
    result = ""
    end = 0
    for n in range(len(string)//max_width):
        if n != 0:
            result += "\n"
        end_char = (n*max_width)+max_width
        result += string[n*max_width:end_char]
        end = end_char
    if end < len(string):
        result = result + "\n" + string[end:]
    return result

if __name__ == '__main__':
    result = wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4)
    answer = "ABCD\nEFGH\nIJKL\nIMNO\nQRST\nUVWX\nYZ"
    if result == answer:
        print("GOOD")
        print("===============")
    print(result)