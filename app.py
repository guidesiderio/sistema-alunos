alunos = [
    ("Alice", 18),
    ("Bob", 20),
    ("Charlie", 19),
    ("Dave", 22),
    ("Eve", 21),
    ("Frank", 20),
    ("Grace", 19),
    ("Hannah", 22),
    ("Isaac", 18),
    ("Julia", 21)
]



def procurar_aluno():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    aluno_procurado = input("Digite o nome do aluno que deseja encontrar: ")
    for nome, idade in alunos:
        if nome == aluno_procurado:
            print("Aluno específico encontrado:")
            print(f"Nome: {nome}, Idade: {idade}")
            return

    print("Aluno não encontrado na lista.")


def mostrar_menu():
    print("--- Sistema ---")
    print("1. Cadastrar aluno")
    print("2. Mostrar aluno(s)")
    print("3. Pesquisar aluno")
    print("4. Calcular a média das idades")
    print("5. Mostrar o(s) aluno(s) mais velho(s)")
    print("6. Calcular a mediana das idades")
    print("7. Mostrar aluno(s) ordenado(s) por nome")
    print("8. Calular a moda das idades")
    print('0. Sair\n')


def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    aluno = (nome, idade)
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")


def mostrar_alunos():
    print("\nAlunos cadastrados:")
    if alunos:
        for nome, idade in alunos:
            print(f"Nome: {nome}, idade: {idade}")
    else:
        print("Nenhum aluno cadastrado.")


def executar_programa(opcao):
    if opcao == 1:
        cadastrar_aluno()
    elif opcao == 2:
        mostrar_alunos()
    elif opcao == 3:
        procurar_aluno()
    elif opcao == 4:
        calcular_media()
    elif opcao == 5:
        calcular_mais_velho()
    elif opcao == 6:
        calcular_mediana()
    elif opcao == 7:
        ordenar_alunos()
    elif opcao == 8:
        calcular_moda_idades()    
    else:
        print("Opção Inválida!")


def main():

    while True:
        mostrar_menu()
        opcao = int(input("Digite uma opção: "))
        if opcao == 0:
            break
        executar_programa(opcao)
        print()

    print("Programa encerrado.\n")


def calcular_media():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    soma = sum(aluno[1] for aluno in alunos)
    n = len(alunos)
    media = soma / n
    print(f"A média das idades é {media:.2f}")


def calcular_mais_velho():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    idades = [idade for nome, idade in alunos]
    maior_idade = max(idades)
    alunos_mais_velhos = [(nome, idade)
                          for nome, idade in alunos if idade == maior_idade]

    print("Aluno(s) mais velho(s):")
    for nome, idade in alunos_mais_velhos:
        print(f"Nome: {nome}, idade: {idade}")


def calcular_mediana():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    idades_ordenadas = sorted(alunos, key=lambda aluno: aluno[1])
    tamanho = len(idades_ordenadas)
    indice_meio = tamanho // 2

    if tamanho % 2 == 0:
        mediana = (idades_ordenadas[indice_meio][1] +
                   idades_ordenadas[indice_meio - 1][1]) / 2
    else:
        mediana = idades_ordenadas[indice_meio][1]

    print(f"A mediana das idades é {mediana}")


def ordenar_alunos():
    alunos_ordenados_por_nome = sorted(alunos, key=lambda aluno: aluno[0])
    print("\nAlunos cadastrados:")
    if alunos_ordenados_por_nome:
        for nome, idade in alunos_ordenados_por_nome:
            print(f"Nome: {nome}, idade: {idade}")
    else:
        print("Nenhum aluno cadastrado.")


def calcular_moda_idades():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    idades = [idade for _, idade in alunos]
    contagem_idades = {}
    for idade in idades:
        if idade in contagem_idades:
            contagem_idades[idade] += 1
        else:
            contagem_idades[idade] = 1

    moda = []
    max_contagem = max(contagem_idades.values())
    for idade, contagem in contagem_idades.items():
        if contagem == max_contagem:
            moda.append(idade)

    if len(moda) == 1:
        print(f"A moda das idades é: {moda[0]}")
    else:
        print("Moda das idades:")
        for idade in moda:
            print(idade)


if __name__ == "__main__":
    main()
