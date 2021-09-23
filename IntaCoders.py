import csv

class IntaCoders():
    def __init__(self):
        self.adjacencia = {}

    def adiciona(self, vertice):
        self.adjacencia[vertice] = {}

    def coletaVerticeArquivo (self, nomeArquivo):

        with open(nomeArquivo, newline='') as csvfile:
            leitura = csv.reader(csvfile)
            for linha in leitura:
                self.adiciona(linha[1])

    def conecta(self, usuario1, usuario2, peso):
        self.adjacencia[usuario1][usuario2] = peso

    def coletaConexoesArquivo (self, nomeArquivo):
        with open(nomeArquivo, newline='') as csvfile:
            leitura = csv.reader(csvfile)
            for linha in leitura:
                self.conecta(linha[0], linha[1], linha[2])

    def exibeNoSeguidores (self, usuario):
        seguidores = []
        for linha in self.adjacencia.items():
            for item in linha[1].items():
                if usuario in item:
                    seguidores.append(linha[0])

        return print(f"O/A usuário(a) de apelido '{usuario}' tem  {len(seguidores)} seguidores.")

    def exibeQtdPessoasSegue(self, usuario):
        seguidos = len(self.adjacencia[usuario].keys())
        return print(f"O/A usuário(a) de apelido '{usuario}' segue {seguidos} pessoas.")

    def organizaStories(self,usuario):
        listaAmigos = list(self.adjacencia[usuario].items())
            

        listaMelhoresAmigos = []
        listaAmigosComuns = []

        for item in listaAmigos:
            if item[1] == '2':
                listaMelhoresAmigos.append(item[0])
            else:
                listaAmigosComuns.append(item[0])

        for x in range(len(listaMelhoresAmigos)):
            for y in range(len(listaMelhoresAmigos)):
                if listaMelhoresAmigos[x] < listaMelhoresAmigos[y]:
                    listaMelhoresAmigos[x], listaMelhoresAmigos[y] = listaMelhoresAmigos[y], listaMelhoresAmigos[x]
    
        for x in range(len(listaAmigosComuns)):
            for y in range(len(listaAmigosComuns)):
                if listaAmigosComuns[x] < listaAmigosComuns[y]:
                    listaAmigosComuns[x], listaAmigosComuns[y] = listaAmigosComuns[y], listaAmigosComuns[x]
    
        listaFinalStories = listaMelhoresAmigos + listaAmigosComuns

        return print(f"A ordem de exibição dos stories de {usuario} é: {listaFinalStories}.")

    def topKSeguidores (self, k):

        dicionarioNoSeguidores = {}

        for usuario in self.adjacencia:
            seguidores = 0
            for linha in self.adjacencia.items():
                for item in linha[1].items():
                    if usuario in item:
                        seguidores +=1
            dicionarioNoSeguidores[usuario] = seguidores

        listaCrescenteSeguidores = list(dicionarioNoSeguidores.items())

        for x in range(len(listaCrescenteSeguidores)):
            for y in range(len(listaCrescenteSeguidores)):
                if listaCrescenteSeguidores[y][1] < listaCrescenteSeguidores[x][1]:
                    listaCrescenteSeguidores[x], listaCrescenteSeguidores[y] = listaCrescenteSeguidores[y], listaCrescenteSeguidores[x]

        stringTopK = ''
        for item in listaCrescenteSeguidores[:k]:
            stringTopK += str(item[0]) + ', com ' + str(item[1]) + " seguidores; "

        
        return print(f"Os top {k} influencers com mais seguidores são: {stringTopK[:-2]}.")
            
    def exibeCaminhoUsuarios(self, usuario1, usuario2):
        fila = [usuario1]
        visitados = []
        predecessor = {usuario1: None}
        
        while len(fila) > 0:
            primeiro_elemento = fila[0]
            fila = fila[1:]
            visitados.append(primeiro_elemento)
            for adjacente in self.adjacencia[primeiro_elemento].keys():
                
                
                if adjacente == usuario2:
                    pred = primeiro_elemento
                    caminho_invertido = [usuario2]
                    while pred is not None:
                        caminho_invertido.append(pred)
                        pred = predecessor[pred]
                    
                    caminho = ''
                    for no in caminho_invertido[::-1]:
                        caminho += f'{no} -> '
                    return print(f"O caminho entre os dois usuários informados é :{caminho[:-3]}")
                
                if adjacente not in fila and adjacente not in visitados:
                    predecessor[adjacente] = primeiro_elemento
                    fila.append(adjacente)
        return False 
        

meuIntaCoders = IntaCoders()
meuIntaCoders.coletaVerticeArquivo('usuarios.csv')
meuIntaCoders.coletaConexoesArquivo('conexoes.csv')
meuIntaCoders.exibeNoSeguidores('helena42')
meuIntaCoders.exibeQtdPessoasSegue('helena42')
meuIntaCoders.organizaStories('helena42')
meuIntaCoders.topKSeguidores(5)
meuIntaCoders.exibeCaminhoUsuarios('helena42', 'valentina26')