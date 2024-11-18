nota1 = float(input('digite a proimeira nota: '))
nota2 = float(input('digite a sengunda nota: '))

media = (nota1 + nota2)/2

if media >= 5 and media < 7:
    print('Voce esta em RECUPERAÇÃO')
elif media < 5:
    print('Voce esta REPROVADO')
else:
    print('Voce esta APROVADO')

