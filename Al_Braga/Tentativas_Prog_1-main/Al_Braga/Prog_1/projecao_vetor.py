#prod interno (u, v)
def prod_interno(u, v):
    accum = 0.0
    for i in range(len(v)):
        accum = accum + (u[i] * v[i])
    return accum

#prod interno (v)
def prod_interno_2(v):
    accum = 0.0
    for i in range(len(v)):
        accum = accum + (v[i] * v[i])
    return accum

def projecao_vec(u, v):
    escalar = prod_interno(u, v) / prod_interno_2(v)

    projecao = []
    for i in range(len(v)):
        #(prod_int(u,v)/prod_int(v) * 2
        novo_valor = escalar * v[i]

        projecao.append(novo_valor)
    return projecao
vetor_u = [1.0, 2.0, 3.0]
vetor_v = [1.0, 2.0, 3.0]
resultado = projecao_vec(vetor_u, vetor_v)
print(f'Resultado: {resultado}')