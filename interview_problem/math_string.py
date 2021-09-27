"""
take a string and operate on it like a math problem

"3+4/2" -> 5
"3*3+8/4" -> 11
"6+4*2/4-7+1" -> 0
"""


def math_string(string: str) -> int:
    ops = {
        "*": lambda x,y: x*y,
        "/": lambda x,y: int(x/y),
        "+": lambda x,y: x+y,
        "-": lambda x,y: x-y
        }

    for op in ops.keys():
        while op in string:
            ind = string.find(op)
            sub_str = string[ind-1:ind+2]
            res = ops[op](int(sub_str[0]),int(sub_str[2]))
            string = string[:ind-1] + str(res) + string[ind+2:]
    
    return int(string)


if __name__ == "__main__":
    print("solution should be 5, it is {}".format(math_string("3*3+8/4")))

    print("solution should be 11, it is {}".format(math_string("3+4/2")))

    # solution currently fails on negative numbers
    # print(math_string("6+4*2/4-7+9"))