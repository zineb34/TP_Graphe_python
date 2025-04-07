from random import randint

def generer_matrice(size):
    matrice = []
    for i in range(size):
        line = []
        for j in range(size):
            line.append(0)
        matrice.append(line)
        
    for i in range(size):
        for j in range(i,size):
            if i != j:
                value = randint(1, 100)
                matrice[i][j] = value
                matrice[j][i] = value
    return matrice


def save_matrice(matrice, path):
    with open(path, "w") as file:
        file.write(str(len(matrice)) + "\n")
        for line in matrice:
            for item in line:
                file.write(str(item) + "\t")
            file.write("\n")


def read_matrice(path):
    matrice = []
    with open(path, "r") as file:
        size = int(file.readline().strip("\n"))
        for line in file:
            matrice.append(list(map(int, filter(lambda x: x.isdigit(), line.split("\t")))))
    return matrice

matrice = read_matrice(r"matric.txt")


def get_tree_solution(matric):
    size_matrice = len(matric)  
    node_solution = [randint(0, size_matrice - 1)]  
    tree_solution = []  
    weight_total = 0  

    while len(node_solution) < size_matrice:
        minValue = float("inf")
        index = float("inf")
        u = float("inf")

        for node in node_solution:
            for v, weight in enumerate(matric[node]):
                if (weight != 0) and (v not in node_solution) and (weight < minValue):
                    minValue = weight
                    index = v
                    u = node

        if index != float("inf"):
            node_solution.append(index)
            tree_solution.append((u, index))
            weight_total += minValue
    
    return node_solution, tree_solution, weight_total

solution = get_tree_solution(matrice)
print("node solution: ",   solution[0],
      "\nTree solution: ", solution[1],
        "\nWeight total",  solution[2],
    )
