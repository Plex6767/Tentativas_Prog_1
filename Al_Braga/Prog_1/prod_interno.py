def prod_interno(u, v):
    accum = 0.0
    for i in range(len(v)):
        accum = accum + u[i] * v[i]
    return accum
vetor_u = [1.0, 2.0, 5.0]
vetor_v = [7.0, 8.0, 9.0]
r = prod_interno(vetor_u, vetor_v)
print(f'O produto interno é: {r}')
