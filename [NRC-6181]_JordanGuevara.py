#Declaracion de las variables a usar
numero=0
#Bandera para detener while
condicion=True
#lista creada para los docentes
listaDocente=[]
#Creacion de la clase que se tomara encuenta(docentes)
class docente:
    #Creacion del metodo
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    
    def trabajo(self, rol,departamento,salario):
        self.rol=rol
        self.departamento=departamento
        self.salario=salario
        



while condicion==True:
    # Especifica que cantidad debe verificar y llegar para terminar su funcion
    numDocente=int(input("Cuantos docentes desea registar: "))
    # Condicional que verifica si la condicion es verdadera o falsa
    if numDocente>=5:
        # Condicional de repeticion while 
            while numero<=numDocente:
                # Ingreso de los datos a la clase
                nombre=str(input("Ingrese del nombre: "))
                apellido=str(input("Ingreso del apellido"))
                edad=int(input("Ingrese la edad: "))
                # Agrega a la lista asignada
                listaDocente.append(nombre)
                listaDocente.append(apellido)
                listaDocente.append(edad)
                # Ingreso del trabajo del docente
                rol=str(input("Ingrese el rol:"))
                departamento=str(input("Departamento de estudio"))
                salario=float(input("Ingrese el salsrio: "))
                # Agrega a la lista asignada
                listaDocente.append(rol)
                listaDocente.append(departamento)
                listaDocente.append(salario)
                # Bandera que aumenta para negar el condicional while
                numero=numero+1
                # Bandera que cambiara su valor para negaran el condicional while
                condicion=False
                #Muestra del avance
                for i in range(0,len(listaDocente)):
                    '''Los docentes ingresados con su salario son: '''
                    # Mostrara la cantidad de datos que tiene encapsulado
                    print(listaDocente[i])
                

    else:
        # Mensaje que mostrara si la condicion de if es falsa y se repetira la pregunta
        print("Cantidad no existente o es mayor a 5")

