with open('input.txt','r') as f:
    y=f.readline()
    a=0
    b=0
    c=0
    d=0
for litere in y:
    if litere.isupper():
            a+=1
with open('litereA.txt','w') as f:
        f.write(str(a))
for lit in y:
    if lit.islower():
            b+=1
with open('litereB.txt','w') as f:
         f.write(str(b))
for x in y:        
    if ord(x) in range(48,58):
             d+=1
with open('operatori.txt','w') as f:
        f.write(str(d))
for e in y:
    if((ord(e) in range(32,48)) or(ord(e) in range (58,65)) or (ord(e) in range(91,9)) or(ord(e) in range(123,127))):
              c+=1
with open('cifre.txt','w')as f:
        f.write(str(c))
