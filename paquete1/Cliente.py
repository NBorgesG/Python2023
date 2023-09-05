class Cliente:

    def __init__(self, nombre, ci, direccion, telefono, correo):
        self.nombre = nombre
        self.ci = ci
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

    def editarCliente(self):
        print("Se ha editado el cliente")    

    def comprar(self, objeto, suc):
        print(f"El cliente {self.nombre} ha comprado {objeto} en {suc}")
        print(f"Se ha enviado un correo con el total de su compra a {self.correo}")
        
    def __str__(self):
        return "Se ha creado el usuario \nNombre: " +self.nombre + ", ci:" + self.ci + ", direccion: " + self.direccion + ", telefono: " + self.telefono +", correo: "+ self.correo

