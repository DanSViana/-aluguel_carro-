'''
Crie um programa de locação de veículo, que receba o cadastro de um usuário para que ele possa escolher entre 5 veículos previamente cadastrados no sistema, e no final o programa exibe os dados do cliente e do carro que ele decidiu alugar.
O algoritmo deve ser criado com base no conceito de Associação entre Classes visto na aula do dia 18/09/2024.
'''

class Veiculo:
    def __init__(self, modelo, placa, ano):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano

    def __str__(self):
        return f"Modelo: {self.modelo}, Placa: {self.placa}, Ano: {self.ano}"


class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.veiculo_alugado = None

    def alugar_veiculo(self, veiculo):
        self.veiculo_alugado = veiculo


def main():
    # Cadastro dos veículos
    veiculos = [
        Veiculo("Compass", "ABC-1234", 2024),
        Veiculo("Civic", "XYZ-5678", 2022),
        Veiculo("Argo", "DEF-9101", 2020),
        Veiculo("HB20", "GHI-1213", 2023),
        Veiculo("Corolla", "JKL-1415", 2021)
    ]

    # Cadastro do usuário
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    usuario = Usuario(nome, cpf)

    # Exibir veículos disponíveis
    print("\nVeículos disponíveis para locação:")
    for i, veiculo in enumerate(veiculos):
        print(f"{i + 1}. {veiculo}")

    # Escolha do veículo
    opcao = int(input("\nEscolha o número do veículo que deseja alugar: ")) - 1
    if 0 <= opcao < len(veiculos):
        usuario.alugar_veiculo(veiculos[opcao])
        print("\nVeículo alugado com sucesso!")
    else:
        print("Opção inválida!")

    # Exibir dados do usuário e veículo alugado
    if usuario.veiculo_alugado:
        print("\nDados do Cliente:")
        print(f"Nome: {usuario.nome}, CPF: {usuario.cpf}")
        print("Veículo alugado:")
        print(usuario.veiculo_alugado)
    else:
        print("Nenhum veículo foi alugado.")

if __name__ == "__main__":
    main()
