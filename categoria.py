from datetime import date
ano = int(input('digite o seu ano de anscimento: '))
atual = date.today().year

idade = atual - ano

if idade <=9:
    print('Voce tem {} anos por isso esta na categoria MIRiM'.format(idade))
elif idade <=14:
    print('Voce tem  {} anos e esta na categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('Voce tem  {} anos e esta na categoria JUNIOR' .format(idade))
elif idade <=25:
    print('Voce tem  {} anos e esta na categoria SENIOR'.format(idade))
else:
    print('Voce tem  {} anos e esta na categoria MASTER'.format(idade))


