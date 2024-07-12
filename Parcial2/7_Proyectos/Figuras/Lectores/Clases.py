class Lectores:
    def __init__(self,nombre,direccion,telefono):
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono

    #Metodos get y set
    def getNombre(self):
        return self.nombre
    
    def setNombre(self,nombre):
        self.nombre=nombre

    def getDireccion(self):
        return self.direccion
    
    def setDireccion(self,direccion):
        self.direccion=direccion

    def getTelefono(self):
        return self.telefono
    
    def setTelefono(self,telefono):
        self.telefono=telefono

    #Metodos
    def Reservar(self):
        print(f"Esta reservado {self.getNombre()}")
    
    def Entregar(self):
        print(f"Esta entregado el libro {self.getNombre()}")
    


class Estudiante(Lectores):
    def __init__(self, nombre, direccion, telefono,carrera,matricula):
        super().__init__(nombre, direccion, telefono)
        self._carrera=carrera
        self._matricula=matricula

    def getCarrera(self):
        return self._carrera
    
    def setCarrera(self,carrera):
        self._carrera=carrera

    def getMatricula(self):
        return self._matricula
    
    def setMatricula(self,matricula):
        self._matricula=matricula

    def Reservar(self):
        print(f"Esta reservado por el estudiante {self.getNombre()}\nMatricula: {self.getMatricula()}")
    
    def Entregar(self):
        print(f"Esta entregado el libro por el estudiante {self.getNombre}\nMatricula: {self.getMatricula()}")

class Docente(Lectores):
    def __init__(self, nombre, direccion, telefono,modalidad,num_empleado):
        super().__init__(nombre, direccion, telefono)
        self.__modalidad=modalidad
        self.__num_empleado=num_empleado

    def getModalidad(self):
        return self.__modalidad
    
    def setModalidad(self,modalidad):
        self.__modalidad=modalidad

    def getNumeroEmpleado(self):
        return self.__num_empleado
    
    def setNumeroEmpleado(self,numero_empleado):
        self.__num_empleado=numero_empleado

    def Reservar(self):
        print(f"Esta reservado por el docente {self.getNombre()}\nMatricula: {self.getNumeroEmpleado()}")
    
    def Entregar(self):
        print(f"Esta entregado el libro por el docente {self.getNombre()}\nMatricula: {self.getNumeroEmpleado()}")
