import math
import matplotlib.pyplot as plt

# ==========================================
# 1. FUNÇÕES DO PROFESSOR (Com pequenas correções para rodar)
# ==========================================
def produto_interno(u, v):
    N = len(u)
    if len(v) != N: return None
    accum = 0.0
    for i in range(N): accum += u[i]*v[i]
    return accum

def matvecprod(A, u):
    Nl = len(A)
    Nc = len(A[0])
    if len(u) != Nc: return None
    
    v = []
    # Correção: O loop deve englobar a criação do novo vetor
    for i in range(Nl): 
        if len(A[i]) != Nc: 
            return None
        v.append(produto_interno(A[i], u))
    return v

# ==========================================
# 2. RESOLVENDO O EXERCÍCIO: CRIANDO AS MATRIZES
# ==========================================
def criar_matriz_rotacao_2d(angulo_graus):
    # O Python usa radianos, então convertemos os graus
    theta = math.radians(angulo_graus)
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    
    # Criamos a matriz de rotação 2x2 (lista de listas)
    R = [
        [cos_t, -sin_t],
        [sin_t,  cos_t]
    ]
    return R

def criar_matriz_rotacao_3d_z(angulo_graus):
    theta = math.radians(angulo_graus)
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    
    # Matriz 3x3 de rotação no eixo Z (uz=1, ux=0, uy=0)
    R = [
        [cos_t, -sin_t, 0.0],
        [sin_t,  cos_t, 0.0],
        [0.0,    0.0,   1.0]
    ]
    return R

# ==========================================
# 3. VISUALIZAÇÃO COM MATPLOTLIB (A parte divertida!)
# ==========================================
def desenhar_rotacao_2d():
    # Nosso vetor original: aponta para x=2, y=1
    vetor_original = [2.0, 1.0]
    
    # Vamos rotacionar em 90 graus
    angulo = 90
    matriz_R = criar_matriz_rotacao_2d(angulo)
    
    # Usamos a função do professor para multiplicar a matriz pelo vetor!
    vetor_rotacionado = matvecprod(matriz_R, vetor_original)
    
    # --- Configurando o desenho ---
    fig, ax = plt.subplots()
    
    # Desenha o vetor original (Azul)
    ax.quiver(0, 0, vetor_original[0], vetor_original[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Vetor Original')
    
    # Desenha o vetor rotacionado (Vermelho)
    ax.quiver(0, 0, vetor_rotacionado[0], vetor_rotacionado[1], angles='xy', scale_units='xy', scale=1, color='red', label=f'Rotacionado ({angulo} graus)')
    
    # Arrumando o visual do gráfico para ficar fácil de ver
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.grid(True)
    ax.axhline(y=0, color='k') # Linha do eixo X
    ax.axvline(x=0, color='k') # Linha do eixo Y
    plt.title("Rotação de Vetor em 2D")
    plt.legend()
    plt.show()

# Executa a nossa função visual
desenhar_rotacao_2d()
