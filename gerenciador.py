print('{:=^40}'.format('PAGAMENTOS'))
num = float(input('qual foi o valor total da sua compra: '))
print('''Como gostaria de efetuar o pagamento?
        [1] Avista
        [2] Avista no cartão
        [3] Em até 2x no cartão
        [4] 3x ou mais no cartao''')
pag = int(input('Qual opção voce deseja?: '))

if pag == 1:
        total = num - (num * 10/100)
        print('o total da sua compra foi de {:.2f}'.format(total))
elif pag == 2:
        total = num - (num * 5/100)
        print('o total da sua compra foi de {:.2f}'.format(total))
elif pag == 3:
        total = num
        parcela = total / 2
        print('Sua compra no valor de {} vai ser parcelada em 2x de {}'.format(total, parcela))
elif pag == 4:
        total = num +(num * 20/100)
        totpar = int(input('quantas parcelas?'))
        parcela = total / totpar
        print('o valor da sua compra e de {:.2f} foi dividida em {:.2f} co o valor de parcela de {:.2f} '. format(total, totpar, parcela))
