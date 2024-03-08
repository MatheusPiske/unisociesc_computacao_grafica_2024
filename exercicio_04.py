import math

class PenduloSimples:
    def __init__(self, massa, comprimento, angulo_inicial):
        self.massa = massa  # em kg
        self.comprimento = comprimento  # em metros
        self.angulo = math.radians(angulo_inicial)  # convertendo o ângulo inicial para radianos
        self.aceleracao_gravitacional = 9.81  # m/s^2
    
    def calcular_posicao_angular(self, tempo):
        # Calcular o período do pêndulo
        periodo = 2 * math.pi * math.sqrt(self.comprimento / self.aceleracao_gravitacional)
        
        # Calcular a posição angular do pêndulo em relação ao tempo
        posicao_angular = self.angulo * math.cos((2 * math.pi / periodo) * tempo)
        
        return math.degrees(posicao_angular)  # Converter para graus antes de retornar

def teste_calculo_posicao_angular():
    # Teste para verificar se o cálculo da posição angular está correto
    pendulo = PenduloSimples(0.5, 1, 45)  # massa de 0.5 kg, comprimento de 1 metro, ângulo inicial de 45 graus
    assert round(pendulo.calcular_posicao_angular(0), 2) == 45.0  # no tempo inicial, deve ser igual ao ângulo inicial
    assert round(pendulo.calcular_posicao_angular(1), 2) == 27.95  # após 1 segundo, o ângulo deve diminuir
    
if __name__ == "__main__":
    # Entrada do usuário para as características do pêndulo
    massa = float(input("Digite a massa do objeto pendurado (kg): "))
    comprimento = float(input("Digite o comprimento da corda (metros): "))
    angulo_inicial = float(input("Digite o ângulo inicial do pêndulo (graus): "))
    
    # Criar um objeto PenduloSimples com os valores fornecidos
    pendulo = PenduloSimples(massa, comprimento, angulo_inicial)
    
    # Simular o movimento do pêndulo e imprimir a posição angular em diferentes momentos
    duracao_simulacao = int(input("Digite a duração da simulação (segundos): "))
    for tempo in range(duracao_simulacao + 1):
        posicao_angular = pendulo.calcular_posicao_angular(tempo)
        print(f"No tempo {tempo} segundos, a posição angular do pêndulo é {posicao_angular:.2f} graus.")
