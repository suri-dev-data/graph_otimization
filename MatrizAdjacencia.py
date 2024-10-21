

class Adjacence_Matrix:

    matrix = [[]]

    def __init__(self,vertices) -> None:
        self.vertices = vertices
        self.matrix = [[0]*vertices for i in range(self.vertices)]

    def add_arris(self,u : int ,v : int):
        self.matrix[u][v] = "1"
        self.matrix[v][u] = "1"


    def add_vertex(self):
        self.matrix.append([0]*self.vertices)
        [self.matrix[x].append(0) for x in range(len(self.matrix))]

    def delete_arris(self,u:int,v:int):
        self.matrix[u][v] = "0"
        self.matrix[v][u] = "0"
        

                   
    def __bridge(self,father,v) -> None:
        global pre
        global low
        global cont
        cont += 1
        pre[v] = cont
        low[v] = pre[v]
        # # print(pre)
        # # print(low)
        # # print(self.matrix[v])
        # # print(range(len(self.matrix[v])))
        # # print(father)
        # # print(v)
        # print("-------Prox-------")
        for w,pos in zip(self.matrix[v],range(len(self.matrix[v]))):
            if pre[pos] == 0 and w == "1":
                self.__bridge(v,pos)
                if pre[pos] == low[pos]:
                    print("A aresta [{},{}] é Ponte".format(pre[v],pre[pos]))
                low[v] = min(low[v],low[pos])
            elif pos != father  and w == "1":
                low[v] = min(low[v],pre[pos])




    def showBridges(self) -> None:
        global pre
        global low
        global cont 
        pre = [0 for i in range(self.vertices)]
        low = [200 for i in range(self.vertices)]
        cont = 0
        for i in range(len(self.matrix)):
            if pre[i] == 0:
                print("iniciando grafo conexo começado por {}".format(i))
                self.__bridge(i,i)


    def __articulations(self,father,v) -> None:
        global pre
        global low
        global cont
        global pa
        cont += 1
        pre[v] = cont
        low[v] = pre[v]
        pa[v] = 0   
        # # print(pre)
        # # print(low)
        # # print(self.matrix[v])
        # # print(range(len(self.matrix[v])))
        # # print(father)
        # # print(v)
        # print("-------Prox-------")
        for w,pos in zip(self.matrix[v],range(len(self.matrix[v]))):
            if pre[pos] == 0 and w == "1":
                self.__articulations(v,pos)
                if low[pos] >= pre[v]:
                    pa[v] += 1    
                low[v] = min(low[v],low[pos])
            elif pos != father  and w == "1":
                low[v] = min(low[v],pre[pos])




    def showArticulations(self) -> None:
        global pre
        global low
        global cont 
        global pa
        pre = [0 for i in range(self.vertices)]
        low = [200 for i in range(self.vertices)]
        pa = [0 for i in range(self.vertices)]
        cont = 0
        for i in range(len(self.matrix)):
            if pre[i] == 0:
                print("iniciando grafo conexo começado por {}".format(i))
                self.__articulations(i,i)
        for i in range(len(self.matrix)):
            if i == 0 and pa[i] > 1:
                print("O vertice {} é uma articulação".format(i))
            elif i != 0 and pa[i] > 0:
                print("O vertice {} é uma articulação".format(i))




    def __str__(self):
        for i in range(0,len(self.matrix)):
            for j in range(0,len(self.matrix[i])):

                print(self.matrix[i][j],end='')
            print("")
        return " "



adj = Adjacence_Matrix(3)
adj.add_arris(0,2)
adj.add_arris(0,1)
print(str(adj))
adj.showBridges()
print()
print(str(adj))
adj.showArticulations()


