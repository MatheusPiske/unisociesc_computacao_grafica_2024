class Particula:
    def __init__(self, massa, velocidade_x, velocidade_y):
        self.massa = massa
        self.velocidade_x = velocidade_x
        self.velocidade_y = velocidade_y
    
    def calcular_velocidade_final(self, outra_particula):
        # Fórmula para calcular a velocidade final de uma partícula após a colisão elástica
        nova_velocidade_x = ((self.massa - outra_particula.massa) * self.velocidade_x + 
                             (2 * outra_particula.massa * outra_particula.velocidade_x)) / (self.massa + outra_particula.massa)
        nova_velocidade_y = ((self.massa - outra_particula.massa) * self.velocidade_y + 
                             (2 * outra_particula.massa * outra_particula.velocidade_y)) / (self.massa + outra_particula.massa)
        return nova_velocidade_x, nova_velocidade_y

def teste_calculo_velocidade_final():
    # Teste para verificar se o cálculo da velocidade final está correto
    particula1 = Particula(1, 3, 1)
    particula2 = Particula(2, -1, 2)
    nova_velocidade_x, nova_velocidade_y = particula1.calcular_velocidade_final(particula2)
    assert nova_velocidade_x == 1.0
    assert nova_velocidade_y == 1.0

if __name__ == "__main__":
    # Entrada do usuário para as massas e velocidades iniciais das partículas
    massa1 = float(input("Digite a massa da primeira partícula (kg): "))
    velocidade_x1 = float(input("Digite a velocidade inicial da primeira partícula no eixo x (m/s): "))
    velocidade_y1 = float(input("Digite a velocidade inicial da primeira partícula no eixo y (m/s): "))
    
    massa2 = float(input("Digite a massa da segunda partícula (kg): "))
    velocidade_x2 = float(input("Digite a velocidade inicial da segunda partícula no eixo x (m/s): "))
    velocidade_y2 = float(input("Digite a velocidade inicial da segunda partícula no eixo y (m/s): "))
    
    # Criar objetos Particula com os valores fornecidos
    particula1 = Particula(massa1, velocidade_x1, velocidade_y1)
    particula2 = Particula(massa2, velocidade_x2, velocidade_y2)
    
    # Calcular as novas velocidades após a colisão
    nova_velocidade_x1, nova_velocidade_y1 = particula1.calcular_velocidade_final(particula2)
    nova_velocidade_x2, nova_velocidade_y2 = particula2.calcular_velocidade_final(particula1)
    
    # Exibir as velocidades finais
    print("Velocidades finais da primeira partícula:")
    print(f"No eixo x: {nova_velocidade_x1} m/s")
    print(f"No eixo y: {nova_velocidade_y1} m/s")
    print("\nVelocidades finais da segunda partícula:")
    print(f"No eixo x: {nova_velocidade_x2} m/s")
    print(f"No eixo y: {nova_velocidade_y2} m/s")
