import time


def calcular_materiais_fundacao(area_fundacao, proporcao_cimento=1, proporcao_areia=2, proporcao_brita=3):
    # Volume de cada material em metros cúbicos
    volume_cimento = (proporcao_cimento / (proporcao_cimento + proporcao_areia + proporcao_brita)) * area_fundacao
    volume_areia = (proporcao_areia / (proporcao_cimento + proporcao_areia + proporcao_brita)) * area_fundacao
    volume_brita = (proporcao_brita / (proporcao_cimento + proporcao_areia + proporcao_brita)) * area_fundacao

    return volume_cimento, volume_areia, volume_brita


def calcular_materiais_estrutura_madeira(area_estrutura, proporcao_madeira=0.2):
    # Volume de madeira em metros cúbicos
    volume_madeira = proporcao_madeira * area_estrutura

    return volume_madeira


def calcular_materiais_estrutura_alvenaria(area_estrutura, proporcao_tijolos=0.1, proporcao_cimento=0.05):
    # Volume de tijolos e cimento em metros cúbicos
    volume_tijolos = proporcao_tijolos * area_estrutura
    volume_cimento = proporcao_cimento * area_estrutura

    return volume_tijolos, volume_cimento


def calcular_quantidade_concreto(area_fundacao):
    # Adicionando 10% para desperdício
    quantidade_concreto = area_fundacao * 0.1

    return quantidade_concreto


def calcular_custo_materiais(volume_cimento, volume_areia, volume_brita, volume_madeira=0, volume_tijolos=0,
                             volume_ferro=0):
    # Preços médios dos materiais (exemplo)
    preco_cimento = 50  # preço por metro cúbico de cimento
    preco_areia = 30  # preço por metro cúbico de areia
    preco_brita = 40  # preço por metro cúbico de brita
    preco_madeira = 100  # preço por metro cúbico de madeira
    preco_tijolos = 80  # preço por metro cúbico de tijolos
    preco_ferro = 200  # preço por metro cúbico de ferro

    # Cálculo do custo total dos materiais
    custo_total = (volume_cimento * preco_cimento) + (volume_areia * preco_areia) + (volume_brita * preco_brita) + (
                volume_madeira * preco_madeira) + (volume_tijolos * preco_tijolos) + (volume_ferro * preco_ferro)

    return custo_total


def dicas_reciclagem(material):
    if material == "Cimento":
        print("\nO cimento pode ser reciclado em novos materiais de construção ou usado como enchimento em estradas.")
    elif material == "Areia":
        print("\nA areia pode ser reciclada e reutilizada em outras obras ou em paisagismo.")
    elif material == "Brita":
        print("\nA brita pode ser reciclada e reutilizada como agregado em novos concretos.")
    elif material == "Madeira":
        print(
            "\nA madeira pode ser reciclada em produtos de madeira reciclada ou usada como biomassa para produção de energia.")
    elif material == "Tijolos":
        print(
            "\nOs tijolos podem ser triturados e usados como agregado em novos materiais de construção ou em estradas.")
    elif material == "Ferro":
        print("\nO ferro pode ser reciclado e reutilizado na fabricação de novos produtos de metal.")


def imprimir_dicas_reciclagem():
    print("\n===== Dicas de Reciclagem =====")
    print("Escolha o material para ver as dicas de reciclagem:")
    print("1. Cimento")
    print("2. Areia")
    print("3. Brita")
    print("4. Madeira")
    print("5. Tijolos")
    print("6. Ferro")
    print("0. Voltar")


def main():
    while True:
        print("\n===== Calculador de Materiais para Obra =====")
        print("1. Calcular materiais para a fundação")
        print("2. Calcular materiais para a estrutura")
        print("3. Dicas de Reciclagem")
        print("4. Calcular custo dos materiais")
        print("0. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            time.sleep(0.5)
            try:
                area_fundacao = float(input("Digite a área da fundação (em metros quadrados): "))
                proporcao_cimento = float(input("Digite a proporção de cimento (1 parte): "))
                proporcao_areia = float(input("Digite a proporção de areia (em partes): "))
                proporcao_brita = float(input("Digite a proporção de brita (em partes): "))
                volume_cimento, volume_areia, volume_brita = calcular_materiais_fundacao(area_fundacao,
                                                                                         proporcao_cimento,
                                                                                         proporcao_areia,
                                                                                         proporcao_brita)
                quantidade_concreto = calcular_quantidade_concreto(area_fundacao)
                print("\nCalculando...")
                time.sleep(1)
                print("\nMateriais necessários para a fundação:")
                print(f" - Cimento: {volume_cimento:.2f} metros cúbicos")
                print(f" - Areia: {volume_areia:.2f} metros cúbicos")
                print(f" - Brita: {volume_brita:.2f} metros cúbicos")
                print(f"\nQuantidade total de concreto necessária: {quantidade_concreto:.2f} metros cúbicos")
            except ValueError:
                print("Por favor, insira valores válidos para área da fundação e proporções.")
        elif opcao == "2":
            time.sleep(0.5)
            print("\nEscolha o tipo de estrutura:")
            print("1. Estrutura de madeira")
            print("2. Estrutura de alvenaria")
            sub_opcao = input("Opção: ")
            try:
                area_estrutura = float(input("Digite a área da estrutura: "))
                if sub_opcao == "1":
                    proporcao_madeira = float(input("Digite a proporção de madeira: "))
                    volume_madeira = calcular_materiais_estrutura_madeira(area_estrutura, proporcao_madeira)
                    print("\nCalculando...")
                    time.sleep(1)
                    print("\nMateriais necessários para a estrutura de madeira:")
                    print(f" - Madeira: {volume_madeira:.2f} metros cúbicos")
                elif sub_opcao == "2":
                    proporcao_tijolos = float(input("Digite a proporção de tijolos: "))
                    proporcao_cimento = float(input("Digite a proporção de cimento: "))
                    volume_tijolos, volume_cimento = calcular_materiais_estrutura_alvenaria(area_estrutura,
                                                                                            proporcao_tijolos,
                                                                                            proporcao_cimento)
                    print("\nCalculando...")
                    time.sleep(1)
                    print("\nMateriais necessários para a estrutura de alvenaria:")
                    print(f" - Tijolos: {volume_tijolos:.2f} metros cúbicos")
                    print(f" - Cimento: {volume_cimento:.2f} metros cúbicos")
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
            except ValueError:
                print("Por favor, insira um valor válido para a área da estrutura.")
        elif opcao == "3":
            time.sleep(0.5)
            while True:
                imprimir_dicas_reciclagem()
                material = input("Opção: ")
                dicas_reciclagem(material)
                if material == "0":
                    break
        elif opcao == "4":
            time.sleep(0.5)
            try:
                custo_total = calcular_custo_materiais(volume_cimento, volume_areia, volume_brita, volume_madeira=0,
                                                       volume_tijolos=0, volume_ferro=0)
                print("\nCalculando...")
                time.sleep(1)
                print(f"\nCusto total estimado dos materiais: R${custo_total:.2f}")
            except UnboundLocalError:
                print("Por favor, primeiro calcule os materiais necessários.")
        elif opcao == "0":
            time.sleep(0.5)
            print("Obrigado por usar o calculador de materiais!!!!!!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
