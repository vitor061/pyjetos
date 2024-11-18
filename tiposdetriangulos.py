l1 = float(input('primeiro seguimento: '))
l2 = float(input('segundo seguimento: '))
l3 = float(input('terceiro seguimento: '))

if l1<l2+l3 and l2< l1+l3 and l3<l1+l2:
    print('os seguimentos acima formam um triangulo',end='')
    if l1== l2 == l3:
        print("equilatero")
    elif l1 != l2 != l3 != l1:
        print('escaleno')
    else:
        print('isosceles')
else:
    print('nao podem formar um triangulo ')
    