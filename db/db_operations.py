#db/db_operations.py
from db.models import Restaurant, TypeRest, Arrondissement
from db import db
 
def add_restaurant(nom, arrondissement_form, typeRest, description, coords):
    arrondissement = Arrondissement.query.filter_by(
        arrondissement=arrondissement_form
    ).first()
    type_rest = TypeRest.query.filter_by(idTypeRest=typeRest).first()

    new_restaurant = Restaurant(
        nom=nom,
        idArrondissement=arrondissement.idArrondissement,
        idTypeRest=type_rest.idTypeRest,
        description=description,
        coords=coords,
    )

    db.session.add(new_restaurant)
    db.session.commit()


def add_type(type_rest, description):
    new_type = TypeRest(typeRest=type_rest, description=description)
    db.session.add(new_type)
    db.session.commit()


def add_arrondissement(arrondissement):
    new_arrondissement = Arrondissement(arrondissement=arrondissement)
    db.session.add(new_arrondissement)
    db.session.commit()


def get_all_restaurants():
    return Restaurant.query.all()


def get_all_types():
    return TypeRest.query.all()


def get_all_arrondissements():
    return Arrondissement.query.all()
