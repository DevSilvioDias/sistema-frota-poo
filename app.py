class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self._ligado = False

    def alternar_ignicao(self):
        self._ligado = not self._ligado

    def __str__(self):
        status = "Ligado" if self._ligado else "Desligado"
        return f"[{self.ano}] {self.marca} {self.modelo} | Status: {status}"


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas

    def __str__(self):
        return f"{super().__str__()} | Portas: {self.portas}"


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def __str__(self):
        return f"{super().__str__()} | Cilindradas: {self.cilindradas}cc"


def main():
    frota = [
        Carro("Hyundai", "HB20", 2022, 4),
        Carro("Toyota", "Corolla", 2024, 4),
        Moto("Honda", "CB 500", 2023, 500),
    ]

    # Ligando apenas o primeiro veículo para testar
    frota[0].alternar_ignicao()

    print("=== CONTROLE DE FROTA ===")
    for veiculo in frota:
        print(veiculo)


if __name__ == "__main__":
    main()