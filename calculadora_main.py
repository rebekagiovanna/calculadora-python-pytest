
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida")
    return a / b

def ler_numero(mensagem):
    valor = input(mensagem)
    return float(valor)

def main():
    print("Calculadora básica")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    opcao = input("Escolha a operação: ")

    try:
        a = ler_numero("Digite o primeiro valor: ")
        b = ler_numero("Digite o segundo valor: ")

        if opcao == "1":
            resultado = soma(a, b)
        elif opcao == "2":
            resultado = subtracao(a, b)
        elif opcao == "3":
            resultado = multiplicacao(a, b)
        elif opcao == "4":
            resultado = divisao(a, b)
        else:
            print("Opção inválida")
            return

        print("Resultado:", resultado)

    except ValueError:
        print("Entrada inválida. Digite apenas números.")
    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida.")

if __name__ == "__main__":
    main()