# calculadora.py - versao inicial (sem IA)
print("Calculadora")

num1 = float(input("Digite o primeiro numero: "))
op = input("Digite a operacao (+, -, *, /): ")
num2 = float(input("Digite o segundo numero: "))

if op == "+":
    resultado = num1 + num2
elif op == "-":
    resultado = num1 - num2
elif op == "*":
    resultado = num1 * num2
elif op == "/":
    resultado = num1 / num2
else:
    resultado = "Operacao invalida"

print("Resultado: " + str(resultado))
