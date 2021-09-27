def average(array):
    # your code goes here
    distinct = list(set(array))
    avg = sum(distinct)/len(distinct)
    return round(avg, 3)
    
if __name__ == '__main__':
    arr = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]
    result = average(arr)
    print(result)