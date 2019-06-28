def jumpingOnClouds(c):
    # Assume start on a safe cloud
    jumpable = []
    for i, cloud in enumerate(c):
        if cloud == 0:
            jumpable.append(i)

    print("jumpable: {}".format(jumpable))
    last_dis = 0
    min_jumps = []
    for i, pos in enumerate(jumpable):
        if i == len(jumpable)-1:
            min_jumps.append(pos)
            print(min_jumps)
            return len(min_jumps)-1

        dis = pos - jumpable[i + 1]
        print("dis: {}, last_dis: {}".format(dis, last_dis))
        if last_dis != dis:
            min_jumps.append(pos)
            last_dis = dis
        else:
            last_dis = 0


if __name__ == "__main__":
    # first and last cloud are always 0
    total_clouds1 = 7
    clouds1 = [0, 0, 1, 0, 0, 1, 0]
    # answer: 4

    total_clouds2 = 6
    clouds2 = [0, 0, 0, 0, 1, 0]
    # answer: 3

    total_clouds3 = 7
    clouds3 = [0, 0, 0, 0, 0, 1, 0]
    # answer: 3

    print(jumpingOnClouds(clouds3))
