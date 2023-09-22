def b_force(string, sample):
    n, m = len(string), len(sample)

    for i in range(0, n - m + 1):
        it_needs = True
        p = -1
        for j in range(i, i + m):
            p += 1
            if string[j] != sample[p]:
                it_needs = False
                break

        if it_needs:
            return i, i + m - 1

    return 0, 0
