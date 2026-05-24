## Definir as funcoes 
def atacar(nome_atacante, pontos_ataque, nome_defensor, hp_defensor):
    """Funcao para realizar o ataque de um personagem a outro.

    Parametros:
    nome_atacante (str): O nome de quem ataca
    pontos_ataque (int): Os pontos de ataque
    nome_defensor (str): O nome de quem defende
    hp_defensor (int): O HP atual do defensor

    Retorna:
    int: O HP atualizado do defensor após o ataque (não pode ser negativo)
    """

    ## Calculamos o HP resultante subtraindo o ataque do HP atual
    novo_hp = hp_defensor - pontos_ataque
    ## Garantimos que o HP nao fique negativo
    if novo_hp < 0:
        novo_hp = 0
    print(f"{nome_atacante} ataca {nome_defensor} causando {pontos_ataque} de dano. {nome_defensor} agora tem {novo_hp} de vida.")
    return novo_hp


def exibir_placar(nome1, hp1, nome2, hp2):
    """Exibe o status atual dos personagens."""
    print(f"Status: {nome1}: {hp1} HP | {nome2}: {hp2} HP")


def main():
    # Inicio do Jogo
    print("Bem-vindo ao simulador de batalha!")
    # Entrada de dados (convertendo HP e Ataque para inteiros)
    nome_m1 = input("Digite o nome do primeiro personagem: ")
    hp_m1 = int(input(f"Digite o HP de {nome_m1}: "))
    atk_m1 = int(input(f"Digite os pontos de ataque de {nome_m1}: "))

    print("")  # Organizacao visual

    nome_m2 = input("Digite o nome do segundo personagem: ")
    hp_m2 = int(input(f"Digite o HP de {nome_m2}: "))
    atk_m2 = int(input(f"Digite os pontos de ataque de {nome_m2}: "))

    # 2. Validacao de dados
    if hp_m1 <= 0 or atk_m1 <= 0 or hp_m2 <= 0 or atk_m2 <= 0:
        print("Valores inválidos para os personagens. Por favor, insira valores positivos.")
    else:
        turno = 1
        print("\nIniciando a batalha\n")
        exibir_placar(nome_m1, hp_m1, nome_m2, hp_m2)

        # 3. Loop de jogo
        # O loop roda enquanto AMBOS personagens tiverem HP maior que 0
        while hp_m1 > 0 and hp_m2 > 0:
            print(f"\nTurno {turno}:")
            # Personagem 1 ataca o Personagem 2
            hp_m2 = atacar(nome_m1, atk_m1, nome_m2, hp_m2)
            exibir_placar(nome_m1, hp_m1, nome_m2, hp_m2)

            # Verificar se o Personagem 2 ainda está vivo para atacar
            if hp_m2 > 0:
                # Personagem 2 ataca o Personagem 1
                hp_m1 = atacar(nome_m2, atk_m2, nome_m1, hp_m1)
                exibir_placar(nome_m1, hp_m1, nome_m2, hp_m2)

            turno += 1

        # 4. Condição de vitória (verificar quem venceu)
        print("\nBatalha encerrada!")
        if hp_m1 > 0 and hp_m2 <= 0:
            print(f"O grande vencedor do duelo é {nome_m1}!")
        elif hp_m2 > 0 and hp_m1 <= 0:
            print(f"O grande vencedor do duelo é {nome_m2}!")
        else:
            print("Ambos os personagens caíram ao mesmo tempo! É um empate!")


if __name__ == "__main__":
    main()
