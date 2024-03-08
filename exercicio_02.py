import math

def calcular_trajetoria(velocidade, angulo, tempo):
    # Converter ângulo de graus para radianos
    angulo_radianos = math.radians(angulo)
    
    # Componentes da velocidade inicial
    velocidade_inicial_x = velocidade * math.cos(angulo_radianos)
    velocidade_inicial_y = velocidade * math.sin(angulo_radianos)
    
    # Calcular posição do projétil
    posicao_x = velocidade_inicial_x * tempo
    posicao_y = (velocidade_inicial_y * tempo) - (0.5 * 9.81 * tempo**2)  # Aceleração da gravidade
    
    return posicao_x, posicao_y

def teste_calculo_trajetoria():
    # Teste para verificar se a função calcular_trajetoria está correta
    velocidade = 20  # metros por segundo
    angulo = 45  # graus
    tempo = 2  # segundos
    posicao_x, posicao_y = calcular_trajetoria(velocidade, angulo, tempo)
    assert round(posicao_x, 2) == 20.0  # Arredondado para duas casas decimais
    assert round(posicao_y, 2) == 10.10  # Arredondado para duas casas decimais

if __name__ == "__main__":
    # Valores de entrada
    velocidade = float(input("Digite a velocidade inicial (m/s): "))
    angulo = float(input("Digite o ângulo de lançamento (graus): "))
    
    # Calcular trajetória para cada segundo até que o projétil atinja o solo (posição_y <= 0)
    tempo = 0
    while True:
        posicao_x, posicao_y = calcular_trajetoria(velocidade, angulo, tempo)
        if posicao_y <= 0:
            break
        print(f"No instante {tempo} segundos, a posição do projétil é ({posicao_x:.2f}, {posicao_y:.2f}) metros.")
        tempo += 1
    
    # Finalizar com a posição final do projétil
    print(f"O projétil atinge o solo na posição ({posicao_x:.2f}, 0.00) metros.")
