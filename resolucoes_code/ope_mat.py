# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicita o primeiro número ao usuário
numero1 = float(input("Digite o primeiro número: "))

# Solicita o segundo número ao usuário
numero2 = float(input("Digite o segundo número: "))

# Exibe as opções de operação
print("Escolha uma operação:")
print("1. Adição (+)")
print("2. Subtração (-)")
print("3. Multiplicação (*)")
print("4. Divisão (/)")

# Solicita a escolha da operação
operacao = input("Digite o número da operação desejada (1/2/3/4): ")

# Realiza a operação escolhida
if operacao == '1':
    resultado = numero1 + numero2
    print(f"O resultado da adição é: {resultado}")
elif operacao == '2':
    resultado = numero1 - numero2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == '3':
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == '4':
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Não é possível dividir por zero.")
else:
    print("Operação inválida. Por favor, escolha uma operação válida.")