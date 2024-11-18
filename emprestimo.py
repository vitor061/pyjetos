casa = float(input('quaol o valor da casa R$: '))
salario = float(input('qual o seu salario atual? '))
tempo = int(input('em quantos anos voce quer fazer o pagamento? '))
minimo = salario * 30/100


presta = casa/(tempo*12)
print('para pagar uma casa do R${:.2f} em {} anos'.format(casa,tempo))
print('A prestação será de R${:.2f}'.format(presta))
print('O valor minimo é de {}'.format(minimo))

if presta <= minimo:
    print('seu pedidp de imprestimo foi concedido')
else:
    print('seu pedido de emprestimo foi negado')
