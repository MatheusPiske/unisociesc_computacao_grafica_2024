import math

class FreeFallSimulator:
    def __init__(self, initial_height):
        self.initial_height = initial_height
        self.gravity = 9.81  # Aceleração devida à gravidade em m/s^2

    def calculate_position(self, time):
        # A equação para calcular a posição em queda livre é: s = s0 + v0*t + (1/2)*a*t^2
        return self.initial_height - 0.5 * self.gravity * time**2

    def calculate_velocity(self, time):
        # A equação para calcular a velocidade em queda livre é: v = v0 + a*t
        return -self.gravity * time

def run_simulation(initial_height, time_interval, total_time):
    simulator = FreeFallSimulator(initial_height)

    current_time = 0
    while current_time <= total_time:
        position = simulator.calculate_position(current_time)
        velocity = simulator.calculate_velocity(current_time)
        print(f"At time {current_time} s, position: {position:.2f} m, velocity: {velocity:.2f} m/s")
        current_time += time_interval

def test_position_calculation():
    simulator = FreeFallSimulator(10)  # Altura inicial de 10 metros
    assert simulator.calculate_position(0) == 10  # Verifica a posição inicial
    assert math.isclose(simulator.calculate_position(2), 0, rel_tol=1e-9)  # Verifica a posição após 2 segundos

def test_velocity_calculation():
    simulator = FreeFallSimulator(10)  # Altura inicial de 10 metros
    assert simulator.calculate_velocity(0) == 0  # Verifica a velocidade inicial
    assert simulator.calculate_velocity(2) == -19.62  # Verifica a velocidade após 2 segundos

if __name__ == "__main__":
    run_simulation(initial_height=100, time_interval=1, total_time=10)
    test_position_calculation()
    test_velocity_calculation()
    print("All tests passed successfully!")
