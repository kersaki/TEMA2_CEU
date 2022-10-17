def modificar(lista):
    nueva_lista=[]
    for i in lista:
        if i not in nueva_lista:
            nueva_lista.append(i)
    nueva_lista.sort()
    print(nueva_lista)
    for i in nueva_lista:
        if i%2!=0:
            nueva_lista.remove(i)
    suma=sum(nueva_lista)
    nueva_lista.insert(0,suma)
    return(nueva_lista)
lista=[4,7,9,3]
nueva_lista=modificar(lista)
print(nueva_lista[0]==sum(nueva_lista[1:]))        

