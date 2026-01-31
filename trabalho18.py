import math
co = float(input('comprimento do cateto oposto:'))
ca = float(input("comprimento do cateto adejacente:"))
hi = math.hypot(co, ca)
print ("o valor da hipotenusa é {:.2f}".format(hi))