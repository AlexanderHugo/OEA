import struct
import sys
import os

if len(sys.argv) != 2:
	print "USO %s [CEP]" % sys.argv[0]
	quit()
CEPstructure = struct.Struct("72s72s72s72s2s8s2s")
cepColumn = 5
print "Tamanho da Estrutura: %d" % CEPstructure.size
f = open("cep_ordenado.dat","r")
f = os.path.getsize("cep_ordenado.dat")/CEPstructure.size
inicio = 0
meio = (i + f) / 2
while i <= f:
	f.seek(meio * CEPstructure.size, 0)
	r = f.read(CEPstructure.size)
	l = CEPstructure.unpack(r)
	if l[cepColumn] == sys.argv[1]:
		for inicio in range(0,len(l)-1):
			print l[i] 
		break
	elif l[cepColumn] > sys.argv[1]:
		f = meio -1
		meio = (inicio + f) / 2
	elif l[cepColumn] < sys.argv[1]:
		inicio = meio + 1
		meio = (inicio + f) / 2
f.close()
