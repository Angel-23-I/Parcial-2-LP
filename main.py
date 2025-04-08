#Programa de cola de prioridad


#Datos del paciente (Nombre, Edad, sintomas o motivo, gravedad 1 a 5, 1 es la mayor)
class Paciente:
    def __init__(self, nombre, edad, sintomas, gravedad, prioridad):
        self.nombre = nombre
        self.edad = edad
        self.sintomas = sintomas
        self.gravedad = gravedad
        self.prioridad = prioridad
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Sintomas: {self.sintomas}, Gravedad: {self.gravedad}, Prioridad : {self.prioridad}" 
        
#clase nodo
class Nodo:
    def __init__(self, paciente):
        self.paciente = paciente
        self.siguiente = None

#Clase ColaPrioridad Lista enlazada ordenada por gravedad y prioridad.
class ColaPrioridad:
    #Atributos: inicio(primer nodo de la lista)
    def __init__(self):
        self.inicio = None

    #Mostrar cola
    def mostrar_cola(self):
        aux = self.inicio
        while aux != None:
            print(aux.paciente)
            aux = aux.siguiente
            
    #Metodo para agregar un paciente a la cola segun gravedad y prioridad
    def agregar_paciente(self, paciente):
            nuevo_nodo = Nodo(paciente)
            if self.inicio is None:
                self.inicio = nuevo_nodo
            else:
                if paciente.gravedad < self.inicio.paciente.gravedad:
                    nuevo_nodo.siguiente = self.inicio
                    self.inicio = nuevo_nodo
                else:
                    actual = self.inicio
                    while actual.siguiente is not None and paciente.gravedad < actual.siguiente.paciente.gravedad:actual = actual.siguiente
                    nuevo_nodo.siguiente = actual.siguiente
                    actual.siguiente = nuevo_nodo
    #Metodo pasar al siguiente (imprimir y eliminar)
    def pasar_siguiente(self):
        if self.inicio is None:
            print("La cola esta vacia")
        else:
            paciente = self.inicio.paciente
            self.inicio = self.inicio.siguiente
            print("Siguiente paciente: ",paciente.nombre," Edad: ",paciente.edad," Sintomas: ",paciente.sintomas," Gravedad: ",paciente.gravedad," Prioridad: " ,paciente.prioridad)
            print("------ Paciente atendido ------")
            return paciente
        
#Funcion calcular_prioridad_edad(edad, Prioridad 1: niños menores de 12 años, Prioridad 2: adultos mayores de 65 años, Prioridad 3: demás pacientes)
def calcular_prioridad_edad(edad):
    if edad < 12:
        return 1
    elif edad > 65:
        return 2
    else:
        return 3

#Menu principal, (bucle con opciones: ingresar paciente, pasar siguiente paciente, mostrar cola, salir)
cola = ColaPrioridad()
while True:
    print("1. Ingresar paciente")
    print("2. Pasar siguiente paciente")
    print("3. Mostrar cola")
    print("4. Salir")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del paciente: ")
        edad = int(input("Ingrese la edad del paciente: "))
        sintomas = input("Ingrese los sintomas del paciente: ")
        gravedad = int(input("Ingrese la gravedad del paciente: "))
        prioridad = calcular_prioridad_edad(edad)
        paciente = Paciente(nombre, edad, sintomas, gravedad, prioridad)
        cola.agregar_paciente(paciente)
        print("Paciente agregado exitosamente!")
    elif opcion == "2":
        cola.pasar_siguiente()
    elif opcion == "3":
        cola.mostrar_cola()
    elif opcion == "4":
        break
