from DISClib.ADT import list as lt

a = [8,5,4,21,0,9,12,67,89,56,45,34,36,78,14,98,443,65,32]

#Se crea una lista de ejemplo con el TAD lista
listibiris = lt.newList(datastructure="ARRAY_LIST")
for b in a:
    lt.addLast(listibiris,b)

def heapify(array,size,root):
    #Función que se encarga de revisar si los hijos tanto izquierdo como derecho de la raiz son mayores, y en caso de serlo los sube y revisa nuevamente
    largest = root
    left = (largest*2)
    right = (largest*2)+1

    #Compara los valored de los hijos con la raiz y asigna el hijo como valor mayor en caso de que se cumpla
    if left < size and lt.getElement(array,largest) < lt.getElement(array,left):
        largest = left
    
    if right < size and lt.getElement(array,largest) < lt.getElement(array,right):
        largest = right

    #Realiza el intercambio del mayor con la raiz en caso de que se necesite y nuevamente realiza la función recursivamente pero con el hijo que reemplazó.
    if largest != root:
        oldroot = lt.getElement(array, root)
        newroot = lt.getElement(array, largest)
        lt.changeInfo(array,largest,oldroot)
        lt.changeInfo(array,root,newroot)
        heapify(array,size,largest)

def heapsort(array):
    #Función que realiza el ordenamiento
    size = lt.size(array)
    #Se hace heapify por cada una de las raices que tengan al menos un hijo
    #Esto nos dará un maxPQ de todo el arreglo
    for root in range(size//2,0,-1):
        heapify(array,size,root)
    
    #Se hace el proceso de reemplazar la raiz del heap por el elemento más a la derecha y luego se asume que el tamaño del heap es 1 elemento más pequeño para que no se tenga en cuenta el elemento ordenado
    #Nuevamente hace heapify con la nueva raiz para garantizar que sigamos teniendo un maxPQ
    #Se hace este proceso hasta que quede un heap de tamaño 1, ordenandolo
    for subsize in range(size,1,-1):
        oldlast = lt.getElement(array, subsize)
        newlast = lt.getElement(array, 1)
        lt.changeInfo(array,1,oldlast)
        lt.changeInfo(array,subsize,newlast)
        heapify(array,subsize,1)

#Se imprime la lista de ejemplo desordenada y depues se ejecuta el algoritmo y se imprime ordenada
print(listibiris)
heapsort(listibiris)
print(listibiris)
