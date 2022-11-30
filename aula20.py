primeiro_valor = int(input('Digite um valor: '))
segundo_valor = int(input('Digite outro valor: '))

if primeiro_valor > segundo_valor:
    print('O primeiro valor é maior, sendo: ',primeiro_valor)
elif primeiro_valor == segundo_valor:
    print('Os valores são iguais, sendo o primeiro ',primeiro_valor,' e o segundo ',segundo_valor,".")
else:
    print('O segundo valor é maior, sendo: ',segundo_valor)
