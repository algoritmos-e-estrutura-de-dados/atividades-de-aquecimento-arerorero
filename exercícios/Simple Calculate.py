x,a,b = input().split(" ")
x,c,d = input().split(" ")
a = float(a)
b = float(b)
c = float(c)
d = float(d)

dinheiro = round((a*b)+(c*d),2)
print("VALOR A PAGAR: R$ "+format(dinheiro))
