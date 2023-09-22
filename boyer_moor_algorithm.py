from get_symbols import symbols


def pre_bm_bc(x):
    m = len(x)
    table = dict()
    for w in symbols():
        table[w] = m

    for i in range(0, m - 1):
        table[x[i]] = m - 1 - i

    return table


def is_prefix(x, p):
    j, m = 0, len(x)

    for i in range(p, m):
        if x[i] != x[j]:
            return False
        j += 1

    return True


def suffix_length(x, p):
    l, i, j = 0, p, len(x) - 1

    while (i >= 0) & (x[i] == x[j]):
        l, i, j = l + 1, i - 1, j - 1

    return l


def pre_bm_gs(x):
    m = len(x)
    table, last_prefix_position, i = [i * 0 for i in range(0, m)], m, m - 1

    while i > -1:
        if is_prefix(x, i + 1):
            last_prefix_position = i + 1

        table[m - 1 - i] = last_prefix_position - i + m - 1
        i -= 1

    for i in range(0, m - 1):
        slen = suffix_length(x, i)
        table[slen] = m - 1 - i + slen

    return table


def bm(y, x):
    m, n = len(x), len(y)
    answer = list()

    if m == 0:
        answer.append(-1)
        return answer

    bm_bc, bm_gs = pre_bm_bc(x), pre_bm_gs(x)

    i = m - 1
    while i <= n - 1:
        j = m - 1
        while x[j] == y[i]:

            if j == 0:
                answer.append(i)
                break
            i, j = i - 1, j - 1

        i += max(bm_gs[m - 1 - j], bm_bc[y[i]])

    if len(answer) == 0:
        answer.append(-1)

    return answer
