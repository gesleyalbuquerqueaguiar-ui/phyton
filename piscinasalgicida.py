fu = float(input("qual a fundura da sua piscina?"))
la = float(input("qual a largura da sua piscina?"))
co = float(input("qula o comprimento da sua piscina?"))
tl = ((co * la) * fu) * 1000
print ("sua picina possue {} litros de agua".format(tl))
algi= (5 * tl) / 1000
print ("e para mantela com a prevencçao de agua verde sera nessesario"\
       " {} ml de algicida de manutenção".format(algi))