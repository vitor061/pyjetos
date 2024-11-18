num = int(input('digite um número inteiro: '))
print('''escolha uma das bases para conversão:'
      [1] CONVERTER PARA BINARIO
      [2] CONVERTER PARA OCTAL
      [3] CONVERTER PARA HEXADECIMAL''')

opcao = int(input('Sua escolha: '))
if opcao == 1:
    print('{} convertido para binario e {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal e de {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} valor convertido para hexadecimal e {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida , tente novamente')