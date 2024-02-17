import time
import os


def addiction(a, b):
    return a+b


def subtraction(a, b):
    return a-b


def multi(a, b):
    return a*b


def division(a, b):
    if b == 0:
        return 'nao é possivel dividir por 0'
    else:
        return a/b

####### firulas ########


def time_sleep():
    time.sleep(2)


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def barrinha():
    print('.')
    time.sleep(0.5)
    clear()
    print('..')
    time.sleep(0.5)
    clear()
    print('...')
    time.sleep(0.5)
    clear()
    print('....')
    time.sleep(0.5)
    clear()
    print('.....')
    time.sleep(0.5)
    clear()
    print('.')
    time.sleep(0.5)
    clear()
    print('..')
    time.sleep(0.5)
    clear()
    print('...')
    time.sleep(0.5)
    clear()
    print('....')
    time.sleep(0.5)
    clear()
    print('.....')
    time.sleep(0.5)
    clear()


def loading():
    clear()
    barrinha()

####### firulas ########


def main():
    loading()
    print('selecione a operação:\n1. soma\n2. subtração\n3. multiplicação\n4. divisão')
    time.sleep(3)
    loading()

    escolha = input('digite 1, 2, 3 ou 4 para escolher a operação\n')

    loading()

    num1 = float(input("Digite o primeiro número: "))
    loading()
    num2 = float(input("Digite o segundo número: "))
    loading()

    if escolha == '1':
        print("Resultado:", addiction(num1, num2))
    elif escolha == '2':
        print("Resultado:", subtraction(num1, num2))
    elif escolha == '3':
        print("Resultado:", multi(num1, num2))
    elif escolha == '4':
        print("Resultado:", division(num1, num2))
    else:
        print("Opção inválida!")


main()
