#db/models.py
# modèle Arrondissement
from db import db
from datetime import datetime

class Arrondissement(db.Model):
    idArrondissement = db.Column(db.Integer, primary_key=True)
    arrondissement = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Arrondissement {self.arrondissement}>"

# modèle Restaurant
class Restaurant(db.Model):
    idRest = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    idArrondissement = db.Column(
        db.Integer, db.ForeignKey("arrondissement.idArrondissement"), nullable=False
    )
    idTypeRest = db.Column(
        db.Integer, db.ForeignKey("type_rest.idTypeRest"), nullable=False
    )
    description = db.Column(db.Text, nullable=False)
    coords = db.Column(db.String(100), nullable=False) #sous la forme "latitude,longitude"
    date_creation = db.Column(
        db.DateTime, nullable=False, default=lambda: datetime.now()
    )

    def __repr__(self):
        return f"<Restaurant {self.nom}>"

# modlèle TypeRest
class TypeRest(db.Model):
    idTypeRest = db.Column(db.Integer, primary_key=True)
    typeRest = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<TypeRest {self.typeRest}>"
