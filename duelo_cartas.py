import random
from typing import List, Tuple #Importação para Tipagem

# Definindo o peso das cartas com um Dicionário para facilitar a comparação lógica

VALORES_CARTAS = {
    '2': 2, '3': 3, '4':4, '5':5, '6':6, '7':7, '8':8,
    '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A': 14
} 
def gerar_mao (quantidade: int) -> List[str]:
    """ Sorteia cartas aleatórias baseadas na quantidade definida pelo usuário."""
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
    print (f"🃏 Suas Cartas: {', '.join (mao_a)}")
    print (f"🤖 Cartas do Bot: {', '.join (mao_b)}")
    print ("-" * 40)
    print (f"📊 Placar: Você {pontos_a} x {pontos_b} Bot")

    if pontos_a > pontos_b:
        print ("🏆 Resultado: Você Venceu!")
    elif pontos_b > pontos_a:
        print ("💀 Resultado: O Bot Venceu!")
    else:
        print ("🤝 Resultado: Empate!")
    print ("-" * 40)

def main():
    """ Coordena o fluxo do simulador."""
    print ("        --- SIMULADOR DE DUELO V2 ---")

    #NOVIDADE V2: Loop com tratamento de Erros (Exception Handling)
    while True:
        try:
            quantidade= int(input("Quantas cartas quer sortear para o duelo? "))
            if quantidade <= 0:
                print("Por favor digite um número maior que 0.")
                continue
            break #Sai do loop se o número for válido
        except ValueError:
            #Captura o erro caso o usuário digite algo que não seja um número inteiro
            print("❌ Erro: Por vafor, digite apenas números inteiros!")

    # 1. Gera as mãos diretamente com os nomes das cartas
    mao_usuario = gerar_mao(quantidade)
    mao_bot = gerar_mao(quantidade)

    # 2. Calcula a pontuação baseada nos pesos do dicionário
    p_usu, p_bot = calcular_vencedor (mao_usuario, mao_bot)

    # 3. Exibe os resultados
    exibir_resultado(mao_usuario, mao_bot, p_usu, p_bot)

if __name__ == "__main__":
    main() 
