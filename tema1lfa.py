import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
from graphviz import Digraph

gfc = Digraph('finite_state_machine', filename='fsm.gv')
gfc.attr(rankdir = 'LR', size = '8,5')

f = open("read1","r")
cuv = input("cuvant=")
n = int(f.readline())

list_noduri = f.readline()
list_noduri = list_noduri[:len(list_noduri) -1 ]
list_noduri = list_noduri.split(" ")

nod_init = f.readline()
nod_init = nod_init[:len(nod_init) - 1]

gfc.attr('node', style = 'invisible', shape = 'circle')
fake = ' '
gfc.node(fake)

nod_fin = f.readline()
nod_fin = nod_fin[:len(nod_fin) - 1]
nod_fin = nod_fin.split(" ")
if nod_init in nod_fin:
    gfc.attr('node', style = '', shape = 'doublecircle')
else:
    gfc.attr('node', style = '', shape = 'circle')

gfc.edge(fake,nod_init,label = ' ', style = 'bold')

gfc.attr('node', shape = 'doublecircle')

z = len(nod_fin)
for i in range(z):
    gfc.node(nod_fin[i])

gfc.attr('node', shape = 'circle')

l = []
x = f.readline()
x = x[:len(x) - 1]

while x:
    x = x.split(" ")
    gfc.edge(x[0],x[1],label = x[2])
    l.append(x)
    x = f.readline()
    x = x[:len(x) - 1]

stare_init = []

for i in range(len(l)):
    if l[i][0] == nod_init:
        stare_init.append(l[i][2])

if nod_init in nod_fin and len(cuv) == 0:
    print("lambda")

elif nod_init not in nod_fin and len(cuv) == 0:
    print("neacceptat/continua")

else:
    ok = 1
    ant = nod_init
    for i in range(len(cuv)):
        if i == 0 and cuv[i] not in stare_init:
            ok = 0
        else:
            k = 0
            for j in range(len(l)):
                if l[j][0] == ant and cuv[i] in l[ j ][ 2 : len(l[j]) ]:
                    ant = l[j][1]
                    k = 1
                    break
            if j == len(l)-1 and k == 0:
                ok = 0
    if ant not in nod_fin:
        ok = 0
    if ok == 1:
        print("acceptat")
    else:
        print("neacceptat")

gfc.view()