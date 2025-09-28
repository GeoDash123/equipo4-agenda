class Contacto:
    def __init__(self, contacto_id: int, nombre: str, correo: str):
        self.contacto_id = contacto_id
        self.nombre = nombre
        self.correo = correo
        self.telefonos = []
        self.direcciones = []

    def agregar_telefono(self, telefono):
        self.telefonos.append(telefono)

    def agregar_direccion(self, direccion):
        self.direcciones.append(direccion)
