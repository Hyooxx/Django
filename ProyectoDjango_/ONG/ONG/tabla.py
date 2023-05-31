num=int(input("Ingres un número: "));
listaResultados=[];
print(f"----Tabla del {num}----\n");
for i in range(1,11):
    resultado=num*i
    listaResultados.append(resultado)
    print(f"{num} X {i} = {resultado}");
print(f"La lista es: {listaResultados}");

