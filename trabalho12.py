n1 = int(input("qual a altura da parede?"))
n2 = int(input("qual a largura da parede?"))
re = n1 * n2 / 2
print("seria nessessario {} litros de tinta para pintar essa parede".format(re))
n3 = float(input("qual o valor da tinta no balde de 10L?"))
n4 = n3-(n3*5/100)
print("o valor do balde de tinta é {} mas com o desconto de cliente fidelidade" \
 " de 5% fica por apenas {}".format(n3,n4))
sa = int(input('quanto você vai ganhar nesse trabalho fora os gastos' \
'e a porcentagem de salubridade de 3%?'))
print('seu pagamento no total, adicionando 3% de salubridade é' \
'retirando os {} reais gastos na tinta é de {}'.format(n4,sa+(sa*3/100)-n4))