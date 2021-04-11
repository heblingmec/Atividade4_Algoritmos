from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica

p1 = Pessoa(1, "Pablo", "Av. Bento Gonçalves, 1515")
p1.imprimeNome()

f1 = Fisica(2, "Nick", "Rua 1", "blabla", "111.111.111-11", 5, 85.2, 1.78)
f1.imprimeCPF()

j1 = Juridica(3, "Bleu", "Rua 2", "bleble", "222.222.222-0002/22", "2222222", 150)
j1.imprimeCNPJ()

