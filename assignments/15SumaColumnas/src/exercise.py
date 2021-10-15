def main():
    #Se piden los valores de renglones y columnas
    r = int(input(""))
    c= int(input(""))
    
    sum = 0
    suma = [] #Se establece una lista para las sumas

    if r*c <=0: #El programa se asegura que el numero de columnas y renglones sea mayor a 0
        print('Error')
    else:
        matriz=[]
        for r in range(r): #Se crea un ciclo con otro ciclo dentro para construir la lista de listas (matriz)
            renglones = []
            for col in range(c):
                valores = int(input(""))
                renglones.append(valores)
            matriz.append(renglones)

        if len(matriz) > 0:
            for x in range(len(matriz[0])):
                sum=0
                for i in range(len(matriz)):
                    sum += matriz[i][x]
                suma.append(sum)
            print(suma)




if __name__=='__main__':
    main()
