def q1():
    """
    1. Escreva um programa que solicita um número ao usuário e determina se 
    é positivo, negativo ou zero. 
    """
    n = int(input("Digite um numero"))
    if n > 0:
        print("positivo")
    elif n < 0:
        print("negativo")
    else:
        print("zero")

def q2():
    """
    2. Verificação de Número Par/Ímpar: Crie um programa que pede ao usuário 
    um número e imprima se ele é par ou ímpar.
    """
    pass
    n = int(input('Digite um numero'))
    if (n % 2) == 0:
        print('par')
    else:
        print('ímpar')


def q3():
    """
    3. Calculadora Simples: Faça uma calculadora que pede ao usuário dois 
    números e uma operação (+, -, *, /) e imprima o resultado dessa operação.
    """
    pass
    op = str(input('Escolha uma operação'))
    a = float(input('Escolha um numero:'))
    b = float(input('Escolha outro numero:'))
    
def q4():
    """
    4. Maior de Três Números: Escreva um programa que solicita três números 
    ao usuário e imprima o maior dentre eles.
    """
    a = float(input('Escolha um numero:'))
    b = float(input('Escolha outro numero:'))
    c = float(input('Escolha outro numero:'))
    if a > b and a > c :
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)


def q5():
    """
    5. Classificação de Idade: Peça a idade do usuário e imprima a classificação
    em "Criança" (0-12), "Adolescente" (13-19), "Adulto" (20-59) ou "Idoso" (60+).
    """
    pass
    idade = int(input('idade'))
    if 0 <= idade <= 12 :
        print('Criança')
    elif 12 < idade < 19:
        print('Adolescente')
    elif 20 < idade < 59 :
        print('Adulto')
    elif 60 < idade :
        print('Idoso')
    
def q6():
    """
    6. Verificação de Triângulo: Peça ao usuário o comprimento de três 
    lados e verifique se eles podem formar um triângulo. Se sim, determine 
    se é um triângulo equilátero, isósceles ou escaleno.
    """
    pass

def q7():
    """
    7. Conversão de Notas: Escreva um programa que converte uma nota 
    de 0 a 100 em uma escala de conceitos: 
    A (90-100), B (80-89), C (70-79), D (60-69), E (50-59).e F (0-49)
    """
    pass
    nota = int(input('Digite sua idade'))
    if nota < 49 :
        print('F')
    if 59 > nota > 50:
        print('E')
    if 60 > nota > 69:
        print('D')
    if 70 > nota > 79:
        print('C')
    if 80 > nota > 89:
        print('B')
    if 90 > nota > 100:
        print('A')
def q8():
    """
    8. Validação de Login: Crie um programa que pede ao usuário um nome 
    de usuário e uma senha. Se o nome de usuário for "admin" e a senha for 
    "12345", exiba "Acesso concedido", caso contrário, exiba "Acesso negado".
    """
    pass

def q9():
    """
    9. Calculadora de IMC: Peça ao usuário sua altura e peso e calcule o
      índice de massa corporal (IMC). Em seguida, mostre uma mensagem 
      indicando se a pessoa está: Abaixo do peso, Peso normal, Sobrepeso, 
      Obesa ou Muito obesa.
    """
    pass

def q10():
    """
    10. Verificação de Ano Bissexto: Escreva um programa que verifica 
    se um ano fornecido pelo usuário é bissexto ou não.
    """
    pass