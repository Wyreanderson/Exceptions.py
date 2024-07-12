try:
    numero = int(input("Digite um número: "))
    resultado = 100 / numero
except ValueError:
    print("Erro: Digite um número inteiro válido.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
else:
    print("O resultado da divisão é:", resultado)