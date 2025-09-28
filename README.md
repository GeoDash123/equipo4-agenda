classDiagram
    class Contacto {
        +id: int
        +nombre: str
        +correo: str
    }

    class Telefono {
        +id: int
        +numero: str
        +tipo: str
    }

    class Direccion {
        +id: int
        +calle: str
        +ciudad: str
        +estado: str
    }

    Contacto --> Telefono : tiene >
    Contacto --> Direccion : tiene >