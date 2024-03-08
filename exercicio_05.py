import math

class MovimentoCircularUniforme:
    def __init__(self, raio, velocidade_angular):
        self.raio = raio  # raio da trajetória circular
        self.velocidade_angular = velocidade_angular  # velocidade angular em rad/s
    
    def calcular_velocidade_tangencial(self):
        # Velocidade tangencial é o produto do raio pela velocidade angular
        return self.raio * self.velocidade_angular
    
    def calcular_aceleracao_centripeta(self):
        # Aceleração centrípeta é o quadrado da velocidade angular multiplicado pelo raio
        return self.raio * self.velocidade_angular**2
    
def teste_calculo_velocidade_tangencial():
    # Teste para verificar se o cálculo da velocidade tangencial está correto
    movimento = MovimentoCircularUniforme(5, 2)  # raio de 5 metros, velocidade angular de 2 rad/s
    assert movimento.calcular_velocidade_tangencial() == 10  # velocidade tangencial deve ser 10 m/s

def teste_calculo_aceleracao_centripeta():
    # Teste para verificar se o cálculo da aceleração centrípeta está correto
    movimento = MovimentoCircularUniforme(3, 4)  # raio de 3 metros, velocidade angular de 4 rad/s
    assert movimento.calcular_aceleracao_centripeta() == 36  # aceleração centrípeta deve ser 36 m/s^2

if __name__ == "__main__":
    # Entrada do usuário para o raio e a velocidade angular
    raio = float(input("Digite o raio da trajetória circular (metros): "))
    velocidade_angular = float(input("Digite a velocidade angular (rad/s): "))
    
    # Criar um objeto MovimentoCircularUniforme com os valores fornecidos
    movimento = MovimentoCircularUniforme(raio, velocidade_angular)
    
    # Calcular e exibir a velocidade tangencial e a aceleração centrípeta
    velocidade_tangencial = movimento.calcular_velocidade_tangencial()
    aceleracao_centripeta = movimento.calcular_aceleracao_centripeta()
    
    print(f"A velocidade tangencial do objeto é {velocidade_tangencial} m/s.")
    print(f"A aceleração centrípeta do objeto é {aceleracao_centripeta} m/s².")
