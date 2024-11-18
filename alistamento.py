from datetime import date
atual = date.today().year
nascimento = int(input('digite o ano do seu nascimento: '))
alist = atual - nascimento
if alist == 18:
    print('voce tem {} anos precisa fazer o processo militar'.format(alist))
elif alist > 18:
    saldo = 18 + atual
    print('seu prazo de alistamento execedeu, procure o a junta militar')
else:
    print('voce ainda nao tem a idade necessaria para o alistamento obrigatorio')

