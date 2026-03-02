import random
from typing import List, Tuple #Importação para Tipagem

# Definindo o peso das cartas com um Dicionário
# Isso facilita mudar as regras do jogo sem mexer na lógica

VALORES_CARTAS = {
    '2': 2, '3': 3, '4':4, '5':5, '6':6, '7':7, '8':8,
    '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A': 14
} 
def gerar_mao (quantidade: int =10) -> List[str]:
    """ Sorteia cartas aleatórias baseadas nas chaves do dicionário."""
    cartas_disponiveis = list(VALORES_CARTAS.keys())
    return [random.choice(cartas_disponiveis) for _ in range (quantidade)]

def calcular_vencedor (mao_a: List[str], mao_b: List[str]) -> Tuple[int, int]:
    """ Compara os valores das cartas usando o dicionário VALORES_CARTAS."""
    pontos_a = 0
    pontos_b = 0
    #zip() percorre as duas mãos simultaneamente
    for carta_a, carta_b in zip(mao_a, mao_b):
        if VALORES_CARTAS[carta_a] > VALORES_CARTAS[carta_b]:
            pontos_a += 1
        elif VALORES_CARTAS[carta_b] > VALORES_CARTAS[carta_a]:
            pontos_b += 1
    return pontos_a, pontos_b

def exibir_resultado (mao_a: List[str], mao_b: List[str], pontos_a: int, pontos_b: int):
    """ Aresenta as mãos e o veredito final no console."""
    print ("-" * 40)
    print (f"🃏 Cartas Jogador A: {', '.join (mao_a)}")
    print (f"🃏 Cartas Jogador B: {', '.join (mao_b)}")
    print ("-" * 40)
    print (f"📊 Placar: Jogador A {pontos_a} x {pontos_b} Jogador B")

    if pontos_a > pontos_b:
        print ("🏆 Resultado: Vencedor Jogador A!")
    elif pontos_b > pontos_a:
        print ("🏆 Resultado: Vencedor Jogador B")
    else:
        print ("🤝 Resultado: Empate!")
    print ("-" * 40)

def main():
    """ Coordena o fluxo do simulador."""
# 1. Gera as mãos diretamente com os nomes das cartas
    mao_a = gerar_mao()
    mao_b = gerar_mao()

# 2. Calcula a pontuação baseada nos pesos do dicionário
    p_a, p_b = calcular_vencedor (mao_a, mao_b)

# 3. Exibe os resultados
    exibir_resultado(mao_a, mao_b, p_a, p_b)

if __name__ == "__main__":
    main() 