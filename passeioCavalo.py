def passeio_do_cavalo(n):
    h = [2, 1, -1, -2, -2, -1, 1, 2]
    v = [1, 2, 2, 1, -1, -2, -2, -1]
    t = [[0 for _ in range(n)] for _ in range(n)]

    def tenta(i, x, y):
        if i > n * n:
            return True
        for m in range(8):
            xn = x + h[m]
            yn = y + v[m]
            if 0 <= xn < n and 0 <= yn < n and t[xn][yn] == 0:
                t[xn][yn] = i
                if tenta(i + 1, xn, yn):
                    return True
                t[xn][yn] = 0
        return False

    t[0][0] = 1
    if tenta(2, 0, 0):
        for linha in t:
            print(linha)
    else:
        print("Não há solução.")

print("Teste com n = 5")
passeio_do_cavalo(5)
