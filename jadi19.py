vorodi=input()
h1=vorodi.find('h')
h2=vorodi.find('e',h1+1)
h3=vorodi.find('l',h2+1)
h4=vorodi.find('l',h3+1)
h5=vorodi.find('o',h4+1)
TF=h1>=0 and h2>h1 and h3>h2 and h4>h3 and h5>h4
if TF:
 print('YES')
else:
 print('NO')