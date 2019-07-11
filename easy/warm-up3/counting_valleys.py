"""
tracking # of steps,
they are either U or D
start and end at sea level
delta unit change of 1

example: s = [DDUUUUDD]

input = n: # of steps taken
s: string describing the path

Valley is anything below sea level before
going back up?
"""

# modify to only check when we come back up to sea level
# this problem is just poorly written and hard to understand
# what a valley actually is.
def countingValleys(n, s):
    curr_alt = 0  # Sea Level
    valleys = 0
    for step in s:
        if step == 'U':
            curr_alt += 1
            if curr_alt == 0:
                valleys += 1
        elif step == 'D':
            curr_alt -= 1
    return valleys


def FAILURE_countingValleys(n, s):
    curr_alt = 0  # Sea Level
    max_high = 0
    travel_down = False
    travel_up = False
    valleys = 0
    for step in s:
        # maybe try to count depth? Or just monitor altitude change?
        if step == 'U':
            if travel_down:
                travel_up = True
            curr_alt += 1
        elif step == 'D':
            travel_down = True
            curr_alt -= 1
        # Does one step down equal a valley?
        if curr_alt >= max_high:
            max_high = curr_alt
            if travel_down and travel_up:
                travel_up = False
                travel_down = False
                valleys += 1
    if travel_down and travel_up:
        valleys += 1
    return valleys


if __name__ == "__main__":
    n0 = 8
    s0 = ['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U']
    # Solution: 1

    n1 = 8
    s1 = ['D', 'D', 'U', 'U', 'U', 'U', 'D', 'D']
    # Solution: 1

    n2 = 12
    s2 = ['D', 'D', 'U', 'U', 'U', 'D', 'D', 'D', 'D', 'U', 'U', 'U']
    # Solution: 2

    sol = countingValleys(n2, s2)
    print("Num of valleys: {}".format(sol))
