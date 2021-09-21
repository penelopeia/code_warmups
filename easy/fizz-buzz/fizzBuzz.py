"""
common problem:
Write a program that replaces the numbers in a given list of numbers with the following.
If the number is divisible by 3, replace with Fizz instead of the number.
If it's divisible by 5, replace with Buzz.
If it's divisible by both 3 and 5, replace with FizzBuzz.
"""

def fizz_buzz(nums):
    # result = []
    for i, n in enumerate(nums):
        val = n
        if n%3 == 0 and n%5 == 0:
            val = "FizzBuzz"
        elif n%3 == 0:
            val = "Fizz"
        elif n%5 == 0:
            val = "Buzz"
        nums[i] = val
    return nums

if __name__ == "__main__":
    sample = list(range(1, 16))
    result = fizz_buzz(sample)
    for r in result:
        print(r)
