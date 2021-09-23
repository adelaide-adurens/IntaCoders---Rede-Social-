# IntaCoders---Rede-Social-
Projeto Final Segundo Modulo Degree Data Science da Let's Code

DESCRIÇÃO
Para esse projeto nós criaremos uma rede social baseada no Instagram onde teremos um grafo direcionado, já que posso seguir alguém que não me segue. Além disso, teremos conexões que serão melhores amigos e outras que serão conexão comuns. Logo, teremos um grafo direcionado e ponderado.
O objetivo será criar algumas funções relacionadas ao grafo e a rede social:
- Exibir número de seguidores
- Exibir quantidades de pessoas que o usuário segue
- Ordenar a lista de Stories, ou seja, melhores amigos primeiro e depois conexões comuns ordenadas por ordem alfabética -> [melhores amigos em ordem alfabetica , amigos em ordem alfabetica]
- Encontrar top k influencers, ou seja, k pessoas que mais tem seguidores da rede
- Encontrar o caminho entre uma pessoa e outra na rede

DADOS

Para montar o grafo, irei disponibilizar dois arquivos csv contendo:
Usuário da rede: Nome e username
Conexões: Pessoas que cada usuário segue e uma flag indicando se é melhor amigo ou não (2 = Melhor amigo, 1 = não melhor amigo)
Usuarios.csv
Nome, Username
Conexoes.csv
	Username, Pessoa que ele segue, Flag Melhor Amigo
NÃO É PERMITIDA A UTILIZAÇÃO DE BIBLIOTECAS QUE NÃO VIMOS EM AULA.

