def cria_matriz():
    matriz=[]
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append("-")
        matriz.append(linha)
    return matriz

def executa_jogada(turno, matriz,i,j):
    if turno%2!=0:
        if matriz[i][j] == "-":
            matriz[i][j] = "X"
        else:
            print("coordenada invalida, escolha uma posição que nao foi tomada:")
            x = int(input("coordenada X: "))
            y = int(input("coordenada Y: "))
            executa_jogada(turno, matriz,x,y)
    elif turno%2==0:
        if matriz[i][j] == "-":
            matriz[i][j] = "O"
        else:
            print("coordenada invalida, escolha uma posição que nao foi tomada:")
            x = int(input("coordenada X: "))
            y = int(input("coordenada Y: "))
            executa_jogada(turno, matriz,x,y)

def verifica_fim(matriz):
    if matriz[0][0]==matriz[1][1]==matriz[2][2]=="X":
        return 1
    elif matriz[0][0]==matriz[1][1]==matriz[2][2]=="O" :
        return 2
    elif matriz[0][2]==matriz[1][1]==matriz[2][0]=="X":
        return 1
    elif matriz[0][2]==matriz[1][1]==matriz[2][0]=="O":
        return 2
    for i in range(3):
        if matriz[i][0]==matriz[i][1]==matriz[i][2]=="X" :
            return 1
        elif matriz[i][0]==matriz[i][1]==matriz[i][2]=="O" :
            return 2
    for i in range(3):
        if matriz[0][i]==matriz[1][i]==matriz[2][i]=="X" :
            return 1
        elif matriz[0][i]==matriz[1][i]==matriz[2][i]=="O" :
            return 2
    else:
        return 3
    
def jogada():
    print("digite entre 1 e 3 onde deseja jogar")
    x = int(input("coordenada X: "))
    while ( x < 1 or x > 3 ) :
        x = int(input("coordenada invalida, escolha um local dentro do tabuleiro: "))
    y = int(input("coordenada Y: "))
    while ( y < 1 or y > 3 ) :
        y = int(input("coordenada invalida, escolha um local dentro do tabuleiro: "))
    return (x-1),(y-1)