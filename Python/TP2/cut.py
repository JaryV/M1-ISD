import sys

print('Name of script: {}'.format(sys.argv[0]))
print('Number of arguments: {}'.format(len(sys.argv)))
print('The arguments are: {}'.format(str(sys.argv)))



x = [] 
y = []
for arg in sys.argv[4:-1]:
    a = arg.split(',')
    #print(a)
    for p in a:
        xb = p.split('-')
        
        for i in range(2):
            xb[i] = int(xb[i])
    
        x.append(xb)

#print(x)

for xL in x:
    for i in range(xL[0],xL[1]+1):
        y.append(i)

y = list(set(y))
#print(y)

with open(sys.argv[-1], 'r') as file:
    lines = file.readlines()


for line in lines:
    line = line.replace('\n','')
    i = 1
    for word in line.split(sys.argv[2]):
        if i in y:
            print(word + sys.argv[2]),
        i+=1
    print("\n")

#Commande : python cut.py -d , -f 3-5,3-4,1-1 test.txt