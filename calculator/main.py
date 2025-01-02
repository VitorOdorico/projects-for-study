print("==================================")
print("Calculator for Beginners")
print("==================================")
print("+ para adição")
print("- para subtração")
print("/ para divisão")
print("* para multiplicação")
print("==================================")

primeiroValor = input("Digite o primeiro valor: ")
operador = input("Qual será a operação? (+, -, /, *): ")
segundoValor = input("Digite o segundo valor: ")

def realizaCalculo(primeiroValor, operador, segundoValor):
    try:
        num1 = float(primeiroValor)
        num2 = float(segundoValor)

        match operador:
            case "+":
                return num1 + num2
            case "-":
                return num1 - num2
            case "/":
                if num2 == 0:
                    return "Erro: divisão por zero!"
                return num1 / num2
            case "*":
                return num1 * num2
            case _:
                return "Erro: operação inválida! Use +, -, / ou *."
    except ValueError:
        return "Erro: entrada inválida! Certifique-se de inserir números válidos."


resultado = realizaCalculo(primeiroValor, operador, segundoValor)
print("O valor da operação é: " + str(resultado))
