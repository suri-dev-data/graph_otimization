

class Incidence_Matriz:

    matriz = [[]]
    
    def __init__(self,vertices) -> None:
        self.vertices = vertices
        self.matriz = [[] for i in range(vertices)]

    def add_arris(self,u : int ,v : int):
        if u < self.vertices and v  < self.vertices:
            for i in range(self.vertices):
                self.matriz[i-1].append(0) 
            self.matriz[v-1][len(self.matriz[v-1])-1] = "1"
            self.matriz[u-1][len(self.matriz[u-1])-1] = "1"

    def delete_arris(self,u:int,v:int):
        self.matriz[u-1][v-1] = "0"
        self.matriz[v-1][u-1] = "0"

    def __str__(self):
        for i in range(0,len(self.matriz)):
            for j in range(0,len(self.matriz[i])):
                print(self.matriz[i][j],end='')
            print("")
        return " "



adj = Incidence_Matriz(5)
adj.add_arris(4,3)
adj.add_arris(2,3)
adj.add_arris(1,3)


print(str(adj))
    

