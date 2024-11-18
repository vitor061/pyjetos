num1 = int(input('primeiro numero: '))
num2 = int(input('segundo numero: '))

if num1 > num2:
    print('o numero {} é maior que o '.format(num1, num2))
elif num1 < num2:
    print('o nunmero {} é maior que o numero {}'.format(num2, num1))
elif num1 == num2:
    print('nao existe numero maior os dois sao iguais')
