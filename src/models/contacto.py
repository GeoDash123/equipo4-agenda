from src.extensions import db

class Contacto(db.Model):
    __tablename__= "contactos"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    tel = db.Column(db.String(12), nullable=False)
    desc = db.Column(db.String(100), nullable=True)



    def to_dict(self) -> dict[str, object]:
        return {

            "nombre": self.nombre,
            "telefono": self.tel,
            "descripcion": self.desc

        }