alt = float(input('digiite digite a sua altura: '))
peso = float(input('digite o seu peso: '))

cal = peso / (alt**2)

if cal < 18.5:
    print('seu imc e de {:.1f} você esta ABAIXO do peso'.format(cal))
elif 18.5 <= cal < 25:
    print('seu imc e de {:.1f} você esta PESO NORMAL do peso'.format(cal))
elif 25 <= cal < 29.9:
    print('seu imc e de {:.1f} você esta com SOBRE PESO do peso'.format(cal))
elif 30 <= cal < 34.9:
    print('seu imc e de {:.1f} você esta com OBESIDADE GRAU 1 do peso'.format(cal))
elif 35 <= cal < 39.9:
    print('seu imc e de {:.1f} você esta com OBESIDADE GRAU 2 do peso'.format(cal))
elif cal >= 40:
    print('seu imc e de {:.1f} você esta com OBESIDADE MORBIDA do peso'.format(cal))