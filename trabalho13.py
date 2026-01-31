dias = int(input("Quantos dias o carro foi alugado?"))
km = int(input('quantos km foram rodados?'))
total = dias*60+km*0.15
print('somando {} dias e {} o total a pagar é {:.0f}'.format(dias,km,total))